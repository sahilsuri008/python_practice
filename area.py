#!/usr/bin/python

def gather_info():
	ln=input("Enter length: ")
	br=input("Enter breadth: ")
	op=raw_input("Enter area or permieter: ").lower().strip()
	return (ln,br,op)

def calap(ln,br,op):
	if op=='area':
		ar=ln*br
		print "%s is the area of the rectangle." % (ar)
	else:
		pr=2*(ln+br)
		print "%s is the perimeter of the rectangle" % (pr)

while True:
	ln,br,op=gather_info()
	if op.startswith('a'):
		calap(ln,br,op='area')
		break
	elif op.startswith('p'):
		calap(ln,br,op='perimeter')
		break
	else:
		print "Unknown operation sepcified"
