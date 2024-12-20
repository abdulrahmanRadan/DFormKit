from django import forms

def generate_DformKit(model):
    """
    Generates a Django ModelForm dynamically based on the model's fields.
    """
    fields = model._meta.fields  # جلب جميع الحقول من الـ Model
    included_fields = [field.name for field in fields if field.editable]

    # إنشاء Meta class لنموذج النموذج 
    form_meta = type('Meta', (), {'model': model, 'fields': included_fields})


    # إنشاء نموذج ModelForm ديناميكي
    return type(f'{model.__name__}Form', (forms.ModelForm,), {'Meta': form_meta})

def generate_DformKit(model):
    """
    Generates a Django ModelForm dynamically based on the model's fields.
    """
    fields = model._meta.fields  # جلب جميع الحقول من الـ Model
    included_fields = [field.name for field in fields if field.editable]

    # إنشاء Meta class لنموذج النموذج
    form_meta = type('Meta', (), {'model': model, 'fields': included_fields})
    
    # إنشاء نموذج ModelForm ديناميكي
    return type(f'{model.__name__}Form', (forms.ModelForm,), {'Meta': form_meta})


def generate_form_code(model, dynamic_form):
    """
    Generates the code for the form class based on the dynamic form.
    """
    form_code = f'class {model.__name__}Form(forms.ModelForm):\n'
    form_code += '    class Meta:\n'
    form_code += f'        model = {model.__name__}\n'
    form_code += '        fields = [\n'
    form_code += ''.join([f'            "{field_name}",\n' for field_name in dynamic_form.base_fields.keys()])
    form_code += '        ]\n'
    return form_code
