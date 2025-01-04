class FormsFileChecker:
    """
    A utility class to check and ensure required imports in the forms file.
    """

    @staticmethod
    def has_import(file_path, import_statement):
        """
        Check if the given file contains a specific import statement.

        Args:
            file_path (str): The path to the forms file to check.
            import_statement (str): The import statement to search for.

        Returns:
            bool: True if the import statement exists, False otherwise.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return import_statement in content
        except FileNotFoundError:
            return False  # الملف غير موجود يعني السطر أيضًا غير موجود
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    @staticmethod
    def ensure_forms_import(file_path):
        """
        Ensure that 'from django import forms' is present in the file.
        If not, it adds the import statement at the top of the file.

        Args:
            file_path (str): The path to the forms file.
        """
        try:
            # إذا كان الملف غير موجود، يتم إنشاؤه
            with open(file_path, 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                found_import = False

                for line in lines:
                    if line.startswith('from django import forms'):
                        found_import = True
                        break

                if not found_import:
                    lines.insert(0, 'from django import forms\n')
                    file.seek(0)
                    file.writelines(lines)
                    print("Added 'from django import forms' to the file.")
        except FileNotFoundError:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('from django import forms\n')
                print("Created file and added 'from django import forms'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def ensure_models_import(file_path, model_name):
        """
        Ensure that 'from .models import [model_name]' is present in the file.
        If not, it adds the model to the existing import or creates the line.

        Args:
            file_path (str): The path to the forms file.
            model_name (str): The model name to add to the import statement.
        """
        try:
            # إذا كان الملف غير موجود، يتم إنشاؤه
            with open(file_path, 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                found_import = False

                for i, line in enumerate(lines):
                    if line.startswith('from .models import'):
                        found_import = True
                        if model_name not in line:
                            lines[i] = line.strip() + f', {model_name}\n'
                        break

                if not found_import:
                    lines.insert(0, f'from .models import {model_name}\n')
                
                file.seek(0)
                file.writelines(lines)
                print(f"Ensured 'from .models import {model_name}' in the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def has_form_class(file_path, model_name):
        """
        Check if a form class for the given model already exists in the file.

        Args:
            file_path (str): The path to forms file to check.
            model_name (str): The name of the model to search for.
        
        Returns:
            bool: True if the form class exists, False otherwise.
        """
        form_class_name = f"class {model_name}Form"
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return form_class_name in content
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"An unecpected error occurred: {e}")
            return False
    
    @staticmethod
    def warn_and_overwrite(file_path, model_name, form_code):
        """
        Warn the user if the form class exists and prompt for overwrite.

        Args:
            file_path (str): The path to the forms file.
            model_name (str): The name of the model.

        Returns:
            bool: True if the user chooses to overwrite, False otherwise.
        """
        if FormsFileChecker.has_form_class(file_path, model_name):
            response = input(f"Warning: A form class for '{model_name}' already exists. Overwrite? (y/n): ")
            if response.lower() == 'y':
                FormsFileChecker.overwrite_form_class(file_path, model_name, form_code)
                print(f"Overwritten the form class for '{model_name}'.")
                return True
            else:
                print(f"Skipped generating form for '{model_name}'.")
                return False
        return True

    @staticmethod
    def overwrite_form_class(file_path, model_name, form_code):
        """
        Overwrite the existing form class for the given model in the file, replacing `class Meta` fields with `__all__`.

        Args:
            file_path (str): The path to the forms file.
            model_name (str): The name of the model.
            form_code (str): The new code for the form class.
        """
        form_class_name = f"class {model_name}Form"
        try:
            with open(file_path, 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                file.seek(0)
                file.truncate()  # Clear the current file content

                inside_form_class = False
                inside_meta_class = False
                updated_lines = []
                for line in lines:
                    # Check for the start of the target class
                    if line.strip().startswith(form_class_name):
                        inside_form_class = True
                        updated_lines.append(line)
                        continue

                    # If inside the target class, check for class Meta
                    if inside_form_class and line.strip().startswith("class Meta"):
                        inside_meta_class = True
                        continue

                    # If inside Meta, skip all its lines
                    if inside_meta_class:
                        if line.strip().startswith("]") or line.strip() == "":
                            inside_meta_class = False
                        continue

                    # Exit the form class when a new class is encountered
                    if inside_form_class and line.strip().startswith("class ") and not line.strip().startswith(form_class_name):
                        inside_form_class = False

                    # Keep all other lines
                    updated_lines.append(line)

                # Add the new Meta definition with `__all__`
                updated_lines.append(f"    class Meta:\n")
                updated_lines.append(f"        model = {model_name}\n")
                updated_lines.append(f"        fields = '__all__'\n")

                # Write the updated content back to the file
                file.writelines(updated_lines)
                print(f"Successfully overwritten the form class for '{model_name}', using `fields = '__all__'`.")
        except Exception as e:
            print(f"An unexpected error occurred while overwriting the form class: {e}")
