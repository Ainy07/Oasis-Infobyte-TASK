# BMI Calculator with Tkinter and SQLite
This project is a simple BMI (Body Mass Index) Calculator built using Python's Tkinter for the graphical user interface (GUI) and SQLite for data storage. It allows users to calculate their BMI, classify it into categories, and track their BMI history over time.

## Features
- BMI Calculation: Calculates BMI based on user-inputted weight and height.
- BMI Classification: Classifies BMI into categories such as Underweight, Normal weight, Overweight, and Obese.
- Data Storage: Saves each BMI calculation along with the date, time, and user information into an SQLite database.
- ata Visualization: Plots a graph of BMI values over time for a specified user, using Matplotlib.
## Installation
### Prerequisites
- Python 3.x
- Required Python packages: tkinter, sqlite3, matplotlib
You can install the required packages using pip:

```
pip install matplotlib
```

## Usage
1. Run the Application: Start the application by running the following command:

```
python bmi_calculator.py
```
2. Calculate BMI:

-  Enter your name, weight (in kilograms), and height (in meters).
- Click the "Calculate BMI" button to calculate your BMI and see the classification.

3. View Data:

- Click the "View Data" button to see a graph of your BMI over time.
- The graph will display BMI values recorded in the database for the entered name.

# How It Works
1. BMI Calculation: The BMI is calculated using the formula:

BMI
=
Weight (kg)
Height (m)
2

 
2. BMI Classification:

- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 24.9
- Overweight: 25 ≤ BMI < 29.9
- Obese: BMI ≥ 30
3. Data Storage: The BMI data, along with the user's name, weight, height, and classification, is stored in an SQLite database (bmi_data.db).

4. Data Visualization: The BMI data over time is plotted using Matplotlib, providing a visual representation of the user's BMI trends.

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- This project was created to demonstrate the integration of Python's Tkinter, SQLite, and Matplotlib libraries in a real-world application.