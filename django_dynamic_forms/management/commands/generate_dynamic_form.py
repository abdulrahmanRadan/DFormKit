from django.core.management.base import BaseCommand
from django.apps import apps
from pathlib import Path

class Command(BaseCommand):
    help = "Generates a dynamic form for a given model."

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str, help='Specify the model for which to generate the form.')
        parser.add_argument('--app', type=str, help='App name where the model exists.')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model']
        app_label = kwargs['app']

        if not model_name or not app_label:
            self.stderr.write(self.style.ERROR("Please provide both --model and --app arguments."))
            return

        try:
            # Retrieve the model dynamically
            model = apps.get_model(app_label, model_name)
        except LookupError as e:
            self.stderr.write(self.style.ERROR(f"Model {model_name} not found in app {app_label}."))
            return

        # Generate form code
        form_name = f"{model_name}Form"
        fields = [field.name for field in model._meta.fields if field.editable]
        form_code = f"\n\nclass {form_name}(forms.ModelForm):\n"
        form_code += f"    class Meta:\n        model = {model_name}\n        fields = {fields}\n"

        for field in fields:
            form_code += f"    {field} = forms.CharField(required=True)\n"

        # Append form to forms.py without overwriting the existing content
        forms_path = Path(f"{app_label}/forms.py")
        if not forms_path.exists():
            forms_path.touch()  # Create the file if it doesn't exist
            forms_path.write_text("from django import forms\n")  # Add the header

        with forms_path.open("r+") as f:
            existing_content = f.read()
            if form_name in existing_content:
                self.stdout.write(self.style.WARNING(f"Form {form_name} already exists. Skipping generation."))
                return
            f.write(form_code)

        self.stdout.write(self.style.SUCCESS(f"Successfully added form for {model_name} to {forms_path}."))
