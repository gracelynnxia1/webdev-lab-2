import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON data
with open("data.json", "r") as file:
    data = json.load(file)

# Initialize session state
if "selected_city" not in st.session_state:
    st.session_state.selected_city = "Barcelona"

if "study_hours" not in st.session_state:
    st.session_state.study_hours = data[st.session_state.selected_city]["study_hours"]

#Header
def overview():
    st.header("My Study Abroad!")
    st.subheader("Oxford Program 2024")
    st.image("images/granadaheader.jpg", width = 400)
    st.write('---')
overview()

#Select a city
st.write("### Select a city:")
st.session_state.selected_city = st.selectbox("Choose a city", list(data.keys())[:-1]) #NEW
st.session_state.study_hours = data[st.session_state.selected_city]["study_hours"]

st.write(f"## Currently Viewing: {st.session_state.selected_city}")
city_images = {
    "Barcelona": "images/barcelona.jpg",
    "Madrid": "images/madrid.jpg",
    "Granada": "images/granada.JPEG",
    "Oxford": "images/oxford (3).jpg"
}

st.image(city_images[st.session_state.selected_city], caption = f"View of {st.session_state.selected_city}", width = 600)

#Study hours
avg_study_hours = sum(st.session_state.study_hours) / len(st.session_state.study_hours)
st.metric(label="Average Study Hours Per Week", value=round(avg_study_hours,2))

#Expenses dynamic graph
st.write("### Expenses Over a Week")
days = data["days"]
expenses = data[st.session_state.selected_city]["expenses"]

fig, ax = plt.subplots()
ax.plot(days, expenses, marker="o", linestyle="-", color="blue", label="Daily Expenses")
ax.set_xlabel("Days")
ax.set_ylabel("Expenses ($)")
ax.set_title("Daily Expenses in" + st.session_state.selected_city)
ax.set_title("Daily Expenses in " + st.session_state.selected_city)
ax.legend()
st.pyplot(fig)

#Study hsurs dynamic graph 
st.write("### Study Hours Over a Week")
user_adjustment = st.slider("Adjust Study Hours (+/- 2 hours)", -2.0, 2.0, 0.0, 0.1)
expected_study_hours = data[st.session_state.selected_city]["study_hours"]
actual_study_hours = [max(0, h + user_adjustment) for h in expected_study_hours]

fig2, ax2 = plt.subplots()
ax2.plot(days, expected_study_hours, marker="o", linestyle="-", color="green", label="Expected")
ax2.plot(days, actual_study_hours, marker="s", linestyle="--", color="red", label = "Adjusted")
ax2.set_xlabel("Days")
ax2.set_ylabel("Study Hours")
ax2.set_title("Study Hours in " + st.session_state.selected_city)
ax2.legend()
st.pyplot(fig2)

#How was the food at OXford? input
if st.session_state.selected_city == "Oxford":
    st.write("### How do you think the food at Oxford was?")
    food_feedback = st.radio("Your answer:", ["Great", "Okay", "Bad"])
    if food_feedback == "Great":
        st.write("How much do you know about English food...")
    elif food_feedback == "Okay":
        st.write("I wish...")
    else:
        st.write("Yeah that sounds about right!")


#have buttons that the user can click and each button leads to a page
#which of the cities I visited would you like to visit?
#^user input, have options for 4 cities
    #barcelona, madrid, granada, oxford

#barcelona
#4 pics and captions, have them in columns using col function
#dynamic graph that shifts for money spent?

#madrid
#4 pics and captions
#static graph for days i was sick
#streamlit func

#granada
#4 pics and captions
#streamlit func

#oxford
#4 pics and captions
#dynamic graph for hours studied/grades or smthn
#guess how good the food was at oxford
    #user input
    #good -> not quite 
    #bad -> how did you know?!

#ask user would you ever study abroad and have option to record an audio message that I can see