from setuptools import setup, find_packages

setup(
    name="dformkit",
    version="0.1.0",
    author="Abdulrahman Radan",
    author_email="abdulrahmanraadan@gmail.com",
    description="A Django library for generating dynamic forms, views, and templates.",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords=[
        "django",
        "dynamic forms",
        "django forms",
        "form generation",
        "web development",
        "dynamic templates",
    ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "Django>=3.0",
    ],
    entry_points={
        "console_scripts": [
            "dformkit=dformkit.cli:main",
        ],
    },
    project_urls={
        "Author": "https://github.com/abdulrahmanRadan",
        "Homepage": "https://github.com/abdulrahmanRadan/dformkit",
        "Bug Tracker": "https://github.com/abdulrahmanRadan/dformkit/issues",
        "Source Code": "https://github.com/abdulrahmanRadan/dformkit",
        "Documentation": "https://github.com/abdulrahmanRadan/dformkit#readme",
    },
    platforms=["Linux", "Windows", "MacOS"],
    packages=find_packages(),
)
