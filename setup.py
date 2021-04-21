from setuptools import setup
from Project_Arctic_circle_theorem import __version__ as current_version
### probleme pour le nom du projet
#il faut changer theorem- je pense que l'erreur viens d'ici
setup(
  name='aztecdiamond',
  version=current_version,
  description='Theorem Aztec Diamond',
  url='https://github.com/ChristelleFDZ/Project_Arctic_circle_theorem.git',
  author='Djouahra Sonia ; Es-Sbai Omar ; Sow Oumouratou Anna ;Fernandez Christelle:',
  author_email='christelle.fernandez@etu.umontpellier.fr',# a verifier
  license='MIT',
  packages=['src', 'src.aztecdiamond', 'src.domino'],
  zip_safe=False
)