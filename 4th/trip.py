import calendar
from   tkinter import *
from   tkinter import messagebox as msg
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
#import seaborn as sns
matplotlib.style.use('ggplot')
from pandastable import Table
class create_csv:

    def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.message_label = Label(self.f,text='Display the BAR GRAPH Trips per hour of the day. ',font=('Arial', 14))
          self.message_label1= Label(self.f,text='Display the BAR GRAPH  Trips per day of a week.',font=('Arial', 14))
          self.message_label2= Label(self.f,text='Display the BAR GRAPH  Trips per day of the month.',font=('Arial', 14))
          self.message_label3= Label(self.f,text='Display the BAR GRAPH  Trips in a month.',font=('Arial', 14))
          
          
          # Buttons
          self.confirm_button = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.bar_graph)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)
          self.confirm_button1 = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.bar_graph1)
          self.exit_button1 = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)
          self.confirm_button2 = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.bar_graph2)
          self.exit_button2 = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)
          self.confirm_button3 = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.bar_graph3)
          self.exit_button3 = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)
          self.message_label1.grid(row=3, column=0)
          self.confirm_button1.grid(row=4,column=0)
          self.exit_button1.grid(row=4,column=2)
          self.message_label2.grid(row=5, column=0)
          self.confirm_button2.grid(row=6,column=0)
          self.exit_button2.grid(row=6,column=2)
          self.message_label3.grid(row=7, column=0)
          self.confirm_button3.grid(row=8,column=0)
          self.exit_button3.grid(row=8,column=2)
    def bar_graph(self):
         df=pd.read_csv('uber.csv')
         df.head()
         df.tail()
         df=df[:-1]
         df.isnull().sum()
         df=df.dropna()
         df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], format="%m/%d/%Y %H:%M")
         df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], format="%m/%d/%Y %H:%M")
         hour=[]
         day=[]
         dayofweek=[]
         month=[]
         weekday=[]
         for x in df['START_DATE*']:
             hour.append(x.hour)
             day.append(x.day)
             dayofweek.append(x.dayofweek)
             month.append(x.month)
             weekday.append(calendar.day_name[dayofweek[-1]])
         df['HOUR']=hour
         df['DAY']=day
         df['DAY_OF_WEEK']=dayofweek
         df['MONTH']=month
         df['WEEKDAY']=weekday
         time=[]
         df['TRAVELLING_TIME']=df['END_DATE*']-df['START_DATE*']
         for i in df['TRAVELLING_TIME']:
             time.append(i.seconds//60)
         df['TRAVELLING_TIME']=time
         #df=pd.read_csv('uber.csv')
         my_colors = 'rgbkymc'
         df['HOUR'].value_counts().plot(kind='bar',figsize=(10,5),color='green')
         plt.title('Trips per hour of the day')
         plt.xlabel('HOUR------>',color='m')
         plt.ylabel('COUNTS---->',color='c')
         plt.tight_layout()
         plt.legend(loc='best')
         plt.show()
    def bar_graph1(self):
         df=pd.read_csv('uber.csv')
         df.head()
         df.tail()
         df=df[:-1]
         df.isnull().sum()
         df=df.dropna()
         df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], format="%m/%d/%Y %H:%M")
         df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], format="%m/%d/%Y %H:%M")
         hour=[]
         day=[]
         dayofweek=[]
         month=[]
         weekday=[]
         for x in df['START_DATE*']:
             hour.append(x.hour)
             day.append(x.day)
             dayofweek.append(x.dayofweek)
             month.append(x.month)
             weekday.append(calendar.day_name[dayofweek[-1]])
         df['HOUR']=hour
         df['DAY']=day
         df['DAY_OF_WEEK']=dayofweek
         df['MONTH']=month
         df['WEEKDAY']=weekday
         time=[]
         df['TRAVELLING_TIME']=df['END_DATE*']-df['START_DATE*']
         for i in df['TRAVELLING_TIME']:
             time.append(i.seconds//60)
         df['TRAVELLING_TIME']=time
         #df=pd.read_csv('uber.csv')
         my_colors = 'rgbkymc'
         df['WEEKDAY'].value_counts().plot(kind='bar',color='green')
         plt.title('Trips per day of a week.')
         plt.xlabel('WEEKDAY------>',color='m')
         plt.ylabel('COUNTS---->',color='c')
         plt.tight_layout()
         plt.legend(loc='best')
         plt.show()
    def bar_graph2(self):
         df=pd.read_csv('uber.csv')
         df.head()
         df.tail()
         df=df[:-1]
         df.isnull().sum()
         df=df.dropna()
         df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], format="%m/%d/%Y %H:%M")
         df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], format="%m/%d/%Y %H:%M")
         hour=[]
         day=[]
         dayofweek=[]
         month=[]
         weekday=[]
         for x in df['START_DATE*']:
             hour.append(x.hour)
             day.append(x.day)
             dayofweek.append(x.dayofweek)
             month.append(x.month)
             weekday.append(calendar.day_name[dayofweek[-1]])
         df['HOUR']=hour
         df['DAY']=day
         df['DAY_OF_WEEK']=dayofweek
         df['MONTH']=month
         df['WEEKDAY']=weekday
         time=[]
         df['TRAVELLING_TIME']=df['END_DATE*']-df['START_DATE*']
         for i in df['TRAVELLING_TIME']:
             time.append(i.seconds//60)
         df['TRAVELLING_TIME']=time
         #df=pd.read_csv('uber.csv')
         my_colors = 'rgbkymc'
         df['DAY'].value_counts().plot(kind='bar',figsize=(15,5),color='green')
         plt.title('Trips per day of the month')
         plt.xlabel('DAY------>',color='m')
         plt.ylabel('COUNTS---->',color='c')
         plt.tight_layout()
         plt.legend(loc='best')
         plt.show()
    def bar_graph3(self):
         df=pd.read_csv('uber.csv')
         df.head()
         df.tail()
         df=df[:-1]
         df.isnull().sum()
         df=df.dropna()
         df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], format="%m/%d/%Y %H:%M")
         df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], format="%m/%d/%Y %H:%M")
         hour=[]
         day=[]
         dayofweek=[]
         month=[]
         weekday=[]
         for x in df['START_DATE*']:
             hour.append(x.hour)
             day.append(x.day)
             dayofweek.append(x.dayofweek)
             month.append(x.month)
             weekday.append(calendar.day_name[dayofweek[-1]])
         df['HOUR']=hour
         df['DAY']=day
         df['DAY_OF_WEEK']=dayofweek
         df['MONTH']=month
         df['WEEKDAY']=weekday
         time=[]
         df['TRAVELLING_TIME']=df['END_DATE*']-df['START_DATE*']
         for i in df['TRAVELLING_TIME']:
             time.append(i.seconds//60)
         df['TRAVELLING_TIME']=time
         #df=pd.read_csv('uber.csv')
         my_colors = 'rgbkymc'
         df['MONTH'].value_counts().plot(kind='bar',figsize=(10,5),color='green')
         plt.title('Trips in a month')
         plt.xlabel('MONTH------>',color='m')
         plt.ylabel('COUNTS---->',color='c')
         plt.tight_layout()
         plt.legend(loc='best')
         plt.show()


    
root=Tk()
root.title('Bar Graph')
root.geometry('1000x600')
conv_csv = create_csv(root)
root.mainloop()
