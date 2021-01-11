#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import sys, os
import time

import core

from core.banner import *

def Register_key():
   
    Rkey = input("Digite sua Key >> ")
    
    
    with open('core/Saved_key', 'w') as arq:
       
        Fkey = arq.write(Rkey)
        
    print("Key salva com sucesso")
    time.sleep(1)
    menu()


def AccInfo():

    if os.path.exists('core/Saved_key'):

        try:
            arq = open('core/Saved_key', 'r')
            key = arq.read()
            arq.close()

            
            req = requests.get('https://api.hunter.io/v2/account?api_key={}'.format(key))
            dicio = json.loads(req.text)

            accinfo()
            print('\033[1;97m'+"Primeiro Nome: {}".format(dicio["data"]["first_name"]))
            print("Ultimo nome: {}".format(dicio["data"]["last_name"]))
            print("Email: {}".format(dicio["data"]["email"]))
            print("Nome do plano: {}".format(dicio["data"]["plan_level"]))
            print("Nivel do plano: {}".format(dicio["data"]["plan_level"]))
            print("Data de Reset: {}".format(dicio["data"]["reset_date"]))
            print("\n")
            print("[00] Voltar ao menu")
            print("[99] Sair")
            print("\n")
            esc = input("FINDER >> ")

            if esc == '00' or esc == '0':
                menu()
            elif esc == '99' or esc == '9':
                sys.exit()

            else:
                print("comando invalido")
        
        except KeyError:
            print("Erro Verifique a sua KEY API")
            time.sleep(2)
            menu()

    else:
        print('\033[1;31m'+"Voce nao salvou sua key api")
        time.sleep(1)
        Register_key()
  

def domain_search():

    if os.path.exists('core/Saved_key'):    


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
            arq = open('core/Saved_key','r')
            key = arq.read()
            arq.close()
            
            try:
                req = requests.get('https://api.hunter.io/v2/domain-search?domain={}&api_key={}'.format(domin, key))
                
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

                req2 = requests.get('https://api.hunter.io/v2/email-count?domain={}'.format(domin))
                dicio2 = json.loads(req2.text)
                quant = dicio2["data"]["total"]
                    
                print('\033[1;92m'+'-----------------------------------------------------------')
                print('---                TIPOS DE E-MAILS                    ---')
                print('-----------------------------------------------------------''\033[0;0m')

                print('\033[1;33m'+'Quantidade de e-mails: {}'.format(quant))
                print('\033[1;33m'+'E-mails pessoais:{}'.format(dicio2["data"]["personal_emails"]))
                print('\033[1;33m'+'E-mails genericos: {}'.format(dicio2["data"]["generic_emails"]))
                

                    
                print('\033[1;92m'+"-----------------------------------------------------------")
                print('---               E-MAILS ENCONTRADOS                   ---')
                print('-----------------------------------------------------------''\033[0;0m')


                for mail in range(0, quant):
                
        
                    print('\033[1;33m'+'Email: {}'.format(dicio["data"]["emails"][mail]['value']))
                    print('Tipo: {}'.format(dicio["data"]["emails"][mail]["type"]))
                    print("Twitter: {}".format(dicio["data"]["emails"][mail]["twitter"]))
                    print("--------------------------------------------------------------")
                    time.sleep(1)

                    #print('Tipo: {}'.format(dicio["emails"]["value"]))


            except KeyError:
                    print("Erro Verifique o dominio inserido ou a Key")


    else:
        print('\033[1;31m'+"Voce nao salvou sua key api")
        time.sleep(1)
        Register_key()


def email_finder():

    if os.path.exists('core/Saved_key'):


        finder()

        print('\033[1;96m'+"Encontre os endereços de e-mail das pessoas com as quais deseja entrar em contato")
        print("Apenas com o nome, sobrenome E dominio")
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
            arq = open('core/Saved_key','r')
            key = arq.read()
            arq.close()
        
            try:
                req = requests.get('https://api.hunter.io/v2/email-finder?domain={}&first_name={}&last_name={}&api_key={}'.format(dom_name, p_name, u_name, key))

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

    else:
        print('\033[1;31m'+"Voce nao salvou sua key api")
        time.sleep(1)
        Register_key()


def email_verifier():

    if os.path.exists('core/Saved_key'):


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
            arq = open('core/Saved_key','r')
            key = arq.read()
            arq.close()

            try:
                req = requests.get('https://api.hunter.io/v2/email-verifier?email={}&api_key={}'.format(domi, key))

                dicio = json.loads(req.text)
                os.system('clear')
                print("\n")
                print('\033[1;33m'+'Email: {}'.format(dicio["data"]["email"]))
                print('Status: {}'.format(dicio["data"]["status"]))
                print('Resultado: {}'.format(dicio["data"]["result"]))
                print('Servidor SMTP: {}'.format(dicio["data"]["smtp_server"]))
                
            except KeyError:
                print('\033[1;31m'+"Email Nao encontrado"+'\033[0;0m')
    else:
        print('\033[1;31m'+"Voce nao salvou sua key api")
        time.sleep(1)
        Register_key()



def menu():
    os.system('clear')
    banner()
    print("\n")
    print('\033[1;96m'+"Oque deseja fazer?")
    print("\n")
    print("Escolha uma ferramenta para usa-la")
    print("E saber mais sobre")
    print("\n")
    print("[01] EMAIL VERIFIER")
    print("[02] EMAIL FINDER")
    print("[03] DOMAIN SEARCH")
    print("[04] SAVE NEW KEY ")
    print("\n")
    print("[05] INFORMAÇÕES DA CONTA")
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

        elif escolha == '4' or escolha == '04':
            Register_key()
        
        elif escolha == '5' or escolha == '05':
            AccInfo()
        else:           
            
            menu()

if __name__ == "__main__":
    menu()
     
        

    

