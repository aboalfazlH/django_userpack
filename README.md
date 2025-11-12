# Django_Userpack


django_Userpack is a Python library for a advanced user for django

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django_UserPack.

```bash
pip install Django_UserPack
```

## Usage
```python
INSTALLED_APPS = [
    # your apps
    ...
    'django_userpack'
]
```
and in user model:
```python
class CustomUser(AdvancedBaseUser):
    # your settings
```

## Contributing

[Pull requests](https://github.com/aboalfazlH/django_userpack) are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/aboalfazlH/django_userpack/blob/main/README.md)