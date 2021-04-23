import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
### probleme pour le nom du projet
#il faut changer theorem- je pense que l'erreur viens d'ici
setuptools.setup(
  name="aztecdiamond", # name of our package
  version="0.0.1",
  description='Theorem Aztec Diamond',
  url='https://github.com/ChristelleFDZ/projectarcticcircletheorem.git',
  author='Djouahra Sonia ; Es-Sbai Omar ; Sow Oumouratou Anna ;Fernandez Christelle:',
  author_email='christelle.fernandez@etu.umontpellier.fr',
  license='MIT',
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
  
)
