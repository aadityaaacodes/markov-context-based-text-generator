import numpy as np
import json
import os

# json file paths
mFile = 'json/map.json'
pFile = 'json/prob.json'
tFile = 'json/total.json'
iFile = 'json/vocab.json'

def matrixInitialiser():
    '''Initial population of prob.json'''
    #markov matrix
    with open(pFile, "r") as f:
        prob_map = json.load(f)

    with open(tFile, "r") as f:
        total_map = json.load(f)

    with open(mFile, "r") as f:
        n_step = json.load(f)

    # setup
    for i in n_step.keys():
        for j in n_step[i].keys():
            prob_map[i] = {}
    
    with open(pFile, "w") as f:
        json.dump(prob_map, f, indent=4)
    
    for i in n_step.keys():
        for j in n_step[i].keys():
            prob = n_step[i][j]/total_map[i]
            # print(f"{i}:[{j}:{prob}]")
            prob_map[i][j] = prob

    with open(pFile, "w") as json_file:
        json.dump(prob_map, json_file, indent=4)

    # return(prob_map)


def matrixMapper():
    """Extracts all unique words and returns a word-to-index mapping and sorted vocab list."""
    with open(pFile, "r") as f:
        data = json.load(f)
    vocab = sorted(set(data) | set(k for v in data.values() for k in v))
    word2idx = {word: idx for idx, word in enumerate(vocab)}
    with open(iFile, "w") as json_file:
        json.dump(word2idx, json_file, indent=4)

    return vocab


def makeMatrix(vocab):
    """Creates and populates a square adjacency matrix based on the input data and word-to-index mapping."""
    with open(pFile, "r") as f:
        data = json.load(f)
    with open(iFile, "r") as f:
        word2idx = json.load(f)
    matrix = np.zeros((len(vocab), len(vocab)))
    # Populating the matrix
    for src, targets in data.items():
        for tgt, val in targets.items():
            i, j = word2idx[src], word2idx[tgt]
            # print(val)
            matrix[i, j] = val
    # print(matrix.shape)
    return (matrix)


def stateZero(word):
    '''Creating and returning pi0'''
    with open(iFile, "r") as f:
        idx = json.load(f)
    v = matrixMapper()
    arr = np.zeros(len(v))
    arr[idx[word]] = 1
    return(arr)


def operations(A, pi_0):
    """Vector operations for markov mat.
    A -> transition mat.
    pi_0 -> zero state
    """
    pi = np.matmul(pi_0, A)

    for i in range(100):
        new_pi = np.matmul(pi, A)
        if np.all(np.abs(new_pi - pi) < 0.000000001):
            # print(f"Converged at iteration {i}")
            break
        pi = new_pi
        # print(f"Iteration {i}: {pi}")

    return(pi)


def genNext(res):
    '''generates next word based on max prob of pi_n'''
    # highest prob of consecutive word
    ind = (np.argmax(res))
    # res[ind] = 0
    # idx, v = matrixMapper()
    with open(iFile, "r") as f:
        idx = json.load(f)
    # reverse mapping dictionary
    idx2word = {idx: word for word, idx in idx.items()}
    return(idx2word[ind])


def textGen(word, b, limit):
    sentence = ""
    sentence = sentence + word + ": "
    A = makeMatrix(vocab=b)
    pi0 = stateZero(word=word)
    res = operations(A=A, pi_0=pi0)
    w = genNext(res=res)
    sentence = sentence + w + " "
    # print(res, w)
    for i in range(0, limit):
        res = operations(A=A, pi_0=res)
        w = genNext(res=res)
        sentence = sentence + w + " "
        # print(res, w)
    print(sentence)

