greutate = float(input("Greutatea Dvs este: "))
inaltime = float(input("Inaltimea Dvs este: "))

BMI = round(greutate / inaltime ** 2)
            
if (BMI < 18.5):
 print(f"BMI este egal cu {BMI} si sunteti subponderal")
elif (BMI < 25):
    print(f"BMI este egal cu {BMI} si aveti o greutate normala")
elif (BMI < 30):
    print(f"BMI este egal cu {BMI} si sunteti supraponderal")
elif(BMI < 35):
  print(f"BMI este egal cu {BMI} si sunteti obez")
else:
  print(f"BMI este egal cu {BMI} si sunteti obez clinic")