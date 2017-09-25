# natanaelfneto portfolio

The goal of this repository is to make a portfolio page

## Getting Started

To start this project you have to have installed [Python](https://www.python.org/) and the [pip](https://pip.pypa.io/en/stable/installing/) package manager.

### Installing Python

Python already comes with linux, for Mac and Windows. To install on Mac you can download at [python.org](https://www.python.org/) or you can use [Homebrew](https://brew.sh/) package manager. To install Homebrew on Mac use the following code on your terminal:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then, to install python 2.7
```
brew install python
```
or, to install python 3
```
brew install python3
```

For Windows users works the same, you can download at [python.org](https://www.python.org/) or you can use [Chocolatey](https://chocolatey.org/) package manager. To install Chocolatey on Windows use the following code on your terminal, it can be on cmd:
```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```
or with powershell:
```
Set-ExecutionPolicy AllSigned; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Then, to install python 2.7
```
choco install python2
```
or, to install python 3
```
choco install python
```

### Installing pip

[Pip](https://pip.pypa.io/en/stable/installing/) is a python package manager. It comes with python 2.7 or python 3 packages. If for any reason you need to install it manually. To install pip on Mac, use Homebrew
```
brew install pip
```

To install it on Windows use Chocolatey
```
choco install pip
```

### To run the code:

First you need to clone the repository
```
git clone https://github.com/natanaelfneto/natanaelfneto.git
```

Install project remaining requirements with pip
```
pip install -r requirements.txt
```

Run the local server
```
python manager.py runserver
```

And then, access http://localhost:8000 on your browser

## Built With

[Bootstrap4](https://v4-alpha.getbootstrap.com/)
[Django](https://www.djangoproject.com/)
[Python](https://www.python.org/)

## Versioning

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## Authors

[Natanael F. Neto](@natanaelfneto)

## License

MIT License

Copyright (c) 2017 Natanael F. Neto (natanaelfneto)
