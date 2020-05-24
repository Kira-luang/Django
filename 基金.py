# low = int(input('低谷'))
# high = int(input('高位'))
# average = low + (high - low)/2
# print('平均值:', average)

net_value = float(input('昨日净值'))
get_money = float(input('提取金额'))
revalue = float(input('涨幅'))
提取份额 = get_money / (net_value + net_value * revalue)
print(提取份额)

print(提取份额 * (net_value + net_value * revalue))
