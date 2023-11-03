import pyautogui
import easyocr
from screeninfo import get_monitors
import serial
import keyboard
import time


monitors = get_monitors()
monitorx = monitors[0].width
monitory = monitors[0].height

class ScreenShot:
    def __init__(self, monitorx, monitory):
       self.reader = easyocr.Reader(['en'], gpu=True)
       self.screen_area = (0, 0, monitorx, monitory)

    def getScreenShot(self):
        try:
            screenshot = pyautogui.screenshot(region=self.screen_area)
            screenshot.save("screenshot.png")
            return screenshot
        except:
            print("Photograph could not be taken")
            self.getScreenShot()

    def getOCRText(self, screenshot):
        try:
            result = self.reader.readtext('screenshot.png')
            return result
        except:
            print("Ocr could not be read")
            self.getOCRText(screenshot)
    
    def read(self,filename):
        try:
            with open(filename, 'r') as file:
                data = file.read().splitlines()
            list = []
            for i in data:
                list.append(i)    
            return list
        except:
            print("txt file does not exist")
    
    def serial_connection(self):
        input_port = input("Lütfen aygıt yöneticisinden COM portunu girin (Örnek = COM4) : ")
        try:
            self.ser = serial.Serial(port=input_port, baudrate=9600,timeout=.1)
        except:
            print("Port not found")
            self.serial_connection()
        return self.ser
    
    def send_signal_arduino(self,signal):

        try:
            send = self.ser
            send.write(bytes(signal, 'utf-8'))
            time.sleep(0.05)
            data = send.readline()
            print(data)
            return data
        except:
            print("Signal could not be sent")
            self.send_signal_arduino(send,signal)
        
    def read_start_key(self):
        dongu = True
        while dongu:
            if(keyboard.is_pressed(self.start_key)):
                print("Pressed start button")
                dongu = False
        self.read_game_key()

    def read_game_key(self):
        dongu = True
        while dongu:
            if(keyboard.is_pressed(self.first_key)):
                print("First gamer started")
                self.send_signal_arduino("A")
                dongu = False
            elif(keyboard.is_pressed(self.second_key)):
                self.send_signal_arduino("B")
                print("Second gamer started")
                dongu = False
        self.read_game_over()
        
    def read_game_over(self):
        while True:
            ocr_result = self.getOCRText(self.getScreenShot())
            for i in ocr_result[1]:
                if(i == "GAME OVER"):
                    print("GAME OVER signal sent")
                    self.send_signal_arduino("C")
                    self.read_start_key()

    def main(self):
        try:
            self.serial_connection()
            list = self.read("keys.txt")
            self.start_key = str(list[0])
            self.first_key = str(list[1])
            self.second_key = str(list[2])
            print("Startkey " + self.start_key + " Firstkey " + self.first_key + " Secondkey " + self.second_key)

            while True:
                self.read_start_key()      
        except Exception as e:
            print(e)
            
            self.main()
                        
                    

app = ScreenShot(monitorx, monitory)
app.main()

            
