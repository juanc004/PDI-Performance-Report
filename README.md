
# PDI-Performance-Report Generator

## Description
This Python script reads WCN Progress Check data, performs more specific data aggregations, calculates individual and team averages for various WCN events, and generates a detailed PDI Performance Report including new metrics and rankings. The script has been updated to include more robust features, improved data aggregation, and additional metrics.

## Requirements
- Python 3.x
- Pandas library
- `os` library (Optional for future updates)

Install the required packages using:
```bash
pip install -r requirements.txt
```

## How to Run
1. Place your `pdit_wcn_progress_check_wk.csv` in the designated directory.
2. Update the `csv_file_path` in the script with the path where your CSV file is located.
3. Update the `save_path` in the script with the path where you'd like to save the output CSV file.
4. Run the script.

## Features
- Reads WCN Progress Check data from a specific CSV file.
- Performs data aggregation with `numeric_only=True` parameter for accurate calculations.
- Calculates individual and team averages for various WCN events.
- Generates a sorted GPSDSU Performance Report with additional team average metrics.
- Sorts the report by last names in alphabetical order.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## Changelog
For all notable changes to this project, see [CHANGELOG.md](CHANGELOG.md).
