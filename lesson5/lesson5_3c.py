import tools #0914

while True:
    kg=0  #清除變數
    cm=0  #清除變數
    cm,kg = tools.input_data() #呼叫function

    print(f'身高={cm},體重={kg}')
    BMI = tools.calculate_bmi(cm=cm,kg=kg) #引數名稱的呼叫,可以不依照順序
    print(f'BMI={BMI}')
    print(tools.get_status(BMI))
    
    play_again = input("還要繼續嗎?(y,n)")
    if play_again == "n":
        break
print('程式結束')