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
        '\n3. Populations Served'
        '\n4. Successes and Barriers'
        '\n5. I do not wish to edit my data\n\t')
    if message.lower() == '1' or message == 'demographics':
        demographics(self) 
    elif message.upper() == '2' or message == 'workplan steps':
        workPlan()
    elif message.upper() == '3' or message == 'populations served':
        popServed()
    elif message.upper() == '4' or message == 'successes and barriers':
        successBarriers()
    else:
        pass

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
        editForm()
    elif message.upper() == 'STEP 2' or message == '2':
        editForm()
    elif message.upper() == 'STEP 3' or message == '3':
        editForm()
    elif message.upper() == 'STEP 4' or message == '4':
        editForm()
    elif message.upper() == 'EXIT' or message == '5':
        print('Thank you for using the Data Entry Portal. Have a great day!\n')
        menu = False
        sys.exit() 
    else:
        print("I'm sorry, I do not understand. Please choose the step number you would like to enter data.")


#Adds data entered into program to DataEntryPortalReport.py
#def report(self):
    #file = open("DataEntryPortalReport.txt", "a")
    #file.write(self+"\n")
    #pass 

#if __name__ == '__main__':
    #report(input(userName))

    #Add code for adding user inputs to DataEntryPortalReport.py

#Python class demographics: date, agency, POC, county served, intervention name => Q1 - 5
#class demographics:

class demographics:
    def __init__(self, dateEntered, agencyEntered, pointOfContactEntered, countyEntered, interventionEntered):
        self.dateEntered = dateEntered
        self.agencyEntered = agencyEntered
        self.pointOfContactEntered = pointOfContactEntered
        self.countyEntered = countyEntered
        self.interventionEntered = interventionEntered

dateSubmitted = input("1. Please enter today's date: " "  ")
dateEntered = dateSubmitted

agencyName = input("2. Please enter the name of your agency: " "  ")
agencyEntered = agencyName

pointOfContact = input("3. Please enter your agencies point of contact: " "  ")
pointOfContactEntered = pointOfContact

countyServed = input("4. Please enter the county served: " "  ")
countyEntered = countyServed

interventionName = input("5. Please enter the name of the intervention implemented: " "  ")
interventionEntered = interventionName
    
    
    #demoTable = PrettyTable(["dateSubmitted",
    #                        "agencyName", 
    #                         "pointOfContact", 
    #                         "countyServed", 
    #                         "interventionName"])
    #demoTable.add_column("Date:")
    #demoTable.add_column("Name of Agency")
    #demoTable.add_column("Point of Contact")
    #demoTable.add_column("County Served")
    #demoTable.add_column("Name of Intervention")

    #print(demoTable)


#Python class workPlan, overall implementation progress

class workPlan:
    def __init__(self, implementationProgressEntered, targetPopId, haveIntvMaterials, impFidelity, collectedPrePost,haveSharedData):
        self.implementationProgressEntered = implementationProgressEntered 
        self.targetPopId = targetPopId 
        self.haveIntvMaterials = haveIntvMaterials 
        self.impFidelity = impFidelity 
        self.collectedPrePost = collectedPrePost 
        self.haveSharedData = haveSharedData

    implementationProgress = input(f'6. Please select which response option best describes your implementation progress for the intervention, {interventionEntered} '
                              '\nA. No activities B. Planning activities only. C. Implementation/maintenance activities:  ')

    implementationProgressEntered = implementationProgress
    
    #if "no activities":
        #skip to class successes_barriers
    #else: 
        #continue with reporting (question 7) 


# Python class workPlan: "Please type “y” to report you have completed this step and “n” if you have not completed this workplan step."

print("Please type “y” to report you have completed this step and “n” if you have not completed this workplan step.")

targetPop = input("7. Identified a target audience: " " ")
targetPopId = targetPop

intvMaterials = input("8. Obtained intervention materials: " " ")
haveIntvMaterials = intvMaterials

fidelity = input("9. Implemented the intervention with fidelity: " " ")
impFidelity = fidelity

prePostData = input("10. Collected pre- and post-test data: " " ")
collectedPrePost = prePostData

shareData = input("11. Shared the results with stakeholders: " " ")
haveSharedData = shareData

            #(Display in a pie graph the total number of activity steps completed (yeses) out of total number of intervention steps)

            #If steps == 5, or if steps < 5, skip to class successes_barriers 


#Python class populationServed: "Please enter the total number for each population served by each demographics category:
class popServed:
    pass

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


#Python class successBarriers: 
class successBarriers:
    def __init__(self, successesEntered, barriersEntered):
        self.successesEntered = successesEntered
        self.barriersEntered = barriersEntered

successes = input(f"15. Please describe what successes you have experienced in {countyEntered} county in the past six months?: " " ")
successesEntered = successes

barriers = input(f"16. Please describe what barriers you have experienced in {countyEntered} county in the past six months?: " " ")
barriersEntered = barriers



#Python class report:Once user reaches this point, the application will display all of the data entered by the user in  a summary report, including graphs. 
        
# Then the message will display, 
print(f"Thank you {userName} for submitting your form!")   






