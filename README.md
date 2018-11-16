### DAT158ML-Oblig2

### Thoughts

For this Machine-learning assignment I chose Taxi Trip Duration [Kaggle Playground Competition] dataset. Because I think estimating a duration for a given taxi might be fun and realistic. I also wanted to find out what impact the different parameters has on each other. For example if a taxi uses longer time with more passengers.
This is my second ml project. This project gave me a better understanding of how machinelearning works and how it is used in practice. It also refreshed my memory on statistics which is a long time since I had.

### Getting Started

The main jypter file is called **taxi-trip.ipynb**. Here is all the code for the project.
Run the **create_distance_csv.ipynb**. It create two datasets with distances. The calculations take some time.

### Datasets

The primary train dataset (train.csv) and test dataset (test.csv) is at the Kaggle competition website. [NYC Taxi Trip Duration](https://www.kaggle.com/c/nyc-taxi-trip-duration/data)

The datasets for the fastest routes from OSRM can be found [here](https://www.kaggle.com/pepeeee/nyc-estimating-avg-speed-using-fastest-route/data). The files are: fastest_routes_train_part_1.csv, fastest_routes_train_part_2.csv, and fastest_routes_test.csv

### Docker

docker build -f Dockerfile -t 181221/ml .

docker run -d -p 8888:8888 --name jupyter -v <Folder where the project is.>:/root 181221/ml jupyter lab --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token= --notebook-dir='root'

### Requirements

All the requirements to run this project are listen in requirements.txt
