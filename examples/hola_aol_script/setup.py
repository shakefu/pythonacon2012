from setuptools import setup


setup(
        name='hola_aol',
        version='0.0.1-dev',
        description="The Hola AOL script",
        author="Jacob Alheid",
        author_email="jake@about.me",
        py_modules=['hola_aol'],
        entry_points={
            'console_scripts':[
                'hi = hola_aol:hello_world',
                ],
            },
        )

