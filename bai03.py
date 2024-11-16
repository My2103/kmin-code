#bai03.py: Chương trình cho người dùng biết so họ nhập vào là âm, dương hay là số 0

#Prompt a number from user
number = int(input("Nhập một số: "))

#Check negative, positive or zero
if (number == 0):
    print("Đây là số 0.")
else:
    if(number > 0):
        print("Đây là số dương.")
    else:
        print("Đây là số âm.")

#Cách 2
#if (x<=0):
    #if(x<0):
        #print("Đây là số âm.")
    #else:
        #print("Đây là số 0.")
#else:
    #print("Đây là số dương.")