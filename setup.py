from setuptools import setup


setup(
    name='pyramid_ssh_crochet',
    description='SSH into a running Pyramid app using crochet',
    long_description=open('README.rst').read().strip(),
    version='0.0.0',
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    license='MIT',
    url='https://github.com/msabramo/pyramid_ssh_crochet',
    py_modules=['pyramid_ssh_crochet'],
    zip_safe=False,
    install_requires=[
        'crochet',
        'pyasn1',
        'PyCrypto',
        'pyramid',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
    ],
)
