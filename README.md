# Tournament SQL

This project is for the Udacity full stack developer course spring 2017. The project features a functioning python program to keep track of a swiss tournament system. It uses vagrant for development and PostgreSQL as the database.

## Getting started

Instructions on getting a local copy of the project running for development and testing purposes.

### Prerequists

- Vagrant
- VirtualBox

### Installing

1. Download and install vagrant for your OS by following the instructions from Hashicorp https://www.vagrantup.com/intro/getting-started/install.html
2. Download and install VirtualBox for your OS at https://www.virtualbox.org
3. Clone this repository `$ git clone https://github.com/Andurshurrdurr/SwissTournament_SQL`
4. Open a terminal and cd into the cloned repository
5. Get the VM running with Vagrant `$ vagrant up` - This may take a while
6. The VM should now be running, SSH into it `$ vagrant ssh`
7. Once you are running ssh to the vm, you have to initiate the database. First connect to psql shell `$ psql`
8. Create the database `=> CREATE DATABASE tournament;`, psql should return `CREATE DATABASE`
9. Exit the psql shell`=> \q`. Now python should be able to connect to the tournament database and run queries.

### Running the tests

1. Cd into the synced folder located at ~/synced/ `$ cd ~/synced/`
2. Run the python tests to see if the code works: `$ python tournament_test.py`
3. You can now develop the code in the synced folder on the host machine, and test it in the virtual environment by using vagrant. Pretty awesome!

## About Udacity

![Udacity](https://in.udacity.com/assets/images/svgs/logo_wordmark.svg)

Udacity is a for-profit educational organization founded by Sebastian Thrun, David Stavens, and Mike Sokolsky offering massive open online courses. [Wikipedia](https://en.wikipedia.org/wiki/Udacity)

This project is a part of my Udacity Full stack webdeveloper nanodegree.

## License

The MIT License (MIT)

Copyright (c) 2017 Anders Hurum

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
