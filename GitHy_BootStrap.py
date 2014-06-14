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
'''GitHy_BootStrap.py
Provides a Virtualenv BootStrap with the latest stable version of the following
packages:
	https://github.com/pypa/virtualenv
	https://github.com/hylang/hy
'''
#________________________________________________________________Library Imports
import subprocess, threading, re, os, sys, inspect, shutil, argparse, random, math
rows, columns = os.popen('stty size', 'r').read().split() #http://goo.gl/cD4CFf
#"pydoc -p 1234" will start a HTTP server on port 1234, allowing you  to  browse
#the documentation at "http://localhost:1234/" in your preferred Web browser.
cwf = os.path.abspath(inspect.getfile(inspect.currentframe())) # Current Working File
cwfd = os.path.dirname(cwf) # Current Working File Path
#______________________________________________________________________Functions
def GitTar(PkgName=None, GitUrl=None, TagName=None, cwfd=None):
	PkgDir = cwfd + '/Pkg/' + PkgName
	PkgTar = cwfd + '/GitTar/' + PkgName + '.tar'
	print PkgDir
	print PkgTar
	if not os.path.isdir(os.path.dirname(PkgTar)):
		os.mkdir(os.path.dirname(PkgTar))
	if not os.path.isdir(os.path.dirname(PkgDir)):
		os.mkdir(os.path.dirname(PkgDir))
#___delete directory if it exists
	if os.path.isdir(PkgDir):
		shutil.rmtree(PkgDir)
#___clone or untar; overwriting existing files
	if os.path.isfile(PkgTar):
	#___untar to directory
		SPObject_untar = subprocess.Popen(
			['tar', 'xvpf', PkgTar, PkgName],
			stdin=None, stdout=None, stderr=None, cwd=os.path.dirname(PkgDir), env=None)
		SPObject_untar.wait()
	#___git fetch updates
		SPObject_git_fetch = subprocess.Popen(
			['git', 'fetch', '--all'],
			stdin=None, stdout=None, stderr=None, cwd=PkgDir, env=None)
		SPObject_git_fetch.wait()
	else:
	#___git clone --no-checkout GitUrl PkgName
		SPObject_git_clone = subprocess.Popen(
			['git', 'clone', '--no-checkout', GitUrl, PkgDir],
			stdin=None, stdout=None, stderr=None, cwd=None, env=None)
		SPObject_git_clone.wait()
#___tar directory
	SPObject_tar = subprocess.Popen(
		['tar', 'cf', PkgTar, PkgName],
		stdin=None, stdout=None, stderr=None, cwd=os.path.dirname(PkgDir), env=None)
	SPObject_tar.wait()
#___git checkout TagName
	SPObject_git_checkout = subprocess.Popen(
		['git', 'checkout', TagName],
		stdin=None, stdout=None, stderr=None, cwd=PkgDir, env=None)
	SPObject_git_checkout.wait()
#___delete .git directory
	shutil.rmtree(PkgDir + '/.git')

def PkgInstall(PkgName=None, cwfd=None, GitUrl=None, TagName=None):
	print cwfd
	GitTar(PkgName=PkgName, cwfd=cwfd, GitUrl=GitUrl, TagName=TagName)
	PkgDir = cwfd + '/Pkg/' + PkgName
	SPObject_PkgInstall = subprocess.Popen(
		[cwfd + '/BootStrap/bin/python', PkgDir + '/setup.py', 'install'],
		stdin=None, stdout=None, stderr=None, cwd=PkgDir, env=None)
	SPObject_PkgInstall.wait()

#____________________________________________________________________Main Script
if __name__ == "__main__":
	GitTar(GitUrl="https://github.com/pypa/virtualenv.git", PkgName="virtualenv", TagName="1.11.6", cwfd=cwfd)
	SPObject_BootStrap = subprocess.Popen(
		['python', cwfd + '/Pkg/virtualenv/virtualenv.py', 'BootStrap'],
		stdin=None, stdout=None, stderr=None, cwd=cwfd, env=None)
	SPObject_BootStrap.wait()
	#https://github.com/pypa/virtualenv
	PkgInstall(PkgName="virtualenv", GitUrl="https://github.com/pypa/virtualenv.git", TagName="1.11.6", cwfd=cwfd)
	#https://github.com/hylang/hy
	PkgInstall(PkgName="hy", GitUrl="https://github.com/hylang/hy.git", TagName="0.10.0", cwfd=cwfd)
	pass#print "This program wasn't called by another python"
else:
	pass#print "This program was called by another python"

##from http://goo.gl/9XO7sa
#SPObject_Unzip = subprocess.Popen( ['gzip', '-dc', './virtualenv-tmp.tar.gz'],
#	stdin=None, stdout=subprocess.PIPE, stderr=None, cwd=cwfd, env=None)
#SPObject_Untar = subprocess.Popen( ['tar', '-xpvf', '-'],
#	stdin=SPObject_Unzip.stdout, stdout=None, stderr=None, cwd=cwfd, env=None)
#SPObject_Unzip.stdout.close()  # Allow SPObject_Unzip to receive a SIGPIPE if p2 exits.
#SPObject_Untar.wait()
#if (SPObject_Untar.returncode == 0):
#	print "\n\'virtualenv-tmp.tar.gz\' has been unzipped.\n"
#else:
#	print "unzip failed\n"

