#### Django Form Dynamic Todo:

- [x] Check if the forms file contains `from django import forms` and not write it again.
- [x] Check if the forms file contains `from .models import [any value]`, and if not, add the line with the model name replacing `[any value]`.
- [x] If the file already contains that line but imports a different model, append the current model name to the existing line.
- [x] Check whether the forms file contains a form class for the same model, show a warning, and ask in the terminal whether to perform a replacement or not.
- [x] Change the generation of HTML form interfaces from `--v` or `--view` to `-page` or `-p`.
- [x] Make the `-view` or `--v` argument in the terminal consistent.

#### New Tasks:

- [x] Ensure the interfaces are automatically styled using Tailwind CSS.

---

- [x] Change the name of project
