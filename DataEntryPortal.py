import sys
import csv

#Welcome to the program and password verification 
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


#CSV file
#def draftReport ():
 #   with open('testReport2.csv', 'w') as csv_file:
  #      fieldnames = ['date', 'agency', 'POC', 'county', 'intervention', 'implementation status', 'WP Step 1', 'WP Step 2', 'WP Step 3', 'WP Step 4', 'WP Step 5', 'successes', 'challenges']
   #     csv_writer = csv.writer(csv_file, fieldnames=fieldnames, delimiter='\t')
    #    csv_writer.writeheader()
     #   for line in csv_writer.writerow(dateEntered, agencyEntered, pointOfContactEntered, globalCountyEntered, globalInterventionEntered,):
      #      csv_writer.writerow(line)

       # print(f'Thank you {userName} for submitting your form! Have a great day!\n')
        #sys.exit() 



#def createTestReport(testReport):
    #userInputs = (demographics, workPlan, successBarriers)
    #headers = ['date', 'agency', 'POC', 'county', 'intervention', 'implementation status', 'WP Step 1', 'WP Step 2', 'WP Step 3', 'WP Step 4', 'WP Step 5', 'successes', 'challenges']
    #with open('testReport.csv', 'w', newline='') as csvfile:
     #   filewriter = csv.writer(csvfile)
      #  filewriter.writerow(headers)
       # for _r_ in userInputs:
        #    filewriter.writerow(_r_)

#Global variables: FIX OUTPUT!!!!!
def globalCountyEntered():
    global countyEntered
    globalCountyEntered = globalCountyEntered

def globalInterventionEntered():
    global interventionEntered
    globalInterventionEntered = globalInterventionEntered


#Classes
class demographics:
    def __init__(self, dateEntered, agencyEntered, pointOfContactEntered, globalCountyEntered, globalInterventionEntered):
        self.dateEntered = dateEntered
        self.agencyEntered = agencyEntered
        self.pointOfContactEntered = pointOfContactEntered
        self.globalCountyEntered = globalCountyEntered
        self.globalInterventionEntered = globalInterventionEntered
    
    @classmethod
    def from_input(cls):
        return cls(
            dateEntered = input("1. Please enter today's date: " "  "),
            agencyEntered = input("2. Please enter the name of your agency: " "  "),
            pointOfContactEntered = input("3. Please enter your agencies point of contact: " "  "),
            globalCountyEntered = input("4. Please enter the county served: " "  "),
            globalInterventionEntered  = input("5. Please enter the name of the intervention implemented: " "  "),
        )

def varStep1():
    varStep1 = demographics
    return(varStep1)


class workPlan:
    def __init__(self, implementationProgressEntered, targetPopId, haveIntvMaterials, impFidelity, collectedPrePost, haveSharedData):
        self.implementationProgressEntered = implementationProgressEntered 
        self.targetPopId = targetPopId 
        self.haveIntvMaterials = haveIntvMaterials 
        self.impFidelity = impFidelity 
        self.collectedPrePost = collectedPrePost 
        self.haveSharedData = haveSharedData

    @classmethod
    def from_input(cls):
        return cls(
            implementationProgressEntered = input(f'6. Please select which response option best describes your implementation progress for the intervention, {globalInterventionEntered} '
                                                  '\nA. No activities B. Planning activities only. C. Implementation/maintenance activities:  '),
            targetPopId = input("For the next five questions, please type “y” to report you have completed this step and “n” if you have not completed this workplan step."
                                "\n7. Identified a target audience: " " "),
            haveIntvMaterials = input("8. Obtained intervention materials: " " "),
            impFidelity = input("9. Implemented the intervention with fidelity: " " "),
            collectedPrePost  = input("10. Collected pre- and post-test data: " " "),
            haveSharedData  = input("11. Shared the results with stakeholders: " " "),
        )

def varStep2():
    varStep2 = workPlan
    return(varStep2)


class successBarriers:
    def __init__(self, successesEntered, barriersEntered):
        self.successesEntered = successesEntered
        self.barriersEntered = barriersEntered

    @classmethod
    def from_input(cls):
        return cls(
            successesEntered = input(f'15. Please describe what successes you have experienced in {globalCountyEntered} county in the past six months?: ' ' '),
            barriersEntered = input(f'16. Please describe what barriers you have experienced in {globalCountyEntered} county in the past six months?: ' ' '),
        )

def varStep4():
    varStep4 = successBarriers
    return(varStep4)


#Class Attributes 


#Allows user to review form
def reviewForm():
    print(f"Date: {varStep1.dateEntered}")
    print(f"Agency: {varStep1.agencyEntered}")
    print(f"Point of Contact: {varStep1.pointOfContactEntered}")
    print(f"County Served: {varStep1.globalCountyEntered}")
    print(f"Intervention: {varStep1.globalInterventionEntered()}")
    print(f"Overall Implementation Progress: {varStep2.implementationProgressEntered}")
    print(f"Workplan Step 1 Completed: {varStep2.targetPopId}")
    print(f"Workplan Step 2 Completed: {varStep2.haveIntvMaterials}")
    print(f"Workplan Step 3 Completed: {varStep2.impFidelity}")
    print(f"Workplan Step 4 Completed: {varStep2.collectedPrePost}")
    print(f"Workplan Step 5 Completed: {varStep2.haveSharedData}")
    print(f"Successes: {varStep4.successesEntered}")
    print(f"Challenges: {varStep4.barriersEntered}")


    #print(input(f'Data entered:{dateEntered}, {agencyEntered}, {pointOfContactEntered}, {globalCountyEntered}, {globalInterventionEntered}, {implementationProgressEntered}, {targetPopId}, {haveIntvMaterials}, {impFidelity}, {collectedPrePost}, {haveSharedData}, {successesEntered}, {barriersEntered}'))

                       #print({demographics}(dateEntered, agencyEntered, pointOfContactEntered, globalCountyEntered, globalInterventionEntered), 
                       #workPlan(implementationProgressEntered, targetPopId, haveIntvMaterials, impFidelity, collectedPrePost, haveSharedData), 
                       #successBarriers(successesEntered, barriersEntered))


#Allows user to edit form
def editForm():
    formSection = input('\nWhich section would you like to change?'
        '\n1. Demographics'
        '\n2. Workplan Steps'
        '\n3. Populations Served'
        '\n4. Successes and Barriers'
        '\n5. I do not wish to edit my data\n\t')
    if message.lower() == '1' or message == 'demographics':
        varStep1 = demographics.from_input()
    elif message.upper() == '2' or message == 'workplan steps':
        varStep2 = workPlan.from_input()
    elif message.upper() == '3' or message == 'populations served':
        varStep3 = popServed()
    elif message.upper() == '4' or message == 'successes and barriers':
        varStep4 = successBarriers.from_input()
    else:
        pass 


#Data Entry Portal Instructions and Table of Contents. Prompts for the user on how to navigate and exit out of the application.
print(f'\nWelcome to the Data Entry Portal, {userName}! ')

prompt =  'Please enter which step number that corresponds with what section would you like to enter data:'
prompt +=  '\n1. STEP 1 - Demographics'
prompt +=  '\n2. STEP 2 - Workplan Steps'
prompt +=  '\n3. STEP 3 - Population Served'
prompt +=  '\n4. STEP 4 - Successes and Barriers'
prompt +=  '\n5. REVIEW - Review Data Entered'
prompt +=  '\n6. EDIT - Edit Data Entered'
prompt +=  '\n7. EXPORT - Export Form to CSV File'
prompt +=  '\n8. EXIT - Exit the program\n\t'


#This class is an indefite loop that will repeat until the user exits the portal
tableOfContents = True
while tableOfContents == True:
    message = input(prompt)

    if message.upper() == 'STEP 1' or message == '1':
        varStep1 = demographics.from_input(), workPlan.from_input(), successBarriers.from_input()
    elif message.upper() == 'STEP 2' or message == '2':
        varStep2 = workPlan.from_input(), successBarriers.from_input()
    elif message.upper() == 'STEP 3' or message == '3':
        varStep3 = popServed(self)
    elif message.upper() == 'STEP 4' or message == '4':
        varStep4 = successBarriers.from_input()
    elif message.upper() == 'REVIEW' or message == '5':
        reviewForm()
    elif message.upper() == 'EDIT' or message == '6':
        editForm()
    elif message.upper() == 'EXPORT' or message == '7':
        var = draftReport(self)
    elif message.upper() == 'EXIT' or message == '8':
        print(f'Thank you {globalUserName} for using the Data Entry Portal. Have a great day!\n')
        menu = False
        sys.exit() 
    else:
        print("I'm sorry, I do not understand. Please choose the step number you would like to enter data.")


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

#Python class Export:Once user selects this option, the program will export all of the data entered by the user in a CSV file. 

#Use pickle to display data CSV file graphically. 

 


 #Back burner:
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