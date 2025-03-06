import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="ekle", width=600, height=400,pos=(0,0), on_close=dpg.stop_dearpygui):
    dpg.add_text("-", tag="cikti_ekle",indent=10)
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_same_line()
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_same_line()
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_same_line()
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_same_line()
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_same_line()
    dpg.add_button(label="0",   width=60, height=20)
    dpg.add_same_line()
    dpg.add_button(label="0",   width=60, height=20)
    
         

dpg.create_viewport(title="kisi veritabanı", width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
