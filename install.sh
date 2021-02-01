#!/bin/bash -x

# check for essentials on the Pi
sudo apt-get update
sudo apt-get install build-essential git -y

# install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# clone the repository
git clone https://github.com/AnthonySkoury/Air-Traffic-System.git

# dump1090 setup
sudo apt-get install rtl-sdr librtlsdr-dev
cat librtlsdr.pc > /usr/lib/arm-linux-gnueabihf/pkgconfig/librtlsdr.pc
cd Air-Traffic-System/decoder/RTL-SDR/dump1090
make
## edit file https://askubuntu.com/questions/148421/how-to-programmatically-edit-a-file-using-only-terminal
cd ../../../

# database setup
docker pull postgres
docker run --name aircraft_db -e POSTGRES_USER=aircraft_db -e POSTGRES_DB=aircraft_db -e POSTGRES_PASSWORD=raspberry -d -p 5432:5432 postgres

# backend setup
sudo apt-get install libpq-dev python-dev
pip3 install pipenv
# pipenv sync
# cd backend
# python manage.py makemigrations
# python manage.py migrate
# cd ..

# front end setup
## install node https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/
curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
sudo apt install nodejs
npx create-react-app my-app
cd frontend
npm install
npm install google-map-react
