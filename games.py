# Random num gen

import random

leaderboard = []

# print(random.random()*100)
# print(random.randint(40,60))
random_num = random.randint(10, 100)

count = 1
limit = 5
# user_num=int(input("Enter a number: "))
while True:
    if count == 5:
        print("Limit", random_num)
        break
    user_num = int(input("Enter a number: "))

    if user_num == random_num:
        print(f"number match in {count} times")
        leaderboard.append(count)
        play = input("do u wanna play(y/n)").lower()
        if play == "y":
            random_num = random.randint(40, 50)
            count = 0

        else:
            print("Thank you")
            break

    else:

        print("Try Again!!!")
    count += 1
print("Leaderboard(Least attempts = Best):")
leaderboard.sort()
rank = 1
for score in leaderboard:
    print(f"{rank}.{score} attempts")
    rank+=1

