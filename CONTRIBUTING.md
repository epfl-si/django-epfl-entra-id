6. Créer un package
Dans le dossier racine :

pip install twine build

python -m build

python setup.py sdist bdist_wheel
Le package sera dans dist/.


7. (Optionnel) Uploader sur PyPI
Si tu veux le distribuer publiquement :

pip install twine
twine upload dist/*



Pour tester localement dans un autre projet
Tu peux installer le package localement avec :

pip install -e /home/duratti/Workspace/fsd/django-epfl-entra-id



Pour tester l'application avec le package sur git:

pip install git+https://github.com/epfl-si/django-epfl-entra-id.git
