# Django docopt command

Django-docopt-command allows you to write [Django](www.djangoproject.com) [manage.py](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/) commands using the [docopt](www.docopt.org) library. This means that you can define commands using usage strings.

References:

* [Django](www.djangoproject.com): The Web framework for perfectionists with deadlines
* [The docopt library](www.docopt.org): Command-line interface description language
* [Writing custom django-admin commands](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)

```
class Command(DocOptCommand):
	# This usage string defines the command options:
	docs = "Usage: command <option1> <option2> [--flag1]"

	def handle_docopt(self, arguments):
		# arguments contains a dictionary with the options
		pass
```

Django-docopt-command is tested with Django 1.4-1.6 and Python 2.6, 2.7 and 3.3 and is hosted on [github](https://github.com/mbraak/django-docopt-command).

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

```
class Command(DocOptCommand):
	pass
```

**Step 3 - add a docs string**

```
class Command(DocOptCommand):
	docs = "Usage: command <option1> <option2> [--flag1]"
```

**Step 4 - override handle_docopt**

```
class Command(DocOptCommand):
	docs = "Usage: command <option1> <option2> [--flag1]"

	def handle_docopt(self, arguments):
		pass
```

## License

Django-docopt-command is licensed under the Apache 2.0 License.