def calculate_bmi(inches, pounds):
    weigh = pounds * 703 
    bmi = weigh / inches 
    return (bmi / inches)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

def convert_feet_to_inches(height):
    feet, sub = map(int, height.split("'"))
    inches = feet * 12 + sub
    return inches
def kg_to_lbs(weight):
    pounds = float(weight) * 2.20462
    return pounds

def age_group(age):
    age = int(age)
    if age < 50:
        return 'Adult'
    else:
        return 'Senior'