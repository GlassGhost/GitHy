#!/usr/bin/env python
# coding=utf-8
#________________________________________________________________________LICENSE
#	Copyright © 2018 Roy Pfund. All rights reserved.
#
#	Licensed under the Apache License, Version 2.0 (the  "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable  law  or  agreed  to  in  writing,
#	software distributed under the License is distributed on an  "AS
#	IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,  either
#	express or implied. See the License for  the  specific  language
#	governing permissions and limitations under the License.
#__________________________________________________________________DOCUMENTATION
'''stuff.py
"GitHy_BootStrap.PkgInstall" the following packages:
    hy
    clint
    rply
    numpy
	pandas
	sympy
	scipy
	matplotlib
	cython
	bottle
	flask

Revision Tags Last updated 2014-6-13
sudo apt-get install python-dev
'''
#________________________________________________________________Library Imports
import subprocess, threading, re, os, sys, inspect, shutil, argparse, random, math
rows, columns = os.popen('stty size', 'r').read().split() #http://goo.gl/cD4CFf
#"pydoc -p 1234" will start a HTTP server on port 1234, allowing you  to  browse
#the documentation at "http://localhost:1234/" in your preferred Web browser.
cwf = os.path.abspath(inspect.getfile(inspect.currentframe())) # Current Working File
cwfd = os.path.dirname(cwf) # Current Working File Path
#from GitTar import GitTar
import GitHy_BootStrap
#______________________________________________________________________Functions

#____________________________________________________________________Main Script
#GitHy_BootStrap.PkgInstall(PkgName="None", GitUrl=None, TagName=None, cwfd=cwfd)
#https://github.com/cython/cython
GitHy_BootStrap.PkgInstall(PkgName="cython", GitUrl="https://github.com/cython/cython.git", TagName="0.28.2", cwfd=cwfd)
#https://github.com/numpy/numpy
GitHy_BootStrap.PkgInstall(PkgName="numpy", GitUrl="https://github.com/numpy/numpy.git", TagName="v1.14.3", cwfd=cwfd)
#https://github.com/hylang/hy
GitHy_BootStrap.PkgInstall(PkgName="hy", GitUrl="https://github.com/hylang/hy.git", TagName="0.14.0", cwfd=cwfd)
#https://github.com/kennethreitz/clint
GitHy_BootStrap.PkgInstall(PkgName="clint", GitUrl="https://github.com/kennethreitz/clint.git", TagName="v0.5.1", cwfd=cwfd)
#https://github.com/alex/rply.git
GitHy_BootStrap.PkgInstall(PkgName="rply", GitUrl="https://github.com/alex/rply.git", TagName="v0.7.5", cwfd=cwfd)
#https://github.com/pydata/pandas
GitHy_BootStrap.PkgInstall(PkgName="pandas", GitUrl="https://github.com/pydata/pandas.git", TagName="v0.22.0", cwfd=cwfd)
#https://github.com/sympy/sympy
GitHy_BootStrap.PkgInstall(PkgName="sympy", GitUrl="https://github.com/sympy/sympy.git", TagName="sympy-1.1.1", cwfd=cwfd)
#https://github.com/scipy/scipy
GitHy_BootStrap.PkgInstall(PkgName="scipy", GitUrl="https://github.com/scipy/scipy.git", TagName="v1.0.1", cwfd=cwfd)
#https://github.com/matplotlib/matplotlib
GitHy_BootStrap.PkgInstall(PkgName="matplotlib", GitUrl="https://github.com/matplotlib/matplotlib.git", TagName="v2.2.2", cwfd=cwfd)
#https://github.com/defnull/bottle
GitHy_BootStrap.PkgInstall(PkgName="bottle", GitUrl="https://github.com/defnull/bottle.git", TagName="0.12.13", cwfd=cwfd)
#https://github.com/mitsuhiko/flask
GitHy_BootStrap.PkgInstall(PkgName="flask", GitUrl="https://github.com/mitsuhiko/flask.git", TagName="1.0", cwfd=cwfd)

