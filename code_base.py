import winsound
import plyer
from plyer import notification
import tkinter as tk
from tkinter import messagebox
import sqlite3
import time
import keyboard
import datetime
import math
import os
import sys

os.system ("cls")

conn = sqlite3.connect ("repositories.db")
c = conn.cursor ()

c.execute ('''CREATE TABLE IF NOT EXISTS repositories
             (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')

conn.commit ()

def main_menu () :

    global code_base

    code_base = tk.Tk ()
    code_base.attributes ("-fullscreen", True)
    code_base.configure (bg = "black")
    code_base.title ("Code Base Application")

    def one () :

        xavier.destroy ()
        
        global y

        y = tk.Label (code_base, text = "        Warm Welcome, to Code Base !!", font = ("Consolas bold", 31), fg = "light pink", bg = "black")
        y.place (relx = 0.01, rely = 0.01)

    def two () :

        global y

        y.destroy ()

        global z
        
        z = tk.Label (code_base, text = "    Warm Welcome, to Code Base !!", font = ("Consolas bold", 31), fg = "light pink", bg = "black")
        z.place (relx = 0.01, rely = 0.01)

    def three () :

        global z

        z.destroy ()

        global a

        a = tk.Label (code_base, text = "Warm Welcome, to Code Base !!", font = ("Consolas bold", 31), fg = "light pink", bg = "black")
        a.place (relx = 0.01, rely = 0.01)        

    global xavier

    xavier = tk.Label (code_base, text = "                    Warm Welcome, to Code Base !!", font = ("Consolas bold", 31), fg = "light pink", bg = "black")
    xavier.place (relx = 0.01, rely = 0.01)
    code_base.after (750, one)
    code_base.after (1500, two)
    code_base.after (2248, three)

    def four () :

        global shot
        shot = ""
    
        x = open ("C:\\Users\\Admin\\code_base_username.txt", "w")
    
        with open ("C:\\Users\\Admin\\code_base_username.txt", "r") as file :
        
            global user_name
            user_name = str (file.read ()).title ()
        
            if len (user_name) != 0 :
        
                user = tk.Label (code_base, text = f"Hello, {user_name} !!", fg = "white", bg = "black", font = ("Consolas bold", 24))
                user.place (relx = 0.01, rely = 0.23)
                shot += user_name
        
            else :
        
                user = tk.Label (code_base, text = f"Hello, Administrator !!", fg = "white", bg = "black", font = ("Consolas bold", 24))
                user.place (relx = 0.01, rely = 0.23)
                shot += "Administrator"
        
        if shot == "Administrator" :
    
            global new_user_name

            k = tk.Label (code_base, text = "Please enter your nice user name ( you can change this later in the settings) : ", fg = "light blue", bg = "black", font = ("Calibri bold", 16))
            k.place (relx = 0.01, rely = 0.33)
    
            kul = tk.Entry (code_base, fg = "white", insertbackground = "white", bg = "black", font = ("Consolas bold", 14))
            kul.place (relx = 0.593, rely = 0.33512)
            kul.focus_set ()

            def lol () :
            
                new_user_name = str (kul.get ())
                
                with open ("C:\\Users\\Admin\\code_base_username.txt", "w") as cile :
            
                    cile.write (f"{new_user_name}")
            
                messagebox.showinfo ("REQUEST", "PLEASE RELOAD THIS APP. JUST TO CONFIGURE YOUR USER NAME. THEN, ALL WILL GO SMOOTHLY !")

            jos = tk.Button (code_base, text = "Submit", fg = "black", font = ("Calibri bold", 15), bg = "white", command = lol)
	        
            jos.place (relx = 0.78, rely = 0.33512)

        else :
        
            2 == 2

        currentTime = datetime.datetime.now ()
        print ("")
        
        if currentTime.hour < 12 :
            
            a.destroy ()
            
        elif 12 <= currentTime.hour < 18 :
            
            a.destroy ()
        
        else :
            
            a.destroy ()
        
        '''
        tk.Label (code_base, text="Repository Name:").pack()
        name_entry = tk.Entry(code_base)
        name_entry.pack()
    
        tk.Label(code_base, text="Description:").pack()
        description_entry = tk.Text(code_base, height=4)
        description_entry.pack()
    
        #create_button = tk.Button(code_base, text="Create Repository", command=create_repository)
        #create_button.pack()
    
        tk.Label(code_base, text="Repositories:").pack()
    
        global repositories_listbox
        
        repositories_listbox = tk.Listbox(code_base)
        repositories_listbox.pack()
    
        # load_repositories()
    
        code_base.mainloop()
    
        conn.close()
    
    def create_repository():
        name = name_entry.get()
        description = description_entry.get("1.0", tk.END)
    
        c.execute("INSERT INTO repositories (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
    
        messagebox.showinfo("Success", f"Repository '{name}' created successfully!")
        
        #load_repositories()
    
    def load_repositories():
    
        global repositories_listbox, code_base
        
        repositories_listbox.delete(0, tk.END)
    
        c.execute("SELECT name FROM repositories")
        repositories = c.fetchall()
    
        for repo in repositories:
            repositories_listbox.insert(tk.END, repo[0])
    
        #code_base.after(3218, load_repositories)
    '''
    
    code_base.after (3075, four)
    code_base.mainloop ()

main_menu()
