# NIST Deployment

![Setup](docs/images/setup.png?raw=true "Setup")

## Setup

### Devices
 - PC Engines/mini PC
    - 2 x LAN connections
    - 2 x USB connections
 - Turris Omnia
    - 1 x WiFi modem
    - 2 x LAN connections
 - Feather HUZZAH ESP8266
    - USB connection
    - WiFi connection
 - Powered USB Hub
    - 4 x USB connections
    - 1 x Power connections
 - Relay switch
    - Power connection

### IoT testbed
 - 1 x Turris Omnia - WiFi access point
 - 3 x Feather HUZZAH ESP8266 - IoT WiFi devices

### Control testbed
 1. PC Engines/mini PC
  - Reverse SSH, cloud connection
  - USB relay connection connection
  - Powered USB connection
 2. Turris Omnia LAN connection
 3. Relay switch
 4. Powered USB hub

## Development

### Feather HUZZAH ESP8266
#### Install micropython

Instal [esptool](https://github.com/espressif/esptool) with:
```bash
pip3 install esptool
```

Using esptool you can erase the flash with the command:
```bash
esptool.py --port /dev/ttyUSB0 erase_flash
```

Download micropython for ESP8266 with 2MiB+ flash:

[https://micropython.org/download/esp8266](https://micropython.org/download/esp8266)

And then deploy the new firmware using:

```bash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin

```
You might need to change the `port` setting to something else relevant for your PC. You may also need to reduce the baudrate if you get errors when flashing (e.g., down to 115200). The filename of the firmware should also match the file that you have.

To access the prompt over USB-serial you need to use a terminal emulator program. Linux has picocom and minicom.

```bash
picocom /dev/ttyUSB0 -b115200
```

#### Install adafruit-ampy
[Ampy](https://github.com/scientifichackers/ampy) is meant to be a simple command line tool to manipulate files and run code on a CircuitPython or MicroPython board over its serial connection.

```bash
pip3 install --user adafruit-ampy
```

To list the files on ESP use:
```bash
ampy --port /dev/ttyUSB0 ls
```

#### ESP file structure
There are two main python files located on ESP8266 after uploading the firmware:
 - `boot.py` - run on board startup, configures the micropython for the board
 - `main.py` - where the main app is located

If `main.py` is changed, the board needs to be unplugged and the plugged back in for the changes to take effect.

### Powered USB hub

atolla Powered USB 3.0 Hub 20W, 7 Multi USB Data Ports Hub splitter with Individual On/Off Switches+1 USB Smart Charging port with 5V/4A Power.

Changes to hardware:
 - Cut the USB 3.0 power wire
 - Soldered a shunt between the USB power pin and 5.0 V main power socket input

![Hub](docs/images/board.jpg?raw=true "Hub shunt")

### Relay switch

The relay switch box is based on Devantech USB-RLY16L 8 Channel 16A board. The relay controls two channels 1 and 8, which are connected to two power sockets. The PC to box connection is done through CDC serial USB by using the port `/dev/ttyACM0` or similar. The baud rate for the serial connection is `19200` and the commands can be run with `picocom` tool as follows:
```bash
picocom --imap 8bithex /dev/ttyACM0
```

The commands descriptions are depicted in the picture below:

![Commands](docs/images/commands.jpg?raw=true "Relay commands")

Position 0 means that there is no power going to the corresponding power switch.

The relay board construction is as follows:

#### Relay box inside
![Relayinside](docs/images/relay-inside.jpg?raw=true "Relay inside")

#### Relay box outside
![Relayoutside](docs/images/relay-outside.jpg?raw=true "Relay outside")

## Hardware setup

The hardware setup is depicted below:

![Setup](docs/images/setup.jpg?raw=true "Setup")

## Documentation
 1. [https://docs.micropython.org/en/latest/esp8266/quickref.html](https://docs.micropython.org/en/latest/esp8266/quickref.html)