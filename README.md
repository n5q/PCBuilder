# PCBuilder #

A small program designed to assist in purchasing parts for a system written in Python and using the Tk interface.




## INSTRUCTIONS ##

There are two ways of running the program. If you have python installed you can run `git clone https://github.com/NasifQadri/PCBuilder` and then run `gui.py` or if you do not have python installed you can head to the [releases section](https://github.com/NasifQadri/PCBuilder/releases), download and extract the latest .zip, then run PCBuilder.exe


## ##

## Current Features ##

* Option to choose from Intel or AMD processors
* Ratio of budget allocated to each part chnages to best suit the chosen usage
* Displays induvidual prices for each part 
* TKinter GUI interface
* Exports completed build to a .txt file for future refrence




### Current Parts ###

#### Processors ####

* Intel
  * Core i3 8350K
  * Core i5 9600K
  * Core i7 9700K
  * Core i9 9900K
* AMD
  * Ryzen 3 2200G
  * Ryzen 5 2600X
  * Ryzen 7 3700X
  * Ryzen 9 3900X
  
#### Graphics Cards ####

* Nvidia GeForce
  * GTX 1560
  * GTX 1660
  * GTX 1660 Ti
  * RTX 2060
  * RTX 2060 SUPER
  * RTX 2070 SUPER
  * RTX 2080 SUPER
  * RTX 2080 Ti
  
  
  
## In Progress ##
  
* AMD Graphics Cards
* Option to show detailed part information
  * Clock speed
  * VRam (For GPUs)
  * Power usage
  * Overclock information
* Dark theme for the GUI
* Scraping price details from Amazon or Newegg rather than giving static estimates
* Option to add custom parts with prices (Buggy)
* Option to input a custom ratio for each part from the budget
  
  
 ## Future Plans ##
 
* Get part information directly from PCPartPicker using [this API](https://pypi.org/project/pcpartpicker/)
* Create a Discordapp and Telegram bot that can be used in servers or groups
* Scrape part reviews from Amazon and Newegg
* Add RAM clock speeds
* Recommend specific motherboards
* Add peripherals
* Add option for dual GPUs in SLI
* Port application to Android based devices
* Show current system specs and compare to new build
  * Estimate current system resale price and/or if any parts ccan be reused
* Add prices for software and/or operating systems
