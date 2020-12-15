import sys#necessario no python
alphabet = {'A' : 2, 'B' : 3, 'C' : 4, 'D' : 5, 'E' : 6,'F' : 7, 'G' : 8, 'H' : 9, 'I' : 10, 'J' : 11, 'K' : 12, 'L' : 13, 'M' : 14, 'N' : 15, 'O' : 16, 'P' : 17, 'Q' : 18, 'R' : 19, 'S' : 20, 'T' : 21, 'U' : 22, 'V' : 23, 'W' : 24, 'X' : 25, 'Y' : 26, 'Z' : 27, ' ' : 28}
#Alfabeto para transformar


def creatarqkey(n,e,p,q):#criando a chave publuica
    try:
        file = open("Keypublic.txt","w")#criando o arquivo da chave publica
        file.write(str(n))#escrevendo o numero n
        file.write(" ")
        file.write(str(e))#escrevendo o numero e
        file.close()
    except FileNotFoundError:#caso não consiga
        print("Erro ao criar arquivo")


def prime(x):#Dizer se é primo ou não
    tot = 0
    for num in range(1,x+1):
        if x % num == 0:
            tot = tot + 1


    if(tot > 2):
        return 0#nao primo
    else:
        return 1#primo




def mdc(a,b):#funcao para calcular MDC maneira euclidiana

    if(a%b == 0):
        return b
    else:
        mdc(b,a%b)

def find_d(z,e,d):#função para encotrar o d
#lembrando que d*e mod z(função totiente) = 1
    i = 1
    for i in range(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        if(i*e % z == 1):
            d = i
            return d
            break


#'''
def cript(msg,k1,k2):#função para gerar o arquivo criptografado
    tamanho = len(msg)#tamanho da mensagem
    criptmsg = ""#iniciando com nada uma variavel para receber a mensagem criptografada
    for i in range(tamanho):#loop para ir do 0 até tamanho da mensagem
        arr = msg[i]#variavel para receber cada letra
        criptmsg += str(pow(alphabet[arr],k2,k1))#transformação das letras pro numero criptografado
        if(i + 1 < tamanho):
            criptmsg += ' '#separar para saber quem é quem
    try:
        x = criptmsg#numero criptografado
        cript_file = open("Encripttext.txt","w")#criação do arquivo de criptografia
        cript_file.write(criptmsg)#arquivo com os numeros da criptografia
        cript_file.close()

        return x
    except FileNotFoundError:
        print("Não foi gerado o arquivo")
        return -1
        #'''
def descript(msg2,k1,k2):#função para gerar arquivo descriptografado
    reverse_alfa = dict(map(reversed,alphabet.items()))
    #reverse_alfa = dict(map(reversed, alfa.items())) #trocando chave por valor
    descriptmsg = ""
    i = 0
    side = len(msg2)
    while i < side:
         aux = ""
         while i < side and msg2[i] != ' ':
             aux += msg2[i]
             i = i + 1
         i = i + 1
         aux = int (aux)
         descriptmsg += reverse_alfa[pow(aux,k1,k2)]
         #descriptmsg
    try:
        file = open("Decriptxt.txt","w")
        file.write(descriptmsg)
        file.close()
    except FileNotFoundError:
        print("Não foi possivel criar o arquivo descriptografado, tente novamente")



def key():#funcao de criação da chave
    #a chave publica é o par (n,e)
    #Pedido ao usuario os numeros "p","q" e o numero "e" para gerar a chave
    print("Digite o numero p")
    p = int(input())
    print("Digite o numeor q")
    q = int(input())
    print("Digite o Numero e")
    e = int(input())
    n = p*q#criação do numero "n" necessario para criar a chave
    z = (p-1)*(q-1)#função totiente a n
    d = find_d(z,e,0)#função que criar o numero d , necessario na descriptrografia e na criação da chave

    if prime(p) == 0 or prime(q) == 0:#Checando se os dois numeros são primos
        print("Um dos numeros digitados não é primo")
    elif n < 26:#checando se o n é maior que 26
        print("O N tem que ser maior que 26")
    elif mdc((p-1)*(q-1),e) ==1:#checando se o e é coprimo a função totiente
        print("O e não é coprimo")
    elif(find_d(z,e,0))!= d:#checando o numero d
        print("d não encontrado")
    else:
        creatarqkey(n,e,p,q)#função para criar a chave
        print("Chave publica gerada com sucesso")



def init_cript():#função que chama a criptografia
    print("Digite a mensagem de texto a Encriptar")
    msg = input()
    print("Digite o primeiro numero do par da chave recebido anteriormente")
    k1 = int(input())
    print("Digite o segundo numero do par da chave recebido anteriormente")
    k2 = int(input())
    if(cript(msg,k1,k2)!=-1):
        print("Ok")



def init_descript():#função que chama para descriptografar
    print("Digite o numero p")
    p = int(input())
    print("Digite o numeor q")
    q = int(input())
    print("Digite o Numero e")
    e = int(input())
    n = p*q
    z = (p-1)*(q-1)
    d = find_d(z,e,0)
    try:
        file = open("Encripttext.txt","r")
        cryptMsg = file.read()
        file.close()
        descript(cryptMsg,d,n)
        print("successfully decrypted")
    except FileNotFoundError:
        print("Fail")





def main():#Função Principal onde se faz a escolha do que o Usuario necessita
    print("Digite um numero sobre o que vc deseja: 1-Gerar chave 2-Encriptar mensagem 3-Desencriptar")
    x = int(input())#receber o numero que deseja
    if(x == 1):#Criar a chave publica
        key()
    elif(x == 2):
        init_cript()#Criptografar
    elif(x == 3):
        init_descript()#Descriptografar
main()
