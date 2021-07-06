from   tkinter import *
from   tkinter import messagebox as msg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class create_csv:

     def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.message_label = Label(self.f,text='Display the BAR GRAPH  Category of use',font=('Arial', 14))
          
          
          # Buttons
          self.confirm_button = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.bar_graph)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)
     def bar_graph(self):
         '''
         pd.set_option('display.max_rows', 500)
         pd.set_option('display.max_columns', 500)
         pd.set_option('display.width', 1000)
         df=pd.read_csv('empsal.csv')
         df['conv']=df['salary']*0.1
         df['total']=df['salary']+df['hra']+df['conv']
         total_list = df.groupby(['state'])['salary','hra','conv','total'].sum()
         total_list.plot(kind='bar')
         plt.title('State Wise total Figures Of\n salary, hra, conv & total')
         plt.xlabel('States-->')
         plt.ylabel('total Figures')
         plt.tight_layout()
         plt.legend(loc='best')
         plt.show()'''
         df=pd.read_csv('uber.csv')
         my_colors = 'rgbkymc'
         df['CATEGORY*'].value_counts().plot(kind='bar',color=list('bkymc'))
         plt.title('Category of use')
         plt.xlabel('CATEGORY*------>',color='m')
         plt.ylabel('COUNTS---->',color='c')
         plt.tight_layout()
         plt.legend(loc='best')
         plt.show()

    
root=Tk()
root.title('Category of use')
root.geometry('1200x816')
conv_csv = create_csv(root)
bg = PhotoImage(file = "cat.png") 
  
# Create Canvas 
canvas1 = Canvas( root, width =1200, 
                 height = 816) 
  
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw")
#root.configure(bg='blue')
root.mainloop()
