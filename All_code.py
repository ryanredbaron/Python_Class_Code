# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:21:23 2020

@author: Angus

#-------------------------------------------------------------
#Branching Program
x = int(input('Enter an int: '))
if x%2 == 0:
    print('')
    print('even')
else:
    print('')
    print('odd')
print('Done')
#-------------------------------------------------------------
#Nested Conditionals
x = int(input('Enter an int: '))
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print ('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 not by 2')
print('Done')
#-------------------------------------------------------------
#Compound Booleans ELIF
x = 1
y = 2
z = 3
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')
#-------------------------------------------------------------
#IDE Explore
x = 5 
if x != 5:
    print('I am here')
else:
    print('No I am not')
#-------------------------------------------------------------
#While
n = input("You are in a Lost Forest. Go left or right?")
while n == "right":
    n = input("left or right?")
print("You got out!")
#-------------------------------------------------------------
#Control flow, while
n = 0 
while(n < 5):
    print(n)
    n = n+1
#-------------------------------------------------------------
#For
n = 0
for n in range(5):
    print(n)
#-------------------------------------------------------------
#Exercise: vara varb
varA = 2
varB = 2


if type(varA) != str and type(varB) != str:
    if varA > varB:
        print("bigger")
    if varA < varB:
        print("smaller")
    if varA == varB:
        print("equal")
else:
    print("string involved")
#-------------------------------------------------------------
#Exercise: while exercise 1
n = 0
while n < 10:
    n = n + 2
    print(n)
print("Goodbye!")
#-------------------------------------------------------------
#Exercise: while exercise 2
n = 12
print("Hello!")
while n > 2:
    n = n - 2
    print(n)

#-------------------------------------------------------------
#Exercise: while exercise 2
end = 6

foo = 1
sumthis = 0
while foo != end + 1:
    sumthis = sumthis + foo
    foo += 1
print(sumthis)

#-------------------------------------------------------------
#Exercise: for exercise 1
total = 10
for total in range(0,total,2):
    print(total+2)
print("Goodbye!")
#-------------------------------------------------------------
#Exercise: for exercise 2
total = 10
print("Hello!")
for total in range(total,0,-2):
    print(total)
#-------------------------------------------------------------
#Exercise: for exercise 3
end = 6

sumthis = 0
foo = 1
for foo in range(end+1):
    sumthis = sumthis + foo
    foo += 1
print(sumthis)
#-------------------------------------------------------------
#Cube root checking
x = int(input('Int:'))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print("Not cube")
else:
    print(str(ans))

#-------------------------------------------------------------
#Problem 1
s = 'ryan'

vowelcount = 0
for s in s:
    if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
        vowelcount += 1
print("Number of vowels: "+str(vowelcount))

#-------------------------------------------------------------
#Problem 2
s = 'awdshadsindabobasdiojadbobadsabooasdoj'

bobcount = 0
spos = 0
for loc in s:
    if s[spos] == "b":
        if s[spos + 1] == "o":
            if s[spos + 2] == "b":
                bobcount += 1
    spos += 1
    if(spos + 2 == len(s)):
        break
print("Number of times bob occurs is: "+str(bobcount))

#-------------------------------------------------------------
#Problem 3
s = "azcbobobegghakl"
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print("Longest substring in alphabetical order is:", longest)

current = longest =  s[0]
for eachletter in s[1:]:
    if eachletter >= current[-1]:
        current += eachletter
        if len(current) > len(longest):
            longest = current
    else:
        current = eachletter
print("Longest substring in alphabetical order is: ", longest)

#-------------------------------------------------------------
#Exercise: guess my number
NumberMin = 0
NumberMax = 100
NumberGuess = int((NumberMax + NumberMin) / 2)
print("Please think of a number between 0 and 100!")
numberfound = 'FALSE'
while numberfound == 'FALSE':
    print("Is your secret number ",NumberGuess,"?")
    UserInput = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if UserInput == 'h' or UserInput == 'l' or UserInput == 'c':
        if UserInput == 'h':
            NumberMax = NumberGuess
            NumberGuess = int((NumberMax + NumberMin) / 2)
        if UserInput == 'l':
            NumberMin = NumberGuess
            NumberGuess = int((NumberMax + NumberMin) / 2)
        if UserInput == 'c':
            numberfound = 'TRUE'
    else:
        print('Sorry, I did not understand your input.')
print("Game over. Your secret number was:",NumberGuess)
#-------------------------------------------------------------
#Function
def is_even (i):
    '''
    Input: i, a positive int
    Returns true if i is even, otherwise false
    '''
    print("hi")
    return i%2 == 0

is_even(3)
#-------------------------------------------------------------
#Exercise: square
def square(x):
    '''
    x: int or float.
    '''
    return x**2
#-------------------------------------------------------------
#Exercise: Quad
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    z = (a * (x**2) + (b * x) + c)
    return z

#-------------------------------------------------------------
#Function Madness
def func_a():
    print('a')
def func_b(y):
    print('b')
    return y
def func_c(z):
    print('c')
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))
#-------------------------------------------------------------
#Function Madness
x = 12
def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
g(x)
#-------------------------------------------------------------
#Factorial
def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))
#-------------------------------------------------------------
#Factorial
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    floating = base
    if exp == 0:
        return 1
    else:
        while exp != 1:
            floating = base*floating
            exp -= 1
        return floating
#-------------------------------------------------------------
#Factorial
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp <= 0:
        return 1
    return base * rec1`2urPower(base, exp - 1)

#-------------------------------------------------------------
#Exercise: gcd iter
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    mult = min(a,b)
    while mult > 0:
        if(a%mult) == 0 and (b%mult) == 0:
            return mult
        else:
            mult-=1

#-------------------------------------------------------------
#Exercise: Exercise: is in
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    i = len(aStr)
    while i > 0:
        if char == aStr[i-1]:
            return i
        else:
            i-=1
#-------------------------------------------------------------
#Exercise: polysum Grader
import math
def polysum(n,s):
    '''
    Input: n - number of sides(should be an integer)
    s- length of each sides(can be an intger or a float)
    
    Output: Returns Sum of area and the square of the perimeter of the regular polygon(gives a float)
    '''
    def PolyArea(n,s):
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    def PolyPerim(n,s):
        perimeter = n*s
        return perimeter
    sum = PolyArea(n,s) + (PolyPerim(n,s) ** 2)
    return round(sum,4)
#-------------------------------------------------------------
#Exercise: polysum Grader
import math
def polysum(n,s):
    '''
    Input: n - number of sides(should be an integer)
    s- length of each sides(can be an intger or a float)
    
    Output: Returns Sum of area and the square of the perimeter of the regular polygon(gives a float)
    '''
    def PolyArea(n,s):
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    def PolyPerim(n,s):
        perimeter = n*s
        return perimeter
    sum = PolyArea(n,s) + (PolyPerim(n,s) ** 2)
    return round(sum,4)
#-------------------------------------------------------------
#Exercise: Problem 1
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#For each month, calculate statements on the monthly payment and remaining balance.
#12 months = print 2 digit remaining balance
month = 0
while balance != 0:
    month += 1
    balance = round((balance * (1-monthlyPaymentRate))*(1+(annualInterestRate/12)),2)
    #print("Month",month,"Remaining balance:",balance)
    if month%12 == 0:
        print("Remaining balance:",balance)
        break
#-------------------------------------------------------------
#Exercise: Problem 2
balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12

paymentguess = 0
while True:
    testbalance = balance
    for Month in range(12):
        testbalance = round((testbalance - paymentguess)*(1+(monthlyInterestRate)),2)
    if testbalance < 0:
        print("Lowest Payment:",paymentguess)
        break
    else:
        paymentguess += 10
#-------------------------------------------------------------
#Exercise: Problem 3
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
paymentguess = 0
maxdifference = 0.01
MonthlyLower = balance / 12
MonthlyUpper =  (balance*(1 + monthlyInterestRate)**12)/ 12.0
while True:
    testbalance = balance
    paymentguess = (MonthlyUpper + MonthlyLower)/2
    for Month in range(12):
        testbalance = round((testbalance - paymentguess)*(1+(monthlyInterestRate)),2)
    if testbalance > maxdifference:
        MonthlyLower = paymentguess
    elif testbalance < -maxdifference:
        MonthlyUpper = paymentguess
    else:
        break
print('Lowest Payment:', round(paymentguess, 2))
#-------------------------------------------------------------
#Exercise:Tuples
def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    bTup = ()
    i = 0
    for Word in aTup:
        i += 1
        if i%2 == 0 :
            continue
        bTup += (Word,)
    return(bTup)

oddTuples(('I', 'am', 'a', 'test', 'tuple'))
#-------------------------------------------------------------
#Exercise:List
aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
cList == dList
#-------------------------------------------------------------
#Exercise:List
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def timesFive(a):
    return (abs(a ** 2))

applyToEach(testList, timesFive)
print(testList)
#-------------------------------------------------------------
#Exercise:5
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

#print(applyEachTo([inc, square, halve, abs], -3))

#print(applyEachTo([inc, square, halve, abs], 3.0))

print(applyEachTo([inc, max, int], -3))
#-------------------------------------------------------------
#Exercise:
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    totalvalues = 0
    for anDict in aDict.values():
        totalvalues = totalvalues + len(anDict)
    return(totalvalues)
print(how_many(animals))
#-------------------------------------------------------------
#Exercise:
animals = {'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    MaxCount = 0
    BiggestBaddie = ""
    if len(aDict) == 0:
        return None
    for anDict in aDict:
        if len(aDict[anDict]) > MaxCount:
            MaxCount = len(aDict[anDict])
            BiggestBaddie = anDict
    return(BiggestBaddie)

print(biggest(animals))
#-------------------------------------------------------------
#Exercise:Week 3 Problem 1
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import sys

WORDLIST_FILENAME = "words.txt"

def loadWords():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):

    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    WordCheck = ""
    for secretLetter in secretWord:
        for singleletterGuessed in lettersGuessed:
            if secretLetter == singleletterGuessed:
                WordCheck = WordCheck + secretLetter
                break
    return WordCheck == secretWord

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    GuessProgress = ""
    for secretLetter in secretWord:
        LetterFound = False
        for singleletterGuessed in lettersGuessed:
            if secretLetter == singleletterGuessed:
                GuessProgress = GuessProgress + secretLetter
                LetterFound = True
        if LetterFound == False:
            GuessProgress = GuessProgress + "_"
    return GuessProgress

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    RemainingLetters = ""
    for letter in string.ascii_lowercase:
        if letter in lettersGuessed:
            pass
        elif letter not in RemainingLetters:
            RemainingLetters = RemainingLetters + letter
    return RemainingLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    NumberofGuessesLeft = 8
    lettersGuessed = []
    GameStillGoing = True
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long")
    print("-----------")
    while GameStillGoing == True:
        print("You have",NumberofGuessesLeft,"guesses left")
        print("Available Letters:",getAvailableLetters(lettersGuessed))
        GuessedLetter = input("Please guess a letter: ")
        if GuessedLetter not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(GuessedLetter)
            if GuessedLetter in secretWord:
                print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word:"+getGuessedWord(secretWord, lettersGuessed))
                NumberofGuessesLeft -= 1
        print("-----------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            GameStillGoing = False
        if NumberofGuessesLeft == 0:
            print("Sorry, you ran out of guesses. The word was",secretWord,".")
            GameStillGoing = False
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)
#-------------------------------------------------------------
#Exercise:MidTerm - Problem 3
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2
    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    MultGuess = 0
    ExponentGuess = 0
    while MultGuess <= x:
        MultGuess = b**ExponentGuess
        ExponentGuess += 1
    return ExponentGuess - 2

print(myLog(16,2))
#-------------------------------------------------------------
#Exercise:MidTerm - Problem 4
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    RunningTotal = 0
    RunningCounter = 0
    for NumA in listA:
        RunningTotal = RunningTotal + (NumA * listB[RunningCounter])
        RunningCounter += 1
    return RunningTotal
#-------------------------------------------------------------
#Exercise:MidTerm - Problem 5

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    values = aDict.values()
    keys = aDict.keys()
    keysList = []
    keycounter = 0
    for key in keys:
        keycounter = 0
        for value in values:
            if value == aDict[key]:
                keycounter +=1
        if keycounter < 2:
            keysList.append(key)
            keysList.sort()
    return keysList

print(uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0}))
#-------------------------------------------------------------
#Exercise:MidTerm - Problem 6
def max_val(t): 
    ''' 
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t 
    '''
    CheckItem = 0
    for eachitem in t:
        try:
            if eachitem > CheckItem:
                CheckItem = eachitem
        except:
            if max_val(eachitem) > CheckItem:
                CheckItem = max_val(eachitem)
    return CheckItem


print(max_val((5, (1, 2), [[1], [2]])))
print(max_val((5, (1, 2), [[1], [9]])))
#-------------------------------------------------------------
#Exercise:MidTerm - Problem 6
def satisfiesF(L):
    '''
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    '''
    ListofStrings = L[:]
    for SingleString in ListofStrings:
        if f(SingleString)==False:
            L.remove(SingleString)
    return len(L)

run_satisfiesF(L, satisfiesF)


def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
"""
#-------------------------------------------------------------
#Exercise






































































































































































































































































































