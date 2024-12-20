# DFormKit

**DFormKit** is a Python library that helps developers generate **dynamic forms** using **Django ModelForm**, with support for **validation** and **Tailwind CSS** styling.

## Features

- **Automatically generate forms from Django models**.
- **Automatic validation** based on the model fields.
- **Tailwind CSS** support for easy form styling.
- **Generate HTML pages** with forms (optional).
- **Automatically generate unit tests** for the forms.

## Installation

To install the library, run the following command:

```bash
pip install dformkit
```

## Usage

### 1. Generate a dynamic form from a Django model

To automatically generate a **ModelForm** from the `Product` model, use the following command:

```bash
python manage.py dformkit --model=Product
```

### 2. Add validation

To include **validation** for the form based on the model's constraints, use the `--validation` option:

```bash
python manage.py dformkit --model=Product --validation
```

### 3. Add Tailwind CSS styling

To add **Tailwind CSS** styling to the generated form, use the `--tailwind` option:

```bash
python manage.py dformkit --model=Product --tailwind
```

### 4. Generate the form with validation and Tailwind CSS

You can combine all options in one command:

```bash
python manage.py [dformkit] --model=Product --validation --tailwind
```

### 5. Generate HTML pages

You can also generate **HTML pages** for the forms with the `--html` option:

```bash
python manage.py dformkit --model=Product --validation --tailwind --html
```

### 6. Testing the library

To test the library, use **pytest** to run unit tests that verify its functionality:

```bash
pytest
```

## Contributing

If you'd like to contribute to the improvement of the library, follow these steps:

1. Fork the repository.
2. Create a new branch for the feature or bugfix you're working on.
3. Add tests (if applicable).
4. Submit a **Pull Request** with a description of what you've done.

## License

This project is licensed under the [MIT License](LICENSE).
