#!/usr/bin/env python
# coding=utf-8
#________________________________________________________________________LICENSE
#	Copyright © 2014 Roy Pfund. All rights reserved.
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
'''tryhy.py
Local host an equivalent of https://github.com/hylang/tryhy

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
#provide https://github.com/mitsuhiko/flask
GitHy_BootStrap.PkgInstall(PkgName="flask", GitUrl="https://github.com/mitsuhiko/flask.git", TagName="0.10.1", cwfd=cwfd)
#provide https://github.com/hylang/tryhy
GitHy_BootStrap.GitTar(PkgName="tryhy", GitUrl="https://github.com/GlassGhost/tryhy.git", cwfd=cwfd)

BootStrapPython = cwfd + '/BootStrap/bin/python'
tryhyDir= cwfd + '/Pkg/tryhy'

SPObject_tryhy = subprocess.Popen(
	[BootStrapPython, tryhyDir + '/main.py'],
	stdin=None, stdout=None, stderr=None, cwd=tryhyDir, env=None)
SPObject_tryhy.wait()

