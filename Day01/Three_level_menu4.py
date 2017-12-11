#!/usr/bin/env python3
# Author: Zhangxunan

import sys
#字典  市-->区-->街道-->公司
china = {
    '北京':{
        '朝阳区':{
            '望京':['SOHO','360','Microsoft','LG'],
            '三里屯':['UNIQLO','McDonald','KFC','Pizza Hut'],
            '三元桥':['CITIC','Sheraton Hotel','FOUR SEASONS','VW'],
            '亮马桥':['Fenghuang','CCB','ABC','COMM']
        },
        '海淀区':{
            '西二旗':['Baidu','Lenovo','HUAWEI','Oracle'],
            '上地':['Digital China','IBM','Founder','TSINGHUA TONGFANG'],
            '西直门':['CHINA GUODIAN','CEBBANK','CHINA LIFE','BGCTV'],
            '中关村':['Sohu','Sina','Intel','AMD']
        }
    },
    '上海':{
        '浦东新区':{
            '陆家嘴':['SHANGHAI ELECTRIC','SPDB','BAOSTEEL','SAIC MOTOR'],
            '周家渡':['CHINA EASTERN','FOSUN','BAILIAN GROUP','GUANGMING'],
            '花木':['CPIC','TAIPING LIFE','SHANGHAI TOBACCO','SHANGHAI COMM'],
            '东明路':['HP','SAIC-GM','E-VADA','SIEMENS']
        },
        '黄浦区':{
            '南京东路':['KODAK','HITACHI','Alcate','Coca-Cola'],
            '外滩':['Pepsi-Cola','Sony','TOSHIBA','WALMART'],
            '小东门':['FORD','Citigroup','TOYOTA','Carrefour'],
            '豫园':['SAMSUNG','Panasonic','HONDA','HSBC']
        }

    }
}

city_dict = {}
area_dict = {}
street_dict = {}
for i,v in enumerate(china.keys(),1):
    city_dict[i] = v
while True:
    for dic in city_dict:
        print(dic, city_dict[dic])
    choice_city_num = input('请输入一个城市号码(q/Q(退出)):')
    try:
        choice_city_num = int(choice_city_num)
        if choice_city_num not in city_dict:
            print('请输入一个有效的号码!')
            continue
    except:
        if choice_city_num == 'q' or choice_city_num == 'Q':
            sys.exit(1)
        else:
            print('请输入一个号码，不是城市名字或其它!')
            continue
    for i,v in enumerate(china[city_dict[choice_city_num]].keys(), 1):
        area_dict[i] = v
    while True:
        for dic in area_dict:
            print(dic,area_dict[dic])
        print('>>', city_dict[choice_city_num])

        choice_area_num = input('请输入一个区号(b/B(返回) q/Q(退出)):')
        try:
            choice_area_num = int(choice_area_num)
            if choice_area_num not in area_dict:
                print('请输入一个有效的区号!')
                continue
        except:
            if choice_area_num == 'b' or choice_area_num == 'B':
                break
            elif choice_area_num == 'q' or choice_area_num == 'Q':
                sys.exit(2)
            else:
                print('必须输入一个区号，不是区的名字或其它!')
                continue

        for i,v in enumerate(china[city_dict[choice_city_num]][area_dict[choice_area_num]].keys(), 1):
            street_dict[i] = v
        while True:
            for dic in street_dict:
                print(dic, street_dict[dic])
            print('>>', city_dict[choice_city_num], '>>', area_dict[choice_area_num])

            choice_street_num = input("请输入一个街道号码(b/B(返回) q/Q(退出)):")
            try:
                choice_street_num = int(choice_street_num)
                if choice_street_num not in street_dict:
                    print('请输入一个有效的街道号码!')
                    continue
            except:
                if choice_street_num == 'b' or choice_street_num == 'B':
                    break
                elif choice_street_num == 'q' or choice_street_num == 'Q':
                    sys.exit(3)
                else:
                    print('必须输入一个街道号码，不是街道的名字或其它!')
                    continue
            print('>>', city_dict[choice_city_num], '>>', area_dict[choice_area_num], '>>', street_dict[choice_street_num])
            print(','.join(china[city_dict[choice_city_num]][area_dict[choice_area_num]][street_dict[choice_street_num]]))
