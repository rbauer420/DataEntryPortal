#Welcome to the Intervention Data Reporting Portal. Please enter your username and password to gain access and to submit your Intervention Reporting Form: Input username: jdoe
#Input password: password

#(Add instructions for the user on how to navigate, submit and exit out of the application.)


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
print("What is your name?  ")
name = input()

print(f"Hello " + name + "how old are you?  ")
age = input()


