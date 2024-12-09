from setuptools import setup, find_packages

setup(
    name="ModeloDeClientes",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'main = main:start',
        ],
    },
    author="Solange Mac Intyre",
    author_email="macintyre.sj@gmai.com",
    description="Paquete de modelado de clientes en una página de compras",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    #url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
