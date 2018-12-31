from setuptools import setup

setup(
    name='pdfsm',
    version='0.0.1',
    description='PDF file Split and Merge tool',
    url='https://github.com/gaborvecsei',
    author='Gabor Vecsei',
    author_email='vecseigabor.x@gmail.com',
    license='MIT',
    install_requires=['PyPDF2'],
    packages=["pdfsm"],
    entry_points={
        'console_scripts': [
            'pdfsm = pdfsm.pdf_split_merge:split_and_merge'
        ]
    }
)
