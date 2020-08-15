# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:08:06 2020

@author: Hassan Mustafa
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import pandas as pd
Builder.load_string('''
<DataTable>:
    id: Customer_window
    orientation: 'vertical'
    spacing:3
    canvas.before:
        Color:
            rgba: (0.15,0.3,0.7,0.2)
        Rectangle:
            size: self.size
            pos: self.pos
    BoxLayout:
        id: search_result
        size_hint_y:0.9
        RecycleView:
            viewclass: 'CustLabel'
            id: table_floor
            RecycleGridLayout:
                id: table_floor_layout
                cols: 5
                default_size: (None,250)
                default_size_hint: (1,None)
                size_hint_y: None
                height: self.minimum_height
                spacing: 5
    BoxLayout:
        id:search_eng
        size_hint_y:0.1
        height: 20
    
<CustLabel@Label>:
    bcolor: (0.5,0.5,0.5,0.5)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
''')
class DataTable(BoxLayout):
    def __init__(self,table='', **kwargs):
        super().__init__(**kwargs)
        products = table
        col_titles = [k for k in products.keys()]
        rows_len = len(products)
        self.columns = len(col_titles)
        table_data = []
        for t in col_titles:
            table_data.append({'text':str(t),'size_hint_y':None,'height':50,'bcolor':(.06,.45,.45,1)})
        for r in range(rows_len):
            for t in col_titles:
                table_data.append({'text':str(products[t][r]),'size_hint_y':None,'height':30,'bcolor':(.06,.25,.25,1)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data
# class DataTableApp(App):
#     def build(self):
#         return DataTable()

# if __name__=='__main__':
#     DataTableApp().run()