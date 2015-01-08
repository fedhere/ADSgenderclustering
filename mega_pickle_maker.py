import ads
import cPickle as pickle 

#Query ADS see https://github.com/andycasey/ads for the api 
query = ads.query(database='astronomy', rows=20)

#Make a list of formated dictionaries to send to the pickle file
paper_dicts = []
for paper in query:
    paper_dicts.append({'authors':paper.author, 'first_author_affiliation':paper.aff[0],
                        'number_of_citations':paper.citation_count, 'title':paper.title
                        }) 
   
#We can pickle that! 
output = file('papers.pkl', 'w')
pickle.dump(paper_dicts, output)
output.close()