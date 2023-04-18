# integrated-example-pants
An example repository to demonstrate a Integrated Python Monorepo using pants.

# Quick start

Just run `./pants help goals`

## Invoking goals

Invoking goals on all files:

```
./pants lint ::

# Or use globs
./pants lint corridor/**/*.py
```

Invoking a goal on a single file:

```
./pants lint corridor/data_lake/dataset.py
```

You can run on all changed files:

```
./pants --changed-since=main lint
```

# Example Goals

```
# Lint all files
./pants lint ::

# Format files in reports
./pants fmt 'corridor/reports/**'

# Run all tests
./pants test ::

# Run all tests (and show output from pytest)
./pants test --output=all ::

# Run tests (and pass extra arguments)
./pants test corridor/data_lake/dataset_test.py -- -k test_dataset_read

# Build packages
./pants package ::

## Count lines of code
./pants count-loc ::

## Export to a virtualenv for IDE integration
./pants export ::
```