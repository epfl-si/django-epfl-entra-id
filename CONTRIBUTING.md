# Contributing

## Setup

Get the project with:

```bash
git clone git@github.com:epfl-si/django-epfl-entra-id.git
cd django-epfl-entra-id.git
```

Then, create a virtual environment (Python version and some libraries) with
your favourite tool and:

```bash
pip install tox
```

## Test

```bash
tox
```

## Release

1. Bump the correct version
1. Update the file [CHANGELOG.md](CHANGELOG.md)
1. Create and push the tag  
    `git tag -a v<version> -m "django-epfl-entra-id v<version> release"`  
    `git push origin main --tags`
