from setuptools import setup


setup(
  name='aztecdiamond',
  version="1.0.2",
  description='Aztec Diamond theorem',
  url='https://github.com/ChristelleFDZ/projectarcticcircletheorem.git',
  author='Djouahra Sonia; Es-Sbai Omar; Sow Oumouratou Anna; Fernandez Christelle',
  author_email='christelle.fernandez@etu.umontpellier.fr',
  license='MIT',
  packages=['aztecdiamond'],
  zip_safe=False,
  install_requires= ['numpy==1.19.2','pygame==2.0.1', 'memory_profiler==0.58.0']
)