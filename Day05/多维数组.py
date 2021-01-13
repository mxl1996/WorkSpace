wsc = {
    "money":19000,
    "house":{
        "beijing":["三环","四环","五环"],
        "shanghai":["静安区","浦东新区"]
    },
    "car":["bmw",'benz','audi','byd'],
    "pets":[
        {"name":"xiaohei","type":"dog"},
        {"name":"xiaobai","type":"cat"},
        {"name":"xiaofen","type":"cat"},
        {"name":"xiaolan","type":"dog"},
    ]
}


#买了一辆五菱宏光
#在杭州西湖区买了房子
#卖掉北京5环的房子，钱增加了 500w
#收养了一只叫咪咪的猫
#统计一下他总共有几辆车
wsc["car"].append("五菱宏光")
wsc["house"]["hangzhou"] = ["西湖区"]
wsc["house"]["beijing"].remove("五环")
wsc["money"] += 5000000
wsc["pets"].append({"name":"咪咪","type":"cat"})
print(len(wsc["car"]))
print(wsc)