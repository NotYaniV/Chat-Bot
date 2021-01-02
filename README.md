# Implementation of a Contextual Chatbot in PyTorch.  
Simple chatbot implementation with PyTorch. 

- The implementation should be easy to follow for beginners and provide a basic understanding of chatbots.
- The implementation is straightforward with a Feed Forward Neural net with 2 hidden layers.
- Customization for your own use case is super easy. Just modify `intents.json` with possible patterns and responses and re-run the training (see below for more info).

The approach is inspired by this article and ported to PyTorch: [https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077).

## Installation

### Create an environment

For installation of all the packages we will create a virtual environment.
Whatever you prefer (e.g. `conda` or `venv`)

with conda
``` console
conda create -n nameofvenv python=3.8
```
with venv
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```
virtualenv is used to manage Python packages for different projects. 
Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.

### Activate it

We need to now activate the virtual environment
if using conda follow
``` console
conda activate nameofvenv
```
if venv
Mac / Linux:
```console
venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```
### Install PyTorch, NLTK and dependencies

Next we need to download and install all the necessary packages we need 
In our project we will use PYTORCH and NLTK..

To install PYTORCH go to the site and configure accordingly and copy paste the configured package code 
Wait for a moment it will be downloaded.
The one that I used
```console
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

For Installation of PyTorch see [official website](https://pytorch.org/).

Next, we need to install NLTK
```console
sudo apt install python3-nltk
```
### Install Flask
```console
pip install flask
```
If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```
After running all the necessary file run 
```console
python App.py
```
and visit the provided localhost link, should be like the one shown below
```
http://127.0.0.1:5000/#
```
## Customize
Have a look at [intents,json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chat bot. You have to re-run the training whenever this file is modified.
```console
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    ...
  ]
}
```

