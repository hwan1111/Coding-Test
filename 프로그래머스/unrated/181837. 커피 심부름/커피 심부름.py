def solution(order):
    order_dict = {"iceamericano" : 0, "americanoice" : 0, "hotamericano" : 0,\
                  "americanohot" : 0, "icecafelatte" : 1, "cafelatteice" : 1,\
                  "hotcafelatte" :1, "cafelattehot" : 1, "americano" : 0,\
                  "cafelatte" : 1, "anything" :0}
    price = 0
    ame = 0
    latte = 0
    for menu in order:
        if order_dict[menu] == 0:
            ame += 1
        else:
            latte += 1
    price = 4500*ame + 5000*latte
    return price