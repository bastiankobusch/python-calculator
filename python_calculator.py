import os
import yaml

#Functiong defining and translation variable import
def simple_calculator(transl):
    #Initiating loop
    while True:

        print(transl['app_name'])
        try:
            #User input
            num1 = float(input(transl['input_number1']))
            operator = input(transl['input_operator'])
            if operator not in ["+", "-", "*", "/"]:
                print(transl['error_operation']) 
                continue
            num2 = float(input(transl['input_number2']))
        
        #Exception handling
        except ValueError:
            print(transl['error_number'])
            continue

        #Perform calculation
        if operator == "+":
            result = num1 + num2  
        
        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2 

        elif operator == "/":
            result = num1 / num2  

        #Print 
        print("\n" + str(round(result, 3)))

        #Exit choice
        choice = input(transl['input_choice'])
        if choice == "1":
            break

        #Console clear
        #Windows OS
        if os.name=='nt':
            os.system("cls")

        #Mac OS or Linux
        else:
            os.system ("clear")

#Open translations 
language_choice = input("Enter language: DE for german, EN for english: ")
while language_choice not in ['DE', 'EN']:
    print("Invalid language choice. Choose either DE or EN.")
    language_choice = input("Enter language: DE for german, EN for english: ")

#Translation choice german    
project_path = os.path.dirname(os.path.abspath(__file__))
if language_choice == 'DE':
    with open(project_path + "\\DE.yaml",encoding="utf-8") as file:
        translations = yaml.safe_load(file)

#Translation choice english    
if language_choice == 'EN':
    with open(project_path + "\\EN.yaml",encoding="utf-8") as file:
        translations = yaml.safe_load(file)

simple_calculator(translations)
