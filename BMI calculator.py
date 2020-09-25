name = input("Please enter your name: ")
height_m = float(input("Please enter your height in meters: "))
weight_kg = float(input("Please enter your weight in kg: "))
# name = "Thodoris"
# height_m = 1.69
# weight_kg = 45

def bmifunc(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi:",bmi)
    if bmi < 25:
        if bmi < 18.5:
            return name + " is underweight"
        else:
            return name + " is normal weight!!! "
    else:
        return name + " is overweight"
result = bmifunc(name, height_m, weight_kg)
print(result)