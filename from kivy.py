from kivy.app import App
from kivy.uix.button import Button#引入按鈕控鍵,布局和控鍵都在此模塊中
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout #引入盒子布局
from kivy.uix.floatlayout import FloatLayout #為一個容器負責包容控鍵(按鈕或標籤之類的)(浮動佈局)
# 如果你使用 Kivy Language（KV），你可能需要導入 Builder 類
from kivy.lang import Builder

class Box(FloatLayout):
    def __init__(self):#初始化方法（constructor）。當你創建一個新的類的實例（對象）時，這個初始化方法會被自動調用，用於執行一些初始化的工作。在這個方法中，self 代表創建的對象本身。
        super().__init__() #調用父類(App)的初始化方法，確保所有必要的設置被執行
        self.botton = Button(   #可動態添加類別的屬性(self.botton)
            text="你好",
            font_name="C:\\Users\\bigi9\\OneDrive\\桌面\\kivy檔\\msyh.ttc",#添加一個按鈕
            #size_hint=[0.2,0.2] #兩數分別代表螢幕介面的x,y長寬的比例，此為相對尺寸 *注意:使用相對尺寸時要引入函式庫(from kivy.uix.floatlayout import FloatLayout)
            #若想要設定固定尺寸的話，必須先將相對尺寸的參數設為None
            #size_hint_x=None,
            #size_hint_y=None,
            size_hint=[None,None],
            size=[50,50],
            #pos=[200,200] #設置固定位置
            pos_hint={'x':0.2,'y':0.5},
            #相對位置數值界於[0,1],且0可用空格省略,相對位置用來表示的變數有,"x"(表示按鈕的左邊界),"center_x"(表示按鈕的中線),"right"(表示按鈕的右邊界),"y"(表示按鈕下界),"top"(表示按鈕上界),註:需用字典包起來
            background_color=(1,1,1,1),#採rgba格式,默認為灰色 其中rgb的範圍為0~255
            font_size="30px", #字體大小默認為15sp
            color=(100,1,1,1),#字體顏色 一樣採rgba格式
            #background_down=r"C:\Users\bigi9\OneDrive\Pictures\相機相簿"
        )

        self.botton.bind(on_press=self.botton_clicked)

        self.add_widget(self.botton)#將按鈕新增到Box布局
    def botton_clicked(self,botton):
        print("已點擊按鈕")

# 定義應用程式類
class MyApp(App):
    def build(self):
        return Box()
"""
def func1(a: list[int]):
    '''this fuction is use to.....'''
    print('Hi')
"""
"""
aaa: int = 8
aaa = 9
aaa = 7
aaa

abccc = 8
abccc = 8
abccc = 8
"""
'''A this var is use to.....'''
b = 3
'''B this var is use to.....'''

# 啟動應用程式
if __name__ == '__main__':
    MyApp().run()