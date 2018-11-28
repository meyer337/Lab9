def data(file):
    inf = open(file,'r')
    info = inf.readlines()
    lst = []
    for i in info:
        i = i.replace('\n','')
        i = i.split(', ')
        i[3]=float(i[3])
        lst.append(i)
    return lst

def process(dataList):
    tech = 9.5
    ship = 8.75
    admin = 9.25
    sales = 9

    jobrate = {"TECH": 9.5, "SHIP": 8.75, "ADMIN": 9.25, "SALES": 9}
    monthNum = {"Jan": 0, "Feb": 1, "Mar": 2}
    
    payDict = {}
    month = []
    name = []
    job = []
    hours = []
    
    for i in range(len(dataList)):
        date = dataList[i][0].split("-")
        month.append(date[1])
        dataList[i][1]=dataList[i][1].strip(" ")
        name.append(dataList[i][1])
        dataList[i][2]=dataList[i][2].strip(" ")
        job.append(dataList[i][2])
        hours.append(dataList[i][3])

    #print(job)
    #print(jobrate)
    nameSet = set(name)
    for i in nameSet:
        payDict[i]=[0,0,0]
    for i in range(len(dataList)):
        
        payDict[name[i]][monthNum[month[i]]] += (jobrate[job[i]]*hours[i])

    for key, value in payDict.items():
        value[0] = round(value[0],2)
        value[1] = round(value[1],2)
        value[2] = round(value[2],2)
    

    return payDict

def lookup(dictionary, name):
    try:
        total = dictionary[name][0]+dictionary[name][1]+dictionary[name][2]
        flist = [dictionary[name][0],dictionary[name][1],dictionary[name][2],total]
        return flist
    except:
        return False


def main():
    payDict = process(data("employeeHours.txt"))

    print(lookup(payDict, "AStevens"))

main()
