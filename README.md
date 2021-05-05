# Python Library with CLI

This repo serves as a template for starting new Python projects.

This repo has been optimized for a Python library with a CLI and includes all the files needed to create, install, and
publish (to PyPi) a project.

## Testing CLI Locally

There are two ways to test the CLI locally:

### Run as module

```shell
python -m package_name --version
```

### Install into virtual environment for development

```shell
pip install -e ".[test]"
package_cli --version
```

Note: don't forget the `[test]` as this installs the libraries needed for running the unit tests.

## CLI Output

```shell
% package_cli -h
usage: package_cli [-h] [-d] [-v] [echo_text ...]

positional arguments:
  echo_text      Echo some text...

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    Enable debug mode
  -v, --version  Print version number.
```

```shell
 % package_cli --version
v1.0.0
```

```shell
 % package_cli
Able to get to Google!
```
