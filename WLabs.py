# -*- coding: utf-8 -*-


'''
Download Anaconda Distribution for Python 2.7 version 
https://www.anaconda.com/download/#windows 

tkintertable 
pip install tkintertable  
'''

import Tkinter as tk 
import tkMessageBox
import ttk 
#from ttk import * 
from Tkinter import Menu 
from Tkinter import StringVar 
#to use tkintertable  
from tkintertable import TableCanvas, TableModel 

#Open Replenisher GUI
window = tk.Tk() 
window.title("Welcome to Replenisher Task List app") 
window.geometry('800x700')

#User Info
FirstNameLab = tk.Label(window, text="First Name").grid(row=0)
LastnameLab = tk.Label(window, text="Last Name").grid(row=1) 
FirstName = tk.Entry(window)  
LastName = tk.Entry(window)  
FirstName.grid(row=0, column=1)  
LastName.grid(row=1, column=1)  

#Login button
def LoginButton():
    tkMessageBox.showinfo('WLabs Replenisher', 'Successfully Login')
LoginBTN = tk.Button(window,text='Login', command = LoginButton)
LoginBTN.place(relx=0.5, rely=0.5, anchor=tk.CENTER)      

#Logout button 
def LogoutButton():
    global window
    window.destroy()      
LogoutBTN = tk.Button(window,text='Logout', command = LogoutButton)
LogoutBTN.place(relx=1.0, rely=0.0, anchor=tk.NE) 

#Menu Actions of Assignment 
def MenuAssignments():
    AssignmentsWindow = tk.Toplevel(window)
    AssignmentsWindow.title("Replenisher Assignments") 
    AssignmentsWindow.geometry('800x500')
    
    UserList = [
    "User Selection", 
    "User1",
    "User2",
    "User3" 
    ] 
    UserVariable = StringVar(AssignmentsWindow)
    UserVariable.set(UserList[0]) # default value 
    UserOptionMenu = tk.OptionMenu(AssignmentsWindow, UserVariable, *UserList)
    UserOptionMenu.pack()
    
    TaskList = [
    "Task Selection", 
    "Task1",
    "Task2",
    "Task3" 
    ] 
    TaskVariable = StringVar(AssignmentsWindow)
    TaskVariable.set(TaskList[0]) # default value 
    TaskOptionMenu = tk.OptionMenu(AssignmentsWindow, TaskVariable, *TaskList)
    TaskOptionMenu.pack()    
    
    def AddUserTask():
        tkMessageBox.showinfo('Add User and Task', "Added User: " + UserVariable.get() + ";  " + "Added Task: " + TaskVariable.get() )  
    
    AddUserTaskBT = tk.Button(AssignmentsWindow, text="Add User and Task", command=AddUserTask)
    AddUserTaskBT.pack()
    
    #Add a table 
    '''
    RowNum = 2
    ColNum = 2
    for i in range(RowNum): 
        for j in range(ColNum): 
            b = tk.Entry(AssignmentsWindow, text="")
            b.grid(row=i, column=j)
            b.pack()
    '''
    
    #To use tkintertable  
    tframe = tk.Frame(AssignmentsWindow)
    tframe.pack()  
    model = TableModel()
    table = TableCanvas(tframe, model=model)
    table.createTableFrame()
    
    model = table.model
    data = {'rec1': {'User': 'User1', 'Task': 'Task1', 'Status': 'Open', 'Rank': 1, 'Priority': 'High', 'Start Time': '05-19-2018 10:30', 'Finish Time': ''},  
            'rec2': {'User': 'User2', 'Task': 'Task2', 'Status': 'Open', 'Rank': 2, 'Priority': 'Low', 'Start Time': '05-19-2018 11:30', 'Finish Time': '05-19-2018 22:30'},
            'rec3': {'User': 'User3', 'Task': 'Task3', 'Status': 'Open', 'Rank': 3, 'Priority': 'Low', 'Start Time': '05-19-2018 12:30', 'Finish Time': '05-19-2018 22:45'}               
           }  
    model.importDict(data) #Import from a dictionary to populate model
    table.redrawTable()
    
    AssignmentsWindow.mainloop()

#Menu Actions of Task 
def MenuTask():
    TaskWindow = tk.Toplevel(window)
    TaskWindow.title("Add New Tasks") 
    TaskWindow.geometry('800x500')
    
    TaskList = [
    "Add Task"
    ] 
    TaskVariable = StringVar(TaskWindow)
    TaskVariable.set(TaskList[0]) # default value 
    TaskOptionMenu = tk.OptionMenu(TaskWindow, TaskVariable, *TaskList)
    TaskOptionMenu.pack()    
    
    def AddTask():
        tkMessageBox.showinfo('WLabs Replenisher', 'Successfully Add New Task')  
    
    AddTaskBT = tk.Button(TaskWindow, text="Add Task", command=AddTask)
    AddTaskBT.pack()
    
    #To use tkintertable  
    tframe = tk.Frame(TaskWindow)
    tframe.pack()  
    model = TableModel()
    table = TableCanvas(tframe, model=model)
    table.createTableFrame()
    
    model = table.model
    data = {'rec1': {'ID': 'Task1', 'Priority': 'High' },  
            'rec2': {'ID': 'Task2', 'Priority': 'Low'  },
            'rec3': {'ID': 'Task3', 'Priority': 'Low'  }               
           }  
    model.importDict(data) #Import from a dictionary to populate model
    table.redrawTable()
    
    #Add New Row button
    def AddRowButton():
        table.addRow() 
        table.redrawTable() 
    
    AddRowBTN = tk.Button(TaskWindow,text='Add New Row', command = AddRowButton)
    AddRowBTN.place(relx=0.9, rely=0.15, anchor=tk.CENTER)      
        
    TaskWindow.mainloop()

#Menu Actions of User 
def MenuUser():
    UserWindow = tk.Toplevel(window)
    UserWindow.title("Add New User") 
    UserWindow.geometry('800x500')
    
    UserList = [
    "Add User"
    ] 
    UserVariable = StringVar(UserWindow)
    UserVariable.set(UserList[0]) # default value 
    UserOptionMenu = tk.OptionMenu(UserWindow, UserVariable, *UserList)
    UserOptionMenu.pack()
        
    def AddUser():
        tkMessageBox.showinfo('WLabs Replenisher', 'Successfully Add New User')  
    
    AddUserBT = tk.Button(UserWindow, text="Add User", command=AddUser)
    AddUserBT.pack()
    
    #To use tkintertable  
    tframe = tk.Frame(UserWindow)
    tframe.pack()  
    model = TableModel()
    table = TableCanvas(tframe, model=model)
    table.createTableFrame()
    
    model = table.model
    data = {'rec1': {'ID': 'User1', 'First Name': 'Tom', 'Last Name': 'Cross' },  
            'rec2': {'ID': 'User2', 'First Name': 'Jim', 'Last Name': 'Wood' },
            'rec3': {'ID': 'User3', 'First Name': 'Bryan', 'Last Name': 'Bush' }               
           }  
    model.importDict(data) #Import from a dictionary to populate model
    table.redrawTable()

    #Add New Row button
    def AddRowButton():
        table.addRow() 
        table.redrawTable() 
    
    AddRowBTN = tk.Button(UserWindow,text='Add New Row', command = AddRowButton)
    AddRowBTN.place(relx=0.9, rely=0.15, anchor=tk.CENTER)     
    
    UserWindow.mainloop()

#End of Menu Actions 
    
#Help info
def MenuHelp():
    tkMessageBox.showinfo('WLabs Replenisher', 'WLabs, Great!') 

#Menu Items
menu = Menu(window)
ReplenisherItem = Menu(menu, tearoff=0)
ReplenisherItem.add_command(label='Assignments', command = MenuAssignments)
ReplenisherItem.add_separator()
ReplenisherItem.add_command(label='Tasks', command = MenuTask)
ReplenisherItem.add_separator()
ReplenisherItem.add_command(label='Users', command = MenuUser)
menu.add_cascade(label='Select Replenisher Tasks', menu=ReplenisherItem)

HelpMenu = Menu(menu, tearoff=0)
HelpMenu.add_command(label="About Walmart Labs", command = MenuHelp) 
menu.add_cascade(label="Help", menu=HelpMenu) 

window.config(menu=menu)

window.mainloop() 


