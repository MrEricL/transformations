from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	f = open(fname, "rw+")
	l = []

	#builds the list
	with open(fname) as temp_file:
		l = [line.rstrip('\n') for line in temp_file]
	#print l

	i = 0

	while (i < len(l)):
		try:
			temp = l[i+1].split(" ")
		except:
			pass

		if (l[i] == "line"):
			add_edge(points,int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3]),int(temp[4]),int(temp[5]))
			i+=2
		elif (l[i] == "ident"):
			ident(transform)
			i+=1
		elif (l[i] == "scale"):
			tempMatrix = make_scale(float(temp[0]),float(temp[1]),float(temp[2]))
			matrix_mult(tempMatrix,transform)
			i+=2
		elif (l[i] == "move"):
			tempMatrix = make_translate(int(temp[0]),int(temp[1]),int(temp[2]))
			matrix_mult(tempMatrix,transform)
			i+=2
		elif (l[i] == "rotate"):
			if (temp[0] == "x"):
				tempMatrix = make_rotX(int(temp[1]))
			elif (temp[0] == "y"):
				tempMatrix = make_rotY(int(temp[1]))
			else:				
				tempMatrix = make_rotZ(int(temp[1]))
			matrix_mult(tempMatrix,transform)
			i+=2
		elif (l[i] == "apply"):
			matrix_mult(transform,points)
			i+=1
		elif (l[i] == "display"):
			clear_screen(screen)
			for row in range(len(points)):
				for col in range(len(points[row])):
					points[row][col] = int(points[row][col])
			draw_lines(points,screen,color)
			i+=1
		elif (l[i] == "save"):
			save_extension(screen, temp[0])
			i+=1
		elif (l[i] == "end"):
			break
		else:
			i+=1

	print "End parse of " + fname




