import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the page title and layout
st.set_page_config(page_title="My Interactive Website", layout="wide")

# Website Title
st.title("Welcome to My Interactive Streamlit Website")

# Add a description
st.write("""
    This is a simple website built with Streamlit. It demonstrates user interaction
    with input fields, buttons, and data visualization. Let's explore together!
""")

# Sidebar for navigation and user input
st.sidebar.title("Navigation")

# Text input field for user to enter their name
name = st.sidebar.text_input("Enter your name", "")

# If the user enters a name, greet them
if name:
    st.sidebar.write(f"Hello, {name}! Welcome to the site.")

# Slider to choose a number
number = st.sidebar.slider("Select a number", 1, 100, 50)

# Display number and calculate the square of the number
st.write(f"The square of {number} is {number**2}")

# Button to trigger an action
if st.sidebar.button('Click Me!'):
    st.sidebar.write(f"Welcome {name}, enjoy exploring Streamlit!")

# DataFrame display (simple table)
st.write("Here is some sample data to showcase a table:")

# Updated product names
data = {
    'Product': ['Smartphone', 'Laptop', 'Headphones', 'Tablet'],
    'Price': [25, 40, 30, 50],
    'Stock': [100, 50, 75, 30]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Plot a simple line chart
st.write("Here's a simple line chart showing data trends:")

# Create a random dataset and plot a line chart
data = pd.DataFrame({
    'Day': np.arange(1, 11),
    'Sales': np.random.randint(20, 100, size=10)
})

fig, ax = plt.subplots()
ax.plot(data['Day'], data['Sales'], marker='o', color='b', label='Sales')

ax.set_title('Sales Data Over Time')
ax.set_xlabel('Day')
ax.set_ylabel('Sales')
ax.legend()

st.pyplot(fig)

# Footer section
st.write("---")
st.write("Built with Streamlit. Have fun exploring!")
