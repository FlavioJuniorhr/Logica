import os                                                    # importação 

if not os.path.isfile('arquivo1.txt'):                       # confirmação do arquivo
    arquivo = open("arquivo1.txt", "w")
    dados_total = []
    arquivo.write("%s" %dados_total)
    arquivo.close()
else :
    arquivo = open("arquivo1.txt", "r")
    arquivo.close()

def enviarDados(dados):                                      # funções
    arquivo = open("arquivo1.txt", "w+")
    arquivo.write("%s" %dados)
    arquivo.close()
def lerDados():
    arquivo = open("arquivo1.txt", "r")
    return eval(arquivo.read())
dados_total = lerDados()                                    # variaveis
nome, cpf, end, tele, email, senha = ("", "", "", "", "", "")

while True :
    print('========================MENU DE CADASTRO========================')
    print('1-Cadastro')
    print('2-Ler')
    print('3-Deletar')
    print('4-Atualizar')
    print('5-Sair')
    a = int(input("opção: "))
    if a == 1 :                                             # cadastro
        if (len(dados_total) <= 4) and (len(dados_total) >= 0):                          # limitação
            arquivo = open("arquivo1.txt", "w+")
            nome = input('Nome: ')
            cpf = input('Cpf: ')
            end = input("Endereço: ")
            tele = input("Telefone: ")
            email = input("Email: ")
            senha = input("Senha: ")
            dados_total.append([nome, cpf, end, tele, email, senha])
            enviarDados(dados_total)
        else :
            print('limite de cadastro estourado')
    elif a == 2 :
        x = 1
        if (len(dados_total) <= 5) and (len(dados_total) >= 1):
            print("========================DADOS ATUAIS========================")
            for el in dados_total:
                print('Cadastro %s'%x)
                print("Nome: ", el[0])
                print("CPF: ", el[1])
                print("ENDEREÇO: ", el[2])
                print("TELEFONE: ", el[3])
                print("EMAIL: ", el[4])
                print("SENHA: ", el[5])
                print("\n")
                x=x + 1
        else :
        	print('Sistema sem cadastro')
    elif a == 3 :
        if (len(dados_total) >= 0):
            print('Nenhum Cadastro')
        else :
            if (len(dados_total) >= 1):
                print('1 - Cadastro 1')
            if (len(dados_total) >= 2):
               print('2 - Cadastro 2')
            if (len(dados_total) >= 3):
                print('3 - Cadastro 3')
            if (len(dados_total) >= 4):
                print('4 - Cadastro 4')
            if (len(dados_total) >= 5):
                print('5 - Cadastro 5')
            if (len(dados_total) >= 1):
                print('0 - Todos os Cadastros')
            esc = int (input("Qual dado você deseja deletar: "))
            if esc == 1:
                dados_total.pop(0)
                enviarDados(dados_total)
            if esc == 2:
                dados_total.pop(1)
                enviarDados(dados_total)
            if esc == 3:
                dados_total.pop(2)
                enviarDados(dados_total)
            if esc == 4:
                dados_total.pop(3)
                enviarDados(dados_total)
            if esc == 5:
                dados_total.pop(4)
                enviarDados(dados_total)
            if esc == 0:
                if (len(dados_total) == 1) :
                    dados_total.pop(0)
                    enviarDados(dados_total)
                if (len(dados_total) == 2) :
                    dados_total.pop(1)
                    enviarDados(dados_total)
                    dados_total.pop(0)
                    enviarDados(dados_total)
                if (len(dados_total) == 3) :
                    dados_total.pop(2)
                    enviarDados(dados_total)
                    dados_total.pop(1)
                    enviarDados(dados_total)
                    dados_total.pop(0)
                    enviarDados(dados_total)
                if (len(dados_total) == 4) :
                    dados_total.pop(3)
                    enviarDados(dados_total)
                    dados_total.pop(2)
                    enviarDados(dados_total)
                    dados_total.pop(1)
                    enviarDados(dados_total)
                    dados_total.pop(0)
                    enviarDados(dados_total)
                if (len(dados_total) == 5) :
                    dados_total.pop(4)
                    enviarDados(dados_total)
                    dados_total.pop(3)
                    enviarDados(dados_total)
                    dados_total.pop(2)
                    enviarDados(dados_total)
                    dados_total.pop(1)
                    enviarDados(dados_total)
                    dados_total.pop(0)
                    enviarDados(dados_total)
    elif a == 4 :
        if (len(dados_total) >= 1):
            print('1 - Cadastro 1')
        if (len(dados_total) >= 2):
            print('2 - Cadastro 2')
        if (len(dados_total) >= 3):
            print('3 - Cadastro 3')
        if (len(dados_total) >= 4):
            print('4 - Cadastro 4')
        if (len(dados_total) >= 5):
            print('5 - Cadastro 5')
        ec = int (input("Qual dado você deseja atualizar: "))
        if ec == 1:
            print('1 - Nome')
            print('2 - Cpf')
            print('3 - Endereço')
            print('4 - Telefone')
            print('5 - Email')
            print('6 - Senha')
            print('7 - todos')
            esc = int(input('Sua opção :'))
            if esc == 1 :
                nome = input('Nome: ')
                dados_total[0][0]=nome
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 2 :
                cpf = input('Cpf: ')
                dados_total[0][1]=cpf
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 3 :
                end = input("Endereço: ")
                dados_total[0][2]=end
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 4 :
                tele = input("Telefone: ")
                dados_total[0][3]=tele
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 5 :
                email = input("Email: ")
                dados_total[0][4]=email
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 6 :
                senha = input("Senha: ")
                dados_total[0][5]=senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 7 :
                nome = input('Nome: ')
                cpf = input('Cpf: ')
                end = input("Endereço: ")
                tele = input("Telefone: ")
                email = input("Email: ")
                senha = input("Senha: ")
                dados_total[0]=nome,cpf,end,tele,email,senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
        if ec == 2:
            print('1 - Nome')
            print('2 - Cpf')
            print('3 - Endereço')
            print('4 - Telefone')
            print('5 - Email')
            print('6 - Senha')
            print('7 - todos')
            esc = int(input('Sua opção :'))
            if esc == 1 :
                nome = input('Nome: ')
                dados_total[1][0]=nome
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 2 :
                cpf = input('Cpf: ')
                dados_total[1][1]=cpf
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 3 :
                end = input("Endereço: ")
                dados_total[1][2]=end
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 4 :
                tele = input("Telefone: ")
                dados_total[1][3]=tele
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 5 :
                email = input("Email: ")
                dados_total[1][4]=email
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 6 :
                senha = input("Senha: ")
                dados_total[1][5]=senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 7 :
                nome = input('Nome: ')
                cpf = input('Cpf: ')
                end = input("Endereço: ")
                tele = input("Telefone: ")
                email = input("Email: ")
                senha = input("Senha: ")
                dados_total[1]=nome,cpf,end,tele,email,senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
        if ec == 3:
            print('1 - Nome')
            print('2 - Cpf')
            print('3 - Endereço')
            print('4 - Telefone')
            print('5 - Email')
            print('6 - Senha')
            print('7 - todos')
            esc = int(input('Sua opção :'))
            if esc == 1 :
                nome = input('Nome: ')
                dados_total[2][0]=nome
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 2 :
                cpf = input('Cpf: ')
                dados_total[2][1]=cpf
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 3 :
                end = input("Endereço: ")
                dados_total[2][2]=end
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 4 :
                tele = input("Telefone: ")
                dados_total[2][3]=tele
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 5 :
                email = input("Email: ")
                dados_total[2][4]=email
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 6 :
                senha = input("Senha: ")
                dados_total[2][5]=senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 7 :
                nome = input('Nome: ')
                cpf = input('Cpf: ')
                end = input("Endereço: ")
                tele = input("Telefone: ")
                email = input("Email: ")
                senha = input("Senha: ")
                dados_total[2]=nome,cpf,end,tele,email,senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
        if ec == 4:
            print('1 - Nome')
            print('2 - Cpf')
            print('3 - Endereço')
            print('4 - Telefone')
            print('5 - Email')
            print('6 - Senha')
            print('7 - todos')
            esc = int(input('Sua opção :'))
            if esc == 1 :
                nome = input('Nome: ')
                dados_total[3][0]=nome
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 2 :
                cpf = input('Cpf: ')
                dados_total[3][1]=cpf
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 3 :
                end = input("Endereço: ")
                dados_total[3][2]=end
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 4 :
                tele = input("Telefone: ")
                dados_total[3][3]=tele
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 5 :
                email = input("Email: ")
                dados_total[3][4]=email
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 6 :
                senha = input("Senha: ")
                dados_total[3][5]=senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 7 :
                nome = input('Nome: ')
                cpf = input('Cpf: ')
                end = input("Endereço: ")
                tele = input("Telefone: ")
                email = input("Email: ")
                senha = input("Senha: ")
                dados_total[3]=nome,cpf,end,tele,email,senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
        if ec == 5:
            print('1 - Nome')
            print('2 - Cpf')
            print('3 - Endereço')
            print('4 - Telefone')
            print('5 - Email')
            print('6 - Senha')
            print('7 - todos')
            esc = int(input('Sua opção :'))
            if esc == 1 :
                nome = input('Nome: ')
                dados_total[4][0]=nome
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 2 :
                cpf = input('Cpf: ')
                dados_total[4][1]=cpf
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 3 :
                end = input("Endereço: ")
                dados_total[4][2]=end
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 4 :
                tele = input("Telefone: ")
                dados_total[4][3]=tele
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 5 :
                email = input("Email: ")
                dados_total[4][4]=email
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 6 :
                senha = input("Senha: ")
                dados_total[4][5]=senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
            if esc == 7 :
                nome = input('Nome: ')
                cpf = input('Cpf: ')
                end = input("Endereço: ")
                tele = input("Telefone: ")
                email = input("Email: ")
                senha = input("Senha: ")
                dados_total[4]=nome,cpf,end,tele,email,senha
                arquivo=open("arquivo1.txt", "w")
                arquivo.writelines("%s"%dados_total)
                enviarDados(dados_total)
                arquivo.close
        else :
            print('Opção inválida')
    elif a == 5 :
        print('deseja fechar realmente o sistema')
        print('1-Sim')
        print('2-não')
        p = int(input('Sua opção :'))
        
        if p == 1:
            print('Fechando sistema')
            print('by : Júnior Hora e Paulo Henrique')
            quit()
        else :
            print('voltando ao menu:\n')
    else :
        print('opção inválida')