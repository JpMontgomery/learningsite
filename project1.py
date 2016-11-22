import os
l = [1,2,3,4,5,6,7,8,9]
print('        {}| {} | {} \n     ----------\n       {} | {} | {}  \n     ----------\n       {} | {} | {}  '.format(l[1]))
x = int(input('Enter 1 to play tic tac toe, or 0 to quit.'))
while True:
	if x == 1:
		os.system('clear')

	else:
		break
