# 此程序是为了将SQL脚本里的回车、TAB转换为`n、`t，以用于在RunAny一键输出脚本

# 读取SQL脚本文件
f = open('1.sql',encoding='utf-8')
# 把文件里的文本内容赋给字符串
str = f.read()
f.close()
# 把TAB键转换为`t
str = str.replace('\t','`t')
# 把回车键转换为`n
str = str.replace('\n','`n')
# 新建一个脚本文件用于保存转换过的内容
f = open('new.sql','w',encoding='utf-8')
# 保存文件
f.write(str)
f.close()