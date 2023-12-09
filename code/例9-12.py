import pickle

i = 999999
a = 3.1415926
s = '第24届冬季奥林匹克运动会(2022年北京冬季奥运会)于2022年2月4日开幕，2月20日闭幕。'
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (-5, 10, 8)
coll = {4, 5, 6}
dic = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
data = (i, a, s, lst, tu, coll, dic)

with open('sample_pickle.dat', 'wb') as f:
    try:
        pickle.dump(len(data), f)        # 要序列化的对象个数
        for item in data:
            pickle.dump(item, f)         # 序列化数据并写入文件
    except:
        print('写文件异常')

with open('sample_pickle.dat', 'rb') as f:
    n = pickle.load(f)
    for i in range(n):
        x = pickle.load(f)
        print(x)
