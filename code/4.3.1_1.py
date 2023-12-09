a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
# for i, v in enumerate(a_list, start=1):
#     print('列表的第', i, '个元素是：', v)
# for i in range(len(a_list)):
#     print('列表的第', i + 1, '个元素是：', a_list[i])
i = 0
for v in a_list:
    i += 1
    print('列表的第', i, '个元素是：', v)
