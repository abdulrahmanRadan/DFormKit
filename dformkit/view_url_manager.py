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
        url_pattern = f"    path('{model_name.lower()}/', views.{model_name.lower()}_view, name='{model_name.lower()}'),\n"
        urls_path = os.path.join(app_path, 'urls.py')

        try:
            with open(urls_path, 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                file.seek(0)
                inside_urlpatterns = False
                urlpatterns_start = None
                urlpatterns_end = None

                # Find where urlpatterns starts and ends
                for i, line in enumerate(lines):
                    if 'urlpatterns' in line:
                        inside_urlpatterns = True
                        urlpatterns_start = i + 1  # Start after 'urlpatterns = ['
                    elif inside_urlpatterns and ']' in line:
                        urlpatterns_end = i
                        inside_urlpatterns = False

                # إذا لم يكن هناك urlpatterns، يتم إضافة قائمة جديدة بالكامل
                if urlpatterns_start is None or urlpatterns_end is None:
                    file.seek(0)
                    file.write("from . import views\n")
                    file.write("from django.urls import path\n\n")
                    file.write("urlpatterns = [\n")
                    file.write(url_pattern)
                    file.write("]\n")
                    print(f"Created urlpatterns and added URL pattern for {model_name} in urls.py.")
                    return

                # Check for duplicates inside urlpatterns
                existing_paths = set()
                for i in range(urlpatterns_start, urlpatterns_end):
                    line = lines[i]
                    if 'path(' in line:
                        start = line.find("'") + 1
                        end = line.find("'", start)
                        if start > 0 and end > start:
                            existing_paths.add(line[start:end])

                if model_name.lower() + '/' not in existing_paths:
                    # Add the new path before the closing bracket of urlpatterns
                    lines.insert(urlpatterns_end, url_pattern)
                    file.seek(0)
                    file.truncate()
                    file.writelines(lines)
                    print(f"Added URL pattern for {model_name} in urls.py.")
                else:
                    print(f"URL pattern for {model_name} already exists in urls.py.")

        except FileNotFoundError:
            with open(urls_path, 'w', encoding='utf-8') as file:
                file.write("from . import views\n")
                file.write("from django.urls import path\n\n")
                file.write("urlpatterns = [\n")
                file.write(url_pattern)
                file.write("]\n")
                print(f"Created urls.py and added URL pattern for {model_name}.")
