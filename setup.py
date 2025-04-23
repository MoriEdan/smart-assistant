from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smart-assistant",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A powerful and flexible AI assistant system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/smart-assistant",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "google-generativeai>=0.8.5",
        "browser-use>=0.1.41",
        "playwright>=1.51.0",
        "open-interpreter>=0.4.3",
        "vosk>=0.3.45",
        "SpeechRecognition>=3.14.2",
        "pyttsx3>=2.98",
        "python-dotenv>=1.1.0",
        "pydantic>=2.11.3",
        "rich>=14.0.0",
        "typer>=0.15.2",
        "jsonschema>=4.23.0",
        "uv>=0.6.16",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "smart-assistant=main:main",
        ],
    },
    package_data={
        "smart_assistant": [
            "data/*",
            "config/*",
        ],
    },
    include_package_data=True,
) 