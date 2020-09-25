name = input("Please enter your name: ")
height_m = float(input("Please enter your height in meters: "))
weight_kg = float(input("Please enter your weight in kg: "))
def bmifunc(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print(" ")
    print ("The results of the input data and the calculations are the following: ")
    print(name, "your Body Mass Index (BMI) is :",bmi)
    if bmi < 25:
        if bmi < 18.5:
            return name + " you are underweight"
        else:
            return name + " your weight is normal !!! "
    else:
        return name + " you are overweight"
result = bmifunc(name, height_m, weight_kg)
print(result)
print(" ")