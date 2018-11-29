#lab9
#Jinyang Wang, Brett Meyer, Peter Xu
#This program will extract data from a file and calculate their income.


from graphics import *
def menu(payDict):
    win = GraphWin('',300,400)
    title = Text(Point(150,25),'Stiles Publishing')
    title.setSize(20)
    title.setStyle('bold')
    title.draw(win)
    subt = Text(Point(150,50),'Payroll Summary')
    subt.draw(win)
    name = Text(Point(75,75),'Employee Name:')
    name.draw(win)
    namentry = Entry(Point(225,75),10)
    namentry.draw(win)
    #draw the text
    look = Text(Point(85,125),'LOOKUP')
    jan = Text(Point(85,165),'Janunary')
    feb = Text(Point(85,205),'February')
    mar = Text(Point(85,245),'March')
    total = Text(Point(85,285),'Total')
    quitc = Text(Point(210,125),'QUIT')
    for i in [look,jan,feb,mar,total,quitc]:
        i.draw(win)
    #draw the rec
    lookr = Rectangle(Point(40,110),Point(130,140))
    janr = Rectangle(Point(40,150),Point(130,180))
    febr = Rectangle(Point(40,190),Point(130,220))
    marr = Rectangle(Point(40,230),Point(130,260))
    totalr = Rectangle(Point(40,270),Point(130,300))
    quitr = Rectangle(Point(160,110),Point(260,140))
    janv = Entry(Point(210,170),10)
    febv = Entry(Point(210,210),10)
    marv = Entry(Point(210,250),10)
    aLine = Line(Point(160,270),Point(260,270))
    totalv = Entry(Point(210,290),10)
    for i in [lookr,janr,febr,marr,totalr,quitr,janv,febv,marv,totalv,aLine]:
        i.draw(win)

    situation = 1
    while situation != 0:
        if situation == 2:
            Name = namentry.getText()
            if not(Name.isspace()) and Name != "":
                payList = lookup(payDict, Name)
                if payList != -1:
                    janv.setText(payList[0])
                    febv.setText(payList[1])
                    marv.setText(payList[2])
                    totalv.setText(payList[3])
                else:
                    janv.setText("")
                    febv.setText("")
                    marv.setText("")
                    totalv.setText("")
            else:
                janv.setText("")
                febv.setText("")
                marv.setText("")
                totalv.setText("")
                
            situation = 1
                
        click = win.checkMouse()
        if click != None:
            if 40<click.getX() <130 and 110<click.getY() <140:
                situation = 2
            elif 160<click.getX()<260 and 110<click.getY()<140:
                situation = 0
            else: pass
    win.close()

#read the data

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
#return the dictionary
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

#looking for a specific person's data
def lookup(dictionary, name):
    try:
        total = dictionary[name][0]+dictionary[name][1]+dictionary[name][2]
        flist = [dictionary[name][0],dictionary[name][1],dictionary[name][2],total]
        return flist
    except:
        return -1


def main():
    payDict = process(data("employeeHours.txt"))

    menu(payDict)

main()
