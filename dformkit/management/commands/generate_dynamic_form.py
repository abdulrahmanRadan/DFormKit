import os
from django.core.management.base import BaseCommand
from django.apps import apps
from dformkit.generate_form import generate_DformKit  # دالة توليد النماذج
from dformkit.template_creator import TemplateCreator  # استيراد الكلاس الجديد

class Command(BaseCommand):
    help = 'Generates a dynamic form and optionally creates a view template.'

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str, help='Model name to generate the form from', required=True)
        parser.add_argument('--app', type=str, help='App name where the model exists', required=True)
        parser.add_argument('--view', action='store_true', help='Create a view template for the form')  # اختياري
        parser.add_argument('--v', action='store_true', help='Create a view template for the form')  # اختياري

    def handle(self, *args, **kwargs):
        model_name = kwargs['model']
        app_label = kwargs['app']
        create_view = kwargs.get('view', False)  # افتراض عدم إنشاء الواجهة إذا لم يتم تحديد الخيار
        create_view_short = kwargs.get('v', False)
        try:
            # استيراد النموذج بشكل ديناميكي
            model = apps.get_model(app_label, model_name)
            
            dynamic_form = generate_DformKit(model)
            form_code = f'from django import forms\n\nclass {model.__name__}Form(forms.ModelForm):\n'
            form_code += '    class Meta:\n'
            form_code += f'        model = {model.__name__}\n'
            form_code += '        fields = [\n'
            form_code += ''.join([f'            "{field_name}",\n' for field_name in dynamic_form.base_fields.keys()])
            form_code += '        ]\n'
            for field_name, field in dynamic_form.base_fields.items():
                form_code += f'    {field_name} = forms.{field.__class__.__name__}(required={field.required})\n'

            # حفظ النموذج المُولد في forms.py
            forms_path = os.path.join(app_label, 'forms.py')
            if os.path.exists(forms_path):
                with open(forms_path, 'r') as f:
                    existing_content = f.read()
                with open(forms_path, 'w') as f:
                    f.write(existing_content + '\n\n' + form_code)
            else:
                with open(forms_path, 'w') as f:
                    f.write(form_code)

            self.stdout.write(self.style.SUCCESS(f'Successfully generated form for {model_name}'))

            # إنشاء قالب HTML إذا تم استخدام --view
            if create_view or create_view_short:
                template_creator = TemplateCreator(app_label, model_name)
                result = template_creator.create_template()
                self.stdout.write(self.style.SUCCESS(result))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {str(e)}"))
