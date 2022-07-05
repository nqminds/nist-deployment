import network

def do_connect(ssid, key):  
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ssid, key)
    while not wlan.isconnected():
      pass
  print('network config:', wlan.ifconfig())

do_connect("alex-XPS-13-9350", "1234554321")
