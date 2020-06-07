print("몸무게(kg)와 키(cm)를 입력:")
weight = float(input())
tall = float(input())
bmi = weight / (tall * tall * 0.0001)

if(bmi >= 20 and bmi < 25):
    print("표준입니다")
else:
    print("체중관리가 필요합니다")

