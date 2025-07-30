import streamlit as st

st.set_page_config(page_title="Smart Career Advisor", layout="centered")

st.title("🎓 Smart Career Advisor")
st.write("Helping students choose the right career based on their strengths and interests.")

# --- User Inputs ---
name = st.text_input("Student Name")
subjects = st.multiselect(
    "Which subjects are you strong in?",
    ["Mathematics", "English", "Biology", "Chemistry", "Physics", "Government", "Literature", "Economics", "Geography", "Computer Science"]
)

interests = st.multiselect(
    "What are your interests?",
    ["Technology", "Helping People", "Creative Arts", "Business", "Law and Politics", "Nature & Environment", "Medicine", "Problem Solving"]
)

learning_style = st.radio(
    "What is your preferred learning style?",
    ["Practical", "Theoretical", "Visual", "Hands-on"]
)

# --- Career Logic ---
def recommend_careers(subjects, interests):
    recommendations = []

    if "Mathematics" in subjects and "Technology" in interests:
        recommendations.append("Software Engineer")
        recommendations.append("Data Scientist")

    if "Biology" in subjects and "Helping People" in interests:
        recommendations.append("Nurse")
        recommendations.append("Public Health Officer")

    if "Literature" in subjects and "Law and Politics" in interests:
        recommendations.append("Lawyer")
        recommendations.append("Public Policy Analyst")

    if "Economics" in subjects and "Business" in interests:
        recommendations.append("Entrepreneur")
        recommendations.append("Accountant")

    if "Chemistry" in subjects and "Nature & Environment" in interests:
        recommendations.append("Environmental Scientist")
        recommendations.append("Chemical Engineer")

    if "Computer Science" in subjects and "Problem Solving" in interests:
        recommendations.append("AI/ML Engineer")
        recommendations.append("Cybersecurity Analyst")

    if not recommendations:
        recommendations.append("Education Counselor")
        recommendations.append("General Career Advisor")

    return recommendations

# --- Output ---
if st.button("Suggest Careers"):
    if name == "" or not subjects or not interests:
        st.warning("Please complete all fields.")
    else:
        st.subheader(f"👤 Career Advice for {name}")
        careers = recommend_careers(subjects, interests)

        for i, career in enumerate(careers, 1):
            st.markdown(f"**{i}. {career}**")

        st.info("💡 Based on your strengths and interests, these careers are trending and suitable for you.")
