import pandas as pd
import pandas_read_xml as pdx
from pandas_read_xml import flatten
# import tkinter as Tk
from tkinter import filedialog
from tkinter import *
import os


class MyWindow:
    def __init__(self, master, width, height, caption):
        highlight_color = '#e7dfd5'
        light_color = '#84a9ac'
        main_color = '#3b6978'
        dark_color = '#204051'
        master.wm_title(caption)
        master.config(background="#fff")

        header_frame = Frame(master, width=width, height=50, bg=main_color)
        btns_frame = Frame(header_frame, bg=header_frame['bg'],)
        btn_load_bom = Button(btns_frame, text="Select BOM", command=self.get_excel, bg=highlight_color, fg=dark_color)
        btn_load_wire = Button(btns_frame, text="Select Wirelist", command=self.get_excel, bg=highlight_color, fg=dark_color)
        btn_quit = Button(header_frame, text="Quit", command=master.quit, bg=highlight_color, fg=dark_color)

        main_frame = Frame(master, width=width, height=height, bg=highlight_color)
        self.status_monitor = Text(main_frame, takefocus=0, bg=main_frame['bg'])

        footer_frame = Frame(master, width=width, height=25, bg=dark_color)
        copyright_text = Label(footer_frame, text="ihor.chekh@eu.fujikura.com", bg=footer_frame['bg'], fg=light_color)

        header_frame.pack(side=TOP, fill=X)
        btns_frame.pack(side=LEFT, fill=X)
        btn_load_bom.pack(side=LEFT, padx=5, pady=5)
        btn_load_wire.pack(side=LEFT, padx=5, pady=5)

        main_frame.pack(fill=BOTH, expand=1)
        self.status_monitor.pack(fill=BOTH, expand=1)

        footer_frame.pack(side=BOTTOM, fill=X)
        copyright_text.pack()

        btn_quit.pack(side=RIGHT, padx=5, pady=5)

    def get_excel(self):
        global df

        # import_file_path = filedialog.askopenfilename()
        # df = pd.read_cvs(import_file_path)
        import_file_path = 'C:/Users/ihor.chekh/Documents/GitHub/data_science_learning/BOM&Wire analysis/ELZ_TAB016161D_KSK_L0L_160620.xml'
        root_key_list = ['HarnessContainer', 'Harness']
        df = pdx.read_xml(import_file_path, root_key_list)
        connectors = df['Connectors']['Connector']
        new_df = pd.DataFrame(connectors)
        # new_df['AssemblyPartID'] = connectors['ConnectorAssemblyPartRefs']['@AssemblyPartID']

        # for dict_of_items in connectors:
        #     for k, v in dict_of_items.items():
        #         new_df = new_df.append(new_df, {k: v}, ignore_index=True)

        print(new_df)
        new_df.to_excel(f'{import_file_path}_connectors.xlsx')
        # df.to_excel(f'{import_file_path}_new.xlsx')
        # df.loc[(df['@PMD'] == 'SPLICE')].to_excel(f'{import_file_path}_splices.xlsx')

        # print(df)
        # self.status_monitor.insert(0.0, 'Done!')
        # self.status_monitor.insert(0.0, df.columns)

    def print_message(self):
        print("Wow! It's working!")


root = Tk()
window = MyWindow(root, 600, 400, "BOM&Wire Checks")
window.get_excel()
root.mainloop()

df = pd.read_csv
