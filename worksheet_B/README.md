# COMP110 Worksheet B: Flowcharts and Pseudocode (Roberts Ozolins-Ozols)

*n* **is** 0 __*|Number of letters in the secret word*__  
*guessLetterCounter* **is** 0 __*|Number of letters in your guess*__  
*guessesLeft* **is** 4 __*|Number guesses left*__  
*likenessScore* **is** 0 __*|The words likeness score*__  
**print** "Input the secret word"  
**read** *secretWord*  
**for** *letter* **in** *secretWord* __*|List and count the secret words letters*__  
    *n* + 1  
    *secretWord*[*n*] **is** *letter*  
**end for**  
**print** "Welcome to the Secret word game! Your word is", *n* ,"letters long. You have", *guessesLeft* ,"guesses to find out what the word is."  
**while** *guessesLeft* > 0  
    **print** "Make your guess!(", *guessesLeft*, "guesses left)"  
    **read** *guess*  
    **for** *yourGuess* **in** *guess*  
        *guessLetterCounter* + 1 __*|Assign a number to each letter of the guess*__  
        **if** *yourGuess* == *secretWord*[*guessLetterCounter*] __*|Check each corresponding letter against the secret word*__  
            *likenessScore* + 1  
        **end if**  
    **end for**  
    **if** *likenessScore* == *n* __*|Print result if the words are the same*__  
        **print** "YOU WIN!"  
    **else if** *likenessScore* < *n* __*|If the words are not equal remove 1 guess and display likeness score*__  
        *guessesLeft* - 1  
        **print** "Your likeness Score is", *likenessScore*  
    **end if**  
**end while**  
**print** "YOU ARE OUT OF GUESSES! YOU LOSE!"__*|This prints when you are out of guesses*__  


Flowchart [[flowchart.png]]
