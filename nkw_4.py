import sys
while True:
    try:
        test_data=sys.stdin.readline().strip('\n')
        if not test_data:
            continue
        if len(test_data)<8:
            print(test_data+'0'*(8-len(test_data)))
        else:
            int_bei=int(len(test_data)/8)
            canyu_ge=len(test_data)-8*int_bei
            for i in range(int_bei):
                  print(test_data[(i*8):((i+1)*8)])
            if canyu_ge>0:
                print(test_data[-canyu_ge:]+'0'*(8-canyu_ge))
    except Exception as e:
        print(e)
        break