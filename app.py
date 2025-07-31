import streamlit as st
import pandas as pd

# Head
st.set_page_config(page_title="Career Advisor", layout="centered")

st.title("AI-Powered Career Advisor")
st.write("Suggesting careers based on your strengths, interests, and market demand.")

# Input
name = st.text_input("Enter your name")

subjects = st.multiselect("What subject(s) are you good at?", [
    "Mathematics", "English", "Biology", "Chemistry", "Physics",
    "Economics", "Literature", "Government", "Geography",
    "Computer Science", "Agriculture", "Fine Arts", "History", "Commerce"
])

interests = st.multiselect("What are your interests?", [
    "Technology", "Medicine", "Environment", "Business", "Politics & Law",
    "Creative Arts", "Teaching", "Helping People", "Data & Analytics",
    "Finance", "Writing", "Engineering", "Security"
])

learning_style = st.radio("Your Preferred Learning Style", ["Theoretical", "Practical", "Hands-on", "Visual"])

# Trend Awareness
try:
    trend_df = pd.read_csv("career_trends.csv")
    trend_scores = dict(zip(trend_df["career"], trend_df["demand_score"]))
except:
    trend_scores = {}

# Career Recommendation
def recommend_careers(subjects, interests, learning_style):
    careers = []

    # Tech Fields
    if "Mathematics" in subjects and "Technology" in interests:
        careers += ["Software Engineer", "Data Scientist", "AI/ML Engineer"]
    if "Computer Science" in subjects and "Security" in interests:
        careers += ["Cybersecurity Analyst", "Network Administrator"]
    if "Mathematics" in subjects and "Engineering" in interests:
        careers += ["Mechanical Engineer", "Electrical Engineer"]

    # Medical & Health Fields
    if "Biology" in subjects and "Helping People" in interests:
        careers += ["Nurse", "Public Health Officer", "Medical Lab Technician"]
    if "Chemistry" in subjects and "Medicine" in interests:
        careers += ["Pharmacist", "Biomedical Scientist", "Medicinal Chemist"]

    # Chemistry
    if "Chemistry" in subjects and "Technology" in interests:
        careers += ["Computational Chemist", "Cheminformatics Analyst"]

    if "Chemistry" in subjects and "Environment" in interests:
        careers += ["Green Chemist", "Environmental Chemist", "Waste Management Expert"]

    if "Chemistry" in subjects and "Engineering" in interests:
        careers += ["Materials Scientist", "Battery Researcher", "Nanotechnologist"]

    if "Chemistry" in subjects and "Business" in interests:
        careers += ["Industrial Chemist", "Process Chemist", "Quality Control Analyst"]

    # Business & Finance
    if "Economics" in subjects and "Finance" in interests:
        careers += ["Accountant", "Investment Analyst"]
    if "Commerce" in subjects and "Business" in interests:
        careers += ["Entrepreneur", "Business Analyst", "Sales Manager"]

    # Law & Politics
    if "Government" in subjects and "Politics & Law" in interests:
        careers += ["Lawyer", "Public Policy Analyst", "Civil Servant"]

    # Arts & Humanities
    if "Literature" in subjects and "Writing" in interests:
        careers += ["Journalist", "Author", "Editor"]
    if "Fine Arts" in subjects and "Creative Arts" in interests:
        careers += ["Graphic Designer", "Animator", "Fashion Designer"]
    if "English" in subjects and "Teaching" in interests:
        careers += ["Teacher", "Education Consultant"]

    # Agriculture & Environment
    if "Agriculture" in subjects and "Environment" in interests:
        careers += ["Agronomist", "Environmental Scientist"]
    if "Geography" in subjects and "Environment" in interests:
        careers += ["Urban Planner", "Climate Researcher"]

    # General fallback careers
    if not careers:
        careers += ["Career Counselor", "General Education Officer"]

    # Remove duplicates
    return list(set(careers))

# Output
if st.button("Suggest Careers"):
    if not name or not subjects or not interests:
        st.warning("Please complete all fields to get recommendations.")
    else:
        st.subheader(f"Career Advice for {name}")
        suggested = recommend_careers(subjects, interests, learning_style)

        # Attach trend score
        career_with_scores = []
        for career in suggested:
            score = trend_scores.get(career, 0)
            career_with_scores.append((career, score))

        # Sort by score descending
        career_with_scores.sort(key=lambda x: x[1], reverse=True)

        # Display
        for i, (career, score) in enumerate(career_with_scores, 1):
            if score >= 8:
                tag = "🔥 (High Demand)"
            elif score >= 5:
                tag = "⭐ (Growing Trend)"
            else:
                tag = ""
            st.markdown(f"**{i}. {career} {tag}**")

        st.success("Based on your profile and learning style, these careers may suit you.")
