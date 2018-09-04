import csv
with open('test.csv','rt',encoding='utf-8') as myTCsv:
    lines=csv.reader(myTCsv)
    print('type(lines):',type(lines))
    for line in lines:
        pass
with open('c1.csv','wt',encoding='utf-8') as myCsv1:
    myWriter=csv.writer(myCsv1)
    myWriter.writerow([7,'g'])
    myWriter.writerow([8,'h'])
    mylist=[[1,2,3],[5,6,7]]
    myWriter.writerows(mylist)