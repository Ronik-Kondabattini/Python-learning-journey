import random
secret_number=random.randint(1,100)

atempt=0
max_atemptes=10

print("🙌🙌Wellcome to number Guessing Game🙌🙌")
print("🚨🚨Rules🚨🚨:")
print("1.You Have to Guess number between 1 to 100.")
print("2.You will get hint like Think lower or think higher if you are closw to the secrect number")
print("3.You will get total 10 attempts and get score according to that")
print("😊😊Enjoy the game😊😊")

while atempt<max_atemptes:
    guess=int(input("Guess the number: "))
    atempt=atempt+1
    
    if guess<secret_number:
        print("Think higher")
    elif guess>secret_number:
        print("Think lower")
    elif guess==secret_number:
        print("🎉🎉 Excellent!! Your guess is correct🎉🎉")
        score=100-(atempt-1)*10
        print("Your score is: ",score)
        break
    else:
        print("not valid")
        break
    
    #print("Your number of attempts: ",atempt)
if atempt == max_atemptes:
    print("❌ Out of attempts! The correct number was", secret_number)
    score=100-(atempt-1)*10
    print("Your score is: ",score)

    