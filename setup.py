import setuptools

setuptools.setup(
    name="miga-djangoapp",
    version="0.0.1",
    description="MiGA Django app for UI customizations",
    packages=setuptools.find_packages('MiGAAPI'),
    package_dir={
        '': 'MiGAAPI'
    },
    install_requires=[
        'django>=1.11.16',
        'airavata-django-portal-sdk'
    ],
    entry_points="""
[airavata.djangoapp]
quickstart = quickstart.apps:QuickstartConfig
""",
)
