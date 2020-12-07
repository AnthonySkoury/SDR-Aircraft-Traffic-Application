# Air-Traffic-System
An air traffic system that uses an ADS-B receiver to obtain data.

## Note

## General Usage Setup
### Prerequisites
* Raspberry Pi with Raspbian
  * To set up Raspberry Pi: 
    * Install [Raspberry Pi Imager](https://www.raspberrypi.org/software/) 
    * Follow this guide to flash Raspberry Pi OS onto your SD card: https://www.raspberrypi.org/documentation/installation/installing-images/
    * Once the image is installed run the following commands
    ```bash
    sudo apt-get update
    sudo apt-get install build-essential git -y
    ```

* Docker
  * Docker can be set up on the Raspberry Pi or on another machine.
    * [To install on Raspberry Pi](https://docs.docker.com/engine/install/debian/)
    * [To install on Mac/Windows/Linux PC](https://docs.docker.com/get-docker/)

### Installing

First [clone the repository](https://help.github.com/en/articles/cloning-a-repository) via Git using the following command
```bash
git clone https://github.com/AnthonySkoury/Air-Traffic-System.git
```


### Setting up RTL-SDR and Dump1090
* Install rtl-sdr lib using `sudo apt-get install rtl-sdr librtlsdr-dev`
* `git clone https://github.com/antirez/dump1090`
* cd into dump1090 directory
* `make`
* If issues persist with Makefile follow the steps [here](https://github.com/antirez/dump1090/issues/142), in summary:
  * Run `pkg-config --libs librtlsdr --debug` to find the path of `librtlsdr.pc` on Raspbian it is most likely `/usr/lib/arm-linux-gnueabihf/pkgconfig/librtlsdr.pc` and on Linux it is most likely `/usr/lib/x86_64-linux-gnu/pkgconfig/librtlsdr.pc`
  * Change the file to to following:
  
    ```bash
    prefix=/usr
    exec_prefix=${prefix}
    libdir=${exec_prefix}/lib
    includedir=${prefix}/include
    ```
* Run `dump1090 --interactive --net` to start retrieving ADS-B data

### Setting up the database and backend
* Please follow the backend README [here](https://github.com/AnthonySkoury/Air-Traffic-System/blob/main/backend/README.md)

### Setting up the frontend
* Please follow the frontend README [here](https://github.com/AnthonySkoury/Air-Traffic-System/blob/main/frontend/README.md)

## Development

### Tools Used
* [Git](https://git-scm.com/) for version control
* [Django](https://www.djangoproject.com/) for backend
* [React](https://reactjs.org/) for frontend
* [Docker](https://www.docker.com/) for database host
* [PostgreSQL](https://www.postgresql.org/) for database used

Knowledge and skills needed

* Programming Python, Javascript, HTML, CSS to some extent
* General understanding of REST API framework
* General Understanding of how SDRs work

## Contributing

Please contact us or Peter Burke if you are interested in taking this project further.

## Versioning

We use [Git](https://git-scm.com/) for versioning.

## Authors

* **Anthony Skoury** - *Computer Engineer* - [My Website](https://anthonyskoury.github.io/)
* **Randall Cheng** - *Electrical Engineer, Computer Engineer*
* **Alan Wong**

## License
This project is licensed under the APGL_v3 License - see the [LICENSE.md](https://github.com/AnthonySkoury/Air-Traffic-System/blob/main/LICENSE) file for details


## Acknowledgments

* Professor Peter Burke for advising us
* Authors for all the Open-Source Libraries used in this program
* Anyone who develops this project further
