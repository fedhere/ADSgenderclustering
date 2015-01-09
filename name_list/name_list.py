import csv
import sys
import numpy as np
import cPickle
import string as str

maxInt = sys.maxsize
decrement = True

def load_csv(file_name, skip_num, delimiter):
	name_list = []
	with open(file_name, 'rb') as csvfile:
	    spamreader = csv.reader(csvfile, delimiter=delimiter)
	    i = 0
	    for row in spamreader:
	        if i < skip_num:
	        	pass
	        else:
	        	name = row[0]
	        	name.replace('-', '') 
	        	name_list.append(str.lower(name))
	        i += 1
	return name_list

if __name__ == '__main__':
	while decrement:
	    # decrease the maxInt value by factor 10 
	    # as long as the OverflowError occurs.

	    decrement = False
	    try:
	        csv.field_size_limit(maxInt)
	    except OverflowError:
	        maxInt = int(maxInt/10)
	        decrement = True
	
	female_list = load_csv('female_uniq.csv', 5, ',')
	male_list = load_csv('male_uniq.csv', 5, ',')
	cross_list = load_csv('unisex_uniq.csv', 6, ' ')

	female_uniq = set(female_list) - set(cross_list)
	male_uniq = set(male_list) - set(cross_list)

	file_pk = open('female.pkl', 'wb')
	cPickle.dump(female_uniq, file_pk, -1)
	file_pk.close()

	file_pk = open('male.pkl', 'wb')
	cPickle.dump(male_uniq, file_pk, -1)
	file_pk.close()

	file_pk = open('ununqi.pkl', 'wb')
	cPickle.dump(cross_list, file_pk, -1)
	file_pk.close()
	