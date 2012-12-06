from setuptools import setup, find_packages


setup(
        name='like_a_boss',
        version='0.0.1-dev',
        description="You should be writing tests right now.",
        author="Jacob Alheid",
        author_email="jake@about.me",
        packages=find_packages(exclude=['test']),
        test_suite='nose.collector',
        tests_require=[
            'nose',
            'mock',
            ],
        )

