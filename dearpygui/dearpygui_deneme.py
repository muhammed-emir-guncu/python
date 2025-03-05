"""birşeyler birşeyler"""
import dearpygui.dearpygui as dpg


class Kishiler:
    """ekleme"""
    def __init__(self):
        self.liste = dict()
        self.sayi = 0
    def ekle(self):
        """ekleme"""
        isim = dpg.get_value("isim")
        soyisim = dpg.get_value("soyisim")
        self.liste[isim] = soyisim
        dpg.set_value("cikti_ekle", f"{isim} {soyisim} eklendi.")
        print(f"{isim} {soyisim} eklendi.")

    def ileri(self):
        """ekleme"""
        if len(self.liste) != 0:
            self.sayi+=1
            self.sayi=self.sayi % len(self.liste)
            ismler=list(self.liste.keys())
            sismler=list(self.liste.values())
            dpg.set_value("cikti_gor",ismler[self.sayi] +" "+sismler[self.sayi])

    def geri(self):
        """ekleme"""
        if len(self.liste) != 0:
            self.sayi-=1
            self.sayi=self.sayi % len(self.liste) if len(self.liste) != 0 else 1
            ismler=list(self.liste.keys())
            sismler=list(self.liste.values())
            dpg.set_value("cikti_gor",ismler[self.sayi] +" "+sismler[self.sayi])

kisiler=Kishiler()

dpg.create_context()

with dpg.window(label="ekle", width=600, height=400,pos=(0,0), on_close=dpg.stop_dearpygui):
    dpg.add_input_text(label= "Ad", tag= "isim", pos=(10, 20), width=300, height=20)
    dpg.add_input_text(label= "Soyad", tag= "soyisim", pos=(10, 50), width=300, height=20)
    dpg.add_button(label="ekle", callback=kisiler.ekle, pos=(10, 80), width=30, height=20)
    dpg.add_text("-", tag="cikti_ekle", pos=(10, 100))

with dpg.window(label="gor", width=600,height=400,pos=(600,0),on_close=dpg.stop_dearpygui):
    dpg.add_text("-",tag="cikti_gor", pos=(20,20))
    dpg.add_button(label="geri", tag="geri", callback=kisiler.geri,
                    pos=(20, 50), width=30, height=20)
    dpg.add_button(label="ileri", tag="iler", callback=kisiler.ileri,
                    pos=(60, 50), width=30, height=20)


dpg.create_viewport(title="kisi veritabanı", width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
