#AGE CALCULATOR
def agecalculator(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days /365.25)
    print (age)
agecalculator (1994,3,14)
    
