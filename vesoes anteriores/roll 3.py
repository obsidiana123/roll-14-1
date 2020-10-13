# coding=UTF-8
import fala
import modifique_a_pergunta
import escute
import dicionario
import linux


    
fala.fala("sistema funcionando")

while True:

    conversa = dicionario.leia_dicionario()

    pergunta=escute.escute()        
    verifica= pergunta in conversa
    if(verifica == True):
        fala.fala(conversa[pergunta])
            
##############comandos especificos#############################################

    if(pergunta == "modificar resposta" ):
        modifique_a_pergunta.modifique()          
        verifica = True  ### para continuar codigo

    if(pergunta == "não escutei nada" ):
        #não fazer nada          
        verifica = True  ### para continuar codigo

    if(pergunta == "desligar sistema" ):
        fala.fala("desligando o sistema")
        linux.desligar()         
        verifica = True  ### para continuar codigo    

    if(pergunta == "reiniciar sistema" ):
        fala.fala("reiniciando sistema")
        linux.reiniciar()
        verifica = True  ### para continuar codigo          

        
##########################################################################################
            

##################não sei responder isto ###################################           
    if(verifica == False): # se o item digitado não esta contido no item executa o codigo abaixo
        fala.fala("ainda não posso responder isto,  o que devia responder")

        escuta2 = escute.escute()
        
        if(escuta2 == 'nada'):
            fala.fala("ok")
        else:         
            conversa[pergunta] = escuta2
            dicionario.escreva_dicionario(conversa)
          

############################################################################             
