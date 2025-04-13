# aiflow/setup.py
from setuptools import setup, find_packages

setup(
    name="aiflow",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "pytest>=7.0.0",
    ],
    entry_points={
        'console_scripts': [
            'aiflow=aiflow.cli:main',
        ],
    },
    author="AIFlow Developer",
    author_email="example@example.com",
    description="A language for AI workflows",
    long_description=open("README.md").read() if hasattr(__file__, "read") else "",
    long_description_content_type="text/markdown",
    keywords="ai, workflow, language",
    url="https://github.com/example/aiflow",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)