from setuptools import setup

setup(
    name='botstat',
    version='0.0.1',
    description='Search engine analyser for nginx/apache web servers',
    long_description=open('README.md').read(),
    license='MIT',
    url='',
    author='Sergey Taran',
    author_email='taransergey@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='cli apache nginx system',
    packages=['botstat'],
    install_requires=['pyparsing'],
    entry_points={
        'console_scripts': [
            'botstat = botstat.botstat:main',
        ],
    },
)