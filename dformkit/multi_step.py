# dformkit/multi_step.py

from django import forms
from django.core.exceptions import ValidationError
from django.utils.module_loading import import_string
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect

class Step:
    """كلاس لتمثيل خطوة واحدة في النموذج"""
    def __init__(self, title, fields):
        self.title = title
        self.fields = fields

class MultiStepForm(forms.Form):
    """الكلاس الرئيسي للنماذج متعددة الخطوات"""
    steps = []  # سيتم تعبئتها عبر Meta

    class Meta:
        steps = []  # يُعرّف المستخدم الخطوات هنا

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # التحقق مما إذا كانت `Meta` تحتوي على `steps` وتمريرها إلى `self.steps`
        if hasattr(self.Meta, 'steps'):
            self.steps = self.get_steps()
        else:
            raise ValueError("يجب تعريف 'steps' داخل Meta في نموذج MultiStepForm")

    def get_steps(self):
        """تحويل الخطوات من Meta إلى كائنات Step"""
        return [
            Step(step['title'], step['fields']) 
            for step in self.Meta.steps
        ]

    def get_step_fields(self, step_index):
        """الحصول على حقول خطوة محددة"""
        return self.steps[step_index].fields


class MultiStepView(View):
    form_class = None  # سيتم تعيينه إلى كلاس نموذج متعدد الخطوات الذي ينشئه المستخدم
    session_key = "dformkit_multistep_data"
    template_name = "dformkit/multi_step.html"
    

    def get(self, request, step=1):
        if not self.form_class.steps or not hasattr(self.form_class.steps, 'steps') or not self.form_class.steps:
            return HttpResponse("خطأ: النموذج متعدد الخطوات لا يحتوي على أي خطوات!", status=500)
        
        step = max(1, min(step, len(self.form_class.steps)))
        step_index = step - 1

        # جلب البيانات المخزنة في الجلسة (لدمج بيانات الخطوات السابقة)
        form_data = request.session.get(self.session_key, {})

        # إنشاء نموذج للخطوة الحالية باستخدام الدالة المساعدة
        form = self.create_step_form(step_index, initial=form_data)
        print("Steps:", self.form_class.steps) 
        return render(request, self.template_name, {
            'form': form,
            'current_step': step,
            'total_steps': len(self.form_class.steps),
            'step_title': self.form_class.steps[step_index].title,
        })

    def post(self, request, step=1):
        step_index = step - 1
        form = self.create_step_form(step_index, data=request.POST)

        if form.is_valid():
            # حفظ بيانات الخطوة الحالية في الجلسة
            form_data = request.session.get(self.session_key, {})
            form_data.update(form.cleaned_data)
            request.session[self.session_key] = form_data

            if step < len(self.form_class.steps):
                return redirect('multistep', step=step + 1)
            else:
                return self.final_step(request, form_data)
        return render(request, self.template_name, {'form': form})

    def create_step_form(self, step_index, data=None, initial=None):
        """إنشاء نموذج ديناميكي للخطوة المحددة"""
        fields = self.form_class().get_step_fields(step_index)
        valid_fields = {field: self.form_class.base_fields[field] for field in fields if field in self.form_class.base_fields}
        form_class = type('StepForm', (forms.Form,), valid_fields)
        return form_class(data=data, initial=initial)

    def final_step(self, request, form_data):
        """معالجة البيانات بعد الخطوة الأخيرة (مثل حفظها أو إرسالها)"""
        if self.session_key in request.session:
            del request.session[self.session_key]
        return render(request, 'success.html', {'data': form_data})
