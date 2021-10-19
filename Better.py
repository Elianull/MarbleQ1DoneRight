import pandas as pd
import numpy as np

arr1 = pd.read_csv(open("test1.txt"),delimiter=",").values
arr2 = pd.read_csv(open("test2.txt"),delimiter=",").values
arr3 = pd.read_csv(open("test3.txt"),delimiter=",").values
arr4 = pd.read_csv(open("test4.txt"),delimiter=",").values

def wordPresent(arr,word,x,y):
    if (x >= len(arr) or y >= len(arr)):
        return False
    if (len(word) == 0):
        return True
    if (arr[x][y]==word[0]):
        return wordPresent(arr,word[1:],x+1,y) or wordPresent(arr,word[1:],x,y+1)
    else:
        return wordPresent(arr,word,x+1,y) or wordPresent(arr,word,x,y+1)

# Apparently Python has no method overloading? Weird that that's missing honestly.
def wordPresentS(arr,word):
    return wordPresent(arr,word,0,0)

assert(wordPresentS(arr1,"cat") == False)
assert(wordPresentS(arr1,"aaaaa") == True)
assert(wordPresentS(arr2,"horiz") == True)
assert(wordPresentS(arr3,"vert") == True)