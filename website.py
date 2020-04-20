import pygame               #importerar nödvändiga delar
pygame.init()

import paho.mqtt.client as mqtt
import time

display_width = 1100                #sätter hur bred/hög skärmen är
display_height = 600
display = pygame.display.set_mode((display_width, display_height))  #skapar skärmen

def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect (client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")                           #definerar dem här sakerna
    else:
        print("bad connection returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected result code " + str(rc))

def draw(Direction):
    display.fill((255, 255, 255))

    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 296, display_height/2 - 54, 200, 100))  
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 297, display_height/2 - 53, 200, 100)) # ritar buttons och gör bakgrunden vit
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 298, display_height/2 - 52, 200, 100)) # ritar också texten
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 299, display_height/2 - 51, 200, 100))
    pygame.draw.rect(display, (0, 255, 0), (display_width/2 - 300, display_height/2 - 50, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Forward', 1, (0,0,0))
    display.blit(text, (display_width/2 - 275, display_height/2 + 70))

    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 96, display_height/2 - 54, 200, 100))  
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 97, display_height/2 - 53, 200, 100))
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 98, display_height/2 - 52, 200, 100))
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 99, display_height/2 - 51, 200, 100))
    pygame.draw.rect(display, (255, 0, 0), (display_width/2 + 100, display_height/2 - 50, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Backward', 1, (0,0,0))
    display.blit(text, (display_width/2 + 115, display_height/2 + 70))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Direction: ' + Direction, 1, (0,0,0))
    display.blit(text, (20, 20))
    pygame.display.update()

port = 8883
broker = "maqiatto.com"
client =mqtt.Client("py1")      #username password och sånt
MQTT_USERNAME  = "carl.pettersson@abbindustrigymnasium.se"
MQTT_PASSWORD  = "Snuten12"


run = True

if run == True:
    Direction = "null"  #vad som står på direction
    draw(Direction)

while run:
    for event in pygame.event.get():  #gör så att man kan stänga programmet
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pos()   #får mus positionen
    click = pygame.mouse.get_pressed() #gör så att man vet om musen är tryckt och vilken knapp man tryckte

    if mouse[0] > display_width/2 - 300 and mouse[0] < display_width/2 - 100:
        if mouse[1] > display_height/2 - 50 and mouse[1] < display_height/2 + 50:
            if click[0] == True:
                print("forward = True")   #gör så att om musen trycker på en "knapp" så kommer Direction säga forward
                Direction = "forward"  #och hjulen på bilen kommer börja snurra framåt. 
                draw(Direction)    

                client.on_connect=on_connect
                client.on_disconnect=on_disconnect
                client.on_log=on_log                    #Loggar vad som skickas och liknande.
                client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)

                print("connecting to broker ", broker, )

                client.connect(broker, port=1883)  #connectar till broker
                client.loop_start()
                client.subscribe("carl.pettersson@abbindustrigymnasium.se/drive", 1)        #subscribar till en topic
                client.publish("carl.pettersson@abbindustrigymnasium.se/drive", "T", 0)   #publishar T till broker

                client.loop_stop()
                client.disconnect()    #disconnectar till broker

    if mouse[0] > display_width/2 + 100 and mouse[0] < display_width/2 + 300:
        if mouse[1] > display_height/2 - 50 and mouse[1] < display_height/2 + 50:   #"knappen" area
            if click[0] == True:
                print("forward = False")
                Direction = "backward"          #samma som över men backwards
                draw(Direction)

                client.on_connect=on_connect
                client.on_disconnect=on_disconnect
                client.on_log=on_log
                client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)

                print("connecting to broker ", broker, )

                client.connect(broker, port=1883)
                client.loop_start()
                client.subscribe("carl.pettersson@abbindustrigymnasium.se/drive", 1)
                client.publish("carl.pettersson@abbindustrigymnasium.se/drive", "F", 0)

                client.loop_stop()
                client.disconnect()
