Source from <https://github.com/andrei-tatar/imagotag-hack/tree/master/firmware/src>

To run it on the cc2510 board:

- Compile it using PlatformIO
- cd to <project_dir>/.pio/build/Generic8051
- Run objcopy -I ihex -O binary firmware.hex firmware.bin (names may vary)
- Upload .bin file to the board