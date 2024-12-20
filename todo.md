#### Django Form Dynamic Todo:

- [x] Check if the forms file contains `from django import forms` and not write it again.
- [ ] Check if the forms file contains `from .models import [any value]`, and if not, add the line with the model name replacing `[any value]`.
- [ ] If the file already contains that line but imports a different model, append the current model name to the existing line.
- [ ] Check whether the forms file contains a form class for the same model, show a warning, and ask in the terminal whether to perform a replacement or not.
- [ ] Make the `--view` or `--v` argument in the terminal consistent.
- [ ] Modify the form page in `.html`.

#### New Tasks:

- [ ] Customize the form validation for `name = forms.CharField(required=True)` to make it optional unless `--v` or `--validation` is specified.
- [ ] Change the generation of HTML form interfaces from `--v` or `--view` to `--html` or `--h`.
- [ ] Ensure the interfaces are automatically styled using Tailwind CSS.

---

- [x] Change the name of project
