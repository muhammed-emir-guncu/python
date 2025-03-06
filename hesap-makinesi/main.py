"""aman"""
import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="ekle", width=600, height=400,pos=(0,0), on_close=dpg.stop_dearpygui):
    dpg.add_text("-", tag="cikti_ekle")
    dpg.add_button(label="1", pos=(10, 50), width=60, height=20)
    dpg.add_button(label="2", pos=(80, 50), width=60, height=20)
    dpg.add_button(label="3", pos=(150,50), width=60, height=20)
    dpg.add_button(label="+", pos=(220,50), width=60,height=20)
    dpg.add_button(label="*", pos=(290,50), width=60,height=20)
    dpg.add_button(label="4", pos=(10, 80), width=60, height=20)
    dpg.add_button(label="5", pos=(80, 80), width=60, height=20)
    dpg.add_button(label="6", pos=(150, 80), width=60, height=20)
    dpg.add_button(label="-", pos=(220,80), width=60,height=20)
    dpg.add_button(label="/", pos=(290,80), width=60,height=20)
    dpg.add_button(label="7", pos=(10, 110), width=60, height=20)
    dpg.add_button(label="8", pos=(80, 110), width=60, height=20)
    dpg.add_button(label="9", pos=(150, 110), width=60, height=20)
    dpg.add_button(label="=", pos=(220,110), width=60,height=50)
    dpg.add_button(label="AC", pos=(290,110), width=60,height=50)
    dpg.add_button(label="0", pos=(10,140), width=130,height=20)
    dpg.add_button(label=".", pos=(150,140), width=60,height=20)
    

dpg.create_viewport(title="kisi veritabanı", width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
