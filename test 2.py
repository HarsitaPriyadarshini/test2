import ipywidgets as widgets
from IPython.display import display, clear_output

def calculate_bmi(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        
        if height <= 0 or weight <= 0:
            return "Height and Weight must be positive numbers."
        
        bmi = weight / (height / 100) ** 2  # Convert height from cm to meters
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        return f"BMI: {bmi:.2f}\nCategory: {category}"
    except ValueError:
        return "Please enter valid numbers for height and weight."

height_input = widgets.Text(
    value='',
    placeholder='Enter height in cm',
    description='Height (cm):',
    disabled=False
)

weight_input = widgets.Text(
    value='',
    placeholder='Enter weight in kg',
    description='Weight (kg):',
    disabled=False
)

output = widgets.Output()

def on_button_clicked(b):
    with output:
        clear_output()
        result = calculate_bmi(height_input.value, weight_input.value)
        print(result)

button = widgets.Button(description="Calculate BMI")
button.on_click(on_button_clicked)

display(height_input)
display(weight_input)
display(button)
display(output)