# Retail Sales Data Processing and Business Insights Generation

## Overview

This project implements an end-to-end data engineering workflow for retail sales data. The objective was to transform raw retail transaction data into a clean analytical dataset and generate  business insights through KPI reporting and Power BI dashboards.

The solution includes data profiling, data cleaning, transformation, PII masking, KPI generation, and business intelligence reporting.

---

## Project Objectives

* Assess data quality issues in retail transaction data
* Handle missing and inconsistent data
* Standardize product and category information
* Protect sensitive customer information through PII masking
* Generate business KPIs
* Build interactive dashboards for business reporting

---

## Technology Stack

* Python
* Pandas
* Power BI Desktop
* VS Code

---

## Data Engineering Workflow

Raw Excel Workbook

↓

Data Ingestion

↓

Data Profiling

↓

Data Cleaning & Transformation

↓

PII Masking

↓

Revenue Calculation

↓

KPI Generation

↓

Power BI Dashboard

---

## Key Data Processing Activities

### Data Profiling

* Missing value analysis
* Duplicate record detection
* Invalid quantity identification
* Data quality assessment

### Data Cleaning

* Missing price handling using product master data
* Invalid quantity removal
* Date standardization
* Product standardization
* Category standardization

### Data Privacy

* Email masking
* Phone number masking

### KPI Generation

* Total Revenue
* Total Transactions
* Total Customers
* Average Order Value (AOV)
* Revenue by Category
* Revenue by City
* Revenue by Payment Method
* Monthly Revenue Trends

---

## Dashboard Pages

### Executive Dashboard

* Revenue Overview
* Customer Metrics
* Revenue by Category
* Revenue by City

### Product Performance

* Product Revenue Analysis
* Category Contribution
* Product Ranking

### Regional Insights

* Revenue by City
* Revenue by Payment Method

### Revenue Trends

* Monthly Revenue Analysis
* Transaction Trends

---

## Key Insights

* Electronics generated the highest revenue among all product categories.
* Laptop was the highest revenue-generating product.
* Chennai generated the highest city-level revenue.
* Revenue distribution across major cities remained relatively balanced.
* Clothing contributed the lowest share of total revenue.
* Standardization improved aggregation accuracy and reporting consistency.

---

## Repository Structure

* code/ → Python scripts for profiling, cleaning, and KPI generation
* output/ → Cleaned datasets and KPI output files
* powerbi/ → Power BI dashboard (.pbix)
* documentation/ → Project report and dashboard screenshots

---

## Deliverables

* Data Profiling Script
* Data Cleaning & Transformation Script
* KPI Generation Script
* Cleaned Dataset
* Power BI Dashboard
* Project Documentation

---


## Implementation Note

The solution was implemented locally using Python (Pandas) and Power BI, in accordance with the assessment guidelines which allowed local implementation as an alternative to Azure-based deployment.




