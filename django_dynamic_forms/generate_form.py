from django import forms

def generate_dynamic_form(model):
    """
    Generates a Django ModelForm dynamically based on the model's fields.
    """
    fields = model._meta.fields  # جلب جميع الحقول من الـ Model
    form_fields = {}

    # قائمة الحقول التي سيتم تضمينها في النموذج
    included_fields = []

    for field in fields:
        field_name = field.name
        field_type = field.get_internal_type()

        # تجاهل الحقول غير القابلة للتعديل مثل `created_at` أو الحقول التي هي `auto_now`
        if field.editable:
            included_fields.append(field_name)

            # تخصيص نوع الحقل بناءً على نوعه في الـ Model
            if field_type == 'CharField':
                form_fields[field_name] = forms.CharField(max_length=field.max_length, required=field.blank)
            elif field_type == 'IntegerField':
                form_fields[field_name] = forms.IntegerField(required=field.blank)
            elif field_type == 'DecimalField':
                form_fields[field_name] = forms.DecimalField(max_digits=field.max_digits, decimal_places=field.decimal_places, required=field.blank)
            elif field_type == 'TextField':
                form_fields[field_name] = forms.CharField(widget=forms.Textarea, required=field.blank)
            elif field_type == 'DateTimeField':
                form_fields[field_name] = forms.DateTimeField(required=field.blank)

    # توليد نموذج باستخدام ModelForm مع الحقول المعدلة
    return type(f'{model.__name__}Form', (forms.ModelForm,), {'Meta': type('Meta', (), {'model': model, 'fields': included_fields})})
