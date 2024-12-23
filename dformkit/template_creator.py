import os

class TemplateCreator:
    """
    Class responsible for generating HTML templates for forms with Tailwind CSS styling.
    """

    def __init__(self, app_label, model_name):
        self.app_label = app_label
        self.model_name = model_name

    def create_template(self):
        """
        Creates an HTML template for the model's form with Tailwind CSS styling.
        Ensures the template is saved in the appropriate templates directory.
        """
        # تحديد مسار مجلد القوالب
        templates_path = os.path.join(self.app_label, 'templates')
        if not os.path.exists(templates_path):
            templates_path = os.path.join(os.getcwd(), 'templates')
            if not os.path.exists(templates_path):
                os.makedirs(templates_path)

        # تحديد مسار ملف القالب
        template_file = os.path.join(templates_path, f"{self.model_name.lower()}_form.html")

        if not os.path.exists(template_file):
            # محتوى القالب
            template_content = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{self.model_name} Form</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      /* Backup formats */
      .container {{
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        width: 100%;
      }}
      .text-2xl {{
        font-size: 1.5rem;
      }}
      .font-bold {{
        font-weight: bold;
      }}
      .mb-4 {{
        margin-bottom: 1rem;
      }}
      .text-center {{
        text-align: center;
      }}
      .space-y-4 > * + * {{
        margin-top: 1rem;
      }}
      .flex {{
        display: flex;
      }}
      .flex-col {{
        flex-direction: column;
      }}
      .justify-center {{
        justify-content: center;
      }}
      .bg-white {{
        background-color: #ffffff;
      }}
      .p-6 {{
        padding: 1.5rem;
      }}
      .rounded-lg {{
        border-radius: 0.5rem;
      }}
      .shadow-lg {{
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
          0 4px 6px -2px rgba(0, 0, 0, 0.05);
      }}
      .w-full {{
        width: 100%;
      }}
      .max-w-prose {{
        max-width: 65ch;
      }}
      .invalid-feedback {{
        color: red;
        margin-top: 5px;
        font-size: 0.875em;
        background-color: red;
      }}
      .py-2 {{
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
      }}
      .px-4 {{
        padding-left: 1rem;
        padding-right: 1rem;
      }}
      .bg-blue-500 {{
        background-color: #3b82f6;
      }}
      .text-white {{
        color: #ffffff;
      }}
      .font-semibold {{
        font-weight: 600;
      }}
      .rounded-md {{
        border-radius: 0.375rem;
      }}
      .shadow-sm {{
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      }}
      .hover\\:bg-blue-700:hover {{
        background-color: #1d4ed8;
      }}
      .focus\\:outline-none:focus {{
        outline: none;
      }}
      .focus\\:ring-2:focus {{
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.5);
      }}
      .focus\\:ring-indigo-500:focus {{
        border-color: #6366f1;
      }}
      .focus\\:ring-offset-2:focus {{
        margin-right: 0.5rem;
      }}
      .bg-gray-100 {{
        background-color: #f3f4f6;
      }}
      .border {{
        border-width: 1px;
        border-color: rgb(60, 164, 130);
      }}
      .mx-2 {{
        margin-left: 0.5rem;
        margin-right: 0.5rem;
      }}
      .px-2 {{
        padding-left: 0.5rem;
        padding-right: 0.5rem;
      }}
      .font-medium {{
        font-weight: 500;
      }}
      .items-center {{
        align-items: center;
      }}
      .m-2 {{
        margin: 0.5rem;
      }}
      .mt-3 {{
        margin-top: 0.75rem;
      }}
      input {{
        height: 30px;
      }}
      .errorlist {{
        text-align: center;
        list-style-type: none;
      }}
      .errorlist li {{
        background-color: rgb(230, 29, 29);
        margin: 0px 5px;
        color: rgb(63, 60, 60);
        padding: 5px;
        border-radius: 4px;
      }}
    </style>
  </head>
  <body class="bg-gray-100 w-full flex justify-center items-center m-2 mt-3">
    <div class="container bg-white p-6 rounded-lg shadow-lg w-full max-w-prose">
      <h1 class="text-2xl font-bold mb-4 text-center">{self.model_name} Form</h1>
      <form method="post" class="space-y-4">
        {{% csrf_token %}}
        {{% for field in form %}}
        <div class="form-group flex flex-col justify-center">
          {{{{ field.label_tag }}}}
          {{{{ field }}}}
          {{% if field.errors %}}
          <p class="invalid-feedback text-sm mt-1">{{{{ field.errors }}}}</p>
          {{% endif %}}
        </div>
        {{% endfor %}}
        <button
          type="submit"
          class="w-full py-2 px-4 bg-blue-500 text-white font-semibold rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          Submit
        </button>
      </form>
    </div>
  </body>
</html>
"""
            # كتابة القالب في الملف
            with open(template_file, 'w') as f:
                f.write(template_content)
                
            self.add_form_customizations()
            return f"Template created: {template_file}"
        else:
            return f"Template already exists: {template_file}"

    
    def add_form_customizations(self):
      """
      Adds customizations to the form in forms.py only for fields present in the model.
      """
      forms_path = os.path.join(self.app_label, 'forms.py')
      if not os.path.exists(forms_path):
          print(f"Error: forms.py not found in {self.app_label}.")
          return

      from django.db import models
      from django import forms
      from importlib import import_module

      # استيراد الموديل للحصول على الحقول
      try:
          model_module = import_module(f"{self.app_label}.models")
          model_class = getattr(model_module, self.model_name)
      except (ModuleNotFoundError, AttributeError) as e:
          print(f"Error: Could not load model {self.model_name} from {self.app_label}. ({e})")
          return

      with open(forms_path, 'r+', encoding='utf-8') as file:
          lines = file.readlines()
          file.seek(0)
          inside_form_class = False
          updated_lines = []
          found_model_form = False
          added_init_method = False

          # استخراج الحقول من الموديل
          model_fields = {field.name: field for field in model_class._meta.fields}

          for line in lines:
              if f"class {self.model_name}Form" in line:
                  inside_form_class = True
                  found_model_form = True

              if inside_form_class and "class Meta" in line and not added_init_method:
                  added_init_method = True
                  updated_lines.append("    error_css_class = 'error'\n")
                  updated_lines.append("\n    def __init__(self, *args, **kwargs):\n")
                  updated_lines.append("        super().__init__(*args, **kwargs)\n")

                  # تحديث التنسيقات بناءً على أنواع الحقول
                  for field_name, field in model_fields.items():
                      field_type = type(field).__name__
                      if field_type == 'CharField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'bg-gray-100 border mx-2 px-2 rounded-md font-medium'}})\n")
                      elif field_type == 'EmailField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'bg-gray-100 border mx-2 px-2 rounded-md'}})\n")
                      elif field_type == 'TextField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'bg-gray-100 border mx-2 px-2 rounded-md'}})\n")
                      elif field_type == 'DateField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'bg-gray-100 border mx-2 px-2 rounded-md', 'type': 'date'}})\n")
                      elif field_type == 'FileField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'bg-gray-100 border mx-2 px-2 rounded-md'}})\n")
                      elif field_type == 'IntegerField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'bg-gray-100 border mx-2 px-2 rounded-md'}})\n")
                      elif field_type == 'URLField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'bg-gray-100 border mx-2 px-2 rounded-md'}})\n")
                      elif field_type == 'BooleanField':
                          updated_lines.append(f"        self.fields['{field_name}'].widget.attrs.update({{'class': 'form-checkbox bg-gray-100 border mx-2 px-2 rounded-md'}})\n")

              updated_lines.append(line)

          if not found_model_form:
              print(f"Warning: {self.model_name}Form not found in forms.py.")

          file.seek(0)
          file.truncate()
          file.writelines(updated_lines)

          print(f"Customizations applied to fields: {', '.join(model_fields.keys())}.")
