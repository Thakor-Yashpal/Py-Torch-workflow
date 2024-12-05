from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Py-Torch-workflow", 
    version="0.1.0", 
    author="Yashpalsinh",
    author_email="itachia755@gmai.com",
    description="This a simple projects for learning pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    url="https://github.com/Thakor-Yashpal/Py-Torch-workflow",  
    packages=find_packages(exclude=["tests", "notebooks", "docs"]), #  Don't include test files, etc.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    install_requires=[  
        "torch",
        "torchvision",
        "numpy",
    ],
    python_requires=">=3.7",  
    extras_require={ 
        "dev": ["pytest", "flake8", "mypy"], 
    },
    entry_points={  
        "console_scripts": [
            "my_script = my_pytorch_project.scripts.my_script:main",
        ],
    },
)
# Add next f1