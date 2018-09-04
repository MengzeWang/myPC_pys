import csv,operator
import numpy as np
def loadTrainData():
    l=[]
    with open('train.csv') as trDt:
        for trDti in csv.reader(trDt):
            l.append(trDti)#42001*785
    #print(l[0])
    print(len(l))
    l.remove(l[0])
    l=np.array(l)
    print('type(l)',type(l))
    print('l.shape',l.shape)
    label=l[:,0]
    data=l[:,1:]
    print('type(label)',type(label))
    return normalizing(toInt(data)),toInt(label)
def toInt(array):
    array=np.mat(array)
    m,n=np.shape(array)    newArray=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            newArray[i,j]=int(array[i,j])
    return newArray
def normalizing(array):
    m,n=array.shape
    for i in range(m):
        for j in range(n):
            if array[i,j]!=0:
                array[i,j]=1
    return array

def loadTestData():
    l=[]
    with open('test.csv') as file:
        lines=csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    data=np.array(l)
    return normalizing(toInt(data))
    
def loadTestResult():
    l=[]
    with open('knn_benchmark.csv') as file:
        lines=csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    label=np.array(l)
    return toInt(label[:,1])
    
    
def classify(inX,dataSet,labels,k):
    inX=np.mat(inX)
    dataSet=np.mat(dataSet)
    labels=np.mat(labels)
    dataSetSize=dataSet.shape[0]
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=np.array(diffMat)**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    #print('sortedDistIndicies',sortedDistIndicies)
    classCount={}
    for i in range(k):
        voteIlabel=labels[0,sortedDistIndicies[i]]
        #print('type(voteIlabel):',type(voteIlabel))
        #print('voteIlabel:',voteIlabel)
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)#py3.5:iteritems->items
    return sortedClassCount[0][0]
    
def saveResult(result):
    with open('result.csv','wt') as myFile:
        myWriter=csv.writer(myFile)
        for i in result:
            tmp=[]
            tmp.append(i)
            myWriter.writerow(tmp)
def handwritingClassTest(usedTestData_percent=25):
    trainData,trainLabel=loadTrainData()
    testData=loadTestData()
    #testLabel=loadTestResult()
    m,n=np.shape(testData)
    #errorCount=0
    resultList=[]
    for i in range(int(m*usedTestData_percent/100)):
        classifierResult=classify(testData[i],trainData[0:20000],trainLabel[0:20000],5)
        resultList.append(classifierResult)
        #print("the classifier came back with:%d,the real answeris :%d" %(classifierResult,testLabel[0,i]))
        print("the number %d(total:%d) classifier came back with:%d" %(i,int(m*usedTestData_percent/100),classifierResult))
        #if (classifierResult!=testLabel[0,i]):errorCount += 1.0
    #print("\nthe total number of errors is:%d" % errorCount)
    #print("\nthe total error rate is:%f" %(errorCount/float(m)))
    saveResult(resultList)
    
if __name__=='__main__':
    handwritingClassTest(100)