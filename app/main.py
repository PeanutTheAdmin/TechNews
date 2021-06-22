#!/usr/bin/env python3

import kivy
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

            url = ('https://www.bleepingcomputer.com/')

            d = requests.get(url)
            soup = bs(d.content , 'html.parser')
            article_title = soup.title.text
            article = soup.find('div', class_ = 'bc_latest_news_text')
            headline = article.h4.a.text
            headline_text = article.p.text

            output = self.latest_news = (f'Website Title: {article_title}\n\nHeadline: {headline}\n\nHeadline Text: {headline_text}')
            
            print(output)
        except:
            self.latest_news = ('No Data or Wrong Spelling')


class TechApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    TechApp().run()
