from setuptools import setup


setup(
        name='myplugin',
        version='0.0.1-dev',
        description="The Hola AOL plugin",
        author="Jacob Alheid",
        author_email="jake@about.me",
        py_modules=['myplugin'],
        entry_points={
            'hola_aol':[
                'myplugin = myplugin:hello_world',
                ],
            },
        )

