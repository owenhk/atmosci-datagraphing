# Graph 3 points with a colorbar!

### If you just want a time vs. altitude graph - easy setup!

First, you'll need to download a bit of stuff.

You'll need an IDE, Visual Studio Code is easy and lightweight - [Download VSCode](https://code.visualstudio.com/download)

You'll also need Python (duh!) - [Download Python, get the latest version](https://https://www.python.org/downloads/)

And you'll need to get this GitHub project onto your computer. Luckily, this is super easy!

Open up **Terminal** and run ``git clone https://github.com/owenhk/atmosci-datagraphing``.

If you don't have Git, run these commands one by one in Terminal:

``/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"``

``brew install git``

Then try running the git clone again.

Now find the folder that was just installed (it's probably in either Downloads or Documents) and drag it into Visual Studio Code.

Open up the .env file, and change the values.


CSV_LOCATION - Where on your Mac the copy of your .csv is. This CSV needs to **only** have 3 columns, it doesn't matter the order; Altitude, Temperature, Time.

SAVE_LOCATION - Where on your Mac the .png of the graph should be saved to.

MIDPOINT - What the center of your colorbar should be. The lower this value is, the bigget colder temperature differences look (good for showing Stratosphere.) I set mine to -25.

2nd to last step, almost there! Open Terminal again and run these commands, one by one:

``cd folder-you-put-this-folder-in-either-Downloads-or-Documents``

``cd atmosci-datagraphing``

``pip3 install -r requirements.txt``

Now, you're all done! Click on `plotter.py` and click the play button. A .png graph will be generated!

### If you want to do more

Open up TODO.md and check what can be done! That's your job to do. Feel free to add more tasks for the next person to do.