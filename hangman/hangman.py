import random, json
def init():
    print("Select Categories:\n\
           1. Famous Manga\n\
           2. Famous Tech Company\n")
    
    #loops if input is not valid
    while True:
        cat_number = int(input("Please choose words category : "))
        if cat_number == 1:
            hangman_main(cat_number-1)
            break
        elif cat_number == 2:
            hangman_main(cat_number-1)
            break
        else:
            print("Invalid category. Please try again")

def hangman_main(file_index):
    "this is main function for reading file and printing output"

    #read word category file
    file_name_list = ["FamousManga.json", "TechCompany.json"]
    file_name = file_name_list[file_index]
    file = open(file_name, 'r')
    word_list = json.load(file)
    file.close()

    #random word index from word list length
    word_dict = word_list[random.randrange(len(word_list))]

    #show hint
    print('Hint: \"%s\"' %''.join(list(word_dict.values())))

    
    word = list(word_dict.keys())[0]

    #create answer space
    answer_list = ['_' if word[i].isalpha() else word[i] for i in range(len(word))]
    #initial score = 0
    score = 0
    #initial wrong word list is empty
    wrong_list = []
    #initial remaining wrong = 10
    wrong_left = 10
    #total space = amount of '_' in answer list
    total_space = answer_list.count('_')

    #game start
    while True:
        if '_' not in answer_list:
            print('You are the winner!! your score is %.2f \n\
You guessed wrong %d times' %(score, 10-wrong_left))
            break
        if wrong_left == 0:
            print("You lose. Please try again next time")
            break
        print(*answer_list, sep=' ', end='')
        print("    score %.4f, remaining wrong guess %d, wrong guessed: %s" %(score, wrong_left, ' '.join(wrong_list)))
        guess = input("Please enter an alphabet you guess : ")

        #wrong input check
        if not guess.isalpha():
            print("This is not ALPHABET!")
            continue
        elif len(guess) > 1:
            print("You can enter only 1 alphabet.")

        #already guess check
        elif guess in wrong_list:
            print("You already guessed this.")
            continue
        elif guess in answer_list:
            print("You already guessed this.")
            continue

        elif guess in word and guess.isalpha():
        #loop to find guess in word 
        #break when word.find(guess) = -1 in other words there is no guess in word
            begin = 0
            while True:
                index = word.find(guess, begin, len(word))
                if index == -1:
                    break
                answer_list[index] = guess
                score += (1/total_space * 100)
                begin = index+1

        else:
            wrong_left -= 1
            wrong_list.append(guess)


init()
