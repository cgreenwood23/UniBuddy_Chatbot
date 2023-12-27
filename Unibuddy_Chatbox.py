questions = [
"where is the fees office",
"where can i find out more about student accomdation options",
"who can help me find out more about the curriculum",
"what clubs does the university offer",
"who is my student mentor",
"what events are happening on campus"
]

answers = [
"The fees office is located in the South-west of campus. A blue building on the second floor, it should be signposted.",
"Student accomadation options can be found on the university website or there are advisors which can be found on campus",
"You can speak to your Course Advisor or Orientation Leadership.",
"The univeristy offers a wide range of clubs and societies which can be found on the university website",
"You will find out your student mentor during induction week",
"The university offers a wide range of events during freshers week, you can find these on the student union website."
]

print("""\nHi, I am your UniBuddy Chatbot!:)
            
I am here to help you have a positive first university experience.
            
Before we can get to your questions, I need some basic information.
--------- """)
name = input("Firstly, what is your name? ")
print(f"\nHi {name}! It is so nice to meet you!")

age = int(input(f"\nHow old will you be when starting univerity {name}? "))

if age <= 17:
    print("Woah! You must be very talented, you're starting university at a young age.")
elif age >= 18 and age <= 30:
    print("A big life change, what an exciting time in your life!")
else:
    print("Impressed to be starting university later in life, never stop learning!")

faculty = input("\nWhat faculty in the university do you belong to? ")
print(f"Ah, the {faculty} faculty is incredible!")
print(f"""---------
\nThank you! You have answered all the questions I have.

What can I help you with today {name}? I will try my best to answer your questions.

When you have finished with all your questions, please enter 'bye' into the chat.""")

done = False
while not done:
    question = input("\nDo you have a question I can help you with? ")
    
    question = question.lower()
    question = question.strip("?")
    question = question.strip()

    if (question in questions):
        questions_num = questions.index(question)
        print(answers[questions_num])
    elif (question == "bye"):
        done = True
        print("\nThank you for chatting with me today! Please come back to me with any further question.")
    else:
        print("\nI am not sure I know the answer to that question. I will try to find the answer and get back to you.")
