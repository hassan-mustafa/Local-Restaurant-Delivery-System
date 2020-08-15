# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:26:22 2020

@author: Hassan Mustafa
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from OrdersList import DataTable
from sqlalchemy import create_engine
import pandas as pd
from kivy.lang import Builder
Builder.load_string('''
<AdminWindow>:
    id: main_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (0.15,0.3,0.7,0.2)
        Rectangle:
            size: self.size
            pos: self.pos
    BoxLayout:
        id: top_nav
        size_hint_y: None
        height: 40
        canvas.before:
            Color:
                rgba: (.06, .45, .45,1)
            Rectangle:
                size: self.size
                pos: self.pos
        Button:
            id: file_trigger
            text: 'File'
            on_release: file_dropdown.open(self)
            size_hint: (.2,None)
            height: 40
            Widget:
                on_parent: file_dropdown.dismiss()
                DropDown:
                    id: file_dropdown
                    Button:
                        id: close
                        text: 'quit'
                        size_hint_y: None
                        height: 30
        Label:
            text: 'Sahla'
            font_size: 20
            bold: True
            size_hint: (.8,None)
            height: 40
    BoxLayout:
        id:nav_content
        BoxLayout:
            id:side_tabs
            size_hint_x: .2
            orientation: 'vertical'
            spacing:3
            canvas.before:
                Color:
                    rgba: (.06, .52, .52,1)
                Rectangle:
                    size: self.size
                    pos: self.pos
            ToggleButton:
                id: newOrder_toggle
                text: 'Add New Order'
                size_hint_y: .1
                background_color: (0.15,0.3,0.7,0.2)
                background_normal: ''
                state: 'down'
                on_state: self
            ToggleButton:
                id: SearchCustomer_toggle
                text: 'Search Customer'
                size_hint_y: .1
                background_color: (0.15,0.3,0.7,0.2)
                background_normal: ''
            ToggleButton:
                id: SearchOrder_toggle
                text: 'Search Order'
                size_hint_y: .1
                background_color: (0.15,0.3,0.7,0.2)
                background_normal: ""
            ToggleButton:
                id: Glovers_toggle
                text: 'Glovers'
                size_hint_y: .1
                background_color: (0.15,0.3,0.7,0.2)
                background_normal: ""
            Label:
                id: sp
                text: ''
                size_hint_y: .6
        BoxLayout:
            id:all
            size_hint_x: .8
            padding: (20,10)
            ScreenManager:
                id: scrn_mngr
                Screen:
                    id: scrn_content
                    name: 'scrn_content'
                Screen:
                    id: scrn_product_content
                    name: 'scrn_product_content'
                Screen:
                    id: scrn_analysis
                    name: 'scrn_analysis'
            
            
# <CustomPopup>:
#     title: 'a7a'
#     size_hint: .5, .5
#     auto_dismiss: False
#     GridLayout:
#         cols: 3
#         Label:
#             id: info
#             size_hint: .9, .9
#             halign: 'center'
#             valign: 'middle'
#             text: 'Insert terms of service text here'
#             text_size: self.width, None
#         TextInput:
#             size_hint: 0.6, 0.2
#             id: pwd_field
#             hint_text: "Password"
#             multiline: False
#             password: True
#             pos_hint: {"x":0.2, "top":1}
#             on_text_validate: root.validate_user()
#         Button: 
#             text: 'validate'
#             size_hint: 0.5, 0.3
#             pos_hint: {"x":0, "y":0.1} 
#             on_release: root.validate_user()

''')
# class CustomPopup(Popup):
#     def validate_user(self):
#         pwd = self.ids.pwd_field
#         info = self.ids.info
#         passw = pwd.text
#         if passw == '':
#              info.text = 'password required'
#         else:
#             self.dismiss()
             
class AdminWindow(BoxLayout):
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        x = self.ids.scrn_content
        orders = self.get_orders()
        orderstable = DataTable(table=orders)
        x.add_widget(orderstable)
    def get_orders(self):
         engine = create_engine('mysql://root:hassan@localhost/orders')
         orders_df=pd.read_sql_table('orderstable',engine)
         return orders_df
        
    def second(self):
        second= {
          'TH0':{0:'St0',1:'Sample1',2:'Sample2',3:'Sample4'},
          'TH1':{0:'Stm0',1:'Sample1',2:'Sample2',3:'Sample4'},
          'TH2':{0:'Stmp0',1:'Sampled1.0',2:'Sampled2.0',3:'Sampled4.0'},
          'TH3':{0:'Stmpl0',1:'Sample1',2:'Sample2',3:'Sample4'},
          'TH4':{0:'Stmple0',1:'Sample1',2:'Sample2',3:'Sample4'},
          'TH5':{0:'St0',1:'Sample1',2:'Sample2',3:'Sample4'},
          'TH6':{0:'Stm0',1:'Sample1',2:'Sample2',3:'Sample4'},
          'TH7':{0:'Stmp0',1:'Sampled1.0',2:'Sampled2.0',3:'Sampled4.0'},
          'TH8':{0:'Stmpl0',1:'Sample1',2:'Sample2',3:'Sample4'},
          'TH9':{0:'Stmple0',1:'Sample1',2:'Sample2',3:'Sample4'}}
        return second
        
        
    # def btn(self): 
    #   the_popup = CustomPopup()
    #   the_popup.open()
class AdminApp(App):
    def build(self):
       return AdminWindow()
    
if __name__=='__main__':
    AdminApp().run()