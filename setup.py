from setuptools import setup

setup(
    name="mysk-utils",
    version="0.1",
    description="Utilities for mysk",
    author="Suankularb Wittayalai School",
    author_email="skvc@sk.ac.th",
    url="https://github.com/suankularb-wittayalai-school",
    packages=[
        "mysk_utils",
        "mysk_utils.schema",
        "mysk_utils.schema.atk",
        "mysk_utils.schema.auth",
        "mysk_utils.schema.classroom",
        "mysk_utils.schema.schedule",
        "mysk_utils.schema.student_teacher",
        "mysk_utils.schema.subject",
        "mysk_utils.schema.vaccine",
    ],
    install_requires=[
        "pydantic>=1.9.0",
    ],
)
