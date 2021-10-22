# Common mistakes to avoid

## Bad coding style

Use snake case for functions:

~~MaFonction~~ → ma_fonction

And variables:

~~MaVariable~~ → ma_variable

All UPPERCASE variable is for constants

Give meaningful names to variables and functions

## No or not enough functions

## Too big functions

## No context manager

DO NOT:

```python
f = open('file.log', 'r')
line = f.read()
f.close()
```

DO

```python
with open('file.log', 'r') as f:
    line = f.read()
```

# Self evaluation

## Code

1. Will it run on university computers using Python3?
2. Could anyone read/understand/maintain my code?
3. Does my naming make sense?
4. Do I have comments for complicated sections? It is obvious what functions do? _Docstring_
5. Do I respect Coding Style? _PEP8/Flake8/pylint_
6. Are possible errors handled?
7. Is most of my code in functions?
8. Are my functions too big? Should I split my code in more functions?

## Statistics

1. Who will use the tools?
2. Which information is relevant to each role?
3. What’s the value of each statistic?
4. Am I using the right metric? _Counts/Percentages/Percentiles_

## Presentation/display

1. Is it easy to use?
2. Is the README accurate?
3. Can a user easily access help?
4. Is the user made aware of an issue affecting the quality of the output?
5. Are statistics easy to view?

# Project presentation

* Present features
* Who/which roles will be using the tool
* Explain the value for different roles
* Present technical solution
* List challenges/issues/weaknesses
* Justify choices
* Evaluate robustness/accuracy/error handling
* Present/budget possible evolution

# Chase extra points

* Add help:
  Support `mytool --help` and/or `mytool -h`
* Manage versioning
  https://semver.org/:
  Support `mytool --version`
* Include a CHANGELOG.md
  https://keepachangelog.com/en/1.0.0/
* Specify the LICENSE used
* Have some kind of interface options (CLI or GUI). 
  For example: `mytool.py --debug`
* Log relevant information using the `logging` module
* Use GitHub, show collaboration in GitHub
* Test code for security issues: https://github.com/PyCQA/bandit
* Use a documentation generator. _sphinx_
* Publish your code as a package installable using pip
  https://docs.python-guide.org/writing/structure/
* Run continuous integration with GitHub Actions
