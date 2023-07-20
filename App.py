from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from src.api_request import remoteGet


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.title = "Download youtube"
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        #imagens
        self.window.add_widget(Image(source="./assets/img/Eu.PNG"))

        #AreaTexto
        self.greeting = Label(
                                text        = " ",
                                font_size   = 18,
                                color       = "#00FFCE"
                                )
        self.window.add_widget(self.greeting)

        #textImput
        self.user = TextInput(
                                multiline=False,
                                padding= (20, 20),
                                size_hint = (1, 0.5)
                                )
        self.window.add_widget(self.user)

        #button widget
        self.button = Button(
                                text="BAIXAR",
                                size_hint = (1, 0.5),
                                bold = True,
                                background_color = "#00FFCE"
                                )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        valor_retornado = remoteGet.get(self.user.text)
        # self.greeting.text = "Hello " +  self.user.text + "!"
        self.greeting.text = valor_retornado
        # self.greeting.text =  valor_retornado + "!"

if __name__ == "__main__":
    SayHello().run()




    