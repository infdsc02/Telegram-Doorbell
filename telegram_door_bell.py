from machine import Pin
import network
import utime
import sys

from telegram_exception import Telegram_Exception
from utelegram import Utelegram

TWO_MINUTES = 120000

#PIN OUT
DOOR_BELL = Pin(2, Pin.OUT, value=1)
LED_ERROR = Pin(32, Pin.OUT, value=0)
LED_OK = Pin(33, Pin.OUT, value=0)

#PIN IN
DOOR_BELL_SWITCH = Pin(13, Pin.IN)


WIFI_CONFIG = {
    'ssid':'<SET_WIFI_SSID>',
    'password':'<SET_WIFI_PASSWORD>'
}
UTELEGRAM_CONFIG = {
    'token': '<SET_TELEGRAM_BOT_TOKEN>'
}


def connect_wifi():
    get_elapsed_time = lambda start_time: utime.ticks_diff(utime.ticks_ms(), start_time)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    start_time = utime.ticks_ms()
    sta_if.connect(WIFI_CONFIG['ssid'], WIFI_CONFIG['password'])
    
    print('Trying to connect to ', WIFI_CONFIG['ssid'] +"...")
    
    # Waits two minutes for wifi connection
    while (not sta_if.isconnected()) and (get_elapsed_time(start_time) < TWO_MINUTES):
        pass
    
    if(sta_if.isconnected()):
        print('Connected to ', WIFI_CONFIG['ssid'] +"...")
        return True
    else:
        print("It couldn't connect to ", WIFI_CONFIG['ssid'])
        return False


def handle_button_state(bot: Utelegram):
    start = utime.ticks_ms()
    while True:
        logic_state = DOOR_BELL_SWITCH.value()
        if logic_state == True:     # if pressed the push_button
            delta = utime.ticks_diff(utime.ticks_ms(), start)
            if(delta > 500):
                print("Someone rang the door bell")
                DOOR_BELL.value(0)
                LED_OK.value(1)
                start = utime.ticks_ms()
                try:
                    bot.send(text="Someone rang the door bell")
                except(Telegram_Exception):
                    LED_OK.value(0)
                    LED_ERROR.value(1)
                    sys.exit(-1)
                    
        else:  # if push_button not pressed
            if(DOOR_BELL.value() == 0):
                DOOR_BELL.value(1)
                LED_OK.value(0)
                print("Reset door bell PIN value to 1")
        


if __name__ == "__main__":
    
    connected = connect_wifi()
    if(not connected):
        LED_OK.value(0)
        LED_ERROR.value(1)
        sys.exit(-1)
    
    try:
        bot = Utelegram(UTELEGRAM_CONFIG['token'])
    except(Telegram_Exception):
        LED_OK.value(0)
        LED_ERROR.value(1)
        sys.exit(-1)
        
    handle_button_state(bot)