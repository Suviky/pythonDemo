# 货币转换
inputStr = input("请输入货币:")
if inputStr[0:3] == "RMB":
    USD = eval(inputStr[3:])/6.78
    print("USD{:.2f}".format(USD))
elif inputStr[0:3] == "USD":
    RMB = eval(inputStr[3:])*6.78
    print("RMB{:.2f}".format(RMB))
else:
    print("输入有误")
