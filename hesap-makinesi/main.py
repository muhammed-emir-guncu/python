"""aman"""
import dearpygui.dearpygui as dpg
class Hesap:
    def __init__(self):
        self.sonuc=""
    def topla(self):
        self.sonuc+="+"
    def cikar(self):
        self.sonuc+="-"
    def bol(self):
        self.sonuc+="/"
    def carp(self):
        self.sonuc+="*"
    def e_0(self):
        self.sonuc+="0"
    def e_1(self):
        self.sonuc+="1"
    def e_2(self):
        self.sonuc+="2"
    def e_3(self):
        self.sonuc+="3"
    def e_4(self):
        self.sonuc+="4"
    def e_5(self):
        self.sonuc+="5"
    def e_6(self):
        self.sonuc+="6"
    def e_7(self):
        self.sonuc+="7"
    def e_8(self):
        self.sonuc+="8"
    def e_9(self):
        self.sonuc+="9"
    def nokta(self):
        self.sonuc+="."
    def goster(self):
        dpg.set_value("ekran",self.sonuc)
        print(self.sonuc)
hesab=Hesap()

dpg.create_context()

with dpg.window(label="hesap makinesi", width=600, height=400,pos=(0,0), on_close=dpg.stop_dearpygui):
    dpg.add_text("-", tag="ekran")
    dpg.add_button(label="1",callback=hesab.e_1, pos=(10, 50), width=60, height=20)
    dpg.add_button(label="2",callback=hesab.e_2, pos=(80, 50), width=60, height=20)
    dpg.add_button(label="3",callback=hesab.e_3, pos=(150,50), width=60, height=20)
    dpg.add_button(label="+",callback=hesab.topla, pos=(220,50), width=60,height=20)
    dpg.add_button(label="*",callback=hesab.carp, pos=(290,50), width=60,height=20)
    dpg.add_button(label="4",callback=hesab.e_4, pos=(10, 80), width=60, height=20)
    dpg.add_button(label="5",callback=hesab.e_5, pos=(80, 80), width=60, height=20)
    dpg.add_button(label="6",callback=hesab.e_6, pos=(150, 80), width=60, height=20)
    dpg.add_button(label="-",callback=hesab.cikar, pos=(220,80), width=60,height=20)
    dpg.add_button(label="/",callback=hesab.bol, pos=(290,80), width=60,height=20)
    dpg.add_button(label="7",callback=hesab.e_7, pos=(10, 110), width=60, height=20)
    dpg.add_button(label="8",callback=hesab.e_8, pos=(80, 110), width=60, height=20)
    dpg.add_button(label="9",callback=hesab.e_9, pos=(150, 110), width=60, height=20)
    dpg.add_button(label="=", pos=(220,110), width=60,height=50)
    dpg.add_button(label="AC", pos=(290,110), width=60,height=50)
    dpg.add_button(label="0",callback=hesab.e_0, pos=(10,140), width=130,height=20)
    dpg.add_button(label=".",callback=hesab.nokta, pos=(150,140), width=60,height=20)

dpg.set_frame_callback(1, hesab.goster)
dpg.create_viewport(title="hesap", width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
