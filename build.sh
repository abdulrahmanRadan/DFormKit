#!/bin/bash

# تنظيف المجلدات القديمة
rm -rf build dist

# بناء الحزمة
python -m build

# تحميل الحزمة إلى PyPI
twine upload dist/*