"""This script 
reads text file"""

#Creates a reference to our file, for "r" reading
TEXT_FILE = open("C:\\trainings\python\source.txt", "r")

#Reads our entire file into a variable as a string
TEXTFROMFILE = TEXT_FILE.read()

#split() uses the , in our string to create an array
BEATLES = TEXTFROMFILE.split(',')

for beatle in BEATLES:
	if beatle == 'John':
		print('The Walrus')
	else:
		print(beatle)
input()
		
# for i in range(0,len(beatles)):	#iterate over a range of numeric values
# 		
# 	if beatles[i] == 'Deathstroke': 
# 	
# 		print 'Slade. The one-eyed wonder.'
# 		
# 	elif beatles[i] == 'Clayface':
# 		
# 		print "Clayface. Easily bent out of shape."
# 
# 	else: 
# 	
# 		print beatles[i]

# for index, value in enumerate(beatles): # iterate over the array while having access to the current index and current value
# 
#   if value == 'Bane':
#     print 'Bane. The man who broke the bat.'
#   else:
#     print beatles[index]
# 		