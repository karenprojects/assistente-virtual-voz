import pyttsx3 #Biblioteca para converter texto em fala tem uma voz fem e outra masc
import datetime #Biblioteca para falar de tempo - data e hora
import speech_recognition as sr

texto_fala = pyttsx3.init() #Inicializar

#Função falar
def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate",250 ) #Altera a velocidade da fala
    voices = texto_fala.getProperty('voices') #Chamar uma propiedade atraves da variavel
    texto_fala.setProperty('voice', voices[0].id) #Alteração da voz
    texto_fala.say(audio) #Funçaõr responsavel para converter texto em fala
    texto_fala.runAndWait() #Chama a função


def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M:")#Converte tempo em propiedades necessarias de horas 
    falar("Agora são:")
    falar(Tempo)

def data():
    ano = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = int(datetime.datetime.now().day)
    falar("A data atual é")
    falar(dia)
    falar("do" + mes + "de")
    falar(ano)


def bem_vindo():
    falar("Olá mestre, seja bem vindo de volta!")
    #tempo()
    #data()

    hora = datetime.datetime.now().hour

    if hora >= 5 and hora <12:
        falar("Bom dia mestre!")
    elif  hora >= 12 and hora <18:
        falar("Boa tarde mestre!")
    elif hora >=18 and hora >24:
        falar("Boa noite mestre!")
    else:
        falar("Boa madrugada mestre!")

    falar("Yasmin a sua disposição como posso ajudar?")

#bem_vindo()

#Reconhecimento de fala
def microfone():
    r = sr.Recognizer() #Reconhececendo microfone

    with sr.Microphone() as source:
         r.pause_threshold = 1 # Uma pasua toda vez que o kicrofone receber uma informação
         audio = r.listen(source)

    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio, language = 'pt-BR')

        print(comando)
    
    except Exception as e:
        print(e) #Mostra o erro caso de.
        falar("Por favor repita")
        return "None"
    
    return comando


#Função Principal/ responsavel por introduzir todos os comandos

if __name__ == "__main__":
    bem_vindo()

    while True:
        print("Escutando...")
        comando = microfone().lower()

#Primeiros comandos
    #Caso ache a palavra hora le exceculta o segundo comando; pode trocar a palvra apenas deixe entre as ''
        if 'como você esta' in comando:
            falar("Estou bem! Obrigada por perguntar")
            falar("O que posso te ajudar?")
       
        elif 'hora' in comando:
            tempo()
            
        elif 'data' in comando:
            data()
  

