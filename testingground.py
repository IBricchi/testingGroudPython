#######Beep Project
# def beep(frequency, amplitude, duration):
#     sample = 8000
#     half_period = int(sample/frequency/2)
#     beep = chr(amplitude)*half_period+chr(0)*half_period
#     beep *= int(duration*frequency)

# beep(1000, 1, 1000)

#######math spiral project
####trial 1 works
# import numpy as np
# o = np.pi/3
# a = 1
# l = 1
# x = 0
# y = 0
# for i in range(0,700):
# 	print("(",x,",",y,")")
# 	x += np.cos(a*o)*l
# 	y += np.sin(a*o)*l
# 	a += 1
# 	l /= 2
# print("(",x,",",y,")")
####trial 2
# import numpy as np
# def f(x):
# 	if x == 0:
# 		return 0
# 	else:
# 		return np.cos(x*np.pi/3)/pow(2,x-1)+f(x-1)
# def g(x):
# 	if x == 0:
# 		return 0
# 	else:
# 		return np.sin(x*np.pi/3)/pow(2,x-1)+g(x-1)
# for i in range(0,700):
# 	print("(",f(i),",",g(i),")")

######## plus 1
# cont = True
# total = 0
# while cont==True:
# 	if input("what do you want: ")=="end":
# 		cont=False
# 	else:
# 		total += 1

# print(total)

########## problem math 13 - 1
# from random import randint
# for g in xrange(0,10):
# 	people = 400
# 	rep = 10000
# 	valr = 364

# 	bestr = 0.0
# 	bests = 0.0

# 	error = False

# 	num = 0

# 	for x in xrange(0,rep):
# 		num += 1
# 		birthday = []
# 		for y in xrange(0,people):
# 			birthday.append(randint(1,valr))
# 		cont = True
# 		i = 1
# 		j = 0
# 		while cont == True:
# 			if birthday[i] == birthday[j] and i != j:
# 				bestr += 1
# 				bests += i
# 				# if bestr != 0:
# 				# 	print str(num) + ': ' + str(bests/bestr)
# 				cont = False
# 			if i == valr:
# 				j += 1
# 				i = j+1
# 			i += 1
# 	if bests/bestr-float(int(bests/bestr)) < 0.5:
# 		print int(bests/bestr) + 1
# 	else:
# 		print int(bests/bestr) + 2

########problem math 13-2

# prob = []
# best = 0

# def problemMaths13(x):
# 	answer = x
# 	if x == 0:
# 		return 0
# 	else:
# 		for g in xrange(0,x):
# 			answer -= x - problemMaths13(x-g)
# 		return answer

# for y in xrange(0,400):
# 	prob.append(problemMaths13(y))

# print prob


########hycrypt

# def hycrypt():	
# 	choice = raw_input("Encrypt or decrypt: ")
# 	if choice == "encrypt":
# 		userIn = raw_input("Input text here (all in uppercase letters): ")
# 		inLi = list(userIn)
# 		ascii1 = []
# 		for x in xrange(0,len(inLi)):
# 			ascii1.append(str(ord(inLi[x])))
# 		ascii2 = ''.join(ascii1)
# 		ascii3 = ascii2[::-1]
# 		ascii4 = list(ascii3)
# 		cryptArray = []
# 		while len(ascii4)>0:
# 			tempArray = ascii4[:2]
# 			tempChar = ''.join(tempArray)
# 			cryptArray.append(chr(int(tempChar)+33
# 				))
# 			del ascii4[:2]
# 		crypt = ''.join(cryptArray)
# 		print(crypt)
# 	elif choice == "decrypt":
# 		crypt = raw_input("Input code here: ")
# 		cryptArray = list(crypt)
# 		ascii4 = []
# 		while len(cryptArray)>0:
# 			ascii4.append(str(ord(cryptArray[0])-33))
# 			del cryptArray[0]
# 		ascii3 = ''.join(ascii4)
# 		ascii2 = ascii3[::-1]
# 		ascii1 = list(ascii2)
# 		outLi = []
# 		while len(ascii1)>0:
# 			tempArray = ascii1[:2]
# 			tempChar = ''.join(tempArray)
# 			tempNum = int(tempChar)
# 			outLi.append(chr(tempNum))
# 			del ascii1[:2]
# 		userOut = ''.join(outLi)
# 		print(userOut)
# while True:
# 	hycrypt()


#######fib
# import sys

fibseq = [0,1]
lenfibseq = []
lenlenfibseq = []
lenlenlenfibseq = []
lenlenlenlenfibseq = []
lenlenlenlenlenfibseq = []
lenlenlenlenlenlenfibseq = []

for x in range(2,5000):
	fibseq.append(fibseq[x-1]+fibseq[x-2])
for x in range(0,len(fibseq)):
	lenfibseq.append(len(str(fibseq[x])))
for x in range(1,len(str(fibseq[-1]))):
	lenlenfibseq.append(lenfibseq.count(x))

print(fibseq)
print(lenfibseq)
print(lenlenfibseq)
# print(lenlenlenfibseq)
# print(lenlenlenlenfibseq)
# print(lenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenlenlenlenfibseq)
