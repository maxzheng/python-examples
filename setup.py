from pip.req import parse_requirements
import setuptools


# Filters out relative/local requirements (i.e. ../lib/utils)
remote_requirements = '\n'.join(str(r.req) for r in parse_requirements("requirements.txt", session='dummy') if r.req)

setuptools.setup(
    name='python-examples',
    version='0.0.1',

    author='Max Zheng',
    author_email='maxzheng.os @g gmail.com',

    description='Learn Python using code examples that you can run!',
    long_description=open('README.rst').read(),

    url='https://github.com/maxzheng/python-examples',

    install_requires=remote_requirements,

    license='MIT',

    packages=setuptools.find_packages(),
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
