# Fake News Detector

A Chrome browser extention which warns a user when they are viewing misleading or fake news based on a prediction from a machine learning model. Developed as an entry for the University of Warwick Computing Society remote hackathon.

## Installation

Requires Python3 and the following libraries installed:

- Flask
- Sklearn
- Numpy (for training own models)

### Installing the Chrome extension

1. Download the extension folder (currently pageTestV4)
2. Open Chrome and type `chrome://extensions` into the address bar and press enter
3. Make sure developer mode is enabled at the top right of the window
4. Click `Load unpacked` on the top left of the window and select the folder 

## Usage

To make the extension work, run the `api.py` file in `/api` with `python api.py` (run it from the `/api` folder as otherwise it throws errors). Restart Chrome and everything should be working.

## Training your own models 

Currently the program is trained on a dataset and the models are included to download, however the dataset is fairly small (96 samples in each category) and might not be very accurate as it was taken from limited sources. 

If you wish to train the models on your own datasets, put the files in their corresponding folders in `/api/classifier/data` and run `classifier.py`. In each folder, put every sample in a separate file in this format:

>Title of the article (\n)
>
>Content of the article

