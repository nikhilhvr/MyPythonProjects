print("Welcome to the Best Quiz game of this whole universe")

print("make sure you got your facts right and don't google things :) ")
play = input("Do you want to play this awesome game right now?? Ans: ")
count = 0
if play != "yes":
    quit("okay bie :( You don't deserve this game buddy.. work on your GK skills")
else:
    print("Lessss go!!")

ans = input("People who work together: ".lower())
if ans == "Worker":
    print("Correct!")
    count += 1
else:
    print("Incorrect! Be carefull in next one")  

ans1 = input("One who goes on foot: ".lower())
if ans1 == "Pedestrian":
    print("Correct!")
    count += 1
else:
    print("Incorrect! Be carefull in next one")  

ans2 = input("One who can speak two languages: ".lower())
if ans2 == "Bilingual":
    print("Correct!")
    count += 1
else:
    print("Incorrect! Be carefull in next one")  

ans3 = input("Word with the same meaning: ".lower())
if ans3 == "Synonyms ":
    print("Correct!")
    count += 1
else:
    print("Incorrect! Be carefull in next one")  

ans4 = input("The person who works for free: ".lower())
if ans4 == "Volunteer":
    print("Correct!")
    count += 1
else:
    print("Incorrect! Be carefull in next one") 

ans5 = input("One who speaks less: ".lower())
if ans5 == "Reticent ":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")                    

print("You answered all the questions, Let's see your score" + str(count))
