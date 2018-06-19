from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
import boto3

class MainScreen(Screen):
    pass

class FileSelectScreen(Screen):
    pass

class ReadyToAnalyseScreen(Screen):

    def ana(self, url):
        client = boto3.client('rekognition','eu-west-1')
        with open(url, 'rb') as source_image:
            source_bytes = source_image.read()
        response = client.detect_text(
            Image={
                'Bytes': source_bytes
            }
        )
        s=""


        for i in response['TextDetections']:
            if i["Type"]=='LINE':
                s+=" "+i['DetectedText']

        #print(s)
        return s

class AnalysisScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("SimpleKivy2.kv")

class SimpleKivy2(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    SimpleKivy2().run()
