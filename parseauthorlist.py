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
            print "ratios",femalecount, malecount, float(femalecount)/float(maxauth), float(malecount)/float(maxauth)
 
        print ""
    
