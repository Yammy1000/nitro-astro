import time
from time import localtime, strftime, sleep
from colorama import Fore
import requests
import random
import string
import os
from discord_webhook import DiscordWebhook
import random

currentCode = 1
class astroGen:
    def __init__(this, code_type: str, prox=None, codes=None):
        this.type = code_type
        this.codes = codes
        this.proxies = prox
        this.session = requests.Session()
        this.prox_api = (
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        )

    def __proxies__(this):
        req = this.session.get(this.prox_api).text
        if req != None:
            open("./data/proxies.txt", "a+").truncate(0)
            for proxy in req.split("\n"):
                proxy = proxy.strip()
                proxy = f"https://{proxy}"
                open("./data/proxies.txt", "a").write(f"{proxy}\n")

    def generate(this, scrape=None):
        if scrape == "True":
            this.__proxies__()
        else:
            pass

        os.system("clear")
        currentCode = 0
        for _ in range(int(this.codes)):
            try:
                if this.proxies == "True":
                    prox = {
                        "http": random.choice(
                            open("./data/proxies.txt", "r").read().splitlines()
                        )
                    }
                else:
                    prox = None

                if this.type == "boost":
                    code = "".join(
                        [
                            random.choice(string.ascii_letters + string.digits)
                            for i in range(24)
                        ]
                    )
                else:
                    code = "".join(
                        [

                            random.choice(string.ascii_letters + string.digits)

                            for i in range(16)
                        ]
                    )
                req = 1

                #g mode = speed

                open("./data/code.txt", "a").write(f"{code}\n")
                print(f'Code {code} is saved to codes.txt')
                if req == 200:
                    print(
                        f"{Fore.GREEN}[{strftime('%H:%M', localtime())}] discord.gift/{code} | correct code"
                    )

                    open("./data/valid.txt", "a").write(f"{code}\n")


                    #webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1207462633930891305/Ma3ikJDW5UXMk0SXnicvGIZhOI3tX_O3rx0I8f_rSeCGhfTsjwNodyztEqS19oNK-e90", rate_limit_retry=True, content=f"{code}")
                    #response = webhook.execute()


                if req == 404:
                    print(
                        f"{Fore.RED}[{strftime('%H:%M', localtime())}] discord.gift/{code} | invaild"
                    )
                    open("./data/bad.txt", "a").write(f"{code}\n")

                    #webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1208201975108214834/E8dO7QkDuZxR12bR9Ay2QaeQ2LWldaT8lGZ8mcIG0pxdduQ_gL_JfeEkclWZAbUjqR5Y", rate_limit_retry=True, content=f"{code}")
                    #response = webhook.execute()


                if req == 429:
                    print(
                        f"{Fore.YELLOW}[{strftime('%H:%M', localtime())}] discord.gift/{code} | failed"
                    )
                    open("./data/rated.txt", "a").write(f"{code}\n")

                    #webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1207489068334850161/ZGtBrs39pmjwY3ZJMiLUzHDykMt7LWtsVhOlxTqb9XL4GQPEGaE3U3Vo2tGqtZKc8YJ9", rate_limit_retry=True, content=f"{code}")
                    #response = webhook.execute()

                if req == 1:



                    print(
                        f"{Fore.YELLOW}[{strftime('%H:%M', localtime())}] discord.gift/{code} | LOGGED"
                    )
                    currentCode = currentCode + 1
                    print(f'The current lines are: {currentCode}')
                    open("./data/code.txt", "a").write(f"{code}\n")



            except Exception as e:
                print(f"{Fore.RED}[{strftime('%H:%M', localtime())}] {e}")

        print(
            f"{Fore.LIGHTMAGENTA_EX}[{strftime('%H:%M', localtime())}] Successfully checked {this.codes} codes."
        )
        sleep(1.5)
        os.system("clear")


if __name__ == "__main__":
    while True:
        print(f'{Fore.LIGHTCYAN_EX}[{strftime('%M:%S', localtime())}] Generating Proxies')
        time.sleep(1)
        print(f'{Fore.LIGHTCYAN_EX}[{strftime('%M:%S', localtime())}] Finding Gift links')
        time.sleep(3)
        print(f'{Fore.LIGHTCYAN_EX}[{strftime('%M:%S', localtime())}] Please wait 5-10 seconds')
        time.sleep(7)
        userCode = input(f'{Fore.LIGHTGREEN_EX}[{strftime('%M:%S', localtime())}] Please enter Secret ID: ')
        time.sleep(0.5)
        print(f'{Fore.LIGHTYELLOW_EX}[{strftime('%M:%S', localtime())}] Scanning')
        time.sleep(5)

        if userCode == 'Surnasd74hkaerieKAr' or '3nSru3mKsdmrl:Arisdna' or 'Swe(sejh$asr;<w' or 'Amw47ka4giU&S6df4' or '':
            print(f'{Fore.LIGHTGREEN_EX}[{strftime('%M:%S', localtime())}] Code is valid running scripts')
            time.sleep(2)

            code_type = input(
            f"{Fore.LIGHTMAGENTA_EX}[{strftime('%M:%S', localtime())}] Code Type (boost, classic): "
            )
            prox = input(
            f"{Fore.LIGHTMAGENTA_EX}[{strftime('%M:%S', localtime())}] Proxies (True, False): "
            )

            if prox == "True":
                scrape_proxy = input(
                    f"{Fore.LIGHTMAGENTA_EX}[{strftime('%M:%S', localtime())}] Scrape proxies (True, False): "
                )
            else:
                scrape_proxy = False
            codes = input(
                f"{Fore.LIGHTMAGENTA_EX}[{strftime('%M:%S', localtime())}] Number of codes: "
            )


        else:
            print(f'{Fore.RED}CODE FAILED')
            time.sleep(99999)  # NO DUB FOR YOU BUCKOS

        astroGen(code_type, prox, codes).generate(scrape=scrape_proxy)
