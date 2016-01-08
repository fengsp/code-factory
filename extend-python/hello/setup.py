from setuptools import setup, Extension


setup(
    name="hello-extension",
    version='0.0.1',
    ext_modules=[Extension("hello", ["hellomodule.c"])]
)
