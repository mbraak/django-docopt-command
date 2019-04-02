# Django docopt command

[![Build Status](https://img.shields.io/travis/mbraak/django-docopt-command.svg?style=for-the-badge)](https://travis-ci.org/mbraak/django-docopt-command) [![Version](https://img.shields.io/pypi/v/django-docopt-command.svg?colorB=brightgreen&style=for-the-badge)](https://pypi.python.org/pypi/django-docopt-command/)

[![Coverage Status](https://img.shields.io/coveralls/mbraak/django-docopt-command.svg?style=for-the-badge)](https://coveralls.io/r/mbraak/django-docopt-command?branch=master) [![Requirements Status](https://img.shields.io/requires/github/mbraak/django-docopt-command.svg?style=for-the-badge)](https://requires.io/github/mbraak/django-docopt-command/requirements/?branch=master)

[![License](https://img.shields.io/pypi/l/django-docopt-command.svg?style=for-the-badge&colorB=brightgreen)](https://pypi.python.org/pypi/django-docopt-command/)

Django-docopt-command allows you to write [Django](https://www.djangoproject.com) [manage.py](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/) commands using the [docopt](http://www.docopt.org) library. This means that you can define commands using usage strings.

References:

* [Django](https://www.djangoproject.com): The Web framework for perfectionists with deadlines
* [The docopt library](http://www.docopt.org): Command-line interface description language
* [Writing custom django-admin commands](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)

```python
class Command(DocOptCommand):
	# This usage string defines the command options:
	docs = "Usage: command <option1> <option2> [--flag1]"

	def handle_docopt(self, arguments):
		# arguments contains a dictionary with the options
		pass
```

Django-docopt-command is tested with Django 1.11-2.2 and Python 2.7, 3.5-3.7 and is hosted on [github](https://github.com/mbraak/django-docopt-command).

Note that version 0.3.0 also supports Django 1.8 - 1.10.

### Example

See the *testproject/docopt_example* in the django-docopt-command github repository.

## Usage

Install django-docopt-command.

```
pip install django-docopt-command
```

**Step 1 - management command**

Write a Django custom management command, as described in [Writing custom django-admin commands](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/).

**Step 2 - inherit from DocOptCommand**

```python
class Command(DocOptCommand):
	pass
```

**Step 3 - add a docs string**

```python
class Command(DocOptCommand):
	docs = "Usage: command <option1> <option2> [--flag1]"
```

**Step 4 - override handle_docopt**

```python
class Command(DocOptCommand):
	docs = "Usage: command <option1> <option2> [--flag1]"

	def handle_docopt(self, arguments):
		option1 = arguments['option1']
		option2 = arguments['option2']
```

## License

Django-docopt-command is licensed under the Apache 2.0 License.
