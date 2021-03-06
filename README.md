# ItemCatalogProject
A simple interactive web application for fun. This is based mainly on a [project from udacity](https://github.com/udacity/OAuth2.0)


To enjoy this website please consider the following:
### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).  
(On Mac or Linux systems you can use the regular terminal program.)

### VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

### Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Fetch the Source Code and VM Configuration

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.  
**Other systems:** Use your favorite terminal program.

From the terminal, run:

    git clone https://github.com/Rizialdi/ItemCatalogProject

This will give you a directory named **ItemCatalogProject** complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools. 

## Run the virtual machine!

Using the terminal, change directory to ItemCatalogProject (**cd ItemCatalogProject**), then type **vagrant up** to launch your virtual machine.


## Running the ItemCatalogProject App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.  change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

Type **ls** to ensure that you are inside the directory that contains project.py, database_setup.py, and two directories named 'templates' and 'static'

Now type **python database_setup.py** to initialize the database.

Type **python lotsofitems.py** to populate the database with category and element items. (Optional)

Type **python project.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the ItemCatalogProject app.  You should be able to view, add, edit, and delete element items and categories.

Some screenshot of this project are presented here:

**Landing page of the web app:**
![](https://i.imgur.com/z4MSjD8.png)

**When a category is selected:**
![](https://i.imgur.com/TDIOn1B.png)

**Description of an Item:**
![](https://i.imgur.com/JWfYCay.png)

**Register Page:**
![](https://i.imgur.com/yC6ZICp.png)

**Sign In Page:**
![](https://i.imgur.com/Bgg564I.png)

**Sign In Page when wrong user/password entered:**
![](https://i.imgur.com/Wqb9IvH.png)

**Screen for registered users:**
![](https://i.imgur.com/Y27oL1k.png)

**Page for adding an Item:**
![](https://i.imgur.com/mIqobGP.png)

**Added Item listed:**
![](https://i.imgur.com/VJDboml.png)

**Logout page:**
![](https://i.imgur.com/VRLSPvo.png)

**Error when existing users' name:**
![](https://i.imgur.com/GvJUNyC.png)

