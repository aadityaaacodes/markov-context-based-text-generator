import numpy as np

from markovModel import matrixInitialiser, makeMatrix, operations, matrixMapper, stateZero, genNext, textGen
from feeder import tokeniser, totaller, count_occurences, array_maker, filter_text, restartMap, processFeed, filter_array, array_spiltter


# restartMap()

red_list = [
    # Articles & Determiners
    "the", "a", "an", "this", "that", "these", "those",

    # Pronouns
    "he", "she", "it", "they", "them", "his", "her", "its", "their", "theirs", "who", "whom",

    # Prepositions
    "of", "to", "in", "on", "at", "by", "with", "from", "about", "into", "through",

    # Conjunctions
    "and", "or", "but", "if", "because", "although", "while",

    # Auxiliary & Modal Verbs
    "is", "are", "was", "were", "be", "being", "been",
    "have", "has", "had", "do", "does", "did",
    "can", "could", "would", "should", "will", "shall",
    "may", "might", "must",

    # Other "Empty" Words
    "there", "it", "then", "so", "just", "even", "yet"
]


def initialise():
    restartMap()
    feed = 'feed/01 Harry Potter and the Sorcerers Stone.txt'
    unfiltered_text = processFeed(feed)
    # arr = filter_array(array_maker(txt=filter_text(txt=unfiltered_text)), red_list=red_list)
    arr = array_maker(arr=filter_array(arr=array_spiltter(txt=filter_text(txt=unfiltered_text)), red_list=red_list))
    # print(arr)
    # tokeniser(arr=filter_array(arr=array_maker(txt=filter_text(txt=unfiltered_text)), red_list=red_list))
    tokeniser(arr=arr)
    totaller()
    matrixInitialiser()

def generate(): 
    word = input("Input three words long prompt: ")
    print("Markov model generation [prompt : generation]: ")
    textGen(b=matrixMapper(), word=word, limit=5)

# initialise()
generate()

# textGen(length=95, data=prob_map, A=A, start=start)

# # genNext(data=prob_map, res=res)


# # print(prob_map)
