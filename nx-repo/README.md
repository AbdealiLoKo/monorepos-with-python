# example-python
An example repository to demonstrate a Python application.

# Quick Start

```
npm install

# Running nx with a path
./node_modules/.bin/nx --help
```

## Invoking commands

Invoking targets on multiple projects:

```
./node_modules/.bin/nx run-many --target install
./node_modules/.bin/nx run-many --target lint
```

Or run on a single projects:

```
./node_modules/.bin/nx run data-lake:lint
```

You can run on all changed files:

```
./node_modules/.bin/nx affected --base main --target lint
```

# Example Commands

```
# Lint all files
./node_modules/.bin/nx run-many --target lint

# Format files in reports
./node_modules/.bin/nx run-many --target format

# Run all tests
./node_modules/.bin/nx run-many --target test

# Run all tests (and show output from pytest)
./node_modules/.bin/nx run-many --target test --verbose

# Run tests (and pass extra arguments)
./node_modules/.bin/nx run data-lake:test -- -k test_dataset_read

# Build packages
./node_modules/.bin/nx run-many --target build
```
