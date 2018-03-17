import setuptools


setuptools.setup(
    name='python-examples',
    version='0.0.1',

    author='Max Zheng',
    author_email='maxzheng.os @g gmail.com',

    description='Learn Python using code examples that you can run!',
    long_description=open('README.rst').read(),

    url='https://github.com/maxzheng/python-examples',

    install_requires=open("requirements.txt").read().split('\n'),

    license='MIT',

    packages=['examples'],
    include_package_data=True,

    python_requires='>=3.6',
    setup_requires=['setuptools-git'],

    classifiers=[
      'Development Status :: 5 - Production/Stable',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries :: Python Modules',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='learn python by example',
)
