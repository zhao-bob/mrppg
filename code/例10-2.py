import os
import sys
import shutil
import filecmp

def autoBackup(scrDir, dstDir):
    if ((not os.path.isdir(scrDir)) or
        (not os.path.isdir(dstDir)) or
        (os.path.abspath(scrDir)!=scrDir) or
        (os.path.abspath(dstDir)!=dstDir)):
        usage()
    for item in os.listdir(scrDir):
        scrItem = os.path.join(scrDir, item)
        dstItem = scrItem.replace(scrDir, dstDir)
        if os.path.isdir(scrItem):
            # 创建新增的文件夹，保证目标文件夹的结构与原始文件夹一致
            if not os.path.exists(dstItem):
                os.makedirs(dstItem)
                print('make directory:'+dstItem)
            # 递归调用自身函数
            autoBackup(scrItem, dstItem)
        elif os.path.isfile(scrItem):
            # 只复制新增或修改过的文件
            if not (os.path.exists(dstItem) and
                    filecmp.cmp(scrItem, dstItem, shallow=False)):
                shutil.copyfile(scrItem, dstItem)
                print('file:'+scrItem+'==>'+dstItem)

def usage():
    print('scrDir和dstDir必须是已存在的文件夹绝对路径')
    print('用法:\n{0} c:\\olddir c:\\newdir'.format(sys.argv[0]))
    sys.exit(0)
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    scrDir, dstDir= sys.argv[1], sys.argv[2]
    autoBackup(scrDir, dstDir)
