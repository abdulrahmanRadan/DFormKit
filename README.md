# DFormKit

**DFormKit** is a Python library designed to help Django developers **dynamically generate forms**, manage views, and streamline template creation based on Django models.

---

## Why DFormKit?

This command-line wizard lets you **dynamically generate forms, templates, views, and URL patterns** for your Django models straight from your Terminal. It works seamlessly on Windows, Mac, and Linux, so you can use it on any platform.

While other tools make you wade through a swamp of settings and configurations, **DFormKit** keeps it simple. Just specify your app and model, and voilà! It’ll take you on a smooth ride to creating dynamic forms, no complex options needed—just fun coding! 🔥

---

## Features

- **Dynamic Form Generation:** Automatically generate forms from Django models.
- **Template Creation:** Create HTML templates for forms.
- **View Integration:** Add view functions and URL patterns dynamically.
- **Customizable Templates:** Supports integrating styling frameworks like Tailwind CSS.

---

## 🛠️ Installation

1. Install the library using `pip`:

   ```bash
   pip install dformkit
   ```

2. Add `'dformkit'` to `INSTALLED_APPS` in your Django project's `settings.py` file:

   ```python
   INSTALLED_APPS = [
       ...,
       'dformkit',
   ]
   ```

   - image showing the addition of `'dformkit'` to `INSTALLED_APPS` in `settings.py`.

## ![settings](https://raw.githubusercontent.com/abdulrahmanRadan/DFormKit/main/images/installed_app.png)

## 📈 Upgrade

Stay in the loop with the latest features on GitHub! To upgrade your **DFormKit** tool, simply run:

```bash
pip install --upgrade dformkit
```

Then you’re all set to keep generating dynamic forms from your Terminal! 🥳

---

## 🦸 Quick Start

Getting started with **DFormKit** is a piece of cake! Just use the following command style:

```bash
python manage.py dformkit myapp Person
```

**Note:**

- Replace `myapp` with your Django app name.
- Replace `Person` with your model name.

If you don’t specify additional options, it’ll generate a dynamic form for the model and save it in `forms.py`. Easy-peasy!

---

## 👨‍💻 Usage

### Arguments

| Argument | Description                                                     |
| -------- | --------------------------------------------------------------- |
| `app`    | The name of your Django app. This argument is **[Required]**.   |
| `model`  | The name of your Django model. This argument is **[Required]**. |

### Options

| Option           | Description                                                              |
| ---------------- | ------------------------------------------------------------------------ |
| `-page` or `--p` | Generate an HTML template for the form.                                  |
| `-view` or `--v` | Add a view function to `views.py` and a URL pattern to `urls.py`.        |
| `--pv` or `--vp` | Combine all options: generate the form, template, view, and URL pattern. |

---

## Examples

### 1. Generate a Form Only

```bash
python manage.py dformkit myapp Person
```

- **What it does:** Generates a dynamic form for the `Person` model in the `myapp` application.
- **Output:** The form is saved in `forms.py`.

---

### 2. Generate a Form and Template

```bash
python manage.py dformkit myapp Person -page
```

or

```bash
python manage.py dformkit myapp Person --p
```

- **What it does:** Generates the form and an HTML template for it.
- **Output:** The form is saved in `forms.py`, and the template is saved in the `templates` folder.

- This is the code generated with this command in templates/[formname]\_form.html

## ![htmlfile](https://raw.githubusercontent.com/abdulrahmanRadan/DFormKit/main/images/htmlform.png)

---

### 3. Generate a Form, View, and URL Pattern

```bash
python manage.py dformkit myapp Person -view
```

or

```bash
python manage.py dformkit myapp Person --v
```

- **What it does:** Generates the form, adds a view function to `views.py`, and adds a URL pattern to `urls.py`.
- **Output:** The form, view, and URL pattern are created.

![urlviewfile](https://raw.githubusercontent.com/abdulrahmanRadan/DFormKit/main/images/urls.py.png)
![urlviewfile](https://raw.githubusercontent.com/abdulrahmanRadan/DFormKit/main/images/views-py.png)

---

### 4. Combine All Options

```bash
python manage.py dformkit myapp Person --pv
```

or

```bash
python manage.py dformkit myapp Person --vp
```

- **What it does:** Combines all the above steps into one command.
- **Output:** The form, template, view, and URL pattern are generated.

- this is the new form code in forms.py when use this command

## ![image](https://raw.githubusercontent.com/abdulrahmanRadan/DFormKit/main/images/forms.py.png)

## 🧰 Additional Features

### Using Named Arguments

You can use named arguments for more flexibility. For example:

```bash
python manage.py dformkit -app=myapp -model=Person -view
```

or

```bash
python manage.py dformkit -app=myapp -model=Person --pv
```

- **What it does:** Works the same as positional arguments but provides a more explicit way to specify the app and model.

---

### Overwriting Existing Forms

If the form already exists in `forms.py`, the library will warn you before overwriting it. You can choose to proceed or skip.

---

### Customizing Templates

The generated templates are fully customizable. You can integrate styling frameworks like **Tailwind CSS** or **Bootstrap** by modifying the generated HTML files.

---

## Testing the Library

You can run unit tests using **pytest**:

```bash
pytest
```

---

## Contributing

We welcome contributions! Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Write tests if applicable.
4. Submit a **Pull Request** with details about your changes.

---

## ❓ Frequently Asked Questions (FAQ)

### 1. What happens if the form already exists in `forms.py`?

- If the form already exists, the library will warn you before overwriting it. You can choose to proceed or skip.

### 2. Can I customize the generated templates?

- Yes, the generated templates are fully customizable. You can integrate styling frameworks like Tailwind CSS or Bootstrap.

### 3. How do I add validation to the form?

- Validation is automatically handled based on the constraints defined in your Django model (e.g., `max_length`, `null`, `blank`, etc.).

---

## 🚀 Conclusion

**DFormKit** simplifies the process of generating forms, templates, views, and URL patterns in Django. By following the steps above, you can quickly set up dynamic forms for your models and streamline your development workflow.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
