# DashbuttonDaemon
This repository provides a daemon that executes code if a dashbutton is pressed - [https://gasperphoenix.github.io/DashbuttonDaemon](https://gasperphoenix.github.io/DashbuttonDaemon)

## Usage examples

I combined the DasbuttonDaemon with the code of my [FritzBox](https://gasperphoenix.github.io/FritzBox/) project to switch a night light (connected to a Fritz!DECT switchable plug) on and off using an Amazon dashbutton.

You could also use it to call a special HTTP-request on [IFTT](https://ifttt.com/discover) to execute your own services opening a door to many useful applications.

## Prepare your dashbutton

I'm using Amazon Dashbuttons for this project. First you need to configure your dashbutton using a device like a mobile phone as described by Amazon in the manual shipped with your new dashbutton. Enter your WLAN credentials and proceed but when you reach the step to select a product close your app without selecting one of them. This ensures that the dashbutton will not order any products once it is pushed. But it still wakes up and connects to the WLAN while being pushed. 

## Detect dashbutton and MAC address

I wrote a small script *DetectDashbutton.py* to detect Dashbuttons and their MAC address. To us it just execute the following command in the root folder of this archive and press the Dashbutton afterwards.

```
sudo python3 DetectDashbutton.py
```

This will result in an output like this.

```
[2018-09-08 00:00:00] - [INFO]: New MAC detected: 6C:56:97:xx:xx:xx (Amazon Technologies Inc.)
[2018-09-08 00:00:00] - [INFO]: New MAC detected: 44:4E:6D:xx:xx:xx                        
```

Look for a line including *(Amazon ...)* at the end. This is your Dashbutton and its MAC address.

Hint: The first 6 characters of a MAC address include the vendor information which you can lookup on [admin subnet](https://www.adminsub.net/mac-address-finder) to determine the vendor of this network node.

## Using the daemon to initiate actions based on Dashbutton push events

The script *DashbuttonDaemon.py* provides a framework to initiate actions everytime a Dashbutton is pressed.

To use the script you first need to add all your Dashbuttons to the following list in the script. Make sure to use uppercase letters. I already added two Dashbuttons as example.
 
```
DASH_BUTTONS = {"6C:56:97:55:96:CD" : "First_Dashbutton",
                "6C:56:97:17:2A:BE" : "Second_Dashbutton"} # HW MAC must be in upper case
```

Further down in the script you find the callback method *button_pressed* that is executed everytime a Dashbutton is pressed. Put your own code in here to do your stuff once a Dashbutton is pressed.

You may wonder why I added the variable now_ts, button1_ts and button2_ts to the script and why I'm checking them against a value of 5 in the callback. This is a debounce mechanism I needed to add as sometimes a Dashbutton is pressed it sends out multiple ARP requests resulting in multiple invocations of the callback if a Dashbutton is pressed only once. Therefore I'm debouncing every button with a 5 seconds delay :-)  