
team_work_list = [10, 20, 30, 40, 50, 60, 70, 80] 

#1.Define a list of numbers [10, 20, 30, 40, 50].
print(type(team_work_list)) 

print("Length of the list: ", len(team_work_list)) #2.Print the length of the list

print("First element of the list is: ", team_work_list[0]) #3.Print the first element of the list

print("Last element of the list is: ", team_work_list[-1])  #4.Print the last element of the list

# Function to ask the user for choice A or B
def ask_choice(prompt):
    while True:
        choice = input(prompt).upper()
        if choice in ['Y', 'N']:
            return choice
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")

#5.Append a new number to the list, ensuring it's not already in the list
while True:
    new_number = int(input("Enter a new number to append to the list: "))
    if new_number not in team_work_list:
        team_work_list.append(new_number)
        print("Updated list is:", team_work_list)
        if ask_choice("Do you want to add one more number to the list? (Y) Yes / (N) No: ") == 'N':
            break
    else:
        print("The number is already in the list. Please enter a different number.")

#7.Remove the ANY element from the list, ensuring it's in the list
while True:
    specific_number = int(input("Enter the element you want to delete from the list: "))
    if specific_number in team_work_list:
        team_work_list.remove(specific_number)
        print("The list after removal ", specific_number, ":", team_work_list) # 8.Print the list after removal
        if ask_choice("Do you want to delete one more number from the list? (Y) Yes / (N) No: ") == 'N':
            break
    else:
        print("The element you entered is not in the list. Please enter a different number.")

#9.Check if a specific number (provided by the user) exists in the list and print the result
number_to_check = int(input("Enter a number to check if it exists in the list: ")) 
if number_to_check in team_work_list:
    print(f"{number_to_check} exists in the list.")
else:
    print(f"{number_to_check} does not exist in the list.")

