#bai03.py: In ra loi gioi thieu (ham co tra ve)

def xin_chao(ten, nam_sinh):
    print(f"Xin chao, minh ten la {ten}.")
    print(f"Minh sinh nam {nam_sinh}.")
    print("Rat vui duoc gap ban.")
    tuoi = 2024 - nam_sinh
    return tuoi
    #Có thể return theo dạng dấu phẩy hoặc một list
    #return tuoi, "hello"
    #return [tuoi, "hello"]
    #Nếu chỉ muốn in tuổi trong list thì print(t[0])

t = xin_chao("My", 2004)
print("Minh " + str(t) + " tuoi.")

#print("Minh " + xin_chao("My", 2004) + " tuoi ") #Có thể làm cách này, thay vì dùng biến t. 
                                                #Tuy nhiên vẫn nên tạo biến




