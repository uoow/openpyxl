# # 读写图片。复制一份
# with open('toki.jpg','rb') as rf:
#     with open('toki_copy.jpg','wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)


# 用shelve模块把变量保存到文件
# import shelve

# shelfFile = shelve.open('myCat')
#
# cats = ['Garfield','Tom','Kitty']
# shelfFile['cats'] = cats
# shelfFile.close()

# 从文件里读取变量
# sh = shelve.open('myCat')
# print(sh['cats'])
# print(sh.keys())
# print(list(sh.keys()))
# print(sh.values())
# print(list(sh.values()))


# 把变量写入到py文件保存
# import pprint
#
# cats = [{'name':'Garfield','desc':'chubby'},
#         {'name':'Tom','desc':'naughty'},
#         {'name':'Kitty','desc':'pretty'}]
# s = pprint.pformat(cats)
# print(type(s))
# with open('myCats.py','w') as fileObj:
#     fileObj.write('cats = ' + s + '\n')


import myCats

print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])