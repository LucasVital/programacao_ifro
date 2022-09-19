import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyApp(App):

    def build(self):
        
        Gridlayout = GridLayout(rows=2, cols=1)
        Gridlayout.add_widget(Label(text='Hello world'))
        Gridlayout.add_widget(Button(text='ok'))

        return Gridlayout



if __name__ == '__main__':
    MyApp().run()
    