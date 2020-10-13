import pickle
from gtts import gTTS
import os
import speech_recognition as sr


# coding=UTF-8

r = sr.Recognizer()

AudioDoTexto = gTTS(text= "sistema funcionando", lang='pt')
AudioDoTexto.save("/tmp/audio.mp3")
os.system("mpg321 /tmp/audio.mp3")

conversa = {
    'oi':'eae',
    'Qual o seu nome?':'irineu, você não sabe e nem eu',
    'prazer em te conhecer':'Igualmente meu patrão',
    }


while True:
    print("iniciando gravação")
    os.system("arecord -d 4 -D dmic_sv -c2 -r 44100 -f S32_LE -t wav -V mono -v som.wav") 
    WAV_FILE = 'som.wav'
    
    with sr.WavFile(WAV_FILE) as source:
    
         
        audio = r.record(source)
    try:
        print("numero de itens:" + str(len(conversa))) # mostra a quantdade de ites na lista conversa

        arq = open('dialogo.txt','rb') #abrir o arquivo para leitura - o "b" significa que o arquivo é binário
        conversa = pickle.load(arq)#Ler a stream a partir do arquivo e reconstroi o objeto original.
        arq.close() #fechar o arquivo  
        #print (conversa) #imprime o conteúdo do dict

        
        escuta = r.recognize_google(audio, language="pt-BR")
        print(" Voce disse:" + escuta)
        pergunta=escuta
        
        verifica= pergunta in conversa
        if(verifica == True):
            print(conversa[pergunta])        
            AudioDoTexto = gTTS(text= conversa[pergunta], lang='pt')
            AudioDoTexto.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            
##############comandos especificos#############################################

        if(pergunta == "modifique a pergunta" ):
            print("qual pergunta deseja modificar")
            AudioDoTexto = gTTS(text= "qual pergunta deseja modificar", lang='pt')
            AudioDoTexto.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            print("iniciando gravação")
            os.system("arecord -d 4 -D dmic_sv -c2 -r 44100 -f S32_LE -t wav -V mono -v som.wav") 
            WAV_FILE = 'som.wav'
            with sr.WavFile(WAV_FILE) as source:
                pergunta3 = r.record(source)
            try:
                escuta3 = r.recognize_google(pergunta3, language="pt-BR")
                print(" Voce disse:" + escuta3)
                testo22 = conversa[escuta3]
                print("qual qual a nova resposta para  "+ escuta3 )
                AudioDoTexto = gTTS(text= "qual a nova resposta para "+ escuta3, lang='pt')
                AudioDoTexto.save("/tmp/audio.mp3")
                os.system("mpg321 /tmp/audio.mp3")
                print("iniciando gravação")
                os.system("arecord -d 4 -D dmic_sv -c2 -r 44100 -f S32_LE -t wav -V mono -v som.wav") 
                WAV_FILE = 'som.wav'
                with sr.WavFile(WAV_FILE) as source:
                    pergunta4 = r.record(source)
                try:
                    escuta4 = r.recognize_google(pergunta4, language="pt-BR")
                    print(" Voce disse:" + escuta4)
                    conversa[escuta3] = escuta4
                    arq = open('dialogo.txt','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
                    pickle.dump(conversa,arq) #Grava uma stream do objeto "dic" para o arquivo.
                    arq.close()
                    print(" resposta modificada")
                    
                except sr.UnknownValueError:
                    print("não entendi")
                except sr.RequestError as e:
                    print("erro ao chamar google speech; {0}".format(e))     

            except sr.UnknownValueError:
                print("não entendi")
        
        
            except sr.RequestError as e:
                print("erro ao chamar google speech; {0}".format(e))            
            
            verifica = True  ### para continuar codigo
##########################################################################################
            

##################não sei responder isto ###################################           
        if(verifica == False): # se o item digitado não esta contido no item executa o codigo abaixo

            AudioDoTexto = gTTS(text= "ainda não posso responder isto", lang='pt')
            AudioDoTexto.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            print("ainda não posso responder isto ")


            AudioDoTexto = gTTS(text= "o que devia responder", lang='pt')
            AudioDoTexto.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            print("o que devia responder")

            print("iniciando gravação")
            os.system("arecord -d 4 -D dmic_sv -c2 -r 44100 -f S32_LE -t wav -V mono -v som.wav") 
            WAV_FILE = 'som.wav'
            
            with sr.WavFile(WAV_FILE) as source:
                pergunta2 = r.record(source)
            try:
                escuta2 = r.recognize_google(pergunta2, language="pt-BR")
                print(" Voce disse:" + escuta2)

            except sr.UnknownValueError:
                print("nada arquivado")
        
        
            except sr.RequestError as e:
                print("erro ao chamar google speech; {0}".format(e))            
            

            pergunta2 = escuta2
                
            #pergunta2=input("o que devia responder") # le o que foi escrito
            if(pergunta2 == 'nada'):
                print('ok')
                AudioDoTexto = gTTS(text= "ok", lang='pt')
                AudioDoTexto.save("/tmp/audio.mp3")
                os.system("mpg321 /tmp/audio.mp3")

            else:         
                conversa[pergunta] = pergunta2
                arq = open('dialogo.txt','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
                pickle.dump(conversa,arq) #Grava uma stream do objeto "dic" para o arquivo.
                arq.close()

                
    except sr.UnknownValueError:
        print("Roll disse: Fale comigo")
        
        
    except sr.RequestError as e:
        print("erro ao chamar google speech; {0}".format(e))            
            
             
