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
