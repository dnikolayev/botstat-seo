from setuptools import setup

setup(
    name='botstat',
    version='0.1.3',
    description='Search engine analyser for nginx/apache web servers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://www.endurantdevs.com',
    author='Endurant Devs',
    author_email='info@endurantdevs.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='cli apache nginx system',
    packages=['botstat'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=['pyparsing', 'dateutils', 'ua-parser',
                      'user-agents', 'apache-log-parser',
                      'ConfigArgParse'],
    entry_points={
        'console_scripts': [
            'botstat = botstat.botstat:main',
        ],
    },
)
