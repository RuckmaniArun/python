import random
import csv
import os
print("Welcome to Number Guessing Game!!")

CSVfile="chances.csv"

def check_CSV_file_Exists():
    if os.path.exists(CSVfile):
        print("File available")
    else:
        print("File not available, so create CSV file")
        with open(CSVfile,"w", newline="") as fp:
            writer=csv.writer(fp)
            writer.writerow(["chances"])
        print("chances.csv file is created")
            

def Generate_Random_Num():
    random_num=random.randint(1,10)
    #print(f"System generated Random number: {random_num}")
    print("User turn to guess the number")
    return random_num

def play_game(random_num):
    chances=1
    user_input=int(input("Enter number between 1 and 10:"))
    while True:
        print("Chances count", chances)
        chances=chances+1
        if user_input==random_num:
            print("Congratulations, you guessed right!!")
            break
        elif user_input > random_num:
            print(f"Number is too high, guess <= {user_input}")
        elif user_input < random_num:
            print(f"Number is too less, guess >= {user_input}")

        if chances<=3:
            user_input=int(input("Enter number between 1 and 10:"))
            #print("Chances count", chances)
            with open(CSVfile,"a") as fp:
                writer=csv.writer(fp)
                writer.writerow([chances])
        else:
            print(f"System generated Random number: {random_num}")
            break

def Number_GuessingName():  
    check_CSV_file_Exists()
    get_random=Generate_Random_Num()
    #print("Random number in another function",get_random)
    play_game(get_random)
    
Number_GuessingName()
    
print("Game over")
 