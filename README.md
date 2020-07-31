# Surfs Up

This project is a practice for interafcing with sqlite databases and flask web servers.

The Hawaii.sqlite database contains weather and station data for the island of Oahu. We used sqlalchemy sessions to query the database and extract weather data (climate_analysis.ipynb) to see if the island had a climate that was compatable with a surf and ice cream shop (it did). We then used a flask instance to practive querying the data from a web address (app.py). And lastly I created a function that took in an int between 1-12 and returned descriptive information on the temperature and percipitation for that month (challenge.py)
