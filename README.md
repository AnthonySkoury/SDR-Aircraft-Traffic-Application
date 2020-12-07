# Air-Traffic-System
An air traffic system that uses an ADS-B receiver to obtain data.

## Getting Started



#### Note


### Prerequisites

## Hardware Setup
### Prerequisites
* Raspberry Pi with Raspbian
  * To set up Raspberry Pi: 
    * Install [Raspberry Pi Imager](https://www.raspberrypi.org/software/) 
    * Follow this guide to flash Raspberry Pi OS onto your SD card: https://www.raspberrypi.org/documentation/installation/installing-images/
### Setting up RTL-SDR and Dump1090
* Install rtl-sdr lib using `sudo apt-get install rtl-sdr librtlsdr-dev`
* `git clone https://github.com/antirez/dump1090`
* cd into dump1090 directory
* `make`
* If issues persist with Makefile follow the steps [here](https://github.com/antirez/dump1090/issues/142), in summary:
  * Run `pkg-config --libs librtlsdr --debug` to find the path of `librtlsdr.pc` on Raspbian it is most likely `/usr/lib/arm-linux-gnueabihf/pkgconfig/librtlsdr.pc` and on Linux it is most likely `/usr/lib/x86_64-linux-gnu/pkgconfig/librtlsdr.pc`
  * Change the file to to following:
  
    `prefix=/usr`

    `exec_prefix=${prefix}`

    `libdir=${exec_prefix}/lib`
    
    `includedir=${prefix}/include`
* Run `dump1090 --interactive --net` to start retrieving ADS-B data

## General Usage
* [Docker](https://www.docker.com/)

## Development
* [Git](https://git-scm.com/) for version control
* [Django](https://www.djangoproject.com/) for backend
* [React](https://reactjs.org/) for frontend


Knowledge and skills needed

* Programming Python, Javascript, HTML, CSS to some extent
* General understanding of REST API framework
* General Understanding of how SDRs work


### Installing

To get a developer environment running please do the following:

#### Initial setup



#### Creating the project

* Clone the repository via [Git](https://help.github.com/en/articles/cloning-a-repository)

#### Project Setup




#### Demo

## Building then running the program



### Debugging the program



## Deployment

For deploying follow these steps





## Built With



## Contributing

Please contact us or Peter Burke if you are interested in taking this project further.

## Versioning

I use [Git](https://git-scm.com/) for versioning.

## Authors

* **Anthony Skoury** - *Computer Engineer* - [My GitHub](https://github.com/AnthonySkoury)
* **Randall Cheng** - *Electrical Engineer, Computer Engineer*
* **Alan Wong**

## License
This project is licensed under the APGL_v3 License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* Professor Peter Burke for advising us
* Authors for all the Open-Source Libraries used in this program
* Anyone who develops this project further
