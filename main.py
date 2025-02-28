import network
import urequests
import utime
from machine import ADC, Pin

# Configuración WiFi
SSID = "" #SSID de tu internet
PASSWORD = "" #Contraseña de tu internet

# Configuración de ThingSpeak
CHANNEL_ID = "" #ID de tu canal en ThingSpeak
WRITE_API_KEY = "" #API KEY para escribir en tu canal en ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Configuración del sensor LM35
adc = ADC(Pin(26))  # GPIO26 corresponde al ADC0

# Conexión a WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)   
    while not wlan.isconnected():
        print("Conectando a WiFi...")
        utime.sleep(1)
    print("Conectado a WiFi!", wlan.ifconfig())

# Envío de datos a ThingSpeak
def send_to_thingspeak(value):
    url = f"{THINGSPEAK_URL}?api_key={WRITE_API_KEY}&field1={value}"
    try:
        response = urequests.get(url)
        print("Respuesta de ThingSpeak:", response.text)
        response.close()
    except Exception as e:
        print("Error al enviar datos:", e)
        
# Inicio del programa
connect_wifi()
while True:
    adc_value = adc.read_u16()  # Leer valor ADC (0-65535)
    voltage = (adc_value / 65535.0) * 3.3  # Convertir a voltaje
    temperature = voltage * 100  # Convertir voltaje a temperatura en grados Celsius
    print(f"Temperatura medida: {temperature:.2f}°C")
    send_to_thingspeak(temperature)
    utime.sleep(180)  # Enviar datos cada 180 segundos