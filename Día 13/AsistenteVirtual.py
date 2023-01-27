import pyttsx3, speech_recognition as sr, pywhatkit, yfinance as yf, pyjokes

import webbrowser, datetime, wikipedia


## TRANSFORMAR AUDIO DEL MICROFONO EN TEXTO
def transformAudioText():
    ## Recognizer en variable
    r = sr.Recognizer()

    ## Configurar el micrófono
    with sr.Microphone() as origen:
        ## Tiempo de espera para la activación de micrófono
        r.pause_threshold = 0.8

        ## Informar que se comenzó la grabación
        print("Ya puedes hablar")

        ## Guardar lo que se escucha como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language = "es-per")

            # Prueba de texto
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido
        
        ## Si no comprende el audio
        except sr.UnknownValueError:

            # Prueba de que no se comprendió el audio
            print("Oops, no entendí")

            # Devolver error
            return "Sigo esperando"
        
        ## En caso de no resolver el pedido
        except sr.RequestError:
            # Prueba de que no se comprendió el audio
            print("Oops, no hay servicio")

            # Devolver error
            return "Sigo esperando"
        
        ## Errores inesperados
        except:
            # Prueba de que no se comprendió el audio
            print("Oops, algo ha salido mal")

            # Devolver error
            return "Sigo esperando"

## TRANSFORMAR TEXTO A VOZ
def asistenteHablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    ## Pronunciar Mensaje
    engine.say(mensaje)
    engine.runAndWait()

## INFORMAR EL DÍA DE LA SEMANA():
def pedirDia():
    ## Variable con la fecha actual
    dia = datetime.date.today()
    print(dia)

    ## Variable para el dia de la semana
    diaSemana = dia.weekday()
    print(diaSemana)

    ## Diccionario conteniendo los nombres de los días
    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}

    ## Decir el día de la semana
    asistenteHablar(f'Hoy es {calendario[diaSemana]}')

## INFORMAR LA HORA ACTUAL
def pedirHora():
    ## Variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento, son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    
    asistenteHablar(hora)

def saludoInicial():
    ## Crear variable con datos de hora

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'



    ## Decir el saludo
    asistenteHablar(f'{momento}, Hola, soy Mariell, tu asistente personal. ¿En qué puedo ayudarte?')

## FUNCION PRINCIPAL DEL ASISTENTE
def centroPedidos():
    # Activar saludo
    saludoInicial()

    # Variable iterable
    comenzar = True

    # Loop central
    while(comenzar):
        # Activar el micro y guardar el pedido en un string
        pedido = transformAudioText().lower()

        if 'abrir youtube' in pedido:
            asistenteHablar('Con gusto, estoy abriendo Youtube')
            # Abrir youtube
            webbrowser.open('https://youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            asistenteHablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        
        elif 'qué día es hoy' in pedido:
            pedirDia()
            continue

        elif 'qué hora es' in pedido:
            pedirHora()
            continue

        elif 'busca en wikipedia' in pedido:
            asistenteHablar('Buscando pedido en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            # Establecer wikipedia en español
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 1)
            asistenteHablar('Wikipedia dice lo siguiente:')
            asistenteHablar(resultado)
            continue

        elif 'busca en internet' in pedido:
            asistenteHablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            asistenteHablar('Esto es lo que he encontrado')
            continue
        
        elif 'reproducir' in pedido:
            asistenteHablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            asistenteHablar(pyjokes.get_joke('es'))

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip() # strip sirve para eliminar los espacios en blanco
            cartera = {'apple': 'APPL', 
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            
            try:
                accionBuscada = cartera[accion]
                accionBuscada = yf.Ticker(accionBuscada)
                precioActual = accionBuscada.info['regularMarketPrice']
                asistenteHablar(f'La encontré, el precio de {accion} es {precioActual}')
                continue
            except:
                asistenteHablar('Perdón, pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            asistenteHablar('Me voy a descansar, cualquier cosa me avisas')
            break       
# transformAudioText()
# pedirDia()
# pedirHora()
# saludoInicial()
centroPedidos()