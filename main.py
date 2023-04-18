from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

GUI = Builder.load_file('tela.kv')

class MeuApp (App):
  def build(self):
    return GUI