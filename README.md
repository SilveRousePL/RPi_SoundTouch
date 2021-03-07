# RPi_SoundTouch

## Helpful commands:

#### Static IP:
```
sudo vim /etc/dhcpcd.conf
```

#### Gstreamer
```
sudo apt install gstreamer-1.0
```

#### If problems with run mpr121.py
```
sudo modprobe i2c_bcm2708
```
#### If problems with sound, please check 
```
sudo raspi-config
```

#### Disable test audio message 
```
sudo mv /usr/share/piwiz/srprompt.wav /usr/share/piwiz/srprompt.wav.bak
```

## TODO:
- Scripts autostart