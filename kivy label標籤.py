from kivy.app import App
from kivy.uix.button import Button#引入按鈕控鍵,布局和控鍵都在此模塊中
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout #引入盒子布局
from kivy.uix.floatlayout import FloatLayout #為一個容器負責包容控鍵(按鈕或標籤之類的)(浮動佈局)
# 如果你使用 Kivy Language（KV），你可能需要導入 Builder 類
from kivy.lang import Builder

class Box(FloatLayout):
    def __init__(self):
        super().__init__()
        self.label = Label(
            text="pan[ref=label]baoni[/ref]",
            text_size=(500,500), 
            markup=True,
            strikethrough=True
        )

        self.add_widget(self.label)
# 定義應用程式類
class MyApp(App):
    def build(self):
        return Box()

# 啟動應用程式
if __name__ == '__main__':
    MyApp().run()