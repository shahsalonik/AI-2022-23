import nltk



'''
CHAPTER 2
'''
# 4: Read in the texts of the State of the Union addresses, using the state_union corpus reader.
#    Count occurrences of men, women, and people in each document. 
#    What has happened to the usage of these words over time?

# 5: Investigate the holonym-meronym relations for some nouns. 
#    Remember that there are three kinds of holonym-meronym relation, so you need to use: 
#       member_meronyms(), part_meronyms(), substance_meronyms(), 
#       member_holonyms(), part_holonyms(), and substance_holonyms().

# 7: According to Strunk and White's Elements of Style, the word however, used at the start 
#    of a sentence, means "in whatever way" or "to whatever extent", and not "nevertheless". 
#    They give this example of correct usage: However you advise him, he will probably do as 
#    he thinks best. (http://www.bartleby.com/141/strunk3.html) 
#    Use the concordance tool to study actual usage of this word in the various texts 
#    we have been considering. 
#    See also the LanguageLog posting "Fossilized prejudices about 'however'" at: 
#              http://itre.cis.upenn.edu/~myl/languagelog/archives/001913.html

# 9: Pick a pair of texts and study the differences between them, 
#    in terms of vocabulary, vocabulary richness, genre, etc. 
#    Can you find pairs of words which have quite different meanings across the two texts, 
#    such as monstrous in Moby Dick and in Sense and Sensibility?

# 12: The CMU Pronouncing Dictionary contains multiple pronunciations for certain words. 
#     How many distinct words does it contain? 
#     What fraction of words in this dictionary have more than one possible pronunciation?

# 17: Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.

# 18: Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.

# 23: Zipf's Law: Let f(w) be the frequency of a word w in free text. 
#     Suppose that all the words of a text are ranked according to their frequency, 
#     with the most frequent word first. Zipf's law states that the frequency of a word type is 
#     inversely proportional to its rank (i.e. f × r = k, for some constant k). 
#     For example, the 50th most common word type should occur three times as frequently as the 
#     150th most common word type.
#     a. Write a function to process a large text and plot word frequency against word rank using
#        pylab.plot. Do you confirm Zipf's law? (Hint: it helps to use a logarithmic scale). 
#        What is going on at the extreme ends of the plotted line?
#     b. Generate random text, e.g., using random.choice("abcdefg "), taking care to include 
#        the space character. You will need to import random first. 
#        Use the string concatenation operator to accumulate characters into a (very) long string.
#        Then tokenize this string, and generate the Zipf plot as before, and compare 
#        the two plots. What do you make of Zipf's Law in the light of this?

# 27: The polysemy of a word is the number of senses it has. 
#     Using WordNet, we can determine that the noun dog has 7 senses with: 
#     len(wn.synsets('dog', 'n')). Compute the average polysemy of nouns, verbs, 
#     adjectives and adverbs according to WordNet.

'''
CHAPTER 3
'''
# 20: Write code to access a favorite webpage and extract some text from it. 
#     For example, access a weather site and extract the forecast top temperature for 
#     your town or city today.

# 22: Examine the results of processing the URL http://news.bbc.co.uk/ 
#     using the regular expressions suggested above. 
#     You will see that there is still a fair amount of non-textual data there, p
#     articularly Javascript commands. You may also find that sentence breaks have not been 
#     properly preserved. Define further regular expressions that improve the extraction of text 
#     from this web page.

'''
CHAPTER 6
'''
# 4: Using the movie review document classifier discussed in this chapter, 
#    generate a list of the 30 features that the classifier finds to be most informative. 
#    Can you explain why these particular features are informative? 
#    Do you find any of them surprising?
