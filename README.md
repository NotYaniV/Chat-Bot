# Chat-Bot


For installation of all the packages we will create a virtual environment.
conda create -n nameofvenv python=3.8

virtualenv is used to manage Python packages for different projects. 
Using virtualenv allows you to avoid installing Python packages globally which could break system tools or ## other projects.

We need to now activate the virtual environment
conda activate nameofvenv

Next we need to download and install all the necessary packages we need 
In our project we will use PYTORCH and NLTK..

To install PYTORCh go to the site and configure accordingly and copy paste the configured package code 
Wait for a moment it will be downloaded.
The one that i used
conda install pytorch torchvision torchaudio cpuonly -c pytorch

Next, we need to install NLTK
sudo apt install python3-nltk
