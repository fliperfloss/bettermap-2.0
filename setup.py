from setuptools import setup, find_packages

setup(
    name="bettertest",
    version="0.2",
    description="A script for running Nmap and SSLScan scans with a user-friendly interface.",
    author="biskit",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=[
        'colorama>=0.4.4',  # For colored terminal output
    ],
    entry_points={
        'console_scripts': [
            'scantool = scantool:main_menu',  # Replace 'scantool' with your script name if needed
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
