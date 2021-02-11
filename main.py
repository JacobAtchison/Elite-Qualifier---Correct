import random
import os


width = os.get_terminal_size().columns

#Ps. ignore the interchanbe use of the word root and route,  i only realised later and am too lazy to change them



#Lists of  key words of different connatations that can be used to check and produce different responses
sad_mood_words = ["terrible", "sad","lonely","anxious","alone","bored","depressed", "bad"]
happy_mood_words = ["happy","ok","okay","awesome","great", "good"]

#Functions to randomly pick a response based on the words inputed into console by the user
def generate_topics_s1():
  #prob get rid of the gerenate topics finction, since it the same topic for each section
  topics = [
    "How have you been in the pandemic" + "\n",
  ]
  return random.choice(topics)

#negative is nice/sympathetic root
def negative_response_1_1(user_input):
  responses = [
    "And why do you feel " + user_input + " is there anything you want to talk about?" + "\n",
    "Yes, Well certainly many people feel " + user_input + " and why might you be feeling this way?" + "\n",
  ]
  return random.choice(responses)

def negative_response_1_2(user_input):
  responses = [
    "Ah, I see... And what have you done to remedy this, have you taken initiative in acomplishing anything? Maybe find a new hobby to forget about it, a change in your lifestyle, etc." + "\n",
  ]
  return random.choice(responses)

def negative_response_1_3(user_input):
  responses = [
    "Okay thank you that is all the information I need... I'm am going to prescribe you some anti-depressants. And I mightly suggest that you find some hobbies to enjoy and take our mind off of things. I thank you for giving me the time of day and hope to see you again." + "\n",
  ]
  return random.choice(responses)

#positive is mean/spiteful root
def positive_response_1_1(user_input):
  responses = [
    "Oh, yeah... haha like anyone can be " + user_input + " during a global pandemic. Now please answer honestly " + "\n",
    "*sighs* Alright it seems someone is delusional, There is no way a NORMAL human can be " + user_input + "now please answer again honestly"  + "\n"
  ]
  return random.choice(responses)

def positive_response_1_2(user_input):
  responses = [
    "Ugh, you must be dilusional... I'll go ahead and write you a prescription for phycosis. Now please leave (don't let the door hit you on your way out), I have a meeting with a normal patient" + "\n"
  ]
  return random.choice(responses)


#root for when input is not in any used list
def exception_response_1_1(user_input):
  responses = [
    "yay sounds fun!, but i didnt quite catch that, mind repeating it" + "\n",
    "What, didn't hear you? could you repeat it " + "\n",
  ]
  return random.choice(responses)

def exception_response_1_2(user_input):
  responses = [
    "Oh, " + user_input + " is what you said, well yes that is certainly a way to feel about this whole situation. Could you explain in more detail?",
  ]
  return random.choice(responses)

def exception_response_1_3(user_input):
  responses = [
    "Ohh that is interesting, well im sorry but that is all the time we have for today, I hope you enjoy the rest of your day, i'll walk you to the door.",
  ]
  return random.choice(responses)

def survey_str_to_int(string):
  #checks that "string" is a string that can be turned into an integer
  #if so, turns string into an int and saves that number in str_int
  #if not returns will ask for an appropriate value continuosly
  x = ""
  while True:
    if string.isdigit() == True:
      str_int = int(string)
      #print(str_int)
      while str_int not in range(1, 11):
        x = input("What you input was not a valid response, please type a number between 1 and 10" + "\n")
        if x.isdigit() == True:
          str_int = int(x)
      return str_int
    else:
      while x.isdigit() != True:
        x = input("What you input was not a valid response, please type a number between 1 and 10" + "\n")



#Main chat bot is split into sections, first section is the 
#"talk" with TherapistBot
#second section is the "end survey"
#You can add more sections by upping the "section counter while
#loop" on the end survey section and adding your part before that
def chatbot():
  quit_character = 'exit'
  user_input = ""


  while user_input.lower() != quit_character:
    #Counter for title
    t_counter = 0
    #To do selective testing of a "section" change section_counter to the number you are using to represent that section 
    section_counter = 1

    #This is the therapistBot section
    while section_counter == 1:
       #Title
      if t_counter == 0:
        print("Welcome To TherapistBot 2020 edition".center(width)) #The .center(width) is from stackoverflow "https://stackoverflow.com/questions/33594958/is-it-possible-to-align-a-print-statement-to-the-center-in-python"
        print("Feel free to leave at anytime by typing (exit)".center(width))
        print()
        t_counter = 1

      user_input = input(generate_topics_s1() + "\n")

      #The nice therapist route
      for word in sad_mood_words:
        if user_input.lower() == word:
          user_input = input(negative_response_1_1(user_input) + "\n")
          user_input = input(negative_response_1_2(user_input) + "\n")
          print(negative_response_1_3(user_input) + "\n")
          section_counter += 1
          break

      #The mean therapist route
      for word in happy_mood_words:
        if user_input.lower() == word:
          user_input = input(positive_response_1_1(user_input) + "\n")
          print(positive_response_1_2(user_input) + "\n")
          section_counter += 1
          break
      #Exception route - ipnut word is not in any list used
      user_input = input(exception_response_1_1(user_input) + "\n")
      user_input = input(exception_response_1_2(user_input) + "\n")
      user_input = input(exception_response_1_3(user_input) + "\n")
      section_counter += 1

    #The end survey section - to fix cyclation issue, move each section into its own "chatbot function" but you will have to make user_input etc.. global variables
    while section_counter == 2:
      score = ""
      print()
      print("That is the end of TherapistBot 2020 Edition.".center(width))
      print("I hope you enjoyed your experience".center(width))
      print("If you would be kind enough".center(width))
      print("to complete a survey over your experience".center(width))
      print("We would appreciate it :)".center(width))
      print("If you would like to take the survey type yes, otherwise type no.".center(width) + "\n")
      input()
      print("Ok, then so we will now have you take the survey".center(width))
      print("please answer truthfully we appreciate any type of feed back!!! So dont be shy.".center(width))
      print()
      print("How would you rate TherapistBot's performance in addressing your needs?")
      score = input("please input a number between 1-10".center(width) + "\n")

      while 1 == 1:
        if user_input.lower() == "n":
          user_input = input("Please input your response :)" + "\n")
          score = user_input

        user_input = input("Are you sure that you would rate TherapistBot with a " + str(survey_str_to_int(score)) + "/10? (y/n)" + "\n")
        if user_input.lower() == "y":
          #score = user_input
          print(score)
          break
        if user_input.lower() != "n":
          user_input = input(f"Please input 'y' or 'n' to accept or deny your answer." + "\n")

      if int(score) <= 5:
        print("... ahh I see, well that is unfortunate would you like to expiernce TherapistBot 2020 Edition again? ")
        user_input = input("If so then type 'again'. If you would like to end your survey type 'exit'" + "\n")
        if user_input.lower() == "again":
          section_counter = 1
          break
      else:
        print("... WOW!!! really thank you so much, im glad you enjoyed your expierence. Would you like to Expiernce TherapistBot 2020 Edition again? ")
        user_input = input(f"If so then type 'again'. If you would like to end your survey type 'exit'" + "\n")
        if user_input.lower() == "again":
          section_counter = 1
      break




if __name__ == "__main__":
  chatbot()


#Pay no heed to this
#this is a function full of random code, i was using to test different things wrong with the code, i just shoved it into a function so i could shrink it
def testing():
  #Run to test if consle ipnut is working
  
  import random

  def positive_response_1_1(user_input):
    responses = [
      "Empty test yes",
      "Empty test tet",
    ]
    return random.choice(responses)

  """
  user_input = input("testing type here " + "\n")

  user_input = input(positive_response_1_1(user_input) + "\n")


  c1 = input()
  c1 = int(c1)
  print()
  print(c1)

  while c1 not in range(1, 11):
    print("test")
    break


  if c1 < 1:
    print("test1")

  if 10 < c1:
    print("test2")
  if 10 < c1 and c1 < 1:
    print("test")
  user_input = ""

  def negative_response_1_1(user_input):
    responses = [
      "And why do you feel " + user_input + " is there anything you want to talk about?",
      "Yes, Well certainly many people feel " + user_input + " and why might you be feeling this way?",
    ]
    return random.choice(responses)

  def negative_response_1_2(user_input):
    responses = [
      "Ah, I see... And what have you done to remedy this, have you taken initiative in acomplishing anything? Maybe find a new hobby to forget about it, a change in your lifestyle, etc."
    ]
    return random.choice(responses)

  def finished_responses_s1(user_input):
    responses = [
      "Okay thank you that is all the information I need... I'm am going to prescribe you some anti-depressants. And I mightly suggest that you find some hobbies to enjoy and take our mind off of things. I thank you for giving me the time of day and hope to see you again.",
    ]
    return random.choice(responses)


  sad_mood_words = ["terrible", "sad","lonely","anxious","alone","bored","depressed", "bad"]
  test = ["1", "2", "3", "4", "5"]

  user_input = input()
  for word in sad_mood_words:
    if user_input.lower() == word:
      print("test2")
      exception_s1 = 2
      user_input = input(negative_response_1_1(user_input) + "\n")
      user_input = input(negative_response_1_2(user_input) + "\n")
      print(finished_responses_s1(user_input))
      break

  #fruits = ["apple", "banana", "cherry"]
  #for x in sad_mood_words:
  #  print(x)
  """


