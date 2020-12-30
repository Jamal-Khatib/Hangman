WORDLIST_FILENAME = "words.txt"
import random
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)




def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    c=0
    for i in secretWord:
        if i in lettersGuessed:
            c+=1
    return(c==len(secretWord))
  
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    your_guess1=''
    for i in secretWord:
        if i in lettersGuessed:
            your_guess1+=i
        else:
            your_guess1+=' _ '
    return(your_guess1)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available_letters=''
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in all_letters:
        if i not in lettersGuessed:
            available_letters+=i
    return(available_letters)



def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of word that is '+str(len(secretWord))+(' letters long.'))
    mistakesMade=0
    lettersGuessed=[]
    availableLetters=getAvailableLetters(lettersGuessed)
    guesses_left=8
    
    while not isWordGuessed(secretWord,lettersGuessed) and ( mistakesMade<=8 and guesses_left>0):
        print('---------------')
        print('You have '+str(guesses_left)+' guesses left')
        print('Available Letters: ',getAvailableLetters(lettersGuessed))
        your_guess = input('Please guess a letter: ')
        if (your_guess in secretWord)  and (your_guess not in lettersGuessed):
            lettersGuessed+=[your_guess]
            print('Good Guess:',getGuessedWord(secretWord,lettersGuessed))
        elif your_guess not in secretWord and your_guess not in lettersGuessed:
            mistakesMade+=1
            guesses_left-=1
            lettersGuessed+=[your_guess]
            print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed))
        elif  your_guess in lettersGuessed:
            print('Oops! You’ve already guessed that letter:',getGuessedWord(secretWord,lettersGuessed))
        
    if isWordGuessed(secretWord,lettersGuessed):
          print('---------------')
          print('Congratulations, you won!')
    else:
         print('---------------')
         print('Sorry, you ran out of guesses. The word was',secretWord)

wordlist=loadWords()
secretWord = chooseWord(wordlist).lower()
hangman("Jamal")
