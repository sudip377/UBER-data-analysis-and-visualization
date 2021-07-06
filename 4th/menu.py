# menuprog.py 
# Menu program 

from tkinter import *
from PIL import ImageTk,Image
import os
#from create_dff import *
#import create_dff as p
class Testmenu:

    # Constructor
    def __init__(self, root):

        
       
        # Create menubar
        self.menubar=Menu(root)
        root.config(menu=self.menubar)            # attach the menubar to root
        # Now create Single menubar operation menu
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Data Conversion', menu=self.mysql_menu)
        # Now create menu items under menubar 
        self.mysql_menu.add_command(label='Build DF', command=self.create_df)
        self.mysql_menu.add_command(label='Build CSV', command=self.create_csv)
        self.mysql_menu.add_command(label='Add Column', command=self.addnew_column)

        self.mysql_menu.add_command(label='Convert to Excel', command=self.mysql_to_xls)
         
        # Now add a separator
        self.mysql_menu.add_separator()
        # Now create a Exit menu
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        # Now create Data Maintenance operation menu
        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Data Visualization Reports', menu=self.data_menu)
        self.data_menu.add_command(label='Category _of _use', command=self.rep1)
        self.data_menu.add_command(label='Purposes of Use', command=self.rep2)
        self.data_menu.add_command(label='Bar_Graph_Diff_category', command=self.rep3)
        #self.data_menu.add_command(label='SCATTER_PLOT', command=self.plot)
        
        '''# Prediction Menu
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict', command=self.predict)'''
         

    def create_df(self):
        #os.system("python ")
        import create_dff
        #os.system('python create_df.py')
        #create_df.conv_to_df()
    def create_csv(self):
        import create_csv
        #os.system("python.exe create_csv.py")
    def addnew_column(self):
        import add_col
        #os.system("python.exe add_col.py")
    def mysql_to_xls(self):
        import create_excl
        #os.system("python.exe create_excl.py")
    
    def rep1(self):
        import Category
        #os.system("python.exe  Category.py ")
    def rep2(self):
        import purposes
        #os.system("python.exe  purposes.py")
    def rep3(self):
        import trip
        #os.system("python.exe trip.py")               
     
#=====================================================================================================
  
root=Tk()
root.title('UBER DATA ANALYSIS')

obj=Testmenu(root)
root.geometry('1199x795')
# Add image file 
bg = PhotoImage(file = "img.png") 
  
# Create Canvas 
canvas1 = Canvas( root, width =1199, 
                 height = 795) 
  
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw")
main_lbl=Label(root, text='Uber Data Analysis', fg='black', font=('Arial', -30, 'bold'))
main_lbl.place(x=200, y=250)
root.mainloop()

                                 
        
        
        
        
                 
