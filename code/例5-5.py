from collections import defaultdict

def yanghui(n):
    # 所有元素默认值0
    triangle = defaultdict(int)
    for row in range(n):
        # 每行第一个元素为1
        triangle[row,0] = 1
        print(triangle[row,0], end='\t')       # 下标实际为元组(row, 0)
        # 生成该行后续元素
        for col in range(1, row+1):
            # 如果指定位置的元素不存在，默认为0
            triangle[row,col] = triangle[row-1,col-1] + triangle[row-1,col]
            print(triangle[row,col], end='\t')
        print()

yanghui(14)
