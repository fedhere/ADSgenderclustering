import cPickle
import random
import string

last_name_set = ['hogg', 'johnson', 'blanton', 'foreman-mackey', 'smith', 'williams', 'moore', 'wang']
affiliation_set = ['nyu', 'cmu']

def title_generator(size=6, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))

def random_author_list(author_num):
	female_set = list(cPickle.load(open('female.pkl', 'rb')))
	male_set = list(cPickle.load(open('male.pkl', 'rb')))
	uniq_set = list(cPickle.load(open('ununqi.pkl', 'rb')))

	author_list = []
	for i in range(author_num):
		authors = []
		for j in range(3):
			gender = random.random()
			if gender < 0.3:
				first_name = random.choice(female_set)
			elif gender < 0.9:
				first_name = random.choice(male_set)
			else:
				first_name = random.choice(uniq_set)
			last_name = random.choice(last_name_set)
			authors.append((first_name, last_name))

		affiliation = random.choice(affiliation_set)
		number_of_citations = random.randint(0, 20000)
		title = title_generator()
		author = {'authors':authors, 'first_author_affiliation':affiliation, 
					'number_of_citations':number_of_citations, 'title':title}
		author_list.append(author)
	return author_list
if __name__ == '__main__':
	print random_author_list(200)

	




