import requests
import json
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import *
from kivy.core.image import Image
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty



class TextInputX(TextInput):
    pass


class ScrollViewX(ScrollView):
    pass


class BoxLayoutX(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayoutX, self).__init__(**kwargs)

        Window.size = (self.width*3, self.height*6)

        self.img = Image("Background.jpg")
        with self.canvas:
            Rectangle(source='Background.jpg', pos=self.pos, size=(self.width*8, self.height*8))
        self.inside = BoxLayout(orientation='horizontal', spacing=0, size_hint=(1, None), height="40dp")
        self.inside.cols = 2

        self.inside.txt = TextInput(multiline=False, height="40dp", pos_hint={"y": 0}, size_hint=(1, None), font_size=20, hint_text="Enter location")
        self.inside.txt.bind(on_text_validate=self.on_enter)
        self.inside.add_widget(self.inside.txt)

        self.inside.button = Button(text="Go!", height="40dp", pos_hint={"y": 0}, size_hint=(0.5, None), font_size=20, background_color=(155/255, 195/255, 225/255, 1))
        self.inside.button.bind(on_press=self.clicked_go)
        self.inside.add_widget(self.inside.button)

        self.add_widget(self.inside)

        self.val = 0


    desc = StringProperty()
    time = StringProperty()
    temp = StringProperty()
    feels_like = StringProperty()
    wind = StringProperty()
    pressure = StringProperty()
    humidity = StringProperty()
    visibility = StringProperty()

    def get_weather(self):
        city = self.loc
        key = "3543be2c7e9ca581339f08fb5b0288e2"    # Please use your own API key
        current_weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + key
        five_day_forecast_url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&units=metric&appid=" + key
        current = requests.get(current_weather_url)
        self.current = current.json()
        forecast = requests.get(five_day_forecast_url)
        self.forecast = forecast.json()
        print(current.status_code, forecast.status_code)

    def clear_screen(self):
        self.inside.txt.text = ""

    def on_enter(self, value):
        self.loc = self.inside.txt.text
        print("you clicked [ Enter ]")
        self.get_weather()
        self.clear_screen()
        self.today()

    def clicked_go(self, value):
        self.loc = self.inside.txt.text
        print("you clicked [ Go! ]")
        self.get_weather()
        self.clear_screen()
        self.today()

    def today(self):
        print("you clicked [ NOW ]")
        self.val = 0
        self.desc = self.current["weather"][0]["description"]
        self.time = "now"
        self.temp = str(self.current["main"]["temp"]) + " C"
        self.feels_like = str(self.current["main"]["feels_like"]) + " C"
        self.wind = str(self.current["wind"]["speed"]) + " m/s"
        self.pressure = str(self.current["main"]["pressure"]) + " hPa"
        self.humidity = str(self.current["main"]["humidity"]) + " %"
        self.visibility = str(round(self.current["visibility"] / 1000, 2)) + " km"

    def next(self):
        print("you clicked [  |>  ]")
        try:
            self.val += 1
            assert self.val < 40
            self.desc = str(self.forecast['list'][self.val]["weather"][0]["description"])
            self.time = str(self.forecast['list'][self.val]["dt_txt"])
            self.temp = str(self.forecast['list'][self.val]["main"]["temp"]) + " C"
            self.feels_like = str(self.forecast['list'][self.val]["main"]["feels_like"]) + " C"
            self.wind = str(self.forecast['list'][self.val]["wind"]["speed"]) + " m/s"
            self.pressure = str(self.forecast['list'][self.val]["main"]["pressure"]) + " hPa"
            self.humidity = str(self.forecast['list'][self.val]["main"]["humidity"]) + " %"
            self.visibility = str(round(self.forecast['list'][self.val]["visibility"] / 1000, 2)) + " km"
        except AssertionError:
            if self.val >= 40:
                self.val = 39

    def prev(self):
        print("you clicked [  <|  ]")
        try:
            self.val -= 1
            assert self.val >= 0
            self.desc = str(self.forecast['list'][self.val]["weather"][0]["description"])
            self.temp = str(self.forecast['list'][self.val]["main"]["temp"]) + " C"
            self.feels_like = str(self.forecast['list'][self.val]["main"]["feels_like"]) + " C"
            self.wind = str(self.forecast['list'][self.val]["wind"]["speed"]) + " m/s"
            self.pressure = str(self.forecast['list'][self.val]["main"]["pressure"]) + " hPa"
            self.humidity = str(self.forecast['list'][self.val]["main"]["humidity"]) + " %"
            self.visibility = str(round(self.forecast['list'][self.val]["visibility"] / 1000, 2)) + " km"
        except AssertionError:
            if self.val < 0:
                self.val = 0


class MainWidget(Widget):
    pass


class WeatherApp(App):
    pass

WeatherApp().run()
