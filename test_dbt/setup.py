from setuptools import find_packages, setup

setup(
    name="test_dbt",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "test_dbt": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-snowflake",
        "dbt-snowflake",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

