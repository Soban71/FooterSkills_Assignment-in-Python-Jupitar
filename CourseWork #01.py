#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Raja Asad Mehmood
# MEH21540829
# SD1 coursework 2
# footballer skills program
# 16/04/2023

from tabulate import tabulate
from datetime import datetime

#function to calculate overall rating
def calculate_rating(speed, shooting, passing, defending, dribbling, physicality):
    
    
    # Validate input ratings beteween 1-5
    if not all(0 <= x <= 5 for x in [speed, shooting, passing, defending, dribbling, physicality]):
        print("The rating you entered was invalid")
        return None
    
    
    # Calculate overall rating
    overall_rating = (speed + shooting + passing + defending + dribbling + physicality) * 100 / 30
    return overall_rating

#function to calculate salary range
def calculate_salary(overall_rating):
    if overall_rating >= 80:
        return (1000, 1000)
    elif overall_rating <= 30:
        return (400, 400)
    else:
        return (500, 400)

#unction to calculate player age
def calculate_age(dob):
    today = datetime.today()
    birth_date = datetime.strptime(dob, '%Y-%m-%d')
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Define main function
def main():
    players = []
    while True:
        # Get user input
        uid = input()
        if uid == "end":
            break
        name = input()
        dob = input()
        # checking DOB is valid or noy
        try:
            datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
        #if invalid this message appear
            print("The date of birth you entered was invalid")
            
            #if valid then....
            continue
        
        speed = float(input())
        shooting = float(input())
        passing = float(input())
        defending = float(input())
        dribbling = float(input())
        physicality = float(input())
        
        
        # Calculating the overall rating
        overall_rating = calculate_rating(speed, shooting, passing, defending, dribbling, physicality)
        if overall_rating is None:
            continue
        
        # Calculating salary range
        salary_range = calculate_salary(overall_rating)
        
        
        # Calculate player age
        age = calculate_age(dob)
        
        
        # Store player information
        players.append([uid, name, dob, age, overall_rating, salary_range[0], salary_range[1]])
    
    # sort players by Id
    players.sort(key=lambda x: x[0])
    
    
    
    # Display output  in the table form using tabulate
    headers = ["UID", "Name", "D.o.B", "Age", "Score", "Salary Range"]
    table = [[p[0], p[1], p[2], p[3], "{:.4f}".format(p[4]), "{}-{}".format(p[5], p[6])] for p in players]
    print(tabulate(table, headers=headers))
    
    
    
    # Write results to file
    with open("players.txt", "w") as f:
        f.write(tabulate(table, headers=headers))

if __name__ == "__main__":
    main()

