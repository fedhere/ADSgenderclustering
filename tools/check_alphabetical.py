def checkAlphabetical( listOfNames ):
	firstLetters = [x.strip().upper()[0] for x in listOfNames]
	return firstLetters==sorted(firstLetters)


#print checkAlphabetical( ["Alice", "Bob", "Charlie"] )
#print checkAlphabetical( ["Bob", "Charlie", "Alice"] )  