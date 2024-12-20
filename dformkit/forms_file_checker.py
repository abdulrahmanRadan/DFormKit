class FormsFileChecker:
    """
    A utility class to check if 'from django import forms' exists in the forms file.
    """

    @staticmethod
    def has_forms_import(file_path):
        """
        Check if the given file contains 'from django import forms'.

        Args:
            file_path (str): The path to the forms file to check.

        Returns:
            bool: True if the import statement exists, False otherwise.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return 'from django import forms' in content
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
            return False
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
        if not FormsFileChecker.has_forms_import(file_path):
            try:
                with open(file_path, 'r+', encoding='utf-8') as file:
                    content = file.read()
                    file.seek(0, 0)
                    file.write('from django import forms\n' + content)
                    print("Added 'from django import forms' to the file.")
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' does not exist.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
