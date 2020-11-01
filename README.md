# Project Name: DataEntryPortal

[Program Overview]
  The purpose of this project is to allow users to report data on the progress of their substance use prevention intervention implementation as well as populations served, successes and challenges. The DataEntryProtal creates a report in a separate file for users to review which includes their responses displayed in a list or data visualization format. 


[Python Project Requirements]
    Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program

    Create a class, then create at least one object of that class and populate it with data

    Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program

    Create and call at least 3 functions, at least one of which must return a value that is used

    !!!Visualize data in a graph, chart, or other visual representation of data


[Required system imports:]
  import sys:
      pip install os-sys

  import csv:
      pip install python-csv
  
  from matplotlib import pyplot as plt:
      pip install matplotlib


[Launching program]
  In the terminal enter:
      python DataEntryPortal.py


[Password Verification]
  Once the code is downloaded, the user will be welcomed to the portal and asked for the password, which is "janeDoe".  
  
  If the user enters the correct password, the program will print, "Access Granted," and will be asked to enter their name.
  
  If the user does not enter the correct password, the program will print, "Incorrect Password. Access NOT Granted," and the program will end.
  

[Program Menu]
  After the password verification loop, users will be welcomed to the Data Entry Portal (addressed by the name entered) and the program will enter an endifinite loop named, "tableOfContents," which will repeat until the user exists the program.

  The portal is broken into four steps (programmed as classes): 

      (1) Step 1 - Demograhics (date, name of agency, point of contact, county served, intervention entered)
      (2) Step 2 - Workplan Steps
      (3) Step 3 - Population(s) Served
      (4) Step 4 - Successes and Barriers
      (5) REVIEW - Review Data Entered (Select AFTER you entered data for Steps 1 - 4) 
      (6) VIZ - Data Visualization (Select AFTER you entered data for Steps 1 - 4)
      (7) EXPORT - Export Form to CSV file
      (8) REPORT - Draft Report to TXT file
      (9) EXIT - Exit the program  
      
  If a user enters "step" and a number 1 - 4 (not case sensitive) or only a number, the program will take them to the questions in that class. After the user enters data for every question in the class, the program will take them to the main menu to enter data for all 4 steps.  The users must enter data for all steps and in the order of the steps due to the global variables and functions called througout the program.  

  Once the user is done entering data, they can enter "REVIEW" (not case sensitive) or 5, the program will print the data entered in the terminal and return to the main menu.  If edits to the data a needed, the user only needs to select which step they need to edit data and answer the questions again. 

  Once the user is done entering data, they can enter "VIZ" (not case sensitive) or 6, the program will create three bar graphs based on the data they entered for Step 3 for age, race/ethnicity and target populations served by this intervention. 

  After the user is done entering and reviewing their data, they have the option to export their data to a CSV file by entering "EXPORT" (not case sensitive) or 7.  This function will populate a CSV file titled, "userDataEntryPortalWorkbook.csv" with their data and headers for each of the questions they responded to. 

  After the user is done entering and reviewing their data, they have the option to export their data to a TXT file by entering "REPORT" (not case sensitive) or 8.  This function will populate a TXT file titled, "userDataEntryPortalReport.txt".  The title of the file will say, "{Name of County Entered} INTERVENTION TRACKING FORM and beneath that there will be headers describing each section of the report and their responses for each of the questions they responded to. 

  If the user enters "EXIT" (not case sensitive) or 9, they will be thanked for using the Data Entry Portal and the program will end.  
  
  If the user enters anything other than the promps, the program will print, "I'm sorry, I do not understand. Please choose the step number you would like to enter data.")
  

[Step 1: Demographics]  
  Users will be asked to enter the date, name of their agency, name of point of contact, name of county they serve, and the name of the substance use prevention intervention implemtned in the county they serve (e.g. Strengthening Families, Too Good For Drugs. Local Capacity Building, Media Campaigns, etc.).  The name of the intervention will be imported to the print statement in Step 2 and Step 3 and the name of the county entered will be inputed in Step 4. 
  
 
[Step 2: Workplan Steps]  
  Users will be asked to select from a multiple choice bank their overall implementation progress for the substance use prevention intervention entered in Step 1.  The choice options include, "A. No activities B. Planning activities only. C. Implementation/maintenance activities". The user should enter "A", "B", or "C", but there is no error message if another response is entered. 

  Users will then be asked to input yes "y" or no "n" to report if they have or have not completed the five fidelity steps of their workplan.
  ########### "y" and "n" upper


[Step 3: Population(s) Served]  
Users will be asked to enter whole numbers of people served based on target populations for the intervention entered in Step 1.

Target populations include: 
    People under 18 years old 
    People between 18 and 29 years old
    People 30 or older 
    People who identify as Asian
    People who identify as Black or African American
    People who identify as Caucasian or White
    People who identify as Hispanic
    People who identify as another race or ethnicity not captured in the other categories
    People who live in rural areas 
    People who are classified as having low socio-econmic status
    People who are students
    People who are Veterans

Values inputed by the user will be converted to an integer.

###########Histogram 


[Step 4: Successes and Barriers]  
  The last two questions will allow users to describe the successes and barriers faced during the substance use prevention intervention implementation for the county they entered in Step 1 in an open-ended field.  
