# DFormKit

**DFormKit** is a Python library designed to help Django developers **dynamically generate forms**, manage views, and streamline template creation based on Django models.

## Features

- **Dynamic Form Generation:** Automatically generate forms from Django models.
- **Template Creation:** Create HTML templates for forms.
- **View Integration:** Add view functions and URL patterns dynamically.
- **Validation Support:** Validation is automatically handled based on model constraints.
- **Customizable Templates:** Supports integrating styling frameworks like Tailwind CSS.

## Installation

To install the library, run the following command:

```bash
pip install dformkit
```

## Usage

### 1. Generate a Dynamic Form from a Django Model

Generate a **ModelForm** for a model, e.g., `Product`, using:

```bash
python manage.py dformkit --model=Product --app=your_app
```

### 2. Create a Template for the Form

To generate an **HTML template** for the form:

```bash
python manage.py dformkit --model=Product --app=your_app --page
```

or

```bash
python manage.py dformkit --model=Product --app=your_app --p
```

### 3. Add View and URL Pattern

Automatically add a **view function** and **URL pattern** for the form:

```bash
python manage.py dformkit --model=Product --app=your_app --view
```

or

```bash
python manage.py dformkit --model=Product --app=your_app --v
```

### 4. Combine All Options

You can combine form generation, template creation, and view addition in one command:

```bash
python manage.py dformkit --model=Product --app=your_app --page --view
```

### 5. Testing the Library

Run unit tests using **pytest**:

```bash
pytest
```

## Contributing

We welcome contributions! Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Write tests if applicable.
4. Submit a **Pull Request** with details about your changes.

## License

This project is licensed under the [MIT License](LICENSE).
