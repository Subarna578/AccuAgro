from subarna_package import weather_detect,crop_detect
print("WELCOME TO AGROVIT\n")
print("1. Weather Detection \
       2. Favorable crops based on season and soil \
       3. Soil Moisture Detection \
       4. Exit")

choose=int(input("Enter the num\n"))
if choose==1:
    weather_detect()
elif choose==2:
    crop_detect()
    
elif choose==4:
    exit(0)

   

