#project2014-P002.py
#Lets determine some factors of a number

#First do some housekeeping

FAC = int(1) #The factor test number
FACTORS = [] # Create an empty list for the factors to be stored in
FINDEX = int(0) # Prime the list index variable

# Begin the adventure
# Ask for a number to factor and make it an interger
NUM = int(input("Please give me a number: ")) 

print("The number you entered is: ", NUM)

# Start the loop to find the factors
for x in range(1, NUM): # Test for factors through the number itself

    if NUM % FAC == 0: # Check for an even division
        print ("A factor is: ", FAC)  # If the remainder is zero print the factor
        
        FACTORS[FINDEX:] = [FAC] # Place the factor into the list.
                            # This was tuff, you have to use [x:] to load the list
                            # Specifing a range x to the end
                            
        FINDEX = FINDEX + 1 # Add one to the index
        
        FAC = FAC + 1 # Add one to the factor test
        
    else:
       FAC = FAC + 1 # Add one to the factor test and restart
    
else: 
    print (" The list of factors is ", FACTORS)
    print ("all done") # We are all done 

input() # To keep the window open on gui systems, as suggested by +Nevrin O
