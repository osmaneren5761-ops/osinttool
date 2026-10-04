from pystyle import Colorate, Colors
import clear
import os
import colorama
from colorama import Fore, init , Style
import requests
import whois
import customtkinter as ctk
import fade
import whois
import time
import instaloader
from cryptography.fernet import Fernet
import base64
import random
import discord
from discord.ext import commands
import socket
os.system("title worex Tools")



hostname = socket.gethostname()

root = (Fore.LIGHTMAGENTA_EX+f"""
┌──({hostname}@worex)-[~Menu -]│
└─$>""")

ascii_ = '''

██╗  ██╗ █████╗ ███╗   ███╗███████╗██████╗ ██╗   ██╗███╗   ██╗
██║ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██╗██║   ██║████╗  ██║
█████╔╝ ███████║██╔████╔██║█████╗  ██████╔╝██║   ██║██╔██╗ ██║
██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║██║╚██╗██║
██║  ██╗██║  ██║██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

                                                                                           
┌─────────────────┐                        ┌─────────┐                                     
├──── Osint-Tools ┤────────────┬───────────┤ Discord ├────────────┐
└─────────────────┘            │           └─────────┘            │
├ [01] OSINT Araştırma Menüsü ├ [02] Discord Araçları Menüsü      │          
│─────────────────────────────────────────────────────────────────│
│ [N] Sonraki Sayfa  |  [B] Geri  |  [C] Yapımcı | [Q] Çıkış      │
└─────────────────────────────────────────────────────────────────┘

   
'''

def main():
    clear.clear()
    COLs = Colorate.Diagonal(Colors.blue_to_red, ascii_)
    print(COLs)
    
    choice = input(root)
    
    if choice == "1" or choice == "01":
        clear.clear()
        osintmenu()
    if choice == "2" or choice == "02":
        clear.clear()
        discordmenu()
    if choice == "c" or choice == "C":
        clear.clear()
        Credit()
    if choice == "q" or choice == "Q":
        exit()
    if choice == "n" or choice == "N":
        input("[YAKINDA] Sonraki menü yakında geliyor! ")
        clear.clear()
        main()
    if choice == "b" or choice == "B":
        input("[YAKINDA] Geri menü yakında geliyor! ")
        clear.clear()
        main()
    else:
        input("[HATA] Geçersiz seçenek...")
        clear.clear()
        main()


def Credit():
    print(Fore.CYAN + r"""
+----------------------------------------------------------+
|                                                          |
|    ██████╗██████╗ ███████╗██████╗ ██╗████████╗           |
|   ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝           |
|   ██║     ██████╔╝█████╗  ██║  ██║██║   ██║              |
|   ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║              |
|   ╚██████╗██║  ██║███████╗██████╔╝██║   ██║              |
|    ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝              |
|                                                          |
|              Yapımcı    : worex                          |
|              Proje      : worex-Tools                    |
|              Discord    : KAMERUN                        |
|              Sürüm      : 1.0                            |
+----------------------------------------------------------+
""" + Style.RESET_ALL)
    input("Menüye dönmek için enter tuşuna basın...")
    clear.clear()
    main()
  
  
  
def discordmenu():
  ascii_discord = '''
████████▄   ▄█     ▄████████  ▄████████  ▄██████▄     ▄████████ ████████▄  
███   ▀███ ███    ███    ███ ███    ███ ███    ███   ███    ███ ███   ▀███ 
███    ███ ███▌   ███    █▀  ███    █▀  ███    ███   ███    ███ ███    ███ 
███    ███ ███▌   ███        ███        ███    ███  ▄███▄▄▄▄██▀ ███    ███ 
███    ███ ███▌ ▀███████████ ███        ███    ███ ▀▀███▀▀▀▀▀   ███    ███ 
███    ███ ███           ███ ███    █▄  ███    ███ ▀███████████ ███    ███ 
███   ▄███ ███     ▄█    ███ ███    ███ ███    ███   ███    ███ ███   ▄███ 
████████▀  █▀    ▄████████▀  ████████▀   ▀██████▀    ███    ███ ████████▀  
                                                     ███    ███            
╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                            DISCORD ARAÇLARI
╙──────────────────────────────────────────────────────────────────────────────────────────────────────────────╜

├─ [01] Discord Webhook Spam            ├─ [06] Discord ID → Token İlk Parça    ├─ [11] Discord DM Bot
├─ [02] Discord Webhook Silici          ├─ [07] Discord Sunucu Bilgisi          ├─ [12] Discord Token DM
├─ [03] Discord Token Bilgisi           ├─ [08] Discord Token Kontrol           ├─ [13] Yakında...
├─ [04] Discord ID Bilgisi              ├─ [09] Discord Nitro Üretici           ├─ [14] Yakında...
├─ [05] Discord Webhook Bilgisi         ├─ [10] Discord Bot ID → Davet Linki    ├─ [15] Discord Menüsünden Çık

  '''
  coilorat = Colorate.Diagonal(Colors.blue_to_red, ascii_discord)
  print(coilorat)
  root_discord = (Fore.LIGHTMAGENTA_EX+"""
┌──(User@worex)-[~DISCORD]│
└─$>""")
  choicediscord = input(root_discord)
  if choicediscord == "1" or choicediscord == "01":
    webhooksend()
  if choicediscord == "2" or choicediscord == "02":
    webhookdel()
  if choicediscord == "3" or choicediscord == "03":
    discordtokeninfo()
  if choicediscord == "4" or choicediscord == "04":
    discord_idinfo()
  if choicediscord == "5" or choicediscord == "05":
    webhook_info()
  if choicediscord == "6" or choicediscord == "06":
    idtofristpartoken()
  if choicediscord == "7" or choicediscord == "07":
    serverinfo()
  if choicediscord == "8" or choicediscord == "08":
    tokencheck()
  if choicediscord == "9" or choicediscord == "09":
    nitrogen()
  if choicediscord == "10" or choicediscord == "010":
    idinvite()
  if choicediscord == "11" or choicediscord == "011":
    dmalld()
  if choicediscord == "12" or choicediscord == "012":
    dmalltoken()
  if choicediscord == "15" or choicediscord == "015":
    main()
    
    
def dmalltoken():
    clear.clear()
    ascii_dmalltoken = """
██████╗ ███╗   ███╗ █████╗ ██╗     ██╗     
██╔══██╗████╗ ████║██╔══██╗██║     ██║     
██║  ██║██╔████╔██║███████║██║     ██║      Token
██║  ██║██║╚██╔╝██║██╔══██║██║     ██║     
██████╔╝██║ ╚═╝ ██║██║  ██║███████╗███████╗
╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
[!]Ctrl + C : Çıkış
[!]RATE LIMIT TEHLİKESİ! ÖNEMLİ HESAPTA KULLANMAYIN.
                                                                                                                                                                                                                     
   """
    print(fade.greenblue(ascii_dmalltoken))
    token = input(Fore.LIGHTBLUE_EX + "Hesap Token'ı : ")  
    message = input(Fore.LIGHTBLUE_EX +"Gönderilecek Mesaj : ")

    headers = {
        'Authorization': token
    }
    channelid = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    rsp = channelid.json()
    
    for channel in rsp: 
      time.sleep(random.uniform(6.5, 7.5))
      requests.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages',headers=headers,json={"content": message})  
      print(Fore.LIGHTGREEN_EX+f"Mesaj gönderildi → Kanal ID : {channel['id']}")
      
    if channelid.status_code == '429':
      print("Rate limit yediniz!")
      input("Menüye dönmek için enter'a basın...")
      clear.clear()
      discordmenu()
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    discordmenu()
def dmalld():
    clear.clear()
    ascii_dmall = """
██████╗ ███╗   ███╗ █████╗ ██╗     ██╗     
██╔══██╗████╗ ████║██╔══██╗██║     ██║     
██║  ██║██╔████╔██║███████║██║     ██║     
██║  ██║██║╚██╔╝██║██╔══██║██║     ██║     
██████╔╝██║ ╚═╝ ██║██║  ██║███████╗███████╗
╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                           
    [!] DM'yi durdurmak için Ctrl + C tuşuna basın.
    [!] DM durduğunda tüm mesajlar gönderilmiş demektir, çıkmak için tekrar Ctrl + C basın.                                                                                                                                                                              
   """
    print(fade.greenblue(ascii_dmall))
    print()
    bottoken = input(Fore.LIGHTBLUE_EX + "Bot token'ını girin: ")
    prefixs = input("Kullanmak istediğiniz komut öneki (örneğin + veya !): ")


    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True 
    bot = commands.Bot(command_prefix=f"{prefixs}", intents=intents)
    
    @bot.command()
    async def dmall(ctx, *, message):
      for member in ctx.guild.members:
        if member.bot : 
          continue
        
        await ctx.send('Toplu DM başlatılıyor...')
        await member.send(message)  
        print(Fore.LIGHTGREEN_EX+f"Gönderildi → {member.id} | {member.name}")
    print()
    
    print(Fore.LIGHTRED_EX+f'Botun davetli olduğu bir sunucuda "{prefixs}dmall <mesaj>" yazarak komutu çalıştırın.')
    bot.run(bottoken)
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    discordmenu()
    
    
  
def idinvite():
    clear.clear()
    ascii_idbot = """
██╗██████╗     ████████╗ ██████╗     ██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗
██║██╔══██╗    ╚══██╔══╝██╔═══██╗    ██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝
██║██║  ██║       ██║   ██║   ██║    ██║██╔██╗ ██║██║   ██║██║   ██║   █████╗  
██║██║  ██║       ██║   ██║   ██║    ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝  
██║██████╔╝       ██║   ╚██████╔╝    ██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗
╚═╝╚═════╝        ╚═╝    ╚═════╝     ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝
                                                                               
                                                                                                                           
   """
    print(fade.greenblue(ascii_idbot))
    print()
    cod = input(Fore.LIGHTBLUE_EX+"Discord Bot ID'sini girin : ")
    url =  f"https://discord.com/oauth2/authorize?client_id={cod}&scope=bot&permissions=8"
    print()
    print(Fore.LIGHTGREEN_EX+f"[{cod}] Bot davet linki : ",url)
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    discordmenu()
    
def check(code):
    valid = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code}')

    if not valid.status_code == 200:
        return False
    else:
        return True
  
def gene():
    code = ""
    for i in range(19):
        code += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return code
  
def nitrogen():
    clear.clear()
    ascii_ntrogen = """
███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                                                                           
   """
    print(fade.greenblue(ascii_ntrogen))
    with open('nitrocodes-generated.txt', 'w') as file:
      numbers = int(input(Fore.LIGHTBLUE_EX+"Üretilecek nitro kod sayısı : "))
      for _ in range(numbers):
            code = gene()
            valid = check(code)

            if valid:
                print(Fore.GREEN + f' Geçerli Nitro Kodu Üretildi : {code}')
                file.write(f'{code} - GEÇERLİ\n')
            else:
                print(Fore.RED + f' Geçersiz Nitro Kodu Üretildi : '+Fore.WHITE+code)
                file.write(f'{code} - GEÇERSİZ\n')
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    discordmenu()

def tokencheck():
  ascii_stkencheck = """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║  ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║  ██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                        
  [1] Tek token kontrolü
  [2] Çoklu token kontrolü                                                     
   """

  clear.clear()
  print(fade.greenblue(ascii_stkencheck))
  choix2tigre = input(Fore.LIGHTBLUE_EX+"Seçiminizi girin : ")
  if choix2tigre == "1" or choix2tigre == "01":
    onecheck()
  if choix2tigre == "2" or choix2tigre == "02":
    multicheck()
  
  
  
def onecheck():
  token = input(Fore.LIGHTBLUE_EX + "Discord Token'ını girin : ")
  headers = {'Authorization': token}
    
  res = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
  if res.status_code == 200:
        print(Fore.LIGHTGREEN_EX + f"[+] Geçerli Token : {token}")
        print("Kullanıcı :", res.json()['username'])
  if res.status_code == 401:
        print(Fore.LIGHTRED_EX + f"[-] Geçersiz token : {token}")
    
  print()
  input("Menüye dönmek için enter'a basın...")
  clear.clear()
  discordmenu()
    
    
    
    
def multicheck():
    tokens = input(Fore.LIGHTBLUE_EX + "Discord Token'larını girin (virgülle ayrılmış) : ")
    tokens = tokens.split(",")  
    
    for token in tokens:
        headers = {'Authorization': token}
        res = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        print()
        
        if res.status_code == 200:
            print(Fore.LIGHTGREEN_EX + f"[+] Geçerli Token : {token}")
            print("Kullanıcı :", res.json()['username'])
        elif res.status_code == 401:
            print(Fore.LIGHTRED_EX + f"[-] Geçersiz token : {token}")
        else:
            print(Fore.LIGHTRED_EX + "Discord API hatası.")
    
    
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    discordmenu()
   
def serverinfo():
  ascii_serverinfo = """
███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝██╔═══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║██╔██╗ ██║█████╗  ██║   ██║
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║██║╚██╗██║██╔══╝  ██║   ██║
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██║██║ ╚████║██║     ╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                            
   """

  clear.clear()
  print(fade.greenblue(ascii_serverinfo))
  invite = input(Fore.LIGHTBLUE_EX+"Discord sunucu davet linkini girin : ")
  invite_code = invite.split("/")[-1]

  response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
  api = response.json()
  
  type_value = api.get('type', "n/a")
  code_value = api.get('code', "n/a")
  expires_at = api.get('expires_at', "n/a")
  flags = api.get('flags', "n/a")

  server_info = api.get('guild', {})
  server_id = server_info.get('id', "n/a")
  server_name = server_info.get('name', "n/a")
  server_icon = server_info.get('icon', "n/a")
  server_features = server_info.get('features', [])
  server_features_str = ' / '.join(server_features) if server_features else "n/a"
  server_verification_level = server_info.get('verification_level', "n/a")
  server_nsfw_level = server_info.get('nsfw_level', "n/a")
  server_description = server_info.get('description', "n/a")
  server_nsfw = server_info.get('nsfw', "n/a")
  server_premium_subscription_count = server_info.get('premium_subscription_count', "n/a")

  channel_info = api.get('channel', {})
  channel_id = channel_info.get('id', "n/a")
  channel_type = channel_info.get('type', "n/a")
  channel_name = channel_info.get('name', "n/a")
  print()
  print(Fore.LIGHTBLUE_EX+f"""
📋 Davet Bilgileri:

🔹 Davet Linki        : {invite}
🔹 Tür                : {type_value}
🔹 Kod                : {code_value}
🔹 Son Kullanma       : {expires_at}

🏰 Sunucu:
  - ID                 : {server_id}
  - Ad                 : {server_name}
  - Açıklama           : {server_description}
  - İkon               : {server_icon}
  - Özellikler         : {server_features_str}
  - Doğrulama Seviyesi : {server_verification_level}
  - NSFW Seviyesi      : {server_nsfw_level}
  - NSFW               : {server_nsfw}
  - Nitro Abone Sayısı : {server_premium_subscription_count}

📺 Kanal:
  - ID                 : {channel_id}
  - Ad                 : {channel_name}
  - Tür                : {channel_type}

🏳️ Bayraklar          : {flags}
""")
  print()
  input("Menüye dönmek için enter'a basın...")
  clear.clear()
  discordmenu()
    
def idtofristpartoken():
  ascii_tokenfirst = """
██╗██████╗          ██╗      ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██║██╔══██╗         ╚██╗     ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
██║██║  ██║    █████╗╚██╗       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██║██║  ██║    ╚════╝██╔╝       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║██████╔╝         ██╔╝        ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚═╝╚═════╝          ╚═╝         ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                                                            
   """

  clear.clear()
  print(fade.greenblue(ascii_tokenfirst))
  tokenfirst= input(Fore.LIGHTBLUE_EX+"Discord ID'sini girin : ")
  decodetoken = base64.b64encode(tokenfirst.encode()).decode().rstrip("=")
  print()
  print(Fore.LIGHTBLUE_EX+f"'{tokenfirst}' ID'sine ait Token İlk Parça : {decodetoken} ")
  print()
  input("Menüye dönmek için enter'a basın...")
  clear.clear()
  discordmenu()


def webhook_info(): 
  ascii_webok = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝  Information
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                            
   """

  clear.clear()
  print(fade.greenblue(ascii_webok))
  webhook = input(Fore.LIGHTBLUE_EX+"Discord Webhook URL'sini girin : ")
  r = requests.get(webhook)
  jso = r.json()

  print("🔎 Webhook Bilgileri")
  print()
  print(f"🆔 ID              : {jso.get('id', 'N/A')}")
  print(f"🧩 Uygulama ID     : {jso.get('application_id', 'N/A')}")
  print(f"🖼️ Avatar          : {jso.get('avatar', 'N/A')}")
  print(f"📺 Kanal ID        : {jso.get('channel_id', 'N/A')}")
  print(f"🏠 Sunucu ID       : {jso.get('guild_id', 'N/A')}")
  print(f"🌍 Ad              : {jso.get('name', 'N/A')}")
  print(f"🔑 Token           : {jso.get('token', 'N/A')}")
  print()
  input("Menüye dönmek için enter'a basın...")
  clear.clear()
  discordmenu()

def discord_idinfo():
    ascii_idinfo = """
██╗██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
██║██╔══██╗    ██║████╗  ██║██╔════╝██╔═══██╗
██║██║  ██║    ██║██╔██╗ ██║█████╗  ██║   ██║
██║██║  ██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
██║██████╔╝    ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                             
"""

    clear.clear()
    print(fade.greenblue(ascii_idinfo))

    user_id = input(Fore.LIGHTBLUE_EX+"Discord kullanıcı ID'sini girin : ")
    url = f"https://discordlookup.mesalytic.moe/v1/user/{user_id}"
    res = requests.get(url)
    data = res.json()
    print()
    print(Fore.LIGHTBLUE_EX+"🔎 Discord Kullanıcı Bilgileri")
    print(f"👤 Kullanıcı Adı      : {data.get('username', 'N/A')}")
    print(f"🆔 Kullanıcı ID       : {data.get('id', 'N/A')}")
    print(f"📅 Oluşturulma Tarihi : {data.get('created_at', 'N/A')}")
    print(f"🌐 Küresel Ad         : {data.get('global_name', 'N/A')}")
    avatar = data.get("avatar", {})
    print(f"🖼️ Avatar URL         : {avatar.get('link', 'N/A')}")
    print(f"🎞️ Animasyonlu Avatar : {avatar.get('is_animated', False)}")
    banner = data.get("banner", {})
    print(f"🖼️ Banner URL         : {banner.get('link', 'N/A')}")
    print(f"🎞️ Animasyonlu Banner : {banner.get('is_animated', False)}")
    print(f"🎨 Banner Rengi        : {banner.get('color', 'N/A')}")
    print(f"🎨 Vurgu Rengi         : {data.get('accent_color', 'N/A')}")
    badges = data.get("badges", [])
    print(f"🏅 Rozetler            : {', '.join(badges) if badges else 'Yok'}")
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    discordmenu()
  
def webhookdel(): 
  ascii_webhookdel = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗  SİLİCİ
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                                            
    """
  clear.clear()
  print(fade.greenblue(ascii_webhookdel))
  webhook = input(Fore.LIGHTBLUE_EX+"Silinecek webhook URL'sini girin : ")
  requests.delete(webhook)
  print(f"[BİLGİ] Webhook '{webhook}' silindi ")
  print()
  input("Menüye dönmek için enter'a basın...")
  discordmenu()
  
def discordtokeninfo():
    ascii_tokeninfo= """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗  ██╗    ██╗███╗   ██╗███████╗ ██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║  ██║    ██║████╗  ██║██╔════╝██╔═══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║  ██║    ██║██╔██╗ ██║█████╗  ██║   ██║
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║  ██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║  ██║    ██║██║ ╚████║██║     ╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝                                          
    """
    clear.clear()
    print(fade.greenblue(ascii_tokeninfo))
    token = input(Fore.LIGHTBLUE_EX+"Discord token'ını girin: ")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    response = requests.get("https://discord.com/api/v8/users/@me", headers=headers)
    user = response.json()

    full_username       = user.get("username", "None")
    display_name        = user.get("global_name", "None")
    user_id             = user.get("id", "None")
    email               = user.get("email", "None")
    email_verified      = user.get("verified", "None")
    phone_number        = user.get("phone", "None")
    has_2fa             = user.get("mfa_enabled", "None")
    locale              = user.get("locale", "None")
    avatar_hash         = user.get("avatar", "None")
    avatar_decoration   = user.get("avatar_decoration_data", "None")
    public_flags        = user.get("public_flags", "None")
    internal_flags      = user.get("flags", "None")
    banner_hash         = user.get("banner", "None")
    banner_color        = user.get("banner_color", "None")
    accent_color        = user.get("accent_color", "None")
    nsfw_allowed        = user.get("nsfw_allowed", "None")

    print("🔎 Discord Hesap Bilgileri")
    print()
    print(f"👤 Kullanıcı Adı       : {full_username}")
    print(f"📛 Görünen Ad          : {display_name}")
    print(f"🆔 Kullanıcı ID        : {user_id}")
    print(f"📧 E-posta             : {email}")
    print(f"✅ E-posta Doğrulandı  : {email_verified}")
    print(f"📱 Telefon Numarası    : {phone_number}")
    print(f"🔐 2FA Aktif           : {has_2fa}")
    print(f"🌍 Dil                 : {locale}")
    print(f"🖼️ Avatar Hash         : {avatar_hash}")
    print(f"✨ Avatar Dekorasyonu   : {avatar_decoration}")
    print(f"🚩 Genel Bayraklar     : {public_flags}")
    print(f"🎌 İç Bayraklar        : {internal_flags}")
    print(f"🖼️ Banner Hash         : {banner_hash}")
    print(f"🎨 Banner Rengi        : {banner_color}")
    print(f"🎨 Vurgu Rengi         : {accent_color}")
    print(f"🔞 NSFW İzinli         : {nsfw_allowed}")
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    discordmenu()


def webhooksend(): 
  ascii_webhooksend = """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗  GÖNDERİCİ
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                                            
    """
  clear.clear()
  print(fade.greenblue(ascii_webhooksend))
  webhook = input(Fore.LIGHTBLUE_EX+"Webhook URL'sini girin : ")
  message = input(Fore.LIGHTBLUE_EX+"Gönderilecek mesajı yazın : ")
  count = int(input(Fore.LIGHTBLUE_EX+"Gönderilecek mesaj sayısı  : "))
  message_to_send = {
    "content":f"{message}"
}
  webhook_url = f"{webhook}"
  for _ in range(count):
    requests.post(webhook_url,json=message_to_send)
    print(f'✅ Gönderildi: "{message}"')
  print()
  input("Menüye dönmek için enter'a basın...")
  discordmenu()
  
  
  
  
  
  

def osintmenu():

  ascii_osint = """
▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄ 
███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
███    ███   ███        ███▌ ███   ███     ███   ▀ 
███    ███ ▀███████████ ███▌ ███   ███     ███   Made by worex <3   
███    ███          ███ ███  ███   ███     ███     
███    ███    ▄█    ███ ███  ███   ███     ███     
 ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀

╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                            OSINT ARAÇLARI
╙──────────────────────────────────────────────────────────────────────────────────────────────────────────────╜

├─ [01] Leakcheck.io Arama              ├─ [06] GitHub E-posta Bulucu           ├─ [11] Alt Alan Adı Bulucu
├─ [02] IP Bilgileri                    ├─ [07] Telefon Araştırma               ├─ [12] E-posta Sızma Kontrolü
├─ [03] OsintKit GUI                    ├─ [08] WHOIS Sorgulama                 ├─ [13] Instagram Araştırma
├─ [04] DNS Sorgulama                   ├─ [09] E-posta Doğrulayıcı             ├─ [14] genderize.io (İsim → Cinsiyet)
├─ [05] GitHub Bilgi Araştırma          ├─ [10] Tüm OSINT Siteleri              ├─ [15] OSINT Menüsünden Çık

                                                                                      
"""
  COLorss = Colorate.Diagonal(Colors.blue_to_red, ascii_osint)
  print(COLorss)
  root_osint = (Fore.LIGHTMAGENTA_EX+"""
┌──(User@worex)-[~OSINT]│
└─$>""")
  choiceosint = input(root_osint)
  if choiceosint == "1" or choiceosint == "01":
    clear.clear()
    leakcheck()
  if choiceosint == "2" or choiceosint == "02":
    ip()
  if choiceosint == "3" or choiceosint == "03":
    launch_gui()
  if choiceosint == "4" or choiceosint == "04":
    dnsscan()
  if choiceosint == "5" or choiceosint == "05":
    github_info()
  if choiceosint == "6" or choiceosint == "06":
    githubemail()
  if choiceosint == "7" or choiceosint == "07":
    phonelookup()
  if choiceosint == "8" or choiceosint == "08":
    whhois()
  if choiceosint == "9" or choiceosint == "09":
    emailverif()
  if choiceosint == "10" or choiceosint == "010":
    osintwebsite()
  if choiceosint == "11" or choiceosint == "011":
    subfinder()
  if choiceosint == "12" or choiceosint == "012":
    mailcompromise()
  if choiceosint == "13" or choiceosint == "013":
    clear.clear()
    instagraminfo()
  if choiceosint == "14" or choiceosint == "014":
    genderiz()
  if choiceosint == "15" or choiceosint == "015":
    main()
  else:
    print("[HATA] Geçersiz seçenek")
    time.sleep(1)
    clear.clear()
    osintmenu()
  


def genderiz():
  clear.clear()
  name  = input(Fore.LIGHTBLUE_EX+"Cinsiyet tahmini yapılacak isim/tam isim girin : ")
  res = requests.get(f'https://api.genderize.io/?name={name}')
  data = res.json()
  gender = data.get('gender','N/A')
  propability = data.get('probability','N/A')
  nome = data.get('name','N/A')
  count = data.get('count','N/A')
  print()
  print(Fore.LIGHTBLUE_EX+f"""
       İsim         : {nome}
       Cinsiyet     : {gender}
       Olasılık     : {propability}%
       Toplam       : {count}""")
  print()
  input("Menüye dönmek için enter'a basın...")
  clear.clear()
  osintmenu()
def instagraminfo():
    ascii_insta = """
██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║ Araştırma
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                                                                   
    """
    clear.clear()
    print(fade.greenblue(ascii_insta))
    username  = input(Fore.LIGHTBLUE_EX+"Araştırılacak Instagram kullanıcı adını girin : ")
    
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, username)

    print()
    print(Fore.LIGHTBLUE_EX+f"Tam Ad      : {profile.full_name}")
    print(f"Kullanıcı Adı: {profile.username}")
    print(f"Biyografi   : {profile.biography}")
    print(f"Takipçi     : {profile.followers}")
    print(f"Takip Edilen: {profile.followees}")
    print(f"Gönderi     : {profile.mediacount}")
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    osintmenu()
    
def mailcompromise():
    ascii_compro = """
██╗     ███████╗ █████╗ ██╗  ██╗     ███╗   ███╗ █████╗ ██╗██╗     
██║     ██╔════╝██╔══██╗██║ ██╔╝     ████╗ ████║██╔══██╗██║██║     
██║     █████╗  ███████║█████╔╝      ██╔████╔██║███████║██║██║     
██║     ██╔══╝  ██╔══██║██╔═██╗      ██║╚██╔╝██║██╔══██║██║██║     
███████╗███████╗██║  ██║██║  ██╗     ██║ ╚═╝ ██║██║  ██║██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
      E-postanın sızdırılıp sızdırılmadığını kontrol et                                                              
    """
    clear.clear()
    print(fade.greenblue(ascii_compro))
    mail = input(Fore.LIGHTBLUE_EX+"Sızma kontrolü yapılacak e-postayı girin : ")
    response = requests.get(
        "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email",
        params={"email": mail}
    )

    data = response.json()
    stealers = data.get("stealers", [])

    if not stealers:
        print(f"{mail} adresi için herhangi bir sızma tespit edilmedi")
    else:
        for idx, item in enumerate(stealers, 1):
            print(f"Sızdırılan Cihaz #{idx}")
            print(f"📅 Sızma Tarihi         : {item.get('date_compromised', 'N/A')}")
            print(f"💻 Bilgisayar Adı       : {item.get('computer_name', 'N/A')}")
            print(f"🖥️ İşletim Sistemi      : {item.get('operating_system', 'N/A')}")
            print(f"🦠 Malware Yolu          : {item.get('malware_path', 'N/A')}")
            print(f"🛡️ Antivirüsler         : {', '.join(item.get('antiviruses', [])) or 'Yok'}")
            print(f"🌍 IP Adresi            : {item.get('ip', 'N/A')}")
            print(f"🔢 Toplam Servis        : {item.get('total_user_services', 'N/A')}")
            print(f"🔑 En Çok Şifreler      : {', '.join(item.get('top_passwords', [])) or 'Yok'}")
            print(f"📧 En Çok Girişler      : {', '.join(item.get('top_logins', [])) or 'Yok'}")
            print("─" * 50)
        input("Menüye dönmek için enter'a basın...")
        clear.clear()
        osintmenu()



def subfinder():
    ascii_sub = """
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗███████╗    
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔════╝    
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║███████╗    Bulucu 
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║╚════██║    
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║███████║   
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝                                                                       
    """
    clear.clear()
    print(fade.greenblue(ascii_sub))
    link = input(Fore.LIGHTBLUE_EX+"Alt alan adı taraması yapılacak domaini girin : ")
    res = requests.get(f"https://api.hackertarget.com/hostsearch/?q={link}")
    print()
    print(res.text)
    print()
    save = input(".txt dosyası olarak kaydetmek istiyor musunuz? (E/H) : ")
    if save.lower() in ["h", "hayır", "n", "no"]:
      clear.clear()
      osintmenu()
    else:
      with open(f"Subdomains-{link}.txt", "w") as file:
        file.write(res.text)
        input(f"Subdomains-{link}.txt dosyası oluşturuldu...")
        clear.clear()
        osintmenu()

def osintwebsite():
    ascii_osintweb = """
┌──────────────┐   ┌───────────────┐   ┌───────────────┐
│ [01] E-posta │   │ [03] Yüz      │   │ [05] Kullanıcı│
│     OSINT    │   │     OSINT     │   │     OSINT     │
│--------------│   │---------------│   │---------------│
│ E-posta Siteleri ││ Yüz Siteleri  │   │ Kullanıcı Adı Siteleri│
└──────────────┘   └───────────────┘   └───────────────┘

┌──────────────┐   ┌──────────────┐   ┌───────────────┐
│ [02] IP      │   │ [04] Kişi    │   │[06] Çerçeveler│
│     OSINT    │   │     Araştırma│   │               │
│--------------│   │--------------│   │---------------│
│ IP Siteleri  │   │ Kişi Siteleri│   │Çerçeve Siteleri│
└──────────────┘   └──────────────┘   └───────────────┘

────────────────────────────────────────────────────────────────────────────
                     [07] Ana OSINT Menüsüne Dön
────────────────────────────────────────────────────────────────────────────

                                                                                                                                                    
    """
    clear.clear()
    print(fade.greenblue(ascii_osintweb))
    sitechoice = input(Fore.LIGHTBLUE_EX+"Seçiminiz ->  ")
    
    if sitechoice == "1" or sitechoice == "01":
        clear.clear()
        email_osint = [
            "https://epieos.com",
            "https://haveibeenpwned.com",
            "https://emailrep.io",
            "https://hunter.io",
            "https://leakcheck.io",
            "https://snusbase.com",
            "https://dehashed.com"
        ]
        print(Fore.LIGHTBLUE_EX+"E-posta OSINT Siteleri:")
        print()
        for site in email_osint:
            print(site)
        print()
        input("Menüye dönmek için enter'a basın...")
        clear.clear()
        osintwebsite()

    if sitechoice == "2" or sitechoice == "02":
        clear.clear()
        ip_osint = [
            "https://www.shodan.io",
            "https://ipinfo.io",
            "https://portscanner.online",
            "https://www.abuseipdb.com",
            "https://search.censys.io",
            "https://threatfox.abuse.ch"
        ]
        print(Fore.LIGHTBLUE_EX+"IP OSINT Siteleri:")
        print()
        for site in ip_osint:
            print(site)
        print()
        input("Menüye dönmek için enter'a basın...")
        clear.clear()
        osintwebsite()

    if sitechoice == "3" or sitechoice == "03":
        clear.clear()
        face_osint = [
            "https://pimeyes.com/en",
            "https://yandex.com/images",
            "https://facecheck.id"
        ]
        print(Fore.LIGHTBLUE_EX+"Yüz Tanıma OSINT Siteleri:")
        print()
        for site in face_osint:
            print(site)
        print()
        input("Menüye dönmek için enter'a basın...")
        clear.clear()
        osintwebsite()

    if sitechoice == "4" or sitechoice == "04":
        clear.clear()
        person_lookup = [
            "https://www.pagesjaunes.fr",
            "https://webmii.com",
            "https://www.idcrawl.com",
            "https://www.whitepages.com",
            "https://www.truepeoplesearch.com",
            "https://www.peekyou.com"
        ]
        print(Fore.LIGHTBLUE_EX+"Kişi Arama Siteleri:")
        print()
        for site in person_lookup:
            print(site)
        print()
        input("Menüye dönmek için enter'a basın...")
        clear.clear()
        osintwebsite()

    if sitechoice == "5" or sitechoice == "05":
        clear.clear()
        username_osint = [
            "https://whatsmyname.app",
            "https://www.namecheckr.com",
            "https://usersearch.org",
            "https://github.com/sherlock-project/sherlock (Github-Aracı)",
            "https://github.com/soxoj/maigret (Github-Aracı)"
        ]
        print(Fore.LIGHTBLUE_EX+"Kullanıcı Adı OSINT Siteleri:")
        print()
        for site in username_osint:
            print(site)
        print()
        input("Menüye dönmek için enter'a basın...")
        clear.clear()
        osintwebsite()

    if sitechoice == "6" or sitechoice == "06":
        clear.clear()
        osint_frameworks = [
            "https://osintframework.com",
            "https://www.maltego.com",
            "https://www.spiderfoot.net",
            "https://github.com/lanmaster53/recon-ng (Github-Aracı)"
        ]
        print(Fore.LIGHTBLUE_EX+"OSINT Çerçeveleri ve Araçları:")
        print()
        for site in osint_frameworks:
            print(site)
        print()
        input("Menüye dönmek için enter'a basın...")
        clear.clear()
        osintwebsite()

    if sitechoice == "7" or sitechoice == "07":
        clear.clear()
        osintmenu()
        
def emailverif():
    ascii_mailverif = """
███████╗███╗   ███╗ █████╗ ██╗██╗         ██╗   ██╗███████╗██████╗ ██╗███████╗██╗███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██║   ██║██╔════╝██╔══██╗██║██╔════╝██║██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██║   ██║█████╗  ██████╔╝██║█████╗  ██║█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝  ██║██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗     ╚████╔╝ ███████╗██║  ██║██║██║     ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                   
    """
    clear.clear()
    print(fade.greenblue(ascii_mailverif))
    emails = input(Fore.LIGHTBLUE_EX+"Doğrulanacak e-postayı girin : ")
    res = requests.get(f"https://api.hunter.io/v2/email-verifier?email={emails}&api_key=2cde17cd082478662ec5f9cf832f4402ad73bc1c")
    respons = res.json()
    data = respons.get('data')
    print("Durum:", data.get("status"))
    print("Sonuç:", data.get("result"))
    print("Eski API Uyarısı:", data.get("_deprecation_notice"))
    print("Puan:", data.get("score"))
    print("E-posta:", data.get("email"))
    print("Regex:", data.get("regexp"))
    print("Rastgele:", data.get("gibberish"))
    print("Tek Kullanımlık:", data.get("disposable"))
    print("Webmail:", data.get("webmail"))
    print("MX Kayıtları:", data.get("mx_records"))
    print("SMTP Sunucusu:", data.get("smtp_server"))
    print("SMTP Kontrol:", data.get("smtp_check"))
    print("Herkese Açık:", data.get("accept_all"))
    print("Engelli:", data.get("block"))
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    osintmenu()
def whhois():
    ascii_whois = """
██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██║    ██║██║  ██║██╔═══██╗██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║ █╗ ██║███████║██║   ██║██║███████╗    ███████╗██║     ███████║██╔██╗ ██║
██║███╗██║██╔══██║██║   ██║██║╚════██║    ╚════██║██║     ██╔══██║██║╚██╗██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║    ███████║╚██████╗██║  ██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                       
    """
    clear.clear()
    print(fade.greenblue(ascii_whois))
    link = input(Fore.LIGHTBLUE_EX+"WHOIS sorgulaması yapılacak domaini girin : ")
    whhois = whois.whois(link)
    print(whhois)
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    osintmenu()
    
def leakcheck():
    ascii_art = """   
             *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***
            **             *              **
            """
    clear.clear()
    print(fade.greenblue(ascii_art))
    search = input(Fore.LIGHTBLUE_EX+"Leakcheck.io araması (Kullanıcı adı veya e-posta) --> ")
    api = f"https://leakcheck.io/api/public?check={search}"
    res = requests.get(api)
    data = res.json()
    print(f"Durum     : {data['success']}")
    print(f"Alanlar   : {data['fields']}")
    print(f"Kaynaklar : {data['sources']}")
    print()
    print()
    question = input(Fore.LIGHTBLUE_EX+"Sonuçları txt dosyasına kaydetmek istiyor musunuz? E/H : ") 
    if question.lower() in ['e', 'evet', 'y', 'yes']:
      with open("result-leakcheck.io.txt", "w", encoding="utf-8") as file:
         file.write(f"Durum: {data['success']}\n")
         file.write("-------------------------------\n")
         file.write(f"Alanlar: {data['fields']}\n")
         file.write("-------------------------------\n")
         file.write(f"Kaynaklar: {data['sources']}\n")
         input(Fore.LIGHTWHITE_EX+"Leakcheck sonuçları 'result-leakcheck.io.txt' dosyasına kaydedildi...")  
         clear.clear()
         osintmenu()
    else:
      clear.clear()
      osintmenu()
    
    
  
def phonelookup():
    ascii_art = """
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗    ██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║██╔██╗ ██║█████╗  ██║   ██║
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║██║╚██╗██║██╔══╝  ██║   ██║
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ██║██║ ╚████║██║     ╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                             
    """
    clear.clear()
    print(fade.greenblue(ascii_art))
    phone_number = input(Fore.LIGHTBLUE_EX+"Araştırılacak telefon numarasını girin : ")
    response = requests.get(f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey=num_live_pWHeBCRhv2VgqQ9nFOBTaDEDgVsKeHBa6VE6oghz")
    data = response.json()
    phone_lookup_result = (
    f"[*] Geçerli            : {data.get('valid')}\n"
    f"[*] Numara             : {data.get('number')}\n"
    f"[*] Yerel Format       : {data.get('local_format')}\n"
    f"[*] Uluslararası       : {data.get('international_format')}\n"
    f"[*] Ülke Kodu          : {data.get('country_prefix')}\n"
    f"[*] Ülke ISO           : {data.get('country_code')}\n"
    f"[*] Ülke Adı           : {data.get('country_name')}\n"
    f"[*] Konum              : {data.get('location')}\n"
    f"[*] Operatör           : {data.get('carrier')}\n"
    f"[*] Hat Türü           : {data.get('line_type')}"
    )
    print()
    print(phone_lookup_result)
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    osintmenu()

    
def githubemail():
    ascii_art = """
                /|  /|  -----------------------------------
                ||__||  |                                 |
               /   O O\__  Ben büyük bir hacker'ım!!      |
              /          \ GitHub e-postanı bulabilirim!  |
             /      \     \                               |
            /   _    \     \ ------------------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       | Made by worex (:D)
 ___/ /   |       |       | Basit script
|____/    c_c_c_C/ \C_c_c_c
    """
    clear.clear()
    print(fade.greenblue(ascii_art))
    Username = input(Fore.LIGHTYELLOW_EX+"GitHub kullanıcı adını girin --> ")
    repos = input(Fore.LIGHTYELLOW_EX+"GitHub reposunun adını girin --> ")
    res = requests.get(f"https://api.github.com/repos/{Username}/{repos}/commits")
    data = res.json()
    first_commit = data[0]
    author = first_commit.get('commit', {}).get('author', {})
    Email = author.get('email', 'N/A')
    User = author.get('name', 'N/A')
    print(f"""
+----+------------------+-------------+
| ID | Kullanıcı Adı    | E-posta     | 
+----+------------------+-------------+ 
| 1  | {User}           | {Email}     |
+----+-------------+------------------+""")
    input(Fore.WHITE+"Menüye dönmek için enter'a basın..")
    clear.clear()
    osintmenu()
    
    
  
def ip():
  art = '''
██╗██████╗       ██╗███╗   ██╗███████╗ ██████╗ 
██║██╔══██╗      ██║████╗  ██║██╔════╝██╔═══██╗
██║██████╔╝█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║██╔═══╝ ╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║           ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝           ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
    '''
  clear.clear()
  print(fade.greenblue(art))
  search_ip = input(Fore.LIGHTBLUE_EX+"Araştırılacak IP adresini girin --> ")
  res = requests.get(f"http://ip-api.com/json/{search_ip}")
  data = res.json()
  query = f"{data.get('query', 'N/A')}\n"
  status = f"{data.get('status', 'N/A')}\n"
  country = f"{data.get('country', 'N/A')}\n"
  countryCode = f"{data.get('countryCode', 'N/A')}\n"
  region = f"{data.get('region', 'N/A')}\n"
  regionName = f"{data.get('regionName', 'N/A')}\n"
  city = f"{data.get('city', 'N/A')}\n"
  zip = f"{data.get('zip', 'N/A')}\n"
  lat = f"{data.get('lat', 'N/A')}\n"
  lon = f"{data.get('lon', 'N/A')}\n"
  timezone = f"{data.get('timezone', 'N/A')}\n"
  isp = f"{data.get('isp', 'N/A')}\n"
  org = f"{data.get('org', 'N/A')}\n"
  print(f"""
╔══════════════ IP ARAŞTIRMA SONUCU ══════════════╗
║ IP          : {query}
║ Durum       : {status}
║ Ülke        : {country}
║ Ülke Kodu   : {countryCode}
║ Bölge       : {region}
║ Bölge Adı   : {regionName}
║ Şehir       : {city}
║ Posta Kodu  : {zip}
║ Enlem       : {lat}
║ Boylam      : {lon}
║ Saat Dilimi : {timezone}
║ ISS         : {isp}
║ Organizasyon: {org}
╚══════════════════════════════════════════════╝
  """)
  input(Fore.LIGHTBLUE_EX+"Menüye dönmek için enter'a basın...")
  clear.clear()
  osintmenu()







def launch_gui():
    app = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app.title("Osint-kit Gui - By :D")
    app.geometry("900x750")

    def whhois():
        link = entry.get()
        whhois_res = whois.whois(link)
        result_textbox.delete(1.0, ctk.END)
        result_textbox.insert(1.0, whhois_res)

    whois_label = ctk.CTkLabel(
        app,
        text="Whois Sorgulama",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    whois_label.pack()

    labeel = ctk.CTkLabel(master=app, text="WHOIS ile taranacak web sitesinin linki : ")
    labeel.pack()

    entry = ctk.CTkEntry(master=app, width=200, height=10)
    entry.pack()

    button = ctk.CTkButton(master=app, text="Tara", command=whhois)
    button.pack()

    label_info = ctk.CTkLabel(master=app, text="Whois tarama sonucu : ")
    label_info.pack()

    result_textbox = ctk.CTkTextbox(app, height=150, width=3900)
    result_textbox.pack()

    def ipinfo():
        ip = entry_ip.get()
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        ip_lookup_result = (
            f"[*] Ülke        : {data.get('country')}\n"
            f"[*] Ülke Kodu   : {data.get('countryCode')}\n"
            f"[*] Şehir       : {data.get('city')}\n"
            f"[*] Posta Kodu  : {data.get('zip')}\n"
            f"[*] Saat Dilimi : {data.get('timezone')}\n"
            f"[*] Organizasyon: {data.get('org')}\n"
            f"[*] Bölge       : {data.get('region')}\n"
            f"[*] Bölge Adı   : {data.get('regionName')}\n"
            f"[*] AS          : {data.get('as')}\n"
            f"[*] Enlem       : {data.get('lat')}\n"
            f"[*] Boylam      : {data.get('lon')}"
        )
        result_textbox_ip.delete(1.0, ctk.END)
        result_textbox_ip.insert(1.0, ip_lookup_result)

    ipinfo_label = ctk.CTkLabel(
        app,
        text="IP Araştırma",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    ipinfo_label.pack()

    label_ip = ctk.CTkLabel(master=app, text="IP adresi : ")
    label_ip.pack()

    entry_ip = ctk.CTkEntry(master=app, width=200, height=10)
    entry_ip.pack()

    button_ip = ctk.CTkButton(master=app, text="IP Bilgilerini Al", command=ipinfo)
    button_ip.pack()

    label_ip2 = ctk.CTkLabel(master=app, text="IP Bilgi Çıktısı : ")
    label_ip2.pack()

    result_textbox_ip = ctk.CTkTextbox(app, height=150, width=3900)
    result_textbox_ip.pack()

    def phone():
        phone_number = entry_phone.get()
        response = requests.get(
            f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey=num_live_pWHeBCRhv2VgqQ9nFOBTaDEDgVsKeHBa6VE6oghz"
        )
        data = response.json()
        phone_lookup_result = (
            f"[*] Geçerli            : {data.get('valid')}\n"
            f"[*] Numara             : {data.get('number')}\n"
            f"[*] Yerel Format       : {data.get('local_format')}\n"
            f"[*] Uluslararası       : {data.get('international_format')}\n"
            f"[*] Ülke Kodu          : {data.get('country_prefix')}\n"
            f"[*] Ülke ISO           : {data.get('country_code')}\n"
            f"[*] Ülke Adı           : {data.get('country_name')}\n"
            f"[*] Konum              : {data.get('location')}\n"
            f"[*] Operatör           : {data.get('carrier')}\n"
            f"[*] Hat Türü           : {data.get('line_type')}"
        )
        result_textbox_phone.delete(1.0, ctk.END)
        result_textbox_phone.insert(1.0, phone_lookup_result)

    phone_label = ctk.CTkLabel(
        app,
        text="Telefon Numarası Araştırma",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    phone_label.pack()

    label_phone = ctk.CTkLabel(master=app, text="Telefon numarası : ")
    label_phone.pack()

    entry_phone = ctk.CTkEntry(master=app, width=200, height=10)
    entry_phone.pack()

    button_phone = ctk.CTkButton(master=app, text="Numara Bilgilerini Al", command=phone)
    button_phone.pack()

    label_phone2 = ctk.CTkLabel(master=app, text="Telefon Bilgi Çıktısı : ")
    label_phone2.pack()

    result_textbox_phone = ctk.CTkTextbox(app, height=150, width=3900)
    result_textbox_phone.pack()
    app.mainloop()


def dnsscan():
    ascii_art = '''
██▄      ▄      ▄▄▄▄▄       █    ████▄ ████▄ █  █▀  ▄   █ ▄▄  
█  █      █    █     ▀▄     █    █   █ █   █ █▄█     █  █   █ 
█   █ ██   █ ▄  ▀▀▀▀▄       █    █   █ █   █ █▀▄  █   █ █▀▀▀  
█  █  █ █  █  ▀▄▄▄▄▀        ███▄ ▀████ ▀████ █  █ █   █ █     
███▀  █  █ █                    ▀              █  █▄ ▄█  █    
      █   ██                                  ▀    ▀▀▀    ▀   
                                                            '''
    clear.clear()                                                      
    print(fade.greenblue(ascii_art))
    choice = input(Fore.LIGHTBLUE_EX+"DNS taraması yapılacak linki girin : ")
    api = "https://api.hackertarget.com/dnslookup/?q=" + choice
    res = requests.get(api)
    results = res.text
    print()
    print(results)
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    osintmenu()
    
    
    

def github_info():
    clear.clear()
    target = input(Fore.LIGHTBLUE_EX+"GitHub kullanıcı adını girin --> ")
    res = requests.get(f"https://api.github.com/users/{target}")
    data = res.json()
    name = f"{data.get('login', 'N/A')}"
    idd = f"{data.get('id', 'N/A')}"
    avatar_url = f"{data.get('avatar_url', 'N/A')}"
    bio = f"{data.get('bio', 'N/A')}"
    location = f"{data.get('location', 'N/A')}"
    public_repos = f"{data.get('public_repos', 'N/A')}"
    twitter_username = f"{data.get('twitter_username', 'N/A')}"
    followers = f"{data.get('followers', 'N/A')}"
    following = f"{data.get('following', 'N/A')}"
    print()
    print(Fore.LIGHTBLUE_EX+f"""
╠══════════════ GITHUB KULLANICI BİLGİLERİ ══════════════╣
║ Kullanıcı Adı   : {name}
║ ID              : {idd}
║ Avatar URL      : {avatar_url}
║ Biyografi       : {bio}
║ Konum           : {location}
║ Repolar         : {public_repos}
║ Twitter         : {twitter_username}
║ Takipçi         : {followers}
║ Takip Edilen    : {following}
╚══════════════════════════════════════════════╝
  """)
    print()
    input("Menüye dönmek için enter'a basın...")
    clear.clear()
    osintmenu()
    


main()