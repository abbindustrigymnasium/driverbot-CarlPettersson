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

    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 346, display_height/2 + 54, 200, 100))  
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 347, display_height/2 + 53, 200, 100)) # ritar buttons och gör bakgrunden vit
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 348, display_height/2 + 52, 200, 100)) # ritar också texten
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 349, display_height/2 + 51, 200, 100))
    pygame.draw.rect(display, (0, 255, 0), (display_width/2 - 350, display_height/2 + 50, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Forward', 1, (0,0,0))
    display.blit(text, (display_width/2 - 325, display_height/2 + 75))

    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 146, display_height/2 + 54, 200, 100))  
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 147, display_height/2 + 53, 200, 100))
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 148, display_height/2 + 52, 200, 100))
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 149, display_height/2 + 51, 200, 100))
    pygame.draw.rect(display, (255, 0, 0), (display_width/2 + 150, display_height/2 + 50, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Backward', 1, (0,0,0))
    display.blit(text, (display_width/2 + 165, display_height/2 + 75))

    pygame.draw.rect(display, (150, 150, 0), (display_width/2 - 346, 100, 200, 100))  
    pygame.draw.rect(display, (150, 150, 0), (display_width/2 - 347, 101, 200, 100)) # ritar buttons och gör bakgrunden vit
    pygame.draw.rect(display, (150, 150, 0), (display_width/2 - 348, 102, 200, 100)) # ritar också texten
    pygame.draw.rect(display, (150, 150, 0), (display_width/2 - 349, 103, 200, 100))
    pygame.draw.rect(display, (255, 255, 0), (display_width/2 - 350, 104, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Left', 1, (0,0,0))
    display.blit(text, (display_width/2 - 300, 130))

    pygame.draw.rect(display, (150, 150, 0), (display_width/2 + 146, 100, 200, 100))  
    pygame.draw.rect(display, (150, 150, 0), (display_width/2 + 147, 101, 200, 100))
    pygame.draw.rect(display, (150, 150, 0), (display_width/2 + 148, 102, 200, 100))
    pygame.draw.rect(display, (150, 150, 0), (display_width/2 + 149, 103, 200, 100))
    pygame.draw.rect(display, (255, 255, 0), (display_width/2 + 150, 104, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Right', 1, (0,0,0))
    display.blit(text, (display_width/2 + 190, 130))

    pygame.draw.rect(display, (150, 150, 0), (display_width/2 - 103, display_height/2 - 73, 206, 106))
    pygame.draw.rect(display, (255, 255, 0), (display_width/2 - 100, display_height/2 - 70, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('Straight', 1, (0,0,0))
    display.blit(text, (display_width/2 - 75, display_height/2 - 50))

    green_button_text = pygame.font.SysFont('arial', 20)
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

    keys = pygame.key.get_pressed()

    if mouse[0] > display_width/2 - 350 and mouse[0] < display_width/2 - 150 or keys[pygame.K_w]:
        if mouse[1] > display_height/2 + 50 and mouse[1] < display_height/2 + 150 or keys[pygame.K_w]:
            print("forward")
            if click[0] == True or keys[pygame.K_w]:
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

    if mouse[0] > display_width/2 + 150 and mouse[0] < display_width/2 + 350 or keys[pygame.K_s]:
        if mouse[1] > display_height/2 + 50 and mouse[1] < display_height/2 + 150 or keys[pygame.K_s]:   #"knappen" area
            print("backward")
            if click[0] == True or keys[pygame.K_s]:
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

    if mouse[0] > display_width/2 + 150 and mouse[0] < display_width/2 + 350 or keys[pygame.K_d]:
        if mouse[1] > 104 and mouse[1] < 204 or keys[pygame.K_d]:   #"knappen" area
            print("Right")
            if click[0] == True or keys[pygame.K_d]:
                print("forward = False")
                Direction = Direction          #samma som över men backwards
                draw(Direction)

                client.on_connect=on_connect
                client.on_disconnect=on_disconnect
                client.on_log=on_log
                client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)

                print("connecting to broker ", broker, )

                client.connect(broker, port=1883)
                client.loop_start()
                client.subscribe("carl.pettersson@abbindustrigymnasium.se/drive", 1)
                client.publish("carl.pettersson@abbindustrigymnasium.se/drive", "R", 0)

                client.loop_stop()
                client.disconnect()

    if mouse[0] > display_width/2 - 350 and mouse[0] < display_width/2 - 150 or keys[pygame.K_a]:
        if mouse[1] > 104 and mouse[1] < 204 or keys[pygame.K_a]:   #"knappen" area
            print("Left")
            if click[0] == True or keys[pygame.K_a]:
                print("forward = False")
                Direction = Direction          #samma som över men backwards
                draw(Direction)

                client.on_connect=on_connect
                client.on_disconnect=on_disconnect
                client.on_log=on_log
                client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)

                print("connecting to broker ", broker, )

                client.connect(broker, port=1883)
                client.loop_start()
                client.subscribe("carl.pettersson@abbindustrigymnasium.se/drive", 1)
                client.publish("carl.pettersson@abbindustrigymnasium.se/drive", "L", 0)

                client.loop_stop()
                client.disconnect()

    if mouse[0] > display_width/2 - 100 and mouse[0] < display_width/2 + 100 or keys[pygame.K_SPACE]:
        if mouse[1] > display_height/2 - 70 and mouse[1] < display_height/2 + 30 or keys[pygame.K_SPACE]:   #"knappen" area
            print("Straight")
            if click[0] == True or keys[pygame.K_SPACE]:
                print("forward = False")
                Direction = Direction          #samma som över men backwards
                draw(Direction)

                client.on_connect=on_connect
                client.on_disconnect=on_disconnect
                client.on_log=on_log
                client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)

                print("connecting to broker ", broker, )

                client.connect(broker, port=1883)
                client.loop_start()
                client.subscribe("carl.pettersson@abbindustrigymnasium.se/drive", 1)
                client.publish("carl.pettersson@abbindustrigymnasium.se/drive", "S", 0)

                client.loop_stop()
                client.disconnect()
