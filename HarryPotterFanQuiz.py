#Executes code for user to choose their level
levelcount = 0
while levelcount < 1:
    print "Welcome to the Ultimate Harry Potter Fan Quiz! Would you like to be tested on Harry Potter spells, characters or actors? Possible inputs are: spells, characters and actors"
    levelinput = raw_input()
    if levelinput == "spells" or levelinput == "characters" or levelinput == "actors":
        levelcount = levelcount + 1 #Haha I know the "+=" exists, i just prefer it this way to make it easier for me to understand
    else:
        print "Sorry! that is not an option!"
print "You've chosen Harry Potter " + levelinput + "!"

#Executes code for user to choose how many guesses they want
guesscount = 0
while guesscount <1:
    print "How many guesses would you like to have per question? You MUST input a number"
    guessinput = raw_input()
    if guessinput.isdigit():
        if int(guessinput) > 0:
            guesscount = guesscount + 1
        elif int (guessinput) < 1:
            print "That is not a valid option. Please input a number larger than 0!"
    else:
        print "That is not a valid option. Please input a number larger than 0!"
print "You will get " + str(guessinput) + " guesses for each question!"

#Contains the data for each level
spells = """Wingardium 1.______ is the first spell Harry learns in charms class. 2.______ is the unlocking charm. Obliviate is the 3.______ spell. Finally, the 4.______ Curses are a group of three illegal spells. They include the Killing Curse, Cruciatus Curse and 5.______ Curse."""
spellsanswers = [["Leviosa", "leviosa"], ["Alohamora", "alohamora"], ["Memory", "memory", "Forgetfulness", "forgetfulness"], ["Unforgivable", "unforgivable"], ["Imperius", "imperus"]]

characters = """1.______ is the main character of the novels. His two best friends are 2.______ , a redhead and 3.______. His beloved owl is named 4.______ and 5.______ is his mother’s name."""
charactersanswers = [["Harry Potter", "Harry"], ["Ron Weasley", "Ronald Weasley", "Ron", "Ronald"], ["Hermione", "Hermione Granger"], ["Hedwig", "hedwig"], ["Lily", "Lily Potter", "Lily Evans"]]

actors = """1.______ plays the character Harry in the films. His co-stars 2.______ (Ron) and 3.______ (Hermione) acted alongside him. 4.______ played the character Draco Malfoy. 5.______ who plays a minor character in the movies, is famous for his role of Edward from Twilight."""
actorsanswers = [["Daniel Radcliffe", "Daniel"], ["Rupert Grint", "Rupert", "Ed Sheeran"], ["Emma", "Emma Watson"], ["Tom Felton", "Tom"], ["Robert Pattinson", "Robert"]]

#Checks if the word is a blank meant to be filled in
def check_blanks(word):
    if "___" in word:
        return True
    else:
        return False

#Checks if the first input is the correct answer from a cor
def right_answer(input, list):
    for element in list:
        if input == element:
            return True
    return False

#Executes the quiz, using the check_blanks and right_answer functions to find the questions and checks if the user inputted answers are correct
def play_game(quiz, answer):
    questioncount = 0
    quizlist = quiz.split()
    wronganswercount = 0
    wordcount = 0
    for word in quizlist:
        isblank = check_blanks(word)
        if isblank == True:
            while wronganswercount < int(guessinput):
                userinput = raw_input("What should be substituted for " + word + "?")
                isanswercorrect = right_answer(userinput, answer[questioncount])
                if isanswercorrect == False:
                    wronganswercount = wronganswercount + 1
                    print "Sorry, wrong answer! You have " + str(int(guessinput) - wronganswercount) + " attempt(s) left!"
                else:
                    quizlist[wordcount] = userinput
                    replaced = " ".join(quizlist)
                    questioncount = questioncount + 1
                    wronganswercount = 0
                    wordcount = wordcount + 1
                    print "Correct! The current paragraph reads as such:" + str(replaced)
                    break
        else:
            wordcount = wordcount + 1
    return "The quiz is over! Thanks for playing!"

#Executes the game with coresponding level choice
if levelinput == "spells":
    print spells
    print play_game(spells, spellsanswers)
elif levelinput == "characters":
    print characters
    print play_game(characters, charactersanswers)
elif levelinput == "actors":
    print actors
    print play_game(actors, actorsanswers)
