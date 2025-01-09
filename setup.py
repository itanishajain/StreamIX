from setuptools import setup, find_packages

setup(
    name="streamix",
    version="6.0",
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
    ],
    entry_points={
        "console_scripts": [
            "streamix=streamix.index:main",  # Corrected entry point
        ],
    },
    author="Tanisha Jain",
    author_email="itanishajain@gmail.com",
    description="Streamix: A tool for downloading YouTube videos and audio",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/itanishajain/StreamIX",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)