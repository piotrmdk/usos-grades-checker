import kivy

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from base.tabler import tablemaker


class Controller(FloatLayout):

    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        value = tablemaker()
        self.result.text = value



class ControllerApp(App):

    def build(self):
        return Controller(info='Pobierz oceny')

if __name__ == '__main__':
    ControllerApp().run()
