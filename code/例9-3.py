with open('sample.txt') as fp:      # 假设文件采用CP936编码
    for line in fp:                 # 文件对象可以直接迭代
        print(line)
