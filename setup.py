from setuptools import setup, find_packages

setup(
    name='maltongo',
    author='Matt Newham',
    version='1.0',
    author_email='matt.newham@gmail.com',
    description='Maltongo - Maltego transforms for mongodb',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari=0.5'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)