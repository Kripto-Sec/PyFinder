import requests
import json
import sys, os


def domain_search():
    domain()
    print("\n")
    print('\033[1;96m'+"A pesquisa de domínio lista todas as pessoas que trabalham em uma empresa com seus nomes e endereços de e-mail encontrados na web.")
    print("\n")
    print("[00] Voltar ao Menu")
    print("[99] Sair"+'\033[0;0m')
    domin = input('\033[1;31m'+"Dominio > "+'\033[0;0m')
    
    if domin == '00' or domin == '0':
        os.system('clear')
        menu()
    elif domin == '99' or domin == '9':
        sys.exit()
    else:    
        
        key_da_api = input('\033[1;35m'+"Insira sua KEY API > "+'\033[0;0m')
        try:
            req = requests.get('https://api.hunter.io/v2/domain-search?domain={}&api_key={}'.format(domin, key_da_api))
            
            dicio = json.loads(req.text)
            os.system('clear')
            domain()
            print("\n")
            print('\033[1;92m'+"-----------------------------------------------------------")
            print("---             INFORMAÇÕES DE DOMÍNIO                  ---")
            print("-----------------------------------------------------------"+'\033[0;0m')
            print('\033[1;33m'+'Dominio: {}'.format(dicio["data"]["domain"]))
            print('Disponibilidade: {}'.format(dicio["data"]["disposable"]))
            print('Webmail: {}'.format(dicio["data"]["webmail"]))
            print('organização: {}'.format(dicio["data"]["organization"]))
            print('Pais: {}'.format(dicio["data"]["country"]))
            print('Estado: {}'.format(dicio["data"]["state"]))
            print('\033[1;92m'+"-----------------------------------------------------------")
            print('---               E-MAILS ENCONTRADOS                   ---')
            print('-----------------------------------------------------------''\033[0;0m')
            for mail in range(0, 10):
                print('\033[1;33m'+'Email: {}'.format(dicio["data"]["emails"][mail]['value']))
                print('Tipo: {}'.format(dicio["data"]["emails"][mail]["type"]))
                print("Twitter: {}".format(dicio["data"]["emails"][mail]["twitter"]))
                print("--------------------------------------------------------------")
            #print('Tipo: {}'.format(dicio["emails"]["value"]))


        except KeyError:
            print("Erro Verifique o dominio inserido ou a API")
        

def email_finder():
    finder()

    print('\033[1;96m'+"Encontre os endereços de e-mail das pessoas com as quais deseja entrar em contato")
    print("\n")
    print("[00] Voltar ao menu")
    print("[99] Sair"+'\033[0;0m')
    dom_name = input('\033[1;31m'+"Nome do dominio: "+'\033[0;0m')
    p_name = input('\033[1;31m'+"Primeiro Nome: "+'\033[0;0m')
    u_name = input('\033[1;31m'+"Ultimo Nome: "+'\033[0;0m')
    
    
    
    if dom_name == '00' or dom_name == '0':
        os.system('clear')
        menu()
    elif dom_name == '99' or dom_name == '9':
        sys.exit()
    else:
        key_da_api = input('\033[1;35m'+"Insira sua KEY API > "+'\033[0;0m')
        try:
            req = requests.get('https://api.hunter.io/v2/email-finder?domain={}&first_name={}&last_name={}&api_key={}'.format(dom_name, p_name, u_name, key_da_api))

            dicio = json.loads(req.text)
            os.system('clear')
            print("\n")
            print('\033[1;33m'+'Primeiro Nome: {}'.format(dicio["data"]["first_name"]))
            print('Ultimo Nome: {}'.format(dicio["data"]["last_name"]))
            print('Email: {}'.format(dicio["data"]["email"]))
            print('Cargo: {}'.format(dicio["data"]["position"]))
            print('Twitter: {}'.format(dicio["data"]["twitter"]))
            print('Linkedin: {}'.format(dicio["data"]["linkedin_url"]))
            print('Telefone: {}'.format(dicio["data"]["phone_number"]))
            print("\n")
        except KeyError:
            print("Email Nao encontrado")

def email_verifier():
    email_verifierBanner()

    print("\n")
    print('\033[1;96m'+"Faz uma verificação no e-mail para testar se e valido")
    print("\n")
    print("[00] Para voltar ao menu")
    print("[99] Para sair"+'\033[0;0m')
    print("\n")
    domi = input('\033[1;31m'+'Digite o email para verificar > '+'\033[0;0m')
    



    if domi == '00' or domi == '0':
        os.system('clear')
        menu()
    elif domi == '99' or domi == '9':
        sys.exit()
    else:
        key_da_api = input('\033[1;35m'+"Insira sua KEY API > "+'\033[0;0m')

        try:
            req = requests.get('https://api.hunter.io/v2/email-verifier?email={}&api_key={}'.format(domi, key_da_api))

            dicio = json.loads(req.text)
            os.system('clear')
            print("\n")
            print('\033[1;33m'+'Email: {}'.format(dicio["data"]["email"]))
            print('Status: {}'.format(dicio["data"]["status"]))
            print('Resultado: {}'.format(dicio["data"]["result"]))
            print('Servidor SMTP: {}'.format(dicio["data"]["smtp_server"]))
            
        except KeyError:
            print('\033[1;31m'+"Email Nao encontrado"+'\033[0;0m')


def banner():
    print('\033[1;97m' + "L D F G R A W V R H W S B S K L T")
    print("E J W V " '\033[1;32m' + "P Y F I N D E R " '\033[37m'+"W Q J Z O")
    print('\033[1;97m' + "K A Y U S D G P Y I B F H D I K F" + '\033[0;0m')

def email_verifierBanner():
    print('\033[1;97m' + "L D F G R A W V R H W S B S K L T")
    print("E J W V " '\033[1;32m' + "V E R I F I E R " '\033[37m'+"W Q J Z O")
    print('\033[1;97m' + "K A Y U S D G P Y I B F H D I K F" + '\033[0;0m')


def finder():
    print('\033[1;97m' + "L D F G R A W V R H W S B S K L T")
    print("E J W V " '\033[1;32m' + "F I N D E R " '\033[37m'+"W Q J Z O G Z")
    print('\033[1;97m' + "K A Y U S D G P Y I B F H D I K F" + '\033[0;0m')


def domain():
    print('\033[1;97m' + "L D F G R A W V R H W S B S K L T")
    print("E J W V " '\033[1;32m' + "D O M A I N " '\033[37m'+"W Q J Z O F V")
    print('\033[1;97m' + "K A Y U S D G P Y I B F H D I K F" + '\033[0;0m')

def menu():
    os.system('clear')
    banner()
    print("\n")
    print('\033[1;96m'+"Oque deseja fazer? ")
    print("\n")
    print("Escolha uma ferramenta para usa-la")
    print("E saber mais sobre")
    print("\n")
    print("[01] VERIFICADOR DE EMAIL")
    print("[02] EMAIL FINDER")
    print("[03] PESQUISA DE DOMÍNIO")
    print("\n")
    print("[00] Sair")


    escolha = input('\033[1;31m'+"Finder > "+'\033[0;0m')
   
    os.system('clear')
       

    while True:
        
        if escolha == '0' or escolha == '00':
            sys.exit()
            
        elif escolha == '1' or escolha == '01': 
            email_verifier()
            
        elif escolha == '2' or escolha == '02':
            email_finder()
        
        elif escolha == '3' or escolha == '02':
            domain_search()
        else:           
            
            menu()
menu()       
        

    

