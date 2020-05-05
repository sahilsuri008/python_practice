#!/usr/bin/python

import os

stage=(os.getenv('STAGE') or 'development').upper()

output = "We're running in %s" % stage

if stage.startswith("prod"):
	output = "Danger!!" + output

print(output)




