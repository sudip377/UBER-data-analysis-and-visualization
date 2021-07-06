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
class create_df:

     def __init__(self, root):
          self.f = Frame(root, height=1000, width=500)
          self.f.pack()    
           
          
          self.message_label = Label(self.f,text='Getting an hour, day, days of the week, a month from the date of the trip',font=('Arial', 14))
          
          
          self.confirm_button = Button(self.f,text='Convert', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.add_col1)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)
     

     def add_col1(self):
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
         #df.head()
         self.f = Frame(root, height=200, width=300)
         self.f.pack(fill=BOTH,expand=1)
         self.table = Table(self.f, dataframe=df,read_only=True)
         self.table.show()

      

root=Tk()
root.title('Getting an hour, day, days of the week, a month from the date of the trip')
root.geometry('800x600')
conv_csv = create_df(root)
root.mainloop()

