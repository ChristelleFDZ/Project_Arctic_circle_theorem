# Project Arctic circle theorem
Project for HMMA238

![Aztec Diamonds](http://images.math.cnrs.fr/local/cache-vignettes/L350xH350/arton214-edc85.png?1605705109)

## Youtube presentation

link : https://youtu.be/DYxvR-i5mk0
## Synopsis

This project deals with the arctic circle theorem ( or Aztec Diamonds theorem). The picture at the top is an example of the expected result.

## Install

In order to retrieve this project you shall clone this repository; using the command below (make sure to use it in a command prompt) :

```
$ git clone https://github.com/ChristelleFDZ/projectarcticcircletheorem.git
```

To setup the project correctly, you have to install all the required python packages described in the  **requirements.txt**, all those packages are specified using a specific version. In order to comply with the requirements, please use the command below (execute this command in the same directory), this command shall install all expected packages:

```
pip install -r requirements.txt
```

(OPTIONALLY) More over you can install this project on your python package filesystem in order to use all functions and class provided by this project in your own projects.
Using the command below (make sure to use the correct pip installer if you have multiple python versions on your device):

```
pip install -i https://test.pypi.org/simple/ aztecdiamond==1.0.2
```
Warning : this project is not currently optimized for packaging use (It seems that imports are conflicting).

## Run (the cloned project)

In order to run this python project, you must execute the main.py script. This will run the application. (Make sure to be in the correct directory)

```
python main.py
```


## Documentation

The documentation of this package is available on this website: https://project-arctic-circle-theorem-3.readthedocs.io/en/latest/index.html
Please read carefully each part you want to exploit in the package.

## Structure

In the *\beamer* folder, you can find a presentation of this work.

The *\doc* folder contains some documentation about this project.

Tests functions are implemented in the *\tests* folder in order to ensure the good development of this package.

The folder *\aztecdiamond* contains all the main code.

## Contributors

```
Sonia Djouahra : sonia.djouahra@etu.umontpellier.fr

Omar Es-Sbai : omar.es-sbai@etu.umontpellier.fr

Oumouratou Anna Sow : oumouratou-anna.sow@etu.umontpellier.fr

Christelle Fernandez : christelle.fernandez@etu.umontpellier.fr
```
