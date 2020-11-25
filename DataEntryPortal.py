import sys
import csv
from matplotlib import pyplot as plt

#Welcome to the program and password verification 
print ("Welcome to the Intervention Data Reporting Portal. Please enter your username and password to gain access and to submit your Intervention Reporting Form.")
count = 1
while count < 4:
    userName = input("Enter your username:  ")
    password = input("Enter your password:  ")

    if userName == "janeDoe" and password == "secret":
        print ("Access Granted")
        break
    else:
        print("Incorrect login information. You have three chances to enter the correct username and password.")
        count += 1
    if count == 4:
        print("Incorrect username and/or password. Access NOT granted")
        sys.exit()

# Initialize once the user enters correct user name
askName = input("Welcome to the Data Entry Portal! Can I have your " "name:  ")
userName = askName


#Global variables:
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
            implementationProgressEntered = input(f'6. Please select which response option best describes your implementation progress for the intervention {varStep1.globalInterventionEntered}:  '
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


class popServed:
    def __init__(self, ageUnder18, ageUnder30, ageOver30, Asian, BlackAfricanAmerican, White, Hispanic, otherRaceEthnicity, popRural, popLowSES, popStudents, popVeterans): 
        self.ageUnder18 = ageUnder18
        self.ageUnder30 = ageUnder30
        self.ageOver30 = ageOver30
        self.Asian = Asian
        self.BlackAfricanAmerican = BlackAfricanAmerican
        self.White = White
        self.Hispanic = Hispanic
        self.otherRaceEthnicity = otherRaceEthnicity
        self.popRural = popRural
        self.popLowSES = popLowSES
        self.popStudents = popStudents
        self.popVeterans = popVeterans

    @classmethod
    def from_input(cls):
        return cls(
                ageUnder18 = int(input(f"12a. Please enter the total number (as an integer) of people served who were under the age of 18 and served by the intervention {varStep1.globalInterventionEntered}:" " ")),  
                ageUnder30 = int(input(f"12b. Please enter the total number (as an integer) of people served who were aged 18 to 29 and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                ageOver30 = int(input(f"12c. Please enter the total number (as an integer) of people served who were 30 and older and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                Asian = int(input(f"13a. Please enter the total number (as an integer) of people served who identified as Asian and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                BlackAfricanAmerican = int(input(f"13b. Please enter the total number (as an integer) of people served who identified as Black or African American and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                White = int(input(f"13c. Please enter the total number (as an integer) of people served who identified as Caucasian or White and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                Hispanic = int(input(f"13d. Please enter the total number (as an integer) of people served who identified as Hispanic and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                otherRaceEthnicity = int(input(f"13e. Please enter the total number (as an integer) of people served who identified as another race or ethnicity not captured by other categories and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                popRural = int(input(f"14a. Please enter the total number (as an integer) of people served who lived in rural areas and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                popLowSES = int(input(f"14b. Please enter the total number (as an integer) of people served who were classified as low-socioeconomic status and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                popStudents = int(input(f"14c. Please enter the total number (as an integer) of people served who were students and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
                popVeterans = int(input(f"14d. Please enter the total number (as an integer) of people served who were Veterans and served by the intervention {varStep1.globalInterventionEntered}:" " ")),
        )

def varStep3():
    varStep3 = popServed
    return(varStep3)



class successBarriers:
    def __init__(self, successesEntered, barriersEntered):
        self.successesEntered = successesEntered
        self.barriersEntered = barriersEntered

    @classmethod
    def from_input(cls):
        return cls(
            successesEntered = input(f'15. Please describe what successes you have experienced in {varStep1.globalCountyEntered} county in the past six months?: ' ' '),
            barriersEntered = input(f'16. Please describe what barriers you have experienced in {varStep1.globalCountyEntered} county in the past six months?: ' ' '),
        )

def varStep4():
    varStep4 = successBarriers
    return(varStep4)



#Allows user to review form
def reviewForm():
    print(f"Date: {varStep1.dateEntered}")
    print(f"Agency: {varStep1.agencyEntered}")
    print(f"Point of Contact: {varStep1.pointOfContactEntered}")
    print(f"County Served: {varStep1.globalCountyEntered}")
    print(f"Intervention: {varStep1.globalInterventionEntered}")
    print(f"Overall Implementation Progress: {varStep2.implementationProgressEntered}")
    print(f"Workplan Step 1 Completed: {varStep2.targetPopId}")
    print(f"Workplan Step 2 Completed: {varStep2.haveIntvMaterials}")
    print(f"Workplan Step 3 Completed: {varStep2.impFidelity}")
    print(f"Workplan Step 4 Completed: {varStep2.collectedPrePost}")
    print(f"Workplan Step 5 Completed: {varStep2.haveSharedData}")
    print(f"Population served under 18: {varStep3.ageUnder18}")
    print(f"Population served between 18 and 29: {varStep3.ageUnder30}")
    print(f"Population served 30 or older: {varStep3.ageOver30}")
    print(f"Population served who identified as Asian: {varStep3.Asian}")
    print(f"Population served who identified as Black or African American: {varStep3.BlackAfricanAmerican}")
    print(f"Population served who identified as Caucasian or White: {varStep3.White}")
    print(f"Population served who identified as Hispanic: {varStep3.Hispanic}")
    print(f"Population served who identified as another race or ethnicity: {varStep3.otherRaceEthnicity}")
    print(f"Population served who lived in rural areas: {varStep3.popRural}")
    print(f"Population served who were classified as having low-socioeconomic status: {varStep3.popLowSES}")
    print(f"Population served who were students: {varStep3.popStudents}")
    print(f"Population served who were Veterans: {varStep3.popVeterans}")
    print(f"Successes: {varStep4.successesEntered}")
    print(f"Challenges: {varStep4.barriersEntered}")


#Data visualzation
def dataVisualizationAge():
    plt.style.use("fivethirtyeight")
    agePlotx = ["Under 18", "18 - 29", "30 and older"]
    agePloty = ([varStep3.ageUnder18, varStep3.ageUnder30, varStep3.ageOver30])

    plt.bar(agePlotx, agePloty, color="dodgerblue", label="Pop Served Age")
    plt.legend()
    plt.title("Population Served by Age")
    plt.xlabel("Age Group")
    plt.ylabel("Total Served")
    plt.tight_layout()
    plt.show()


def dataVisualizationRaceEthnicity():
    plt.style.use("fivethirtyeight")
    slices = ([varStep3.Asian, varStep3.BlackAfricanAmerican, varStep3.White, varStep3.Hispanic, varStep3.otherRaceEthnicity])
    labels = ["Asian", "Black/African American", "Caucasian/White", "Hispanic", "Other Race/Ethnicity"]
    colors = ['#26E3E0', '#4ACADE', '#38A6D9', '#4076D9', '#3854BD']
    plt.pie(slices, labels=labels, colors=colors, shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

    plt.title("Population Served by Race and Ethnicity")
    plt.tight_layout()
    plt.show()


def dataVisualizationTargetPop():
    plt.style.use("fivethirtyeight")
    targetPopPlotx = ["Persons in Rural Areas", "Persons Classified as Low SES", "Students", "Veterans"]
    targetPopPloty = ([varStep3.popRural, varStep3.popLowSES, varStep3.popStudents, varStep3.popVeterans])

    plt.plot(targetPopPlotx, targetPopPloty, color="#17becf", label="Target Pop Served")
    plt.legend()
    plt.title("Population Served by Target Populations")
    plt.xlabel("Target Population")
    plt.ylabel("Total Served")
    plt.tight_layout()
    plt.show()


#Class Export: Once user selects this option, the program will export all of the data entered by the user in a CSV file. 
def draftCSV():
    with open('userDataEntryPortalWorkbook.csv', 'w', newline='') as f:
        the_writer = csv.writer(f)

        the_writer.writerow(['date', 'agency', 'POC', 'county', 'intervention', 'implementation status', 'WP Step 1', 'WP Step 2', 'WP Step 3', 'WP Step 4', 
                            'WP Step 5', 'Under 18', 'Under 30', 'Over 30', 'Asian', 'Black/African American', 'White', 'Hispanic', 'Other Race or Ethnicity', 
                            'Rural', 'LowSES', 'Students', 'Veterans', 'Successes', 'Barriers'])
        the_writer.writerow([varStep1.dateEntered, varStep1.agencyEntered, varStep1.pointOfContactEntered, varStep1.globalCountyEntered, varStep1.globalInterventionEntered, 
                            varStep2.implementationProgressEntered, varStep2.targetPopId,varStep2.haveIntvMaterials, varStep2.impFidelity, varStep2.collectedPrePost, 
                            varStep2.haveSharedData, varStep3.ageUnder18, varStep3.ageUnder30, varStep3.ageOver30, varStep3.Asian, varStep3.BlackAfricanAmerican, varStep3.White, 
                            varStep3.Hispanic, varStep3.otherRaceEthnicity, varStep3.popRural, varStep3.popLowSES, varStep3.popStudents, varStep3.popVeterans, varStep4.successesEntered, 
                            varStep4.barriersEntered])

    f.close()


#Class Report: Once user selects this option, the program will export all of the data entered by the user to a TXT file. 
def draftReport():
    with open('userDataEntryPortalReport.txt', 'w') as f:
            f.write(f"{varStep1.globalCountyEntered} INTERVENTION TRACKING FORM\n")
            f.write("\n")
            f.write("\n")
            f.write("Demographics:\n")
            f.write("\n")
            f.write(f"Date: {varStep1.dateEntered}\n")
            f.write(f"Agency: {varStep1.agencyEntered}\n")
            f.write(f"Point of Contact: {varStep1.pointOfContactEntered}\n")
            f.write(f"County Served: {varStep1.globalCountyEntered}\n")
            f.write(f"Intervention: {varStep1.globalInterventionEntered}\n")
            f.write("\n")
            f.write("\n")
            f.write("Implementation Progress:\n")
            f.write("\n")
            f.write(f"Overall Implementation Progress: {varStep2.implementationProgressEntered}\n")
            f.write(f"Workplan Step 1 Completed: {varStep2.targetPopId}\n")
            f.write(f"Workplan Step 2 Completed: {varStep2.haveIntvMaterials}\n")
            f.write(f"Workplan Step 3 Completed: {varStep2.impFidelity}\n")
            f.write(f"Workplan Step 4 Completed: {varStep2.collectedPrePost}\n")
            f.write(f"Workplan Step 5 Completed: {varStep2.haveSharedData}\n")
            f.write("\n")
            f.write("\n")
            f.write("Population Served:\n")
            f.write("\n")
            f.write(f"Population served under 18: {varStep3.ageUnder18}\n")
            f.write(f"Population served between 18 and 29: {varStep3.ageUnder30}\n")
            f.write(f"Population served 30 or older: {varStep3.ageOver30}\n")
            f.write(f"Population served who identified as Asian: {varStep3.Asian}\n")
            f.write(f"Population served who identified as Black or African American: {varStep3.BlackAfricanAmerican}\n")
            f.write(f"Population served who identified as Caucasian or White: {varStep3.White}\n")
            f.write(f"Population served who identified as Hispanic: {varStep3.Hispanic}\n")
            f.write(f"Population served who identified as as another race or ethnicity: {varStep3.otherRaceEthnicity}\n")
            f.write(f"Population served who lived in rural areas: {varStep3.popRural}\n")
            f.write(f"Population served who were classified as having low-socioeconomic status: {varStep3.popLowSES}\n")
            f.write(f"Population served who were students: {varStep3.popStudents}\n")
            f.write(f"Population served who were Veterans: {varStep3.popVeterans}\n")
            f.write("\n")
            f.write("\n")
            f.write("Success and Barriers Experienced:\n")
            f.write("\n")
            f.write(f"Successes: {varStep4.successesEntered}\n")
            f.write(f"Challenges: {varStep4.barriersEntered}\n")
    f.close()

#Data Entry Portal Instructions and Table of Contents. Prompts for the user on how to navigate and exit out of the application.
print(f'\nWelcome to the Data Entry Portal, {userName}! ')

prompt =  'Please enter which step number that corresponds with what section would you like to enter or edit previously entered data:'
prompt +=  '\n1. STEP 1 - Demographics'
prompt +=  '\n2. STEP 2 - Workplan Steps'
prompt +=  '\n3. STEP 3 - Population Served'
prompt +=  '\n4. STEP 4 - Successes and Barriers'
prompt +=  '\n5. REVIEW - Review Data Entered (Select AFTER you entered data for Steps 1 - 4)'
prompt +=  '\n6. VIZ - Data Visualization (Select AFTER you entered data for Steps 1 - 4)'
prompt +=  '\n7. EXPORT - Export Form to CSV File'
prompt +=  '\n8. REPORT - Draft Report to TXT file'
prompt +=  '\n9. EXIT - Exit the program\n\t'


#This class is an indefinite loop that will repeat until the user exits the portal
tableOfContents = True
while tableOfContents == True:
    message = input(prompt)
    try:
        if message.upper() == 'STEP 1' or message == '1':
            varStep1 = demographics.from_input()
        elif message.upper() == 'STEP 2' or message == '2':
            varStep2 = workPlan.from_input()
        elif message.upper() == 'STEP 3' or message == '3':
            varStep3 = popServed.from_input()
        elif message.upper() == 'STEP 4' or message == '4':
            varStep4 = successBarriers.from_input()
        elif message.upper() == 'REVIEW' or message == '5':
            reviewForm()
        elif message.upper() == 'VIZ' or message == '6':
            dataVisualizationAge(), dataVisualizationRaceEthnicity(), dataVisualizationTargetPop()
        elif message.upper() == 'EXPORT' or message == '7':
            draftCSV()
        elif message.upper() == 'REPORT' or message == '8':
            draftReport()
        elif message.upper() == 'EXIT' or message == '9':
            print(f'Thank you {userName} for using the Data Entry Portal. Have a great day!\n')
            menu = False
            sys.exit() 
        else:
            print("I'm sorry, I do not understand. Please choose the step number you would like to enter data.")
    except AttributeError:
        print("You MUST enter data for Steps 1 - 4 before you can review.")
        continue
    except ValueError:
        print("You MUST enter integers for Step 3 before you can visualize your data.")
        continue


