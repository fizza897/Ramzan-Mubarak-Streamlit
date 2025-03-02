import streamlit as st
import pandas as pd
import plotly.express as px 
import requests
import random  

# ✅ Set Page Configuration (Wide Layout)
st.set_page_config(page_title="🌙 Ramzan Insights", layout="wide")

# ✅ Random Background Image
bg_images = [
    "https://media.istockphoto.com/id/1881660531/photo/islamic-background-silhouette-mosques-dome-crescent-moon-on-dusk-sky-twilight-landscape.jpg?s=1024x1024&w=is&k=20&c=QWZsBNHmq7__BpqNLm0DKmNHn7Vvx8LSrosUxIzpldw=",
    "https://plus.unsplash.com/premium_photo-1723662241766-1e9f0c3e72f5?q=80&w=1438&auto=format&fit=crop",
    "https://plus.unsplash.com/premium_photo-1677587536653-0d02efbb70ee?q=80&w=1470&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1537181534458-45dcee76ae90?q=80&w=1527&auto=format&fit=crop"
]
st.markdown(f'''
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("{random.choice(bg_images)}");
            background-size: cover;
            background-position: center;
        }}
    </style>
''', unsafe_allow_html=True)

# ✅ Sehri/Iftar API Fetch Function
def fetch_sehri_iftar(city="Karachi"):
    try:
        url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Pakistan&method=2"
        response = requests.get(url).json()
        return response['data']['timings']['Fajr'], response['data']['timings']['Maghrib']
    except:
        return "04:45 AM", "06:30 PM"  # Default Values

# ✅ Sample Data (Replace with Real Data)
data = pd.DataFrame({
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta'],
    'Zakat Collection (PKR)': [80000, 60000, 75000, 50000, 45000],
    'Taraweeh Attendance (%)': [90, 85, 88, 75, 80],
    'Avg Fast Duration (hrs)': [14.5, 14.3, 14.7, 14.2, 14.6],
    'Charity Distribution (PKR)': [50000, 35000, 40000, 30000, 28000]
})

# ✅ Fetch Sehri/Iftar Timings
sehri_time, iftar_time = fetch_sehri_iftar()

# ✅ Sidebar Customization
sidebar_images = [
    "https://images.unsplash.com/photo-1576764402988-7143f9cca90a?q=80&w=1480&auto=format&fit=crop",
    "https://plus.unsplash.com/premium_photo-1723532605982-5b2cc9d9b28d?q=80&w=1460&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://arynews.tv/wp-content/uploads/2017/05/Ramazan_Crescent.jpg",
    "https://plus.unsplash.com/premium_photo-1672753749524-7553762bfb0e?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZGF0ZXN8ZW58MHx8MHx8fDA%3D"
]
st.sidebar.image(random.choice(sidebar_images), use_container_width=True)
st.sidebar.header("📊 Customize Your Graph")
x_label = st.sidebar.selectbox("X-axis", data.columns, index=0)
y_label = st.sidebar.selectbox("Y-axis", data.columns, index=1)
color_label = st.sidebar.selectbox("Color", data.columns, index=2)
graph_type = st.sidebar.selectbox("Graph Type", ["Bar", "Scatter", "HeatMap", "Pie", "Line", "Box Plot"])

# ✅ Main Section: Title & Sehri/Iftar Timings
banner_images = [
    "https://images.unsplash.com/photo-1740330794911-fb4479e06ad0?q=80&w=1574&auto=format&fit=crop"
]
st.image(random.choice(banner_images), use_container_width=True)
st.markdown("<h1 style='color:black;'>🌙 Ramzan Insights: Zakat, Taraweeh & Fast Duration</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='color:black;'>🕌 Karachi Sehri Time: {sehri_time} | 🍽️ Iftar Time: {iftar_time}</h1>", unsafe_allow_html=True)

# ✅ Function to Generate Graphs
def visualize(graph):
    if graph == "Bar":
        return px.bar(data, x=x_label, y=y_label, color=color_label if color_label in data.columns else None, title=f"{y_label} vs {x_label}")

    elif graph == "Scatter":
        return px.scatter(data, x=x_label, y=y_label, color=color_label if color_label in data.columns else None, title=f"{y_label} vs {x_label}")

    elif graph == "HeatMap":
        return px.density_heatmap(data, x=x_label, y=y_label, z=color_label if color_label in data.columns else None,
                              title=f"HeatMap of {y_label} vs {x_label}")
    elif graph== "Pie":
            return px.density_heatmap(data, x=x_label, y=y_label, color_continuous_scale="Viridis", title=f"HeatMap of {y_label} vs {x_label}")

    elif graph == "Pie":
        return px.pie(data, names=x_label, values=y_label, title=f"{y_label} Distribution")

    elif graph == "Line":
        return px.line(data, x=x_label, y=y_label, color=color_label if color_label in data.columns else None, title=f"{y_label} vs {x_label}")

    elif graph == "Box Plot":
        return px.box(data, x=x_label, y=y_label, color=color_label if color_label in data.columns else None, title=f"{y_label} vs {x_label}")

    else:
        return None  # ✅ If the graph type doesn't match, return None

# ✅ Streamlit Graph Display
st.plotly_chart(visualize(graph_type))

# ✅ Ramzan Reports Section
st.markdown("<h2 style='color:black;'>📜 Ramzan Reports</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

report_images = {
    "zakat": ["https://plus.unsplash.com/premium_photo-1723507273388-c27258881aa3?q=80&w=1388&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"],
    "taraweeh": ["https://plus.unsplash.com/premium_photo-1678463088813-97062d92400a?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"],
    "fasting": ["data:image/jpeg;base64,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"],
    "charity":["https://img.freepik.com/free-photo/medium-shot-people-celebrating-eid-al-fitr_23-2151205063.jpg?t=st=1740843312~exp=1740846912~hmac=d9b971e47d7d3f7eaa1122b505fb1f2a28a8f2e1455f5d9f1ceb150377386d72&w=1060"]
  
}

def show_report(button_label, key):
    if st.button(button_label):
        st.image(random.choice(report_images[key]), use_container_width=True)
        highest_index = data[key.capitalize() + " Collection (PKR)"].idxmax() if key == "zakat" else data[key.capitalize() + " Attendance (%)"].idxmax() if key == "taraweeh" else data["Avg Fast Duration (hrs)"].idxmax() if key == "fasting" else data["Charity Distribution (PKR)"].idxmax()
        highest = data.iloc[highest_index]
        st.write(highest)

with col1:
    show_report("💰 Highest Zakat Collection", "zakat")
    show_report("🕌 Highest Taraweeh Attendance", "taraweeh")

with col2:
    show_report("⏳ Longest Fast Duration", "fasting")
    show_report("🤲 Highest Charity Distribution", "charity")

# ✅ Zakat Calculator
zakat_images = [
    "https://images.unsplash.com/photo-1637597384601-61e937e8bc15?q=80&w=1374&auto=format&fit=crop",
    "https://plus.unsplash.com/premium_photo-1682309657823-d49903c38fbb?q=80&w=1512&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1657972590667-5d94b96ec583?q=80&w=1331&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1552481298-205046c383cf?q=80&w=1470&auto=format&fit=crop"
]
st.markdown("<h2 style='color: black;'>💰 Zakat Calculator</h2>", unsafe_allow_html=True)
st.image(random.choice(zakat_images), use_container_width=True)

st.markdown("<p style='color:black; font-weight:bold;'>Enter Your Savings (PKR)</p>", unsafe_allow_html=True)
amount = st.number_input("", min_value=0)

if st.button("Calculate Zakat"):
    zakat = amount * 0.025
    st.success(f"Your Zakat Payable: PKR {zakat:.2f}")
st.markdown("<p style='color: black; font-size:16px;'>💡 <b>Tip:</b> Customize your graphs using the sidebar & explore different reports!</p>", unsafe_allow_html=True)

