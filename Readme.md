# Internshala Web Scraping and Data Visualization Project

This project involves scraping job/internship data from the Internshala website using BeautifulSoup, cleaning the data, and generating visual representations of the data using various plots.

## Features

- Scraped internship/job data from Internshala.
- Cleaned and preprocessed the scraped data.
- Generated visualizations using Matplotlib and Seaborn.
- Saved the cleaned data to a CSV file.

## Tech Stack

- Python 3.x
- BeautifulSoup (for web scraping)
- Pandas (for data manipulation and cleaning)
- Matplotlib / Seaborn (for data visualization)

## Setup

### Prerequisites

- Python 3.x
- Install the following dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shahpankaj123/Big-Data-lab.git
   cd Big-Data-lab
   ```

2. Run the script to scrape data:

   ```bash
   python web_scrap.py
   ```

3. Clean the data and generate the plot:

   ```bash
   python main.ipynb
   ```

4. The cleaned data will be saved in a CSV file, and the plot will be displayed.

## Data Cleaning Process

The raw data scraped from Internshala contains various inconsistencies and missing values. The following cleaning steps were applied:

1. Removed irrelevant columns.
2. Handled missing values by filling or dropping them.
3. Converted columns to the appropriate data types (e.g., date, salary).
4. Removed duplicate entries.

## Visualizations

The following types of visualizations were generated:

- **Bar Plot**: Distribution of internships by location.
- **Pie Chart**: Proportion of internships based on industry.
- **Line Plot**: Trend of internships over time.

## Usage

Once the project is set up, running the script will:

- Scrape the data from Internshala.
- Clean and preprocess the data.
- Generate and display visualizations.

You can modify the parameters or scraping logic based on your needs, such as changing the number of pages to scrape or the type of data to analyze.

## License

Include licensing information here, if applicable.
