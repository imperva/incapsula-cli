import setuptools
from cwafcli import __version__

setuptools.setup(
    name='cwaf-cli',
    version=__version__,
    packages=setuptools.find_namespace_packages(),
    entry_points={
        "console_scripts": [
            "incap=cwafcli.__main__:main"
        ]
    },
    install_requires=['requests'],
    python_requires='>=3.6',
    url='https://github.com/imperva/incapsula-cli',
    license='Imperva-Community Developer License',
    author='Joe Moore',
    author_email='joe.moore@imperva.com',
    description="Command-line used to interact with Imperva's Cloud-WAF",
    long_description='This application provides a simple to use CLI that reflects industry standards '
                '(such as the AWS cli), and enables customers to easily integrate into configurations '
                'management, orchestration or automation frameworks to support the DevOps model.',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
