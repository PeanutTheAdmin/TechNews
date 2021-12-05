#!/usr/bin/env python3

"""
Required Modules:
    pip install kivy
    pip install requests
    pip install bs4
"""

import kivy
from requests.api import head
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
import kivy.properties as kvprop
from kivy.lang import Builder
import requests
from bs4 import BeautifulSoup as bs

Builder.load_file('main.kv')

class MyScrollView(ScrollView):
    pass

class MyGridLayout(Widget):

    latest_news = kvprop.StringProperty('Refresh For News')

    def pressed(self):
        try:

            url = ('https://www.jacobcavaness.com/')

            d = requests.get(url)
            soup = bs(d.content , 'html.parser')
            article_title = soup.title.text
            article = soup.find('p')
            headline_text = article.text

            output = self.latest_news = (f'Website Title: {article_title}\n\nHeadline Text: {headline_text}')
            
            print(output)
        except:
            self.latest_news = ('No Data or Wrong Spelling')


class TechApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    TechApp().run()
