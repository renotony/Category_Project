In order to use this app you should make sure that the files in this folder
(Category_Project) exist in a folder on your machine - including subfolders
that can be accessed by a Virtual Machine.

When you have the files and folders in place, log in to the virtual machine
and navigate to the folder containing the file database_setup.py.  Execute
the command python database_setup.py at the VM prompt.  This will set up the
database.  When that completes execute python lotsofplays.py which will load
the database with data.  You can then execute python project.py which will
start the server.  When the server has started you can access the app from
a browser by navigating to http://localhost:5000/plays 
