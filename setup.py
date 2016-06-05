from setuptools import setup

setup(
    name='vclock',
    version='0.1.0',
    description='vector clock library',
    url='https://github.com/eugene-eeo/vclock',
    author='Eeo Jun',
    author_email='141bytes@gmail.com',
    package_data={'vclock': ['LICENSE', 'README']},
    include_package_data=True,
    license='MIT',
    py_modules=['vclock'],
)
