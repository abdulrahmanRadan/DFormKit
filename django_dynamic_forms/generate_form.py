# django_dynamic_forms/generate_form.py

from django import forms 
from django.apps import apps
import os

def generate_dynamic_form(model_name, app_label):
    """
    Generates a Django form dynamically based on the model's fields.
    and writes it to forms.py
    """
    model = apps.get_model(app_label, model_name)
    fields = model._meta.fields
    form_fields = {}

    for field in fields:
        field_name = field.name
        field_type = field.get_internal_type()

        if field_type == 'CharField':
            form_fields[field_name] = forms.CharField(max_length=255)
        elif field_type == 'IntegerField':
            form_fields[field_name] = forms.IntegerField()
        elif field_type == 'DateField':
            form_fields[field_name] = forms.DateField()
    
    form_class = type(f'{model.__name__}ModelForm', (forms.ModelForm,),{
        'Meta': type('Meta', (), {
            'model':model,
            'fields': [field.name for field in fields]
        })
    })

    #  Specify the path where the generated code is saved in Forms.py
    forms_file_path = os.path.join('django_dynamic_forms', 'forms.py')

    with open(forms_file_path, 'a') as f:
        f.write(f"\n\n# Generated ModelForm for {model.__name__}\n")
        f.write(f"class {model.__name__}ModelForm(forms.modelForm):\n")
        f.write(f"  class Meta:\n")
        f.write(f"      model = {model.__name__}\n")
        f.write(f"      fields = {str([field.name for field in fields])}\n")
    
    return form_class
