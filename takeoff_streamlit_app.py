
import streamlit as st

def calculate_area(length, width):
    return length * width

def calculate_volume(length, width, height):
    return length * width * height

def save_result(text):
    with open("takeoff_results.txt", "a") as file:
        file.write(text + "\n")

def reset_file():
    with open("takeoff_results.txt", "w") as file:
        file.write("Takeoff Summary\n")
        file.write("----------------\n")

# Streamlit UI
st.title("📐 Quantity Takeoff Estimator")
st.subheader("Choose your takeoff type and enter values:")

if st.button("🔁 Reset File"):
    reset_file()
    st.success("File reset successfully.")

item_name = st.text_input("Enter item name (e.g. wall, tile, concrete):")
takeoff_type = st.selectbox("Select takeoff type", ["Count", "Area", "Volume"])

if takeoff_type == "Count":
    count = st.number_input("Enter number of items", min_value=0, step=1)
    if st.button("➕ Add Count"):
        result = f"{item_name} - Count: {int(count)} units"
        st.success(result)
        save_result(result)

elif takeoff_type == "Area":
    length = st.number_input("Length (m)", min_value=0.0, step=0.1)
    width = st.number_input("Width (m)", min_value=0.0, step=0.1)
    if st.button("➕ Add Area"):
        area = calculate_area(length, width)
        result = f"{item_name} - Area: {area:.2f} sq.m"
        st.success(result)
        save_result(result)

elif takeoff_type == "Volume":
    length = st.number_input("Length (m)", min_value=0.0, step=0.1)
    width = st.number_input("Width (m)", min_value=0.0, step=0.1)
    height = st.number_input("Height (m)", min_value=0.0, step=0.1)
    if st.button("➕ Add Volume"):
        volume = calculate_volume(length, width, height)
        result = f"{item_name} - Volume: {volume:.2f} cu.m"
        st.success(result)
        save_result(result)

if st.button("📄 Show Summary"):
    try:
        with open("takeoff_results.txt", "r") as file:
            content = file.read()
        st.text_area("📊 Takeoff Summary", content, height=200)
    except FileNotFoundError:
        st.warning("No summary file found. Please add some items.")
