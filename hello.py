from datetime import datetime

while True:

#Getting object out of class
    now = datetime.now()

#Variables
    year = now.year
    month = now.month
    day = now.day
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    yearbirth = input("Provide your birth year: ")
    monthbirth = input("Provide your birth month: ")
    daybirth = input("Provide your birth day: ")

    yearbirth=int(yearbirth)
    monthbirth=int(monthbirth)
    daybirth=int(daybirth)


    if yearbirth > year or (yearbirth == year and monthbirth > month) or (yearbirth == year and monthbirth == month and daybirth > day) or daybirth >32 or monthbirth > 13:
        print("Incorrect birthday data, try again and check info")
        break
    else:
        ageyears = year - yearbirth
        agemonth = month - monthbirth
        agedays = day - daybirth

        if 0 <= ageyears <= 3:
                print("Ugu - gaga? Get a job lil nigga")
                break
        elif ageyears > 125:
                print("How you so old maaaan?")
                break
        
        if agemonth < 0:
            ageyears -= 1
            agemonth = agemonth + 12 

        if agedays < 0:
            last_month = month - 1 if month > 1 else 12
            amountdaysinprevmonth = None
            if last_month in [1, 3, 5, 7, 8, 10, 12]:
                amountdaysinprevmonth = 31
            elif last_month in [4, 6, 9, 11]:
                amountdaysinprevmonth = 30
            elif last_month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    amountdaysinprevmonth = 29
                else:
                    amountdaysinprevmonth = 28

            if amountdaysinprevmonth is not None:
                agemonth -= 1
                agedays += amountdaysinprevmonth
            if monthbirth < 0 or yearbirth < 0:
                print('Looks like u gived incorrect data in your birthday date. Please try again')
                break

#tool
    Name = input("Provide your earth name: ")

#Operator

    if month < 3 or month > 11:
        timeofyear = "winter"
        weather = "freezing cold, snowy and windy"
    elif 2 < month < 6:
        timeofyear = "spring"
        weather = "becoming warmer and warmer every day"
    elif 5 < month < 9:
        timeofyear = "summer"
        weather = "hot!"
    elif 8 < month < 12:
        timeofyear = "autumn"
        weather = "a little cold and windy"
    

    print(f"""Hello {Name}, welcome back to earth. You are now {ageyears} years, {agemonth} month and {agedays} days years old.
    Current year is {year} today is the {day}th of the {month} month."
    Time for now is {hours} hours, {minutes} minutes and {seconds} seconds. Now is {timeofyear} so the weather now is {weather}."
    """)
