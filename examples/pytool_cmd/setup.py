from setuptools import setup


setup(
        name='mycmd',
        version='0.0.1-dev',
        description="A pytool.cmd.Command example",
        author="Jacob Alheid",
        author_email="jake@about.me",
        py_modules=['mycmd'],
        install_requires=['pytool'],
        entry_points={
            'console_scripts':[
                'mycmd = mycmd:MyCmd.console_script',
                ],
            },
        )


