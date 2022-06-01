from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from pyfiglet import figlet_format
from rich.console import Console
from rich import print
import requests
import time
import sys
import os

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

opt = Options()
opt.set_headless()

class SpeedTest:
    def __init__(self):
        self.url = 'https://www.speedtest.net/'
        self.navegador = Firefox(options=opt)
        self.console = Console()
        self.requests = requests.get(self.url)

    def Banner(self):
        banner = figlet_format('SpeedTest')
        print(f'[bold][italic]{banner}[/]', 'version: 1.0.0')

    def speedtest(self):
        with self.console.status('Checking connection...') as void:
            if self.requests.status_code == 200:
                print('\n[green][200][/] - OK\n')
                time.sleep(1)
            else:
                print('[red]][?] - Something went wrong![/]')
                sys.exit()

        with self.console.status('Hold...') as void:
            navegador = self.navegador
            navegador.get(self.url)
            time.sleep(2)
    
    def Info(self):
        try:
            ip = self.navegador.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/div[3]')
            time.sleep(1)
            provedor = self.navegador.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[4]/div/div[3]/div/div/div[2]/a')
            time.sleep(1)
            textoip = ip.text
            textoprov = provedor.text
            print(f'''
                =================================+
                = IP: [cyan]{textoip}[/]
                = Provider: [yellow]{textoprov}[/]
                =================================+

                ''')
        except:
            print('[red]Something went wrong, try running again[/]')

    def Start(self):
        try:
            start = self.navegador.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            with self.console.status('Testing network...') as void:
                start.click()
                time.sleep(36)
        except:
            print('[red]Something went wrong, try running again[/]')

    def Speed(self):
        try:
            elemping = self.navegador.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
            time.sleep(1)
            elemdownload = self.navegador.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            time.sleep(1)
            elemupload = self.navegador.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
            time.sleep(1)
            ping = elemping.text
            download = elemdownload.text
            upload = elemupload.text
            print(f'''
                ============= {self.url} =============
                = Ping: :on: {ping}
                = Download: :arrow_up: {download}
                = Upload: :arrow_down: {upload}
                ======================================
                '''
                )
        except:
            print('[red]Something went wrong, try running again[/]')


vini = SpeedTest()
vini.Banner()
vini.speedtest()
vini.Info()
vini.Start()
vini.Speed()
