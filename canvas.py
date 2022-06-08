from turtle import width
from kivy.properties import Clock, StringProperty
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Ellipse
from kivy.uix.widget import Widget
import time, random
from kivy.core.window import Window



class testCanApp(App):
    pass



class CanEx(Widget):
    pass

class CanEx2(Widget):
    pass

class CanEx3(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # with self.canvas:
            # self.rect = Rectangle(pos=(400,200),size=(150,150))

    # def btn_click(self):
    #     x, y = self.rect.pos
    #     y+=10 
    #     self.rect.pos=(x,y)


class CanEx5(Widget):
    otbitt = StringProperty('0')
    count = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (.3,.3,.3,1)
        self.ball_size = 50
        self.vx =3
        self.vy = 3
        
        with self.canvas:
            
            self.ball =   Ellipse(pos=(100,100),width=None,size=(self.ball_size,self.ball_size),source='res1.jpg')
        Clock.schedule_interval(self.update,1/60)


    def on_size(self,*args):
        print(str(self.width) + '\t' + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2,self.center_y -self.ball_size/2 )
    
    def update(self,dt):
        x,y = self.ball.pos
        x+=self.vx
        y+=self.vy
        self.ball.pos = (x,y)
        if y +self.ball_size> self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
            self.count+=1
            self.otbitt = str(self.count)
            
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
            self.count+=1
            self.otbitt = str(self.count)
            

        if x < 0:
            x = self.width - self.ball_size
            self.vx = -self.vx
            self.count+=1
            self.otbitt = str(self.count)
            

        if y < 0:
            y = self.height - self.ball_size
            self.vy = -self.vy
            self.count+=1
            self.otbitt = str(self.count)
            




if __name__ == '__main__':
    testCanApp().run()  
