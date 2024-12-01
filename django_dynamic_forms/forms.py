# django_dynamic_forms/forms.py

from django import forms
from .generate_dynamic_form import generate_dynamic_form
from .models import Product

ProductForm = generate_dynamic_form(Product)