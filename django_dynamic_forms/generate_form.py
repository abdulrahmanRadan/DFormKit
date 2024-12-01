# django_dynamic_forms/generate_form.py

from django import forms 

def generate_dynamic_form(model):
    """
    Generates a Django form dynamically based on the model's fields.
    """
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

    
    return type(f'{model.__name__}Form', (forms.Form,), form_fields)
