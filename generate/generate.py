import random


import random

def	genarate():
	l = []
	l = random.sample(range(100),3)
	return (l)

def	main():
	f = open("numgen5.txt","w")
	l = []
	for i in range(10):
		l = genarate().copy()
		str =['{:.0f}'.format(x) for x in l]
		f.write("%s\n"%(str))
	f.close()



if __name__ == "__main__":
	main()


