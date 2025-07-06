import streamlit as st
import streamlit.components.v1 as components
import json
import os

# Define all available projects
PROJECTS = {
    "Global Trendz Dashboard": {
        "folder": "project1_global_trendz",
        "title": "💼 Global Trendz Sales Dashboard",
        "link": "https://gbntjiwvxz5dndwaokcmuj.streamlit.app/"
    },
    # Future projects can be added here
    # "Amazon Sales Dashboard": {"folder": "project2_amazon_sales", "title": "📦 Amazon Sales Dashboard"}
}

# Page config
st.set_page_config(page_title="📁 Portfolio", layout="wide")

# Main title
st.markdown("""
    <h1 style='text-align: center; font-size: 3rem; margin-bottom: 0;'>👋 Welcome to Kassem's Portfolio</h1>
    <hr style='margin-top: 10px; margin-bottom: 30px; border: 1px solid #444;'>
""", unsafe_allow_html=True)

# Sidebar project selector
st.sidebar.header("📋 Projects")
selected_project_name = st.sidebar.selectbox("Select a project", list(PROJECTS.keys()))
project_info = PROJECTS[selected_project_name]
project_path = f"projects/{project_info['folder']}"

# Load slides from JSON
slides_path = os.path.join(project_path, "slides.json")
with open(slides_path, encoding="utf-8") as f:
    slides = json.load(f)

# Apply custom styles without background gradient
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        color: #f0f0f0;
        background-color: #0e1117;
        min-height: 100vh;
    }

    .nav-btn {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        color: white;
        font-size: 1.8em;
        padding: 0.2em 0.5em;
        backdrop-filter: blur(8px);
        cursor: pointer;
        transition: 0.3s;
        display: inline-block;
    }
    .nav-btn:hover {
        background: rgba(255, 255, 255, 0.3);
    }
    .description-text {
        font-size: 1.4rem;
        color: #f0f0f0;
        line-height: 2.4;
        padding: 15px;
        border-radius: 12px;
        background-color: rgba(50, 50, 50, 0.4);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    .project-link {
        text-align: center;
        margin-top: 20px;
    }
    .project-link a {
        color: #00c4ff;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .project-divider {
        border: none;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        margin: 60px 0 40px;
    }
</style>
""", unsafe_allow_html=True)

# Display title for the selected project
st.header(project_info["title"])

# External project link
if "link" in project_info:
    st.markdown(f"<div class='project-link'>🔗 <a href='{project_info['link']}' target='_blank'>View Full Project</a></div>", unsafe_allow_html=True)

# Initialize session state for slide index
if 'index' not in st.session_state:
    st.session_state.index = 0

# Display current slide
current_slide = slides[st.session_state.index]

# Main layout (text right, image left)
image_col, desc_col = st.columns([6, 6])

with image_col:
    st.image(os.path.join(project_path, current_slide["image"]), use_container_width=True)

with desc_col:
    st.subheader(f"📌 {current_slide['title']}")
    st.markdown(f"<div class='description-text'>{current_slide['description']}</div>", unsafe_allow_html=True)

# Navigation buttons
col1, col2, col3 = st.columns([1, 10, 1])
with col1:
    if st.button("⬅", key="left"):
        st.session_state.index = (st.session_state.index - 1) % len(slides)
with col3:
    if st.button("➡", key="right"):
        st.session_state.index = (st.session_state.index + 1) % len(slides)

# Visual divider before future projects
st.markdown("<hr class='project-divider'>", unsafe_allow_html=True)

# Placeholder: future project sections will go here
# st.subheader("Next Project Coming Soon...")
