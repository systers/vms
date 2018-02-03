# Installation Guide
## Requirements

This tutorial assumes that the user is installing and running the project under the Ubuntu Virtual Machine that is provided by Systers or on their local Ubuntu machine.

## Table of Contents
1. [Install git](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#install-git)
2. [Clone Project](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#clone-project)
2.5 [Install Python] (https://www.python.org/downloads/)
2.6 [Install and make sure pip is working] (https://pip.pypa.io/en/latest/installing/)
3. [Install VirtualBox and Vagrant](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#install-virtualbox-and-vagrant)
4. [Download Systers Ubuntu Virtual Machine](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#download-systers-ubuntu-virtual-machine)
5. [Using Vagrant](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#using-vagrant)
6. [Install PostgreSQL](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#install-postgresql)
7. [Install Django and additional packages](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#install-django-and-additional-packages)
8. [Setup PostgreSQL](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#setup-postgresql)
9. [Generate Database Tables Corresponding to Django Models](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#generate-database-tables-corresponding-to-django-models)
10. [Change Directory Permissions](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#change-directory-permissions)
11. [Run Development Server](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#run-development-server)
12. [Run Unit Tests](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#run-unit-tests)

## Install git

If you don't already have git, you can download it [here](http://git-scm.com/downloads). You must then install git.

## Clone Project

Clone the project from GitHub by running the following command:

    git clone https://github.com/systers/vms

For this project, it would correspond to:

    git clone https://github.com/systers/vms.git

You can setup VMS either through vagrant or directly on your local machine. If you want to install on your local machine, follow instructions after Step 5.

## Install VirtualBox and Vagrant

The Virtual Machine provided by Systers will be downloaded in a later step. We must first install VirtualBox and Vagrant.

The VirtualBox and Vagrant installers can be downloaded from the following websites:

1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](http://www.vagrantup.com/downloads.html)

Install VirtualBox and Vagrant by running the installers.

## Download Systers Ubuntu Virtual Machine

A Vagrant file is located in the top level directory for the project (at [https://github.com/systers/vms](https://github.com/systers/vms)) found on GitHub. In case you do not have a copy of this Vagrant file, here are it's contents:
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box_url = "http://54.183.32.240/vagrant/box/systers-vms.box"
  config.vm.box = "systers-vms-dev"

  config.vm.provider "virtualbox" do |vb|
    vb.gui=true
  end

  config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
  config.vm.network "forwarded_port", guest: 8000, host:8001
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "public_network"
end
```
Save this file as **Vagrantfile** (if you don't already have this file) in the top level directory for the project.

To download the VM, run the following command:

    vagrant up

You must wait a few minutes for the VM to be downloaded completely.

## Using Vagrant

The `vagrant up` command also boots the Virtual Machine.

Once the VM download has completed, upon boot, it may ask you to choose an `Available bridged network interface`. The first option will work in most cases.

You may come across a message that says `default: Warning: Remote connection disconnect. Retrying...` This message means that the VM is still booting up which is why we cannot establish a connection with it. It is normal to wait on this message for a few minutes (~5 minutes in my case) before we are able to get a connection to the VM. You may need to wait a few minutes until you get a message saying `default: Machine booted and ready!`.

You might be prompted for the virtual machine login and password.
Enter "vagrant" as login and "vagrant" as password.
After this the Virtual Machine will be booted completely and the command prompt appears.

File syncing will work properly after you receive this message: `default: Mounting shared folders`. Please wait for this message before proceeding to the next steps.

Once the VM boots up (and you were able to receive the messages specified above), you can ssh onto the VM by running the command:

    vagrant ssh

You will notice that the project is now synced to this VM by changing directory to /vagrant/vms in the virtual machine.

    cd /vagrant/vms

When you make any changes to the project locally, these changes are also reflected (synced) to the project files located in /vagrant/vms, and vice versa.

Here are some additional vagrant commands that may be useful (which you can try later, do not run these commands right now). Proceed to [Install additional modules](#ppm).

Once you are done with the VM, exit out of the ssh session by running:

    exit

To put the VM in suspend mode, run the command:

    vagrant suspend

To shut down the VM, run the command:

    vagrant halt

To start up the VM again, run the command:

    vagrant up
    

## Install PostgreSQL

If you are installing and running the project on your local machine and not on the Systers VM, then you will need to download and install PostgreSQL:

[PostgreSQL](http://www.postgresql.org/download/) (version >= 9.3.4)

**You do not need to download and install Django and PostgreSQL if you are installing and running the project on the Systers VM, as Django and PostgreSQL are already included in the Systers VM.**


## <a name="ppm"></a>Install Django and additional packages

Run the following commands to install required libraries for vms:

    cd vms
    sudo pip install -r requirements.txt

This will also automatically install a correct version of [Django](https://www.djangoproject.com/download/). You can also use another version as long as (version >= 1.7 and version < 1.8)

## Setup PostgreSQL

We will now setup PostgreSQL by first running the postgres client as root:

    sudo -u postgres psql

NOTE: In case, you get an error - postgres: invalid argument: "psql". Then run the following command
    sudo -u <insert postgres username here> psql

Next, we will create a user called `vmsadmin` with a password `0xdeadbeef` (for now) with the permissions to be able to create roles, databases and to login with a password:

    create role vmsadmin with createrole createdb login password '0xdeadbeef';

Next, exit the postgres client by running the command:

    \q

We will need to change the **pg_hba.conf** file to indicate that users will authenticate by md5 as opposed to peer authentication. To do this, first open the **pg_hba.conf** file by running the command:
```
sudo nano /etc/postgresql/x.x/main/pg_hba.conf
```
(where x.x is the version number of postgres)

NOTE: In case you find a file not found error, then the postgresql installation has probably taken place in a different directory. Find the file using the following command
    sudo find / -type f -iname pg_hba\.conf

Now go the directory where the pg_hba.conf file is present.

Change the line `local all postgres peer` to `local all postgres md5`

Also, change the line `local all all peer` to `local all all md5`

NOTE: In case you dont find the entries, just add the entries as mentioned above.

After making these changes, make sure to save the file.

Restart the postgresql client:

    sudo service postgresql restart

Now, we will be able to login to the postgres client with the vmsadmin user that we created by running the following command:

    psql -U vmsadmin -d postgres -h localhost -W

You will be prompted to enter a password, which is `0xdeadbeef`

Next, exit the postgres client again:

    \q

We will now create a database called `vms`:

    createdb -U vmsadmin vms;

You will be prompted to enter a password, which is `0xdeadbeef`

We can now login to the postgres client for the `vms` database:

    psql -U vmsadmin -d vms -h localhost -W

You will be prompted to enter a password, which is `0xdeadbeef`

To view a list of tables for the `vms` database, run this command under the postgres client:

    \dt

We can now manipulate the database by running the appropriate sql commands under this postgres client.

Make sure to exit the postgres client before proceeding to the next steps:

    \q

## Generate Database Tables Corresponding to Django Models

Change directory to where you can find the **manage.py** file (this is located in the top level directory for the project). If you are installing the project on the VM, the project will be located within the **/vagrant/vms** directory.

To view the sql commands that will be generated from syncdb, run the command:

    python manage.py sqlall app_name_here

To generate the database tables that correspond to the Django models, run the command:

    python manage.py syncdb

NOTE: In case, you get the following error django.db.utils.ProgrammingError: relation "auth_user" does not exist, while running the above command do the following
    python manage.py migrate auth
    python manage.py migrate
Now again try running the command 
    python manage.py syncdb


We do not want to create a superuser at this time, so when it asks you to create a superuser, say 'no':

    You just installed Djano's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): no

In addition to this, you would also have to populate the database for django-cities-light. Run the following to do so:

    python manage.py migrate
    python manage.py cities_light

This might take a bit of time. You might get a message saying 'No handlers could be found for logger cities_light'. This is because a logging module hasn't been configured separately.

Check that the tables were created by starting the postgres client and viewing the tables using the `\dt` command.
```
psql -U vmsadmin -d vms -h localhost -W
```
You will be prompted to enter a password, which is `0xdeadbeef`

```
\dt
```
There needs to be at least one organization in the `organization_organization` table in order to register for an account (this be changed later). Add Google as an organization:

    insert into organization_organization values (1, 'Google');

Make sure to exit the postgres client before proceeding to the next steps:

    \q

## Change Directory Permissions

You will have to change the permissions on the **/srv** directory to read, write and execute (**/srv** is the directory where Volunteer resumes are uploaded and stored). To do this, run the following command:

    sudo chmod 777 /srv

NOTE: In case you can the error "/srv: No such file or directory" while running the above comment do the following
    sudo mkdir /srv

After creating the directory, then try to change the permissions i.e., run the following command (sudo chmod 777 /srv)

## Run Development Server

Change directory to where you can find the **manage.py** file (this is located in the top level directory for the project).

Start the development server by running the command (this runs the development server on the VM):

    python manage.py runserver [::]:8000

You can now try out the project by going to [http://localhost:8001/home](http://localhost:8001/home) on a browser on your local machine.

## Run Unit and Functional Tests

You can also run unit and functional tests by running the command:

    python manage.py test name_of_app_here

For example, in the project, there are Django apps called volunteer, job, shift and organization. You can run tests for these apps individually by running these commands separately:
```
python manage.py test volunteer
```
```
python manage.py test job
```
```
python manage.py test shift
```
```
python manage.py test organization
```

If you want to run only unit tests for an app, refer to its test_services file using the dot notation.

For example, if you want to run unit tests for the event app:
```
python manage.py test event.tests.test_services
```

Smilarly, for job app it would be:
```
python manage.py test job.tests.test_services
```

If you want to run all unit tests, run this command:

    python manage.py test

Once you are done with testing out and running the project, you may want to exit the VM and suspend or shut it down by running these commands:

Exit out of the ssh session with the VM by running:

    exit

To put the VM in suspend mode, run the command:

    vagrant suspend

Alternatively, to shut down the VM, run the command:

    vagrant halt
