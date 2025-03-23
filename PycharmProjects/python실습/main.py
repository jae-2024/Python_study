now_time = int(input("현재시간을 입력하시오 : "))
next_class_time = int(input("다음 수업시간을 입력하시오 : "))
money = int(input("현재 가진 돈을 입력하시오 : "))

remaining_time = next_class_time - now_time

if remaining_time <= 15 and money >= 6000:
    print("택시를 타세요.")
elif remaining_time > 15:
    print("걸어가세요.")
else:
    print("택시를 탈 돈이 부족합니다.")

#현재시간, 다음 수업시간, 현재 가진 돈 입력받아서
#남은 시간 15분 이내고 돈이 6000원 이상이면 택시
#남은 시간이 15분 이상이면 걸어오기