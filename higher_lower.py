import art
from game_data import data
import random
import os

print(art.logo)
compare = random.sample(data,2)

def comparing(a,b):
    if a > b:
        return "A"
    else:
        return "B"
temp=[]    
def select_next():
    temp.append(compare[0])
    compare[0]=compare[1]
    filter= [i for i in data if i not in temp and i!= compare[0]]
    compare[1]=random.choice(filter)
    
def game():
    score=0
    while(True):
        print(f'Compare A: {compare[0]["name"]}, {compare[0]["description"]}, from {compare[0]["country"]}')
        print(art.vs)
        print(f'Compare B: {compare[1]["name"]}, {compare[1]["description"]}, from {compare[1]["country"]}')
        comparison = input("Who has more followers ? Type 'A' or 'B': ")

        if comparison == comparing(compare[0]["follower_count"],compare[1]["follower_count"]):
            print("Correct")
            os.system('cls')
            print(art.logo)
            score+=1
            print(f"\nYour score is {score}\n")
            select_next()

        else:
            os.system('cls')
            print(art.logo)
            print(f'Final score: {score}')
            return False

game()






