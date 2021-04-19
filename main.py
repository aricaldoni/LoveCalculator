# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#First turn letters into lowercase
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

#First count compatible letters for word true
true_letter_t= name1_lowercase.count("t") + name2_lowercase.count("t")
true_letter_r= name1_lowercase.count("r") + name2_lowercase.count("r")
true_letter_u= name1_lowercase.count("u") + name2_lowercase.count("u")
true_letter_e= name1_lowercase.count("e") + name2_lowercase.count("e")
total_true_letters = str(true_letter_t + true_letter_r + true_letter_u + true_letter_e)

#Then count compatible letters for word love
love_letter_l= name1_lowercase.count("l") + name2_lowercase.count("l")
love_letter_o= name1_lowercase.count("o") + name2_lowercase.count("o")
love_letter_v= name1_lowercase.count("v") + name2_lowercase.count("v")
love_letter_e= name1_lowercase.count("e") + name2_lowercase.count("e")
total_love_letters = str(love_letter_l + love_letter_o + love_letter_v + love_letter_e)

#count the letters in total_love_letters and the letters in total_true_letters:
score = int(total_true_letters + total_love_letters)

#For Love Scores less than 10 or greater than 90, the message should be:
#For Love Scores between 40 and 50, the message should be
#Otherwise, the message will just be their score.
if score <= 10 or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
