from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text=self.load_epos())
        layout.add_widget(label)
        return layout
    
    def load_epos(self):
        with open('assets/myepos.txt', 'r') as file:
            epos = file.read()
        return epos

if __name__ == '__main__':
    MyApp().run()
