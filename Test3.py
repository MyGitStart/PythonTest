# coding=utf-8

# print 2.0/3

# # sentence=raw_input("Sentence：")
# # screen_width=80
# # text_width = len(sentence)
# # box_width = text_width + 6
# # left_margin = (screen_width - box_width) // 2
# # print
# # print ' ' * left_margin + '+' + '-' * (box_width - 4) + '+'
# # print ' ' * left_margin +'| '+' '*text_width + ' |'
# # print ' ' * left_margin +'| '+ sentence + ' |'
# # print ' ' * left_margin +'| '+' '*text_width + ' |'
# print ' ' * left_margin +'+' +'-'*(box_width - 4)+'+'
# print

# database=[['qwe','123'],['abc','123']]
# username=raw_input('login name:')
# pwd=raw_input('pwd:')
# if [username,pwd] in database:
#     print 'access successful'
# else:
#     print 'access false'
import string
print list("hello")
name = [1, 23, 4]
del name[1:2]
print list(reversed([1, 2, 3]))
print '%-*.*s' % (9, 2, '234.234')  # -表示左对齐，左*表示最小字符宽度，右*表示最大字符宽度（若为实数，则表示小数点后的位数）
print eval(repr('12312324234'))
print string.letters  # 包含所有字母（大小写）,string.lowercase小写字母字符串，string.uppercase大写字母字符串
print string.digits  # 包含0-9的字符串
print '所有可打印的字符：' + (string.printable)  # 所有可打印字符的字符串
print (string.punctuation)  # 包含所有标点的字符串
title = '我'
print len(title)
