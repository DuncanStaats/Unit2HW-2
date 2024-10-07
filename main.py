print("Welcome to a Priate's life Mad Lib!".center(60,'-'))

User_name = input("Enter in your name: ") #print(user_name.title)
date = input("Enter in a month, date, and year(mm/dd/yy): ")
print("Nexat I will  ask you for 5 nouns, 5 verbs, 3 adjectives, and 2 adverbs")

print("I will first ask you for the nouns!")
noun_1 = input("Enter in the first noun please: ")
noun_2 = input("Enter in the second noun please: ")
noun_3 = input("Enter in the third noun please: ")
noun_4 = input("Enter in the fouth noun please: ")
noun_5 = input("Enter in the fifth noun please: ")

print("I will now ask you for the verbs!")
verb_1 = input("Enter in the first verb please: ")
verb_2 = input("Enter in the second verb please: ")
verb_3 = input("Enter in the third verb please: ")
verb_4 = input("Enter in the fourth verb please: ")
verb_5 = input("Enter in the fifth verb please: ")

print("Now I will ask you for the adjectives!")
adjective_1 = input("Enter in the first adjective please: ")
adjective_2 = input("Enter in the second adjective please: ")
adjective_3 = input("Enter in the third adjective please: ")

print("Finally I will ask you for the adverbs!")
adverb_1 = input("Enter in the first adverb please: ")
adverb_2 = input("Enter in the second adverb please: ")

print(f"Your name is {User_name.title()}")
print(f"Today's date is {date}")
print(f"Once upon a time, in a faraway {noun_1}, there lived a {adjective_1} pirate named Captain {noun_2.title()}.\nEvery day, he would {verb_1} on his magnificent {noun_3} and sail across the {adjective_2} sea in search of {noun_4}.\nWith his trusty crew, they would {verb_2} through storms and {verb_3} hidden treasures.\nOne day, as they were {verb_4} towards a mysterious island, they spotted a {adjective_3} ship on the horizon.\nCaptain {noun_2.title()} quickly shouted to his crew to {verb_5} the sails and prepare for battle.\nThey fought {adverb_1} against the enemy pirates, swinging their {noun_5} and shouting battle cries.\nIn the end, Captain {noun_2.title()} and his crew emerged victoriously, their hearts filled with joy and laughter.\nAnd so, they continued their adventures, living {adverb_2} ever after on the high seas!")