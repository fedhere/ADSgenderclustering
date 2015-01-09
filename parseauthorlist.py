import os,sys
import pylab as pl
import pickle, pprint,csv

maxauth=3

if __name__=='__main__':
#read in list of names
    pkl_file = open('name_list/female.pkl', 'rb') 
    femalenames = pickle.load(pkl_file)
    pkl_file = open('name_list/male.pkl', 'rb') 
    malenames = pickle.load(pkl_file)
    
    paperstats={'nauth':[],'ncite':[],'femaleratio':[]}

    print len(femalenames),len(malenames)

#reads in paper list
    pkl_file = open('paperlist.p', 'rb')
    papers = pickle.load(pkl_file)

    #    pprint.pprint(papers)
    print "list of %d papers"%len(papers)

    for ppr in papers:
        #parse paper info
        try:
            ncite= ppr['citation_count']
        except:
            ncite=float('NaN')
            
        nauth= len(ppr['author'])
        authors=ppr['author'][:maxauth]
        


        femalecount=0
        malecount=0
        
        for a in authors: 
            first=a.split()[1]
            if not '.' in first:
                print "nauth,ncite",nauth,ncite,
                print first
                if first in femalenames : 
                    print 'FEMALE'
                    femalecount+=1
                elif first in malenames : 
                    print 'MALE'
                    malecount+=1
                else: print 'UNKNOWN'                
            paperstats['nauth'].append(nauth)
            paperstats['ncite'].append(ncite)

            print "ratios: females",femalecount, "males:", malecount, "femaleratio:",float(femalecount)/float(maxauth), "maleratio:", float(malecount)/float(maxauth)
            paperstats['femaleratio'].append(float(femalecount)/float(maxauth))            
 
        print ""

    for k in paperstats.iterkeys():
        print k,len(paperstats[k])
        
    
    import pylab as plt
    plt.figure()
    plt.title("FEMALE RATION IN THE FIRST 3 AUTHORS")
    plt.hist(paperstats['femaleratio'], color='SteelBlue')
    plt.figure()
    plt.ylabel ("female ratio")
    plt.xlabel ("number of authors")
    plt.scatter(paperstats['nauth'], paperstats['femaleratio'] )
    plt.figure()
    plt.ylabel ("female ratio")
    plt.xlabel ("number of citations")
    plt.scatter(paperstats['ncite'], paperstats['femaleratio'] )
    plt.show()
