form django.core.management.base import BaseCommand
form django_dynamic_forms.generate_dynamic_form import generate_dynamic_form

class Command(BaseCommand):
    help = 'Generates dynamic form based on the model'

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str, help='model name')
        parser.add_argument('--app', type=str, help='App label')

    def handle(slef, *args, **kwargs):
        model_name = kwargs['model']
        app_label = kwargs['app']

        generate_dynamic_form(model_name, app_label)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated form for {model_name} in app {app_label}'))