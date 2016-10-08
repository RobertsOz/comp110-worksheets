# COMP110 Worksheet B: Flowcharts and Pseudocode (Roberts Ozolins-Ozols)

n is 0  
guessLetterCounter is 0  
guessesLeft is 4  
likenessScore is 0  
print "Input the secret word"  
read secretWord  
for letter in secretWord  
    n + 1  
    secretWord[n] is letter  
end for  
print "Welcome to the Secret word game! Your word is", n ,"letters long. You have", guessesLeft ,"guesses to find out what the word is."  
while guessesLeft > 0  
    print "Make your guess!(", guessesLeft, "guesses left)"  
    read guess  
    for yourGuess in guess  
        guessLetterCounter + 1  
        if yourGuess == secretWord[guessLetterCounter]  
            likenessScore + 1  
        end if  
    end for  
    if likenessScore == n  
        print "YOU WIN!"  
    else if likenessScore < n  
        guessesLeft - 1  
        print "Your likeness Score is", likenessScore  
    end if  
end while  
print "YOU ARE OUT OF GUESSES! YOU LOSE!"  
