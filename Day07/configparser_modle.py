# Auther: ZhengZhong,Jiang

import configparser


config = configparser.ConfigParser()
config.read('configparser.info', encoding='utf-8')
ret = config.sections()
print(ret)

ret = config.items('section2')
print(ret)

ret = config.options('section1')
print(ret)

ret = config.has_section('section3')
print(ret)

ret = config.has_option('section1', 'k1')
print(ret)

ret = config.get('section2', 'k3')
print(ret)

# ret = config.add_section('section3')
# config.write(open('configparser.info', 'w'))

ret = config.remove_section('section3')
config.write(open('configparser.info', 'w'))

ret = config.remove_option('section2', 'k4')
config.write(open('configparser.info', 'w'))

ret = config.set('section1', 'k5', 'alex')
config.write(open('configparser.info', 'w'))
