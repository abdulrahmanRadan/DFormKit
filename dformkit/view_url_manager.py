import os 
class ViewUrlManager:
    """
    A utility class to add view function to views.py and routes to urls.py.
    """
    @staticmethod
    def add_view_function(app_path, model_name):
        """
        Add a view function to views.py to render the form.
        """
        view_function = f"""
def {model_name.lower()}_view(request):
    from .forms import {model_name}Form
    if request.method == 'POST':
        form = {model_name}Form(request.POST)
        if form.is_valid():
            # Process the form data here
            pass
    else:
        form = {model_name}Form()
    return render(request, '{model_name.lower()}_form.html', {{'form': form}})
"""
        views_path = os.path.join(app_path, 'views.py')
        try:
            with open(views_path, 'a+', encoding='utf-8') as file:
                file.seek(0)
                content = file.read()
                if f"def {model_name.lower()}_view" not in content:
                    file.write('\n' + view_function)
                    print(f"Added view function for {model_name}  in views.py")
                else:
                    print(f"view function for {model_name} already exists in views.py")
                
        except FileNotFoundError:
            with open(views_path, 'w', encoding='utf-8') as file:
                file.write(view_function)
                print(f"Created views.py and added view function for {model_name}.")
    @staticmethod
    def add_url_pattern(app_path, model_name):
        """
        Add a URL pattern to urls.py for the view function.

        Args:
            app_path (str): The path to the app folder.
            model_name (str): The name of the model for the form.
        """
        url_pattern = f"""
    path('{model_name.lower()}/', views.{model_name.lower()}_view, name='{model_name.lower()}'),
"""

        urls_path = os.path.join(app_path, 'urls.py')
        try:
            with open(urls_path, 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                file.seek(0)
                imported_views = any('from . import views' in line for line in lines)
                for line in lines:
                    file.write(line)
                    if 'urlpatterns' in line:
                        file.write(url_pattern)
                if not imported_views:
                    file.seek(0)
                    content = file.read()
                    file.seek(0)
                    file.write('from . import views\n' + content)
                print(f"Added URL pattern for {model_name} in urls.py.")
        except FileNotFoundError:
            with open(urls_path, 'w', encoding='utf-8') as file:
                file.write("from . import views\n")
                file.write("from django.urls import path\n\n")
                file.write("urlpatterns = [\n")
                file.write(url_pattern)
                file.write("]\n")
                print(f"Created urls.py and added URL pattern for {model_name}.")
