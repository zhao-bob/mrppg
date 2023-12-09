n = int(input('请输入一个大于1的自然数：'))
if n in (2,3):
    print('Yes')
# 偶数必然不是素数
elif n%2 == 0:
    print('No')
else:
    # 大于5的素数必然出现在6的倍数两侧
    # 因为6x+2、6x+3、6x+4肯定不是素数，假设x为大于1的自然数
    m = n % 6
    if m!=1 and m!=5:
        print('No')
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                print('No')
                break
        else:
            print('Yes')
