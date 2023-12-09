jitu, tui = map(int, input('请输入鸡兔总数和腿总数：').split())
tu = (tui - jitu * 2) / 2
if int(tu) == tu and 0 <= tu <= jitu:
    print('鸡：{0},兔：{1}'.format(int(jitu - tu), int(tu)))
else:
    print('数据不正确，无解')
