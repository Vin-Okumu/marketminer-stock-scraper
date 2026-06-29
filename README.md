# MarketMiner: Yahoo Finance Stock Scraper

## Overview
This project extracts stock market data from Yahoo Finance using Python and Beautiful Soup.

## Objectives

- Retrieve stock information dynamically
- Parse HTML content
- Clean extracted data
- Generate visualizations

## Technologies

- Python
- Beautiful Soup
- Requests
- Pandas
- Matplotlib

## Repository Structure

```text
marketminer-stock-scraper/

│
├── data/
│   └── sample_data/
│       └── stock_sample.csv
│
├── notebooks/
│   └── stock_scraping_analysis.ipynb
│
├── src/
│   ├── scrape.py
│   ├── parse.py
│   ├── clean.py
│   └── utils.py
│
├── outputs/
│   ├── charts/
│   │   ├── stock_trend.png
│   │   └── price_distribution.png
│   │
│   └── csv/
│       └── processed_stock.csv
│
├── images/
│   └── project_banner.png
│
├── .gitignore
├── requirements.txt
├── README.md
├── LICENSE
└── main.py
```

## Sample Data

Sample scraped data can be found in:

data/sample_data/

## Outputs

## Outputs

### Scraped Tesla Data
#### Tesla Revenue Trend

![Tesla Revenue Data](images/tesla_historical_revenue.png)

#### Tesla Stock Price Trend

![Tesla Stock Trend](images/tesla_historical_share_price.png)

### Scraped GameStop Data
#### GameStop Revenue Trend

![GameStop Revenue Data](images/gamestop_historical_revenue.png)

#### GameStop Stock Price Trend
![GameStop Stock Trend](images/gamestop_historical_share_price.png)

## Future Improvements

- Support multiple ticker symbols
- Add Streamlit dashboard
- Automate scheduled scraping