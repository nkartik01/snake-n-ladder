from tkinter import *
from random import*
from PIL import *
import time
def initiate():
    im=PhotoImage(file='lenna.gif')
    board=Label(root,image=im)
    board.image=im
    global canvas1
    canvas1=Canvas(root,height=1000,width=1000)
    canvas1.pack(expand=YES,fill=BOTH)
    canvas1.place(x=0,y=0)
    #canvas2=Canvas(root,height=600,width=720)
    #canvas2.place(x=0,y=0)
    canvas1.create_image(0,0,image=im,anchor=NW)
    im2=PhotoImage(file='removed_minion2.png')
    bl=Label(image=im2)
    bl.image=im2
    canvas1.create_image(60,570,image=im2,anchor=NW)
    global control
    control=0
    im3=PhotoImage(file='removed_redbeeti.png')
    rd=Label(image=im3)
    rd.image=im3
    canvas1.create_image(90,570,image=im3,anchor=NW)
    global win
    win=0
    global m
    m=0
    global p1
    p1=1
    global p2
    p2=1
    global dic
    dic={'5':8,'3':22,'21':9,'17':4,'19':7,'11':26,'20':29,'27':1}
    global label
    label=Label(root,text=0)
    global b
    b=Button(root,text='Roll Dice',command=turn)
    b.place(x=750,y=100)
    
def turn():
    global dic,p1,p2,m,win,canvas1,label,b
    b.destroy()
    
    r=randrange(1,7,1)
    if(r==6):
        r=r+randrange(1,7,1)
        if(r==12):
            r=r+randrange(1,7,1)
            if(r==18):
                r=0
    label.destroy()
    label=Label(root,text=r,font='times 25')
    label.place(x=750,y=50)
    if m%2==0:
        if(p1+r>30):
            for i in range(100):
                canvas1.move(2,5,0)
                root.update()
                time.sleep(0.01)
                canvas1.move(2,-5,0)
                root.update()
                time.sleep(0.01)

        if(p1+r<31):
            for i in range(r):
                if(p1%6!=0 and ((p1//6)%6)%2==0):
                    for i in range(12):
                        canvas1.move(2,5,-5)
                        root.update()
                        time.sleep(0.04)
                    for i in range(12):
                        canvas1.move(2,5,5)
                        root.update()
                        time.sleep(0.04)
                elif(p1%6!=0 and ((p1//6)%6)%2!=0):
                    for i in range(12):
                        canvas1.move(2,-5,-5)
                        root.update()
                        time.sleep(0.04)
                    for i in range(12):
                        canvas1.move(2,-5,5)
                        root.update()
                        time.sleep(0.04)
                else:
                    for i in range(24):
                        canvas1.move(2,0,-5)
                        root.update()
                        time.sleep(0.04)
                p1+=1
            if str(p1) in dic.keys():
                temp=p1
                if (p1//6)%2==0:
                    x1=(p1%6)*120
                    y1=(5-(p1//6))*120
                else:
                    x1=(7-(p1%6))*120
                    y1=(5-(p1//6))*120
                p1=dic[str(p1)]

                if (p1//6)%2==0:
                    x2=(p1%6)*120
                    y2=(5-(p1//6))*120
                else:
                    x2=(7-(p1%6))*120
                    y2=(5-(p1//6))*120

                for i in range(100):
                    canvas1.move(2,(x2-x1)/100,(y2-y1)/100)
                    root.update()
                    time.sleep(0.01)
        if(p1==30):
            win=1
        if(p1==p2 and p1!=1):
            if (p2//6)%2==0:
                x1=(p2%6)*120
                y1=(5-(p2//6))*120
            else:
                x1=(7-(p2%6))*120
                y1=(5-(p2//6))*120
            p2=1
            if (p2//6)%2==0:
                x2=(p2%6)*120
                y2=(5-(p2//6))*120
            else:
                x2=(7-(p2%6))*120
                y2=(5-(p2//6))*120
            print(x1,y2,x2,y2)
            for i in range(100):
                canvas1.move(3,(x2-x1)/100,(y2-y1)/100)
                root.update()
                time.sleep(0.01)

    else:
        if(p2+r>30):
            for i in range(100):
                canvas1.move(3,5,0)
                root.update()
                time.sleep(0.01)
                canvas1.move(3,-5,0)
                root.update()
                time.sleep(0.01)
        if(p2+r<31):
            for i in range(r):
                if(p2%6!=0 and ((p2//6)%6)%2==0):
                    for i in range(12):
                        canvas1.move(3,5,-5)
                        root.update()
                        time.sleep(0.04)
                    for i in range(12):
                        canvas1.move(3,5,5)
                        root.update()
                        time.sleep(0.04)
                elif(p2%6!=0 and ((p2//6)%6)%2!=0):
                    for i in range(12):
                        canvas1.move(3,-5,-5)
                        root.update()
                        time.sleep(0.04)
                    for i in range(12):
                        canvas1.move(3,-5,5)
                        root.update()
                        time.sleep(0.04)
                else:
                    for i in range(24):
                        canvas1.move(3,0,-5)
                        root.update()
                        time.sleep(0.04)
                p2+=1
        if str(p2) in dic.keys():
            temp=p2
            if (p2//6)%2==0:
                x1=(p2%6)*120
                y1=(5-(p2//6))*120
            else:
                x1=(7-(p2%6))*120
                y1=(5-(p2//6))*120
            p2=dic[str(p2)]                
            if (p2//6)%2==0:
                x2=(p2%6)*120
                y2=(5-(p2//6))*120
            else:
                x2=(7-(p2%6))*120
                y2=(5-(p2//6))*120
            for i in range(100):
                canvas1.move(3,(x2-x1)/100,(y2-y1)/100)
                root.update()
                time.sleep(0.01)
        if(p2==30):
            win=1
        if(p1==p2 and p1!=1):
            if (p1//6)%2==0:
                x1=(p1%6)*120
                y1=(5-(p1//6))*120
            else:
                x1=(7-(p1%6))*120
                y1=(5-(p1//6))*120
            p1=1
            if (p1//6)%2==0:
                x2=(p1%6)*120
                y2=(5-(p1//6))*120
            else:
                x2=(7-(p1%6))*120
                y2=(5-(p1//6))*120
            print(x1,y1,x2,y2)
            for i in range(100):
                canvas1.move(2,(x2-x1)/100,(y2-y1)/100)
                root.update()
                time.sleep(0.01)
    m+=1
    b=Button(root,text='Roll Dice',command=turn)
    b.place(x=750,y=100)
    turn()
def controler():
    control=1
root=Tk()
canvas=Canvas(root,height=600,width=720)
canvas.pack(expand=YES,fill=BOTH)
initiate()
