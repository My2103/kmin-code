import random
#secret_number = random.randint(1, 100)
secret_number = 21


score = 0


for attempt in range(1, 4):
    # Nhập số dự đoán của người chơi
    guess = int(input(f"Lần đoán thứ {attempt}: Nhập một số từ 1 đến 100: "))

    # Kiểm tra dự đoán
    if guess == secret_number:
        if attempt == 1:
            score = 100
        elif attempt == 2:
            score = 50
        elif attempt == 3:
            score = 30
        print(f"Chúc mừng! Bạn đã đoán đúng số bí mật là {secret_number}. Số điểm của bạn là {score}.")
        break
    else:
        # Gợi ý cho người chơi nếu đoán sai
        if guess < secret_number:
            print("Số của bạn nhỏ quá.")
        else:
            print("Số của bạn lớn quá.")
else:
    print(f"Game over. Số bí mật là {secret_number}. Bạn không đoán đúng trong 3 lần.")