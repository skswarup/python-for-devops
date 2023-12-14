# print("hello , Br0 !")
arn = "id:scar::spy:arn::user/scarspy"
# # # print(arn.split("/")[1].upper()) # SCARSPY
# # #####################
# # # str1="scar"
# # # str2="spy"
# # # str= str1+" "+str2
# # # print(str)
# # ################################
# # # print(len(arn))
# # # print(arn.upper())
print(arn.lower())
# # update= arn.replace("spy","wow")
# # print("updated arn = "+ update)
# #######################################
# text = "Python=is=awesome"
# words = text.split("=")
# print("Words:", words)
#----------------------------------------------------
# text="  you are strong       "
# print(text)
# upd_text= text.strip()
# print(upd_text)
#======================================
# str="you are strong"
# substring="are"
# if substring in str:
#     print(substring +" found in the str.")
# -------------------------------------------------
# Rounding
# result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
# print("Rounded:", result5)
# Rounded: 3.14
# ==================================================
# Integer variables
# num1 = 10
# num2 = 5

# # Integer Division
# result1 = num1 // num2
# print("Integer Division:", result1) # 2

# # Modulus (Remainder)
# result2 = num1 % num2
# print("Modulus (Remainder):", result2) # 0

# # Absolute Value
# result3 = abs(-7)
# print("Absolute Value:", result3) # 7
# =======================================
# Basic Calculator
num_1=int(input("Enter your first number= "))
num_2=int(input("Enter your second number= "))

print("Available operations to Perform :")
print("1- Multiplication , 2- Addition, 3- Division, 4- Substraction")
Choose_Operation = input("choose your operation from above: ")

if Choose_Operation == "1" or Choose_Operation == "*" :
    Muliplication_result= num_1 * num_2
    print("your operation result is= " , Muliplication_result)
elif Choose_Operation == "2" or Choose_Operation == "+" :
    Addition_result= num_1 + num_2
    print("your operation result is= ", Addition_result)
elif Choose_Operation == "3" or Choose_Operation =="/" :
    Division_result= num_1 / num_2
    print("your operation result is= ", Division_result)
elif Choose_Operation == "4" or Choose_Operation =="-" :
    Substraction_result= num_1 - num_2
    print("your operation result is= ", Substraction_result)
else :
    print("Your Operation is INVALID!  TRY AGAIN ")
