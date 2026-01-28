from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cybersecurity-toolkit",
    version="1.0.0",
    author="Cybersecurity Expert Team",
    author_email="security@example.com",
    description="A comprehensive Python-based cybersecurity toolkit for penetration testing and vulnerability assessment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cybersecurity-toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: System :: Networking",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cybersecurity-toolkit=main:main",
        ],
    },
    include_package_data=True,
    keywords="cybersecurity penetration-testing vulnerability-assessment security",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/cybersecurity-toolkit/issues",
        "Source": "https://github.com/yourusername/cybersecurity-toolkit",
        "Documentation": "https://github.com/yourusername/cybersecurity-toolkit/wiki",
    },
)
