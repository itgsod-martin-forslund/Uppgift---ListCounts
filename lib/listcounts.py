def sum(listofnumbers):
    if len(listofnumbers) == 0:
        raise ValueError
    result = 0

    for numbers in listofnumbers:
        result = result + numbers

    return result









def min(listofnumbers):
    pass

def max(listofnumbers):
    pass
    # sum(listOfNumbers=[])
    #
    #
	# sum(listOfNumbers=[10,20,30,40])
	# = 100
    #
	# min(listOfNumbers=[10,20,30,40])
	# = 10
    #
	# max(listOfNumbers=[10,20,30,40])
	# = 40
    #
	# average(listOfNumbers=[10,20,30,40])
	# = 25
    #
	# median(listOfNumbers=[10,20,30,40,50])
	# = 30


numbers=[3,6,1]

print min(numbers)