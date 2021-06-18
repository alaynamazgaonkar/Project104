from collections import Counter
import csv

with open(r"data104.csv", newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)

data=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    data.append(float(num))

def getMean():
    sum=0
    for i in data:
        sum=sum+i
    length=len(data)
    mean=sum/length
    print("The mean is :- ")
    print(mean)

def getMedian():
    data.sort()
    length=len(data)
    if length%2==0:
        median1=float(data[length//2-1])
        median2=float(data[length//2])
        average=median1+median2
        median=average/2
    else:
        median=data[length//2]
    print("The median is :- ")
    print(median)

def getMode():
    data1=Counter(data)
    newdata=data1.items()
    moderange={"60-65": 0, "65-70": 0, "70-75": 0, "75-80": 0,}
    for height,occurance in newdata:
        if 60<float(height)<65:
            moderange["60-65"]+=occurance
        elif 65<float(height)<70:
            moderange["65-70"]+=occurance
        elif 70<float(height)<75:
            moderange["70-75"]+=occurance
        elif 75<float(height)<80:
            moderange["75-80"]+=occurance

    mode_range, mode_occurence = 0, 0
    for range, occurence in moderange.items():
        if occurence > mode_occurence: 
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode=float((mode_range[0]+mode_range[1])/2)  

    print("The mode is :- ")
    print(mode)

print("Enter 1 to get the mean, 2 to get the median or 3 to get the mode :-")
func=int(input(""))
print(" ")

if func==1:
    getMean()
elif func==2:
    getMedian()
elif func==3:
    getMode()
