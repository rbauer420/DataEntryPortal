import sys

print ("Welcome to the Intervention Data Reporting Portal. Please enter your password to gain access and to submit your Intervention Reporting Form:")
 
password = input("Enter your password:  ")
if password == "janeDoe":
    print ("Access Granted")
else:
    print("Incorrect password. Access NOT granted")
    sys.exit() 


# Initialize once the user enters correct user name
askName = input("Welcome to the Data Entry Portal! Can I have your " "name:  ")
userName = askName

def editForm():
    #Allows user to edit form
    formSection = input('\nWhich section would you like to change?'
        '\n1. Demographics'
        '\n2. Workplan Steps'
        '\n2. Populations served'
        '\n2. Successes and Barriers'
        '\n3. None\n\t')
    #if:
    #elif:
    #else:

#(Data Entry Portal Instructions and Table of Contents. Prompts for the user on how to navigate and exit out of the application.)
print(f'\nWelcome to the Data Entry Portal, {userName}! '
        'Please enter which step number that corresponds with what section would you like to enter data:')

prompt =  '\n1. STEP 1 - Demographics'
prompt +=  '\n2. STEP 2 - Workplan Steps'
prompt +=  '\n3. STEP 3 - Population Served'
prompt +=  '\n4. STEP 4 - Successes and Barriers'
prompt +=  '\n5. EXIT - Exit the program\n\t'


#This class is an indefite loop that will repeat until the user exits the portal
tableOfContents = True
while tableOfContents == True:
    message = input(prompt)

    if message.upper() == 'STEP 1' or message == '1':
        demographics()
    elif message.upper() == 'STEP 2' or message == '2':
        workPlan()
    elif message.upper() == 'STEP 3' or message == '3':
        popServed()
    elif message.upper() == 'STEP 4' or message == '4':
        successBarriers()
    elif message.upper() == 'EXIT' or message == '5':
        print('Thank you for using the Data Entry Portal. Have a great day!\n')
        menu = False
        sys.exit() 
    else:
        print("I'm sorry, I do not understand. Please choose the step number you would like to enter data.")
        
#Python class demographics: date, agency, POC, county served, intervention name => Q1 - 5


#Python class implementation phase (name of interventio), "Please select which response option best describes your implementation progress for the {user inputed intervention name}:" > Q6
    #A.	No activities B. Yes implementation/maintenance activities or C. Planning only 
    #if "no activities":
        #skip to class successes_barriers
    #else: 
        #continue with reporting (question 7) 


# Python class workplan_steps: "Please type “y” to report you have completed this step and “n” if you have not completed this workplan step."
    #7.	Identified a target audience: y/n
    #8.	Obtained intervention materials: y/n
    #9.	Implement the intervention with fidelity: y/n
    #10.	Collected pre- and post-test data: y/n
    #11.	Shared the results with stakeholders: y/n

            #(Display in a pie graph the total number of activity steps completed (yeses) out of total number of intervention steps)

            #If steps == 5, or if steps < 5, skip to class successes_barriers


#Python class populations_served: "Please enter the total number for each population served by each demographic category:
    #12. Age:
        #A.	Under 18: ___
        #B.	18 – 29: ___
        #C.	30 or older: ___
    #13. Race and Ethnicity:
        #A.	Asian: ___
        #B.	Black/African American: ___
        #C.	White/Caucasian: ___
        #D.	Hispanic: ___
        #E.	Other: ___
    #14.	Target populations: 
        #A.	Individuals living in rural areas: ___
        #B.	Persons with low SES: ___
        #C.	Students 
        #D.	Veterans: ___

            #(Once user enters data, the program will display the entered data as a bar graph)


#Python class successes_barriers: 
    #15.	Please describe what successes you have experienced in {user input county name} county in the past six months? (O/E)

    #16.	Please describe what barriers you have experienced in {user input county name} county in the past six months? (O/E)



#Python class report:Once user reaches this point, the application will display all of the data entered by the user in  a summary report, including graphs. 
        
        # Then the message will display, 
            # “Thank you {user input POC name} for submitting your form!”



#Participant demographics
#print("What is your name?  ")
#name = input()

#print(f"Hello " + name + "how old are you?  ")
#age = input()


