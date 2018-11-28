from graphics import *

def menu():
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
    janv = Rectangle(Point(160,150),Point(260,180))
    febv = Rectangle(Point(160,190),Point(260,220))
    marv = Rectangle(Point(160,230),Point(260,260))
    totalv = Rectangle(Point(160,270),Point(260,300))
    for i in [lookr,janr,febr,marr,totalr,quitr,janv,febv,marv,totalv]:
        i.draw(win)
    
menu()
