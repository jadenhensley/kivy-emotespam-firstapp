from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        # change window size
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # automatically scales, similar to CSS' flexbox/grid!



        # add widgets to window

        # image widget
        self.window.add_widget(Image(source='pogchamp.png',))

        #Label widget
        self.greeting = Label(text="Enter your twitch gamertag: ",
                              font_size = 18,
                              color="#00ffce") # Note: we can change the properties within each element as you would css.
        self.window.add_widget(self.greeting) # i.e.: add second widget into the grid layout
        
        # text input widget
        self.user = TextInput(multiline=False,
                              padding_y = (20,20),
                              size_hint = (1, 0.5)) # each "widget"/element can have its own properties
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(text="GREET",
                             size_hint = (1, 0.5),
                             bold = True,
                             background_color = '#00FFCE')
        self.button.bind(on_press=self.callback) # need to specify the function to call which is binded to our widget.
        self.emotebutton = Button(text="SPAM POGGERS",
                             size_hint = (1, 0.5),
                             bold = True,
                             background_color = '#00FFCE')        
        self.window.add_widget(self.button)
        self.emotebutton.bind(on_press=self.spam_emote)
        self.window.add_widget(self.emotebutton)

        return self.window # since we are modifying the window to have a function,
        # we now need to return the window both before and after, as it has to 
        # render again and return a different "object" value.

    def callback(self, instance):
        self.greeting.text = "Welcome @" + self.user.text + " to the twitch chat!"
        return self.window # make sure to return the window!!

    def spam_emote(self, instance):
        self.window.add_widget(Image(source='pogchamp.png',))
        return self.window

if __name__ == "__main__":
    SayHello().run()
    # in theory, minimum requirements: App class, with a method, that runs as soon as program ran.