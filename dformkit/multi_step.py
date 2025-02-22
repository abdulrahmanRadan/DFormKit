from django import forms
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect

class Step:
    """كلاس لتمثيل خطوة واحدة في النموذج"""
    def __init__(self, title, fields):
        self.title = title
        self.fields = fields

# هنا نغير الوراثة من forms.Form إلى forms.ModelForm
class MultiStepForm(forms.ModelForm):
    """الكلاس الرئيسي للنماذج متعددة الخطوات"""
    steps = []  # سيتم تعبئتها عبر Meta

    class Meta:
        steps = []  # يُعرّف المستخدم الخطوات هنا

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(self.Meta, 'steps') or not self.Meta.steps:
            raise ValueError("يجب تعريف 'steps' داخل Meta في نموذج MultiStepForm")
        self.steps = self.get_steps()

    def get_steps(self):
        """تحويل الخطوات من Meta إلى كائنات Step"""
        return [Step(step['title'], step['fields']) for step in self.Meta.steps]

    def get_step_fields(self, step_index):
        """الحصول على حقول خطوة محددة"""
        return self.steps[step_index].fields

class MultiStepView(View):
    form_class = None  # سيتم تعيينه إلى كلاس نموذج متعدد الخطوات الذي ينشئه المستخدم
    session_key = "dformkit_multistep_data"
    template_name = "dformkit/multi_step.html"

    def get(self, request, step=1):
        if not self.form_class or not getattr(self.form_class, 'Meta', None) or not self.form_class.Meta.steps:
            return HttpResponse("خطأ: النموذج متعدد الخطوات لا يحتوي على أي خطوات!", status=500)
        
        total_steps = len(self.form_class.Meta.steps)
        step = max(1, min(step, total_steps))
        step_index = step - 1

        # استرجاع البيانات المخزنة في الجلسة
        form_data = request.session.get(self.session_key, {})

        # إنشاء نموذج للخطوة الحالية
        form = self.create_step_form(step_index, initial=form_data)
        return render(request, self.template_name, {
            'form': form,
            'current_step': step,
            'total_steps': total_steps,
            'step_title': self.form_class().get_steps()[step_index].title,
        })

    def post(self, request, step=1):
        step_index = step - 1
        form = self.create_step_form(step_index, data=request.POST)
        if form.is_valid():
            # تحديث البيانات في الجلسة
            form_data = request.session.get(self.session_key, {})
            form_data.update(form.cleaned_data)
            request.session[self.session_key] = form_data

            if step < len(self.form_class.Meta.steps):
                return redirect('multistep', step=step + 1)
            else:
                return self.final_step(request, form_data)
        return render(request, self.template_name, {'form': form})

    def create_step_form(self, step_index, data=None, initial=None):
        fields = self.form_class().get_step_fields(step_index)
        valid_fields = {field: self.form_class.base_fields[field] for field in fields if field in self.form_class.base_fields}
        StepForm = type('StepForm', (forms.Form,), valid_fields)
        return StepForm(data=data, initial=initial)

    def final_step(self, request, form_data):
        if self.session_key in request.session:
            del request.session[self.session_key]
        return render(request, 'success.html', {'data': form_data})
