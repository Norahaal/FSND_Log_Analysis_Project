Purpose of the project:

This project aims to strengthen SQL database skills, get practice interacting with a live database both from the command line and from the code and explore a large database with over a million rows. And build and refine complex queries and use them to draw business conclusions from data.

Essential steps for this project:

- Install Vagrant
- VirtualBox
- python 2
- clone this resptortary: https://github.com/udacity/fullstack-nanodegree-vm
- Unzip this file after downloading it.  
- download the data from here https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip. Unzip the newsdata.sql and put it into vagrant directory to be shared with your virtual machine.
- Copy the files and the content of this repository, by either downloading or cloning it from https://github.com/Norahaal/FSND_Log_Analysis_Project 

Running the project 

Launch the Vagrant VM inside Vagrant sub-directory by using '$ vagrant up' , then log into it using '$ vagrant ssh'.
Then change directory to 'cd /vagrant' and look around it.
To load database and run the requires sql statment use 'psql -d news -f newsdata.sql', 
'psql -d news' . Use 'python quary.py' to run the python code.
To close the VM use exit
