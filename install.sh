#!/bin/bash -x


dt=$(date +"Date : %d/%m/%Y Time : %H:%M:%S");
echo "Beginning script $dt"

REPOSRC=https://github.com/AnthonySkoury/SDR-Aircraft-Traffic-Application.git
LOCALREPO=SDR-Aircraft-Traffic-Application

LOCALREPO_VC_DIR=$LOCALREPO/.git

# check for essentials on the Pi
sudo apt-get update
sudo apt-get install build-essential git -y

# install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# clone the repository
# if [ ! -d $LOCALREPO_VC_DIR ] && [ ! -d .git ]
# then
#     git clone $REPOSRC $LOCALREPO
#     cd $LOCALREPO
# else
#     cd $LOCALREPO
#     git pull $REPOSRC
# fi

# dump1090 setup
sudo apt-get install rtl-sdr librtlsdr-dev
cat librtlsdr.pc > /usr/lib/arm-linux-gnueabihf/pkgconfig/librtlsdr.pc
cd decoder/RTL-SDR/dump1090
make
cd ../../../

# database setup
docker pull postgres
docker run --name aircraft_db -e POSTGRES_USER=aircraft_db -e POSTGRES_DB=aircraft_db -e POSTGRES_PASSWORD=raspberry -d -p 5432:5432 postgres

# backend setup
sudo apt-get install libpq-dev python-dev
sudo apt-get install pipenv
echo 'export PATH="${HOME}/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
pip3 install --user --default-timeout=1000 pipenv
sudo pip3 uninstall backports.functools-lru-cache
sudo apt install python-backports.functools-lru-cache

# pipenv sync
# cd backend
# python manage.py makemigrations
# python manage.py migrate
# cd ..

# front end setup
install node https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/
curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
sudo apt install nodejs
npx create-react-app my-app
cd frontend
npm install
npm install google-map-react

dt2=$(date +"Date : %d/%m/%Y Time : %H:%M:%S");
echo "Finished script $dt2"