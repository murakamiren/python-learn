# 変数定義(グローバル変数)
from datetime import datetime


hello_world = "hello world from python"

# 定数は大文字で
CONST_LIKE = "const"

# print: 出力, echo
print(hello_world, CONST_LIKE)

# def: function
def easy_math(x, y):
    doubleX = x * 2
    ans = doubleX + y
    return ans

answer = easy_math(5,9)

print(answer)

# 配列
fruit_array = ["バナナ", "りんご", "ぶどう", "スイカ", "メロン", "いちご"]

# for文
for fruit in fruit_array:
    print(fruit + "好き")

number_array = [1,2,3,4,5]

def for_func_sample():
    for number in number_array:
        if number >= 3:
            print("3以上")
        elif number < 3:
            print("3より小さい")

for_func_sample()

date_now = datetime.now()

print(date_now)
print(date_now.year, date_now.month, date_now.day)

date_formatted = date_now.strftime("%Y年%m月%d日 %H:%M:%S")

print(date_formatted)