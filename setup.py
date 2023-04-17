from setuptools import setup, find_packages

setup(
    name='tamedai',
    version='0.1.0',
    author='TamedAI GmbH',
    author_email='maintainer@tamedai.com',
    description='A package for using the TamedAI Perceptor API',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Pillow',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
