# Retail Sales Analysis (Python & Pandas)

## Overview

This project analyzes retail sales transaction data using Python and Pandas.
The goal is to transform raw sales records into business-ready insights, focusing on revenue trends and category performance.

The project demonstrates an end-to-end workflow:
data cleaning → metric calculation → aggregation → visualization → export.

## Dataset

Input:

data/data_sales.csv
Contains daily transaction-level sales data with store, category, units sold, price, and cost.

Derived outputs:

daily_revenue_summary.csv – daily aggregated revenue

category_performance_summary.csv – category-level revenue and gross profit metrics

## Key Metrics

Revenue = units_sold × price

Gross Profit = (price − cost) × units_sold

Gross Profit % (GP%) = total_gross_profit / total_revenue × 100

Metrics are calculated at both daily and category levels.

## Visualizations

The following charts are generated and saved as PNG files:

Daily Revenue Trend – line chart showing revenue fluctuations over time

Category Revenue Ranking – bar chart sorted by total revenue

Category GP% Ranking – bar chart sorted by gross profit percentage

All charts are export-ready for reports or presentations.

## Project Structure

Python_training/
│
├── data/
│   ├── data_sales.csv
│   ├── daily_revenue_summary.csv
│   └── category_performance_summary.csv
│
├── output/
│   ├── daily_revenue_trend.png
│   ├── category_revenue.png
│   └── category_gp_percent.png
│
└── Train.py


## Tools & Technologies

Python

Pandas

Matplotlib

PyCharm

## Key Insights

Revenue is concentrated in a small number of categories.

High-revenue categories are not always the most profitable.

Margin-driven categories can be strategically important despite lower revenue.

## Purpose

This project was built as a portfolio example to demonstrate practical data analysis skills applicable to:

Retail analytics

Business intelligence

Data engineering foundations
