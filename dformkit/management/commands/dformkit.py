import os
from django.core.management.base import BaseCommand
from django.apps import apps
from dformkit.generate_form import generate_DformKit, generate_form_code  # استخدام الوظائف من generate_form.py
from dformkit.template_creator import TemplateCreator  # استيراد الكلاس الخاص بالقوالب
from dformkit.check_forms_import import FormsFileChecker  # استيراد كلاس التحقق من forms.py
from dformkit.view_url_manager import ViewUrlManager  # استيراد كلاس إدارة views و urls

class Command(BaseCommand):
    help = 'Generates a dynamic form and optionally creates a view template or URL pattern.'

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str, help='Model name to generate the form from', required=True)
        parser.add_argument('--app', type=str, help='App name where the model exists', required=True)
        parser.add_argument('-page', action='store_true', help='Create a view template for the form')
        parser.add_argument('-p', action='store_true', help='Create a view template for the form')
        parser.add_argument('-view', action='store_true', help='Add view function to views.py and URL pattern to urls.py')
        parser.add_argument('--v', action='store_true', help='Add view function to views.py and URL pattern to urls.py')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model']
        app_label = kwargs['app']
        create_page = kwargs.get('page', False) or kwargs.get('p', False)
        create_view = kwargs.get('view', False) or kwargs.get('v', False)

        try:
            # تحميل الموديل
            model = apps.get_model(app_label, model_name)

            # توليد النموذج ديناميكيًا
            dynamic_form = generate_DformKit(model)

            # إنشاء كود النموذج
            form_code = generate_form_code(model, dynamic_form)

            # التحقق من وجود forms.py وإضافة الاستيراد إذا لزم الأمر
            forms_path = os.path.join(app_label, 'forms.py')
            FormsFileChecker.ensure_forms_import(forms_path)
            FormsFileChecker.ensure_models_import(forms_path, model_name)
            
            if FormsFileChecker.has_form_class(forms_path, model_name):
                if not FormsFileChecker.warn_and_overwrite(forms_path, model_name, form_code):
                    self.stdout.write(self.style.WARNING(f"Skipped generating form for {model_name}."))
                    return
            else:
                with open(forms_path, 'a') as f:
                    f.write('\n\n' + form_code)

            self.stdout.write(self.style.SUCCESS(f"Successfully generated form for {model_name}"))

            # إنشاء قالب HTML إذا تم طلب ذلك
            if create_page:
                template_creator = TemplateCreator(app_label, model_name)
                result = template_creator.create_template()
                self.stdout.write(self.style.SUCCESS(result))

            # إضافة دالة ومسار إذا تم طلب ذلك
            if create_view:
                app_path = os.path.join(os.getcwd(), app_label)
                ViewUrlManager.add_view_function(app_path, model_name)
                ViewUrlManager.add_url_pattern(app_path, model_name)
                self.stdout.write(self.style.SUCCESS(f"Added view function and URL pattern for {model_name}"))
                
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {str(e)}"))
