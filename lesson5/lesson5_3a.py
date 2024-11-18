#from tkinter import N


def input_data(): #0914
    while True:
        try:    
            cm = int(input("請輸入身高(公分):"))
            if cm > 300:
                    raise Exception("超過300公分")
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(f'輸入錯誤{cm}')
            continue
    while True:
        try:    
            kg = int(input("請輸入體重(公斤):"))
            if kg > 300:
                raise Exception("超過300公分")
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(f'輸入錯誤{kg}')
            continue
    return cm,kg

def get_status(bmi:float)->str: #0918
    if BMI >=35:
        print("重度肥胖：BMI≧35")
    elif BMI >=30:
        print("中度肥胖：30≦BMI")
    elif BMI >=27:
        print("輕度肥胖：27≦BMI")
    elif BMI >=24:
        print("過重")
    elif BMI >=18.5:
        print("正常範圍")
    else:
        print("體重過輕")

while True:
    kg=0  #清除變數
    cm=0  #清除變數
    cm,kg = input_data() #呼叫function

    print(f'身高={cm},體重={kg}')
    cm=(cm/100)*(cm/100)
    BMI=round((kg/cm),2)
    print(f'BMI={BMI}')
    get_status(BMI) #0918 呼喚
    
    play_again = input("還要繼續嗎?(y,n)")
    if play_again == "n":
        break

print('程式結束')