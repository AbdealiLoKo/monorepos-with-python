python_tests(  # takes all the *_test.py files by default
    name="tests",
)

resource(
    name="home_ownership",
    source="home_ownership.csv",
)

python_sources(  # takes all the *.py files (not ending with _test.py) by default
    name="lib",
    dependencies=[":home_ownership"],
)

# Creates a python wheel file for this package
# It will automatically create a setup.py file
python_distribution(
    name="dist",
    dependencies=[":lib"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="corridor.data_lake",
        version="0.0.1",
        description="Example datasets to create reports from.",
    ),
)
