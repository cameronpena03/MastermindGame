import random
list1=[]
def create_comp_list():
    while len(list1) < 4:
        random_num=random.randint(1,7)
        if random_num not in list1:
            list1.append(random_num)
    return list1
def get_guess():
    while True:
        try:
            user_input=input("Enter a number: ")
            user_list=[]
            for item in user_input:
                user_list.append(int(item))
            illegal_num1=False
            illegal_num2=False
            illegal_len=False
            for number in user_list:
                if number>7 or number<1:
                    illegal_num1=True
                if user_list.count(number)>1:
                    illegal_num2=True
            if len(user_list)!=4:
                illegal_len=True
            if illegal_num1:
                print "The number is not in range (1-7)"
            if illegal_num2:
                print "The number should be unique"
            if illegal_len:
                print "The number should have a length of 4"
            if not illegal_num1 and not illegal_num2 and not illegal_len:
                return user_list
        except ValueError:
            print "Enter only numbers"
def check_values(num_array,guesses):
    response=[]
    for number in num_array:
        if number in guesses:
            if num_array.index(number)==guesses.index(number):
                response.append("RED")
            else:
                response.append("WHITE")
        else:
            response.append("BLACK")
    random.shuffle(response)
    print response
def check_win():
    win=0
    for item in response_list:
        if item=="RED":
            win=win+1
    if win==4:
        print "You Win!"
    else:
        print "Try Again"
def play_game():
    game_list=create_comp_list()
    guesses=0
    while guesses<5:
        print "Guesses left: " + str(5- guesses)
        user_input=get_guess()
        if check_values(game_list,user_input)==4:
            break
        guesses=guesses+1
    if guesses==5:
        print "Game Over"
        print "The answer was: " + str(game_list)
# Print directions telling the user how to play the game. Then call the
# play_game function to begin the game, using all of your prewritten functions.
play_game()
