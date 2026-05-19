# Research Data Handling Project

## Overview

This project demonstrates basic data engineering and data analysis workflows using pandas.

The project includes:
- Loading CSV, JSON, and Excel files
- Cleaning dirty funding data
- Merging multiple datasets
- Aggregating and analyzing research data
- Exporting cleaned results

---

## Project Structure

```text
data/
    researchers.csv
    publications.json
    funding.xlsx

output/
    clean_research_data.csv

venv/
```
## Hardest Part

The hardest parts during this assignment were:

- Understanding the difference between a pandas DataFrame and a Series
- Understanding how boolean filtering works internally in pandas
- Learning how groupby(), aggregation, and idxmax() interact together
- Understanding merge behavior when researcher IDs are repeated in multiple tables
- Understanding the difference between inner joins and left joins
- Debugging duplicated rows created after merge operations
- Handling dirty funding data containing nulls, negative values, and invalid text
- Understanding when to use .iloc[] versus normal indexing []
- Understanding why some pandas operations return labels instead of positional indexes
- Learning how to build reusable cleaning functions instead of writing repeated code
- Debugging path issues and virtual environment activation in VS Code and PowerShell