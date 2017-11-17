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

# fibseq = [0,1]
# lenfibseq = []
# lenlenfibseq = []
# lenlenlenfibseq = []
# lenlenlenlenfibseq = []
# lenlenlenlenlenfibseq = []
# lenlenlenlenlenlenfibseq = []

# for x in range(2,5000):
# 	fibseq.append(fibseq[x-1]+fibseq[x-2])
# for x in range(0,len(fibseq)):
# 	lenfibseq.append(len(str(fibseq[x])))
# for x in range(1,len(str(fibseq[-1]))):
# 	lenlenfibseq.append(lenfibseq.count(x))

# print(fibseq)
# print(lenfibseq)
# print(lenlenfibseq)
# print(lenlenlenfibseq)
# print(lenlenlenlenfibseq)
# print(lenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenlenlenfibseq)
# print(lenlenlenlenlenlenlenlenlenlenfibseq)



######### PRoblem math 8 2017 November

final_list = [6,2,1,0,0,0,1,9,9,9]
list_to_check = [6,2,1,0,0,0,1,0,0,0]

success_list = []


def how_many_in_list(needle, haystack):
	out = 0
	for x in haystack:
		if needle == x:
			out += 1
	return out

def move_list_up(idk):
	list_len = len(idk)-1
	cont = True
	while cont:
		if idk[list_len] == 9:
			idk[list_len] = 0
			list_len -= 1
		else:
			idk[list_len] += 1
			cont = False
	return idk

totalinfothing = []

while final_list != list_to_check:
	outputinfo = ['',]
	outputinfo.append("Check for number " + ''.join([str(n) for n in list_to_check]) + ":")
	#print("\n"+"Check for number " + ''.join([str(n) for n in list_to_check]) + ":")
	success = True
	for i, thing in enumerate(list_to_check):
		is_something = thing != how_many_in_list(i, list_to_check)
		if is_something:
			outputinfo.append("The digit in position " + str(i+1) + " of this number does not follow the specified rules as there are not exactly " + str(thing) + ", " + str(i) +"'s.")
			#print("The digit in position " + str(i+1) + " of this number does not follow the specified rules as there are not exactly " + str(thing) + ", " + str(i) +"'s.")
			success = False
			break
		else:
			outputinfo.append("The digit in position " + str(i+1) + " of this number follows the specified rule as exactly " + str(thing) + ", " + str(i) +"s are present.")
			#print("The digit in position " + str(i+1) + " of this number follows the specified rule as exactly " + str(thing) + ", " + str(i) +"s are present.")

	if success:
		outputinfo.append("Every digit in this number follows the set rules, hence this number is valid under the prerequisits of the test")
		#print("Every digit in this number follows the set rules, hence this number is valid under the prerequisits of the test")
		x = list_to_check
		success_list.append([])
		success_list[len(success_list)-1].extend(x)
		#print(list_to_check)
	else:
		outputinfo.append("As not every digit in this number follows the set rules, this number is invalid under the prerequisits of the test")
		#print("As not every digit in this number follows the set rules, this number is invalid under the prerequisits of the test")
	
	totalinfothing.extend(outputinfo)
	# for line in outputinfo:
	# 	print(line)


	list_to_check = move_list_up(list_to_check)

totalinfothing.append('')
totalinfothing.append("Hence from the results above one can see that the possible combinations for numbers which are valid according to our test are:")
for success_num in success_list:
	totalinfothing.append(''.join([str(x) for x in success_num]))

for line in totalinfothing:
	print(line)

with open("problemmath-8-2017/problemmath-8-2017-writeup.txt", "w") as output_file:
    for line in totalinfothing:
    	output_file.write('\n' + line)
#print(success_list)


############# Abbreviation thing

# word_list = []

# with open ("abvt/hamlet.txt", "r") as inputfile:
#     lines = inputfile.readlines()

# out_lines = []
# for line in lines:
# 	words = line.split()
# 	outwords = []
# 	for word in words:
# 		if word not in word_list:
# 			word_list.append(word)
# 			outwords.append(word + "(" + str(len(word_list)) + ")")
# 		else:
# 			word_index = str([i for i, j in enumerate(word_list) if j == word][0])
# 			outwords.append(word_index)
# 	out_lines.append(' '.join(outwords))

# with open("abvt/hamletabvr.txt", "w") as outputfile:
# 	for line in out_lines:
# 		print(line)
# 		outputfile.write(line + '\n')






