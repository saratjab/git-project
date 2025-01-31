# Bikeshare Data Analysis

## Overview
This project analyzes bikeshare data from three major US cities (Chicago, New York, and Washington) to provide insights into travel trends. Users can filter the data by city, month, and day of the week, and view statistics on travel times, popular stations, trip durations, and user demographics.

## Dataset
The data files used in this project are:
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

Each dataset includes information such as start time, end time, trip duration, start and end stations, user type, gender (except for Washington), and birth year (except for Washington).

## Features
- **Filtering Options:**
  - Choose from three cities: Chicago, New York, and Washington.
  - Filter by specific months (January to June) or all months.
  - Filter by specific days of the week or all days.

- **Statistics Displayed:**
  - Most frequent travel times (month, day, and hour).
  - Most popular stations and trips.
  - Total and average trip duration.
  - User statistics including counts of user types, genders, and birth years (where available).

- **Interactive Data Viewing:**
  - Users can view raw data in increments of 5 rows upon request.

## Installation & Setup
1. Ensure you have Python installed (recommended version: 3.x).
2. Install required dependencies:
   ```bash
   pip install pandas numpy
   ```
3. Pl