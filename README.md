# ADSgenderclustering

It is commonly thought that representation of minorities among mentors helps addressing underepresentation of minorities in the sciences. 
While this is a very reasonable assumption, it is not quantified in the literature, to my knowledge. One way to test this is to measure whether minorities thent to publish together. 
This code is designed to quantify the clustering of femal authorship: if a woman is one of the main authors of a paper, are other women more likely to be among the first authors?

This code was created within AAS2015 hackday.

As of Sept 2016, it is very much a work in progress.

I analyze 5000 articles extracted from ADS in January 2015. 

Of those I only consider papers with >= 3 authors. Where all three first names can be read and identifies to at least 75% confidence level (where the ratio of gender usage for that first name is >0.75 for either males or females.) 

From the original set of 5000 papers the final sample includes 1288 papers.

I check this with a MC simulation.

# The Nnull hypothesis is that female authors are distributed randomely among papers is strongly rejected by both KS and AD tests to p<0.003 (3-sigma)!
## Note that this result is obtained after counting female and male authors in the final set of papers. So this analysis does not address at all the underrepresentation of women in the field,  although we find women are about 40% of the authors (to 3 authors) in our final sample. 
## Notice also that our sample is biassed in many ways: for example, asian names cannot be associated with gender as easily as non-asian names, long author lists are likely to use initials and thus large collaborations are removed from our sample, and several other biases.

## There is a significant excess of both papers with no and with all three female lead authors, and a deficit of papers with a single female author compared to a random gender distribution!
