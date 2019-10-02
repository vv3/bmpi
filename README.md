# BMPi

# Introduction
This project uses a RPI zero to replace the Braumesiter wifi module. The bmpi hosts a webserver for the front-end and talks to the Braumeister over UART using AT+ commands.

## Features
 * Send commands to the BM
 * update firmware

## Parts

### Parts required to make a cable

- USB to serial adapter (pl2303)
    - https://core-electronics.com.au/usb-to-ttl-serial-uart-rs232-adaptor-pl2303hx.html
- Connector
    - https://au.rs-online.com/web/p/industrial-automation-circular-connectors/1152764/

Note: Ensure that the USB to UART is set to 3.3V. For the core-electronics adapter listed above, remove the case of the USB to serial adapter and change it to 3.3v

## Demo Circuit

<img src="https://github.com/roguenorman/bmpi/blob/master/Circuit.png"/>


Rpi Pin               | Connector Pin
--------------------- | ----------------------------
TX (aka GPIO14)       | Pin 2 (TX)
RX (aka GPIO15)       | Pin 3 (RX)
Ground                | Pin 5 (GND)
                      | Pin 4 (XCK)
5V                    | Pin 1 (Vcc)

## Upgrading the Braumeister firmware
!!Make sure the USB adapter is set to 3.3v.
The BM will enter bootloader when XCK is pulled high to 2v and VCC is pulled high to 3.3v

Windows:
1. Put BM into bootloader mode
2. Connect cable from PC to BM 
3. Set the com port with: MODE COM7: baud=38400 parity=n data=8 dtr=off rts=off octs=off odsr=off
4. Open SpeidelSoftwareUpdater-Windows.exe (can be downloaded from speidel.com)
5. Select firmware
6. Plug in BM mains (buttons on BM turn yellow)
7. Press start update (buttons on BM turn red)
8. When finished, buttons on BM turn green
9. Unplug usb and mains



## License

Licensed under the GNU Lesser General Public License.
https://www.gnu.org/licenses/lgpl.html
