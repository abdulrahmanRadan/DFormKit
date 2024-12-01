from setuptools import setup, find_packages

setup(
    name="django-dynamic-forms",  # اسم المكتبة
    version="0.1.0",  
    packages=find_packages(),  # العثور على جميع الحزم (داخل المكتبة)
    include_package_data=True,
    install_requires=[
        'Django>=3.0',  # الحزم الأساسية المطلوبة
        'requests',      # إذا كنت بحاجة إلى مكتبة requests أو أي حزمة أخرى
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ],
    author="abdulrahman",
    author_email="aboda123li123@gmail.com",
    description="this is django dynamic forms ",
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    # url="رابط المكتبة (إذا كنت ستنشرها)",
)
