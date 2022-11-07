
# Copy of MOVE

import os
from datetime import datetime
from pathlib import Path
import shutil
import time
import tkinter as tk
from tkinter import OptionMenu, StringVar, filedialog, ttk
from turtle import onclick

folder_file = ":/"
dest_path = ":/"

move = False
prc = 0
lbl = 'Ready to Start!'


class Organizer(object):
    def __init__(self):
        pass

    root = tk.Tk()

    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        length=280,
    )

    def organize(self):
        global move
        global folder_file
        global dest_path
        global prc

        mes = {'01': 'Enero',
               '02': 'Febrero',
               '03': 'Marzo',
               '04': 'Abril',
               '05': 'Mayo',
               '06': 'Junio',
               '07': 'Julio',
               '08': 'Agosto',
               '09': 'Septiembre',
               '10': 'Octubre',
               '11': 'Noviembre',
               '12': 'Diciembre'}
        total_files = len(os.listdir(folder_file))
        i = 0
        
        

        # Create Folder to all photos
        Path(dest_path).mkdir(parents=True, exist_ok=True)

        for file in os.listdir(folder_file):


            # time.sleep(1)
            # % Completed
            i += 1
            prc = int((i/total_files)*100) 
            # print(prc)

            # Get file name
            name_file = str(os.path.basename(file))
            # print(name_file)

            file_path = str(folder_file + "/" + name_file)

            # Update Progress Bar
            self.pb['value'] = prc

            self.root.update_idletasks()

            try:

                if "20" in name_file:

                    d = name_file.split("20", 1)[1]
                    # print("separada " + d)

                    d = "20" + d[:6]
                    # print("final " + d)

                    y_path = d[:4]

                    m = mes[d[4:6]]
                    m_path = dest_path + "/" +  y_path + "/" + m

                    #  Create folder for year and month
                    Path(m_path).mkdir(parents=True, exist_ok=True)

                    # Copy or Move file to folder
                    if move:

                        shutil.move(file_path, m_path)
                    else :
                        shutil.copy(file_path, m_path)

                else :

                    c_time= datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')
                    m_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')

                    if c_time < m_time:

                        # print("c_time")

                        y_path = str(c_time)[:4]
                        m = mes[str(c_time)[5:7]]
                        m_path = dest_path + "/" + y_path + "/" + m

                    else:
                        # print("m_time")

                        y_path = str(m_time)[:4]
                        m = mes[str(m_time)[5:7]]
                        m_path = dest_path + "/" + y_path + "/" + m

                    #  Create folder for year and month
                    Path(m_path).mkdir(parents=True, exist_ok=True)

                    # Copy or Move file to folder
                    if move:

                        shutil.move(file_path, m_path)
                    else :
                        shutil.copy(file_path, m_path)
            except:

                try:
                    c_time = datetime.fromtimestamp(
                        os.path.getctime(file_path)).strftime('%Y-%m-%d')
                    m_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')

                    if c_time < m_time:
                        # print("c_time")
                        y_path = str(c_time)[:4]
                        m = mes[str(c_time)[5:7]]
                        m_path = dest_path + "/" + y_path + "/" + m

                    else:
                        # print("m_time")
                        y_path = str(m_time)[:4]
                        m = mes[str(m_time)[5:7]]
                        m_path = dest_path + "/" + y_path + "/" + m

                    #  Create folder for year and month
                    Path(m_path).mkdir(parents=True, exist_ok=True)

                    # Copy or Move file to folder
                    if move:
                        shutil.move(file_path, m_path)
                    else :
                        shutil.copy(file_path, m_path)

                except:
                    e_path = dest_path + "/" + "Error"

                    #  Create folder for year and month
                    Path(e_path).mkdir(parents=True, exist_ok=True)

                    # Copy or Move file to folder
                    if move:
                        shutil.move(file_path, e_path)
                    else:
                        shutil.copy(file_path, e_path)

        

    def gui(self):
        global folder_file
        global dest_path

        my_font = ('times', 8, 'bold')
        my_font1 = ('times', 10, 'bold')


        self.root.geometry("500x500")
        self.root.title("Photo Organizer")

        f_org_txt = tk.Label(self.root, text = "Select a folder to Organize (without subfolders inside)", font= my_font1)
        f_org_txt.grid(row=0, column=1, padx=20, pady=10)

        def openOriginFolder():
            global folder_file

            f_org = filedialog.askdirectory()
            org_label.config(text=f_org)
            folder_file = f_org

        # Select Origin Folder path
        button_org = tk.Button(self.root, text="Select Origin Folder:", font= my_font, command=lambda:openOriginFolder(), bg='lightgray')
        button_org.grid(row=1, column=0, padx=10, pady=20)

        org_label = tk.Label(self.root, text=folder_file,
                             font=my_font, bg='lightblue')
        org_label.grid(row=1, column=1, padx=2,  sticky='w')

        f_dest_txt = tk.Label(
            self.root, text="Select a Destination Folder", font=my_font1)
        f_dest_txt.grid(row=3, column=1, padx=20, pady=10)

        def openDestFolder():
            global dest_path
            f_dest = filedialog.askdirectory()
            dest_label.config(text=f_dest)
            dest_path = str(f_dest)


        # Select Origin Folder path
        button_org = tk.Button(self.root, text="Select Destin Folder:",
                            font=my_font, command=lambda: openDestFolder(), bg='lightgray')
        button_org.grid(row=4, column=0, padx=10, pady=20)

        dest_label = tk.Label(self.root, text=dest_path, font=my_font, bg='lightgreen')
        dest_label.grid(row=4, column=1, padx=2,  sticky='w')


       
        # Progess Bar
   

        self.pb.grid(row=9, column=0, columnspan=2, padx=10, pady=20)


        def selected():
            global move
            global prc

            if select.get() == 'Move':
                move = True
            else :
                move = False 

            # Run Organize  
            # process()      
            self.organize()
            
         # Dropdown Copy/Move
        select = StringVar()
        select.set('Copy')

        drop = OptionMenu(self.root, select, *["Copy", "Move"])
        drop.grid(row=6, column=0)

        # Button to start organize
        button_organize = tk.Button(self.root, text="ORGANIZE", font=my_font, command= selected, bg='lightgreen')
        button_organize.grid(row=6, column=1, sticky='w', padx=10, pady=20)

        # Exception Label
        # ex_label = tk.Label(self.root, text=e,
        #                     font=('times', 8, 'bold'), bg='lightgray', fg='red')
        # ex_label.grid(row=12, column=1, padx=2,  sticky='w')

        self.root.mainloop()


try: 

    def main():
        model = Organizer()
        model.gui()

    if __name__ == "__main__":
        main()
except Exception as e:
    print(e)
