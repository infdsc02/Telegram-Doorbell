# Telegram-Doorbell
Bot de Telegram que envía un mensaje cuando alguien timbra en la puerta. Este proyecto se basa en [micropython-utelegram project](https://github.com/jordiprats/micropython-utelegram). 

El timbre utilizado es el Siemens JSJS-315. Las dos principales carácteristicas relevantes para este proyecto son: 
* Funciona a 3V. (**OJO: este proyecto no soporta, de momento, el uso con timbres clásicos que funcionan a 220V**).
* Permite reproducir archivos MP3. 

## Hardware list:
* Dos breadboard
* Una placa de desarrollo con el chip ESP32
* Un switch
* Un led rojo y otro verde
* Tres resistencias de 220 Ohm

## Montaje
Las siguientes fotografías muestran el montaje del hardware.
![Alt text](https://github.com/infdsc02/Telegram-Doorbell/blob/main/assemble%20images/img1.jpg?raw=true)

![Alt text](https://github.com/infdsc02/Telegram-Doorbell/blob/main/assemble%20images/img2.jpg?raw=true)

![Alt text](https://github.com/infdsc02/Telegram-Doorbell/blob/main/assemble%20images/img3.jpg?raw=true)

![Alt text](https://github.com/infdsc02/Telegram-Doorbell/blob/main/assemble%20images/img4.jpg?raw=true)



## Puesta en marcha
Primero es necesario obtener un token de Telegram, para ello seguir este [tutorial](https://blog.330ohms.com/2021/03/09/crea-tu-propio-bot-de-telegram-con-esp32/)

Una vez se tiene el token de Telegramm, se abre el proyecto y en el fichero telegram_door_bell.py hay que buscar la constante WIFI_CONFIG y en ella setear el SSID y el password de la red wifi a la que se va a conectar el ESP32. Luego en la constante UTELEGRAM_CONFIG se establece el token de Telegram. Por último queda subir los ficheros al ESP32 para que pueder ejecutar el programa.
