from menu import MENU, resources
# 여러가지 문제를 한꺼번에 해결하려는 습관을 버리고 하나씩 해결해 나가는 습관 기르기!!

def report_list(answer):
    """반복문활용하는법 알기!!"""
    for i in MENU[answer]["ingredients"]:
        resources[i] -= MENU[answer]["ingredients"][i]


def coin_count(q, d, n, p):
    """동전을 달러로 바꾸고, 합계를 계산한 함수"""
    quarters = float(q) * 0.25
    dimes = float(d) * 0.10
    nickles = float(n) * 0.05
    pennies = float(p) * 0.01
    return quarters + dimes + nickles + pennies


def coffee_machine():
    money = 0
    re_machine = True
    while re_machine:
        user_answer = input(("What would you like? (espresso/latte/cappuccino): ")).lower()
        if user_answer == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\ncoffee: {resources['coffee']}ml\nMoney: ${money}")
        elif user_answer == "espresso" or user_answer == "latte" or user_answer == "cappuccino":
            print("Please insert coins.")
            quarters_cnt = input("How many quarters?: ")
            dimes_cnt = input("How many dimes?: ")
            nickles_cnt = input("How many nickles?: ")
            pennies_cnt = input("How many pennies?: ")
            coin_sum = coin_count(quarters_cnt, dimes_cnt, nickles_cnt, pennies_cnt)
            if coin_sum < MENU[user_answer]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                re_machine = False
            else:
                a = 0
                for ingredients in MENU[user_answer]["ingredients"]:
                    if resources[ingredients] < MENU[user_answer]["ingredients"][ingredients]:
                        a += 1
                if a == 0:
                    pay_change = round(coin_sum - MENU[user_answer]["cost"], 2)
                    money = round(money + coin_sum, 2)
                    report_list(user_answer)
                    print(f"Here is ${pay_change} in change.")
                    print(f"Here is your {user_answer} Enjoy!")
                else:
                    print("Sorry, we don't have resource")
                    re_machine = False


coffee_machine()