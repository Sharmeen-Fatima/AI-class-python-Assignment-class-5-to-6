#There is we use error handling with user input table..
#lets Starts..
try:
    Table = int(input("Enter your table number and generate your own table. "))

    for Tab in (range(1,11)):
        print(f"{Table} x {Tab} = {Table*Tab}")
except:
    print("Kindly write only number it's a invalid character.. ")
    Tables = int(input("Try again!!... write your number. "))

    for num in (range(1,11)):
        print(f"{Tables} x {num} = {Tables*num}")
    
