# Overview
A simple stock predictor using Facebook's prophet model and interfaced by [this repo](https://github.com/WillKoehrsen/Data-Analysis/tree/master/stocker), we adpot [this repo](https://github.com/koreal6803/Stocker) as a base which changes the very origin interface to allow customized .csv datasets.

## stocker.py
Contains the interfaced API class Stocker, go to the original API integraion repo for detailed usage of methods in Stocker.

## Dataset
We use an integrated dataset about the four companies'(Facebook, Google, Amazon, Apple) stock information from [this](https://www.kaggle.com/stexo92/gafa-stock-prices?fbclid=IwAR2Qhy542X0-2AW--diHgMZvkbIr289E_9f8m1ppMn3azQWTQHYtBnrOsvI) kaggle dataset

You can replace rawData.csv by your own .csv data to have your costumed model, check our splitdata.py as an example if your dataset also contains data of multiple companies.

## Usage
Just simply run model.ipynb(we assume that the datasets you use is available and in the right path, check model.ipynb for correct path)
