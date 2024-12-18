import os

class TemplateCreator:
    """
    Class responsible for generating HTML templates for forms.
    """

    def __init__(self, app_label, model_name):
        self.app_label = app_label
        self.model_name = model_name

    def create_template(self):
        """
        Creates an HTML template for the model's form.
        Ensures the template is saved in the appropriate templates directory.
        """
        # البحث عن مجلد templates
        templates_path = os.path.join(self.app_label, 'templates')
        if not os.path.exists(templates_path):
            # التحقق من مجلد templates الرئيسي
            templates_path = os.path.join(os.getcwd(), 'templates')
            if not os.path.exists(templates_path):
                # إذا لم يوجد أي مجلد، قم بإنشاء مجلد templates داخل التطبيق
                templates_path = os.path.join(self.app_label, 'templates')
                os.makedirs(templates_path)

        # اسم ملف القالب
        template_file = os.path.join(templates_path, f"{self.model_name.lower()}_form.html")
        if not os.path.exists(template_file):
            # محتوى القالب
            template_content = (
                f"<!DOCTYPE html>\n"
                f"<html lang='en'>\n"
                f"<head>\n"
                f"    <meta charset='UTF-8'>\n"
                f"    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
                f"    <title>{self.model_name} Form</title>\n"
                f"</head>\n"
                f"<body>\n"
                f"    <h1>{self.model_name} Form</h1>\n"
                f"    <form method='post'>\n"
                f"        {{% csrf_token %}}\n"
                f"        {{% for field in form %}}\n"
                f"            <div>\n"
                f"                {{{{ field.label_tag }}}}<br>\n"
                f"                {{{{ field }}}}\n"
                f"                {{% if field.errors %}}\n"
                f"                <p style='color: red'>\n"
                f"                {{{{ field.errors }}}}</p>\n"
                f"                {{% endif %}}\n"
                f"            </div>\n"
                f"        {{% endfor %}}\n"
                f"        <button type='submit'>Submit</button>\n"
                f"    </form>\n"
                f"</body>\n"
                f"</html>"
            )

            # حفظ القالب
            with open(template_file, 'w') as f:
                f.write(template_content)

            return f"Template created: {template_file}"
        else:
            return f"Template already exists: {template_file}"
