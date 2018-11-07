#-*- coding：utf-8 -*-
import csv
def anyRoundStastic(latest_round=-1):#-1 mean all round
    with open('daletou.csv') as daletou_history_file:
        readCsv_res=csv.reader(daletou_history_file)
        red_ball_times=list(0 for x in range(35))
        blue_ball_times=list(0 for x in range(12))
        test_round=latest_round
        for readCsv_resi in readCsv_res:
            if test_round==0:
                break
            #print(readCsv_resi)
            for readCsv_resi_red in readCsv_resi[1:6]:
                red_ball_times[int(readCsv_resi_red)-1]+=1
            for readCsv_resi_blue in readCsv_resi[6:]:
                blue_ball_times[int(readCsv_resi_blue)-1]+=1
            test_round-=1
    return [red_ball_times,blue_ball_times]
red_ball_times='249 233 243 203 243 244 249 215 232 238 238 223 239 242 212 184 228 239 249 234 227 280 255 241 252 220 239 231 338 305 287 315 322 283 318'
blue_ball_times='273 284 289 284 308 274 291 276 296 329 298 298'
def returnSortedByTimes(color_ball_times):
    ball_num=1
    i2_list=[]
    if type(color_ball_times) ==str:
        color_ball_times=color_ball_times.split(' ')
    for ball_times in color_ball_times:
        i2_list.append([int(ball_times),int(ball_num)])
        ball_num+=1
    return sorted(i2_list,reverse=True)

'''red_ball_sort=returnSortedByTimes(red_ball_times)
blue_ball_sort=returnSortedByTimes(blue_ball_times)
for red_ball_sorti in red_ball_sort:
    print(red_ball_sorti)
print('----------------')
for blue_ball_sorti in blue_ball_sort:
    print(blue_ball_sorti)'''
wanted_round=-1
while int(wanted_round)!=0:
    wanted_round=input(u'请输入想要查看的最近x期统计结果(直接回车表示看全部,0:退出):')
    if not wanted_round:
        wanted_round=-1
    elif int(wanted_round)==0:
        continue
    all=anyRoundStastic(-1)
    recent=anyRoundStastic(int(wanted_round))
    red_ball_sort_all=returnSortedByTimes(all[0])
    blue_ball_sort_all=returnSortedByTimes(all[1])
    red_ball_sort=returnSortedByTimes(recent[0])
    blue_ball_sort=returnSortedByTimes(recent[1])
    print(u'============最近%d次统计结果============' %(int(wanted_round)))
    print('----------------')
    print(u'[次数，红球号]')
    for red_ball_sorti in red_ball_sort:
        print(red_ball_sorti)
    print('----------------')
    print(u'[次数，蓝球号]')
    for blue_ball_sorti in blue_ball_sort:
        print(blue_ball_sorti)
    print('============总历史出现次数最少&最近%s期出现次数最少============' % wanted_round)
    for magic_len in range(5,36):
        magic_len_all_red=set([x[1] for x in red_ball_sort_all[-magic_len:]])
        magic_len_recent_red=set([y[1] for y in red_ball_sort[-magic_len:]])
        if len(magic_len_all_red&magic_len_recent_red)>=5:
            print(u'小李算法:',sorted(magic_len_all_red&magic_len_recent_red))
            break
    for magic_len in range(1,13):
        magic_len_all_blue=set([x[1] for x in blue_ball_sort_all[-magic_len:]])
        magic_len_recent_blue=set([y[1] for y in blue_ball_sort[-magic_len:]])
        if len(magic_len_all_blue&magic_len_recent_blue)>=2:
            print(u'小李算法:',sorted(magic_len_all_blue&magic_len_recent_blue))
            break
    print('============总历史出现次数最多&最近%s期出现次数最少============' % wanted_round)
    for magic_len in range(5,36):
        magic_len_all_red=set([x[1] for x in red_ball_sort_all[:magic_len]])
        magic_len_recent_red=set([y[1] for y in red_ball_sort[-magic_len:]])
        if len(magic_len_all_red&magic_len_recent_red)>=5:
            print(u'小王算法:',sorted(magic_len_all_red&magic_len_recent_red))
            break
    for magic_len in range(1,13):
        magic_len_all_blue=set([x[1] for x in blue_ball_sort_all[:magic_len]])
        magic_len_recent_blue=set([y[1] for y in blue_ball_sort[-magic_len:]])
        if len(magic_len_all_blue&magic_len_recent_blue)>=2:
            print(u'小王算法:',sorted(magic_len_all_blue&magic_len_recent_blue))
            break
    print('============总历史出现次数最多&最近%s期出现次数最多============' % wanted_round)
    for magic_len in range(5,36):
        magic_len_all_red=set([x[1] for x in red_ball_sort_all[:magic_len]])
        magic_len_recent_red=set([y[1] for y in red_ball_sort[:magic_len]])
        if len(magic_len_all_red&magic_len_recent_red)>=5:
            print(u'小王算法2:',sorted(magic_len_all_red&magic_len_recent_red))
            break
    for magic_len in range(1,13):
        magic_len_all_blue=set([x[1] for x in blue_ball_sort_all[:magic_len]])
        magic_len_recent_blue=set([y[1] for y in blue_ball_sort[:magic_len]])
        if len(magic_len_all_blue&magic_len_recent_blue)>=2:
            print(u'小王算法2:',sorted(magic_len_all_blue&magic_len_recent_blue))
            break
