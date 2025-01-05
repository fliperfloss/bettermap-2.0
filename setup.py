from setuptools import setup, find_packages

setup(
    name="NmapSSLScanTool",  # Name of your tool
    version="1.0.0",  # Version number
    description="A tool for running Nmap and SSLScan with enhanced features.",
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    url="https://github.com/yourusername/yourrepository",  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        "colorama",  # This is the only external dependency
    ],
    entry_points={
        "console_scripts": [
            "nmap-sslscan-tool = your_script_name:main_menu",  # Replace 'your_script_name' with the actual name of your script
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust the license as needed
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
