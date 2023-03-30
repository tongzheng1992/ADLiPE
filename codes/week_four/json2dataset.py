import os
files=os.listdir('./')
files.remove('json2dataset.py')   # 删除这个py文件本身
for i in range(len(files)):
    os.system('labelme_json_to_dataset '+files[i])
input("json转png完成，请输入任意按键退出")