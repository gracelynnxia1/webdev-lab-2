import streamlit as st
import info
import pandas as pd

#About Me
def abtme():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write('---')
abtme()

#Sidebar Links
def links():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Check out my work")
    github_link = f'<a href="{info.my_github_url}><img src="{info.email_image_url}" alt="Email" width = "75" height = "75"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href = "mailto:{info.my_email_address}"><img src="{info.email_image_url} alt = "Email" width = "75" height = "75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links()

#Education
def education(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**") # type: ignore
    st.write(f"**Degree:**{education_data['Degree']}")
    st.write(f"**Graduation Date:**{education_data['Graduation Date']}")
    st.write(f"**GPA:**{education_data['GPA']}")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={"code": "Course Code",
        "names": "Course Names", 
        "sem_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index = True
        )
    st.write("---")
education(info.education_data, info.course_data)

#Professional Experience
def experience(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description) in experience_data.items():
        expander = st.expander(f"{job_title}")
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience(info.experience_data)

#Projects
def projects(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
projects(info.projects_data)

#Skills
def skills(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(info.programming_icons)
        skill_icon = info.programming_icons.get(skill, "")
        st.write(f"{skill} {skill_icon}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        spoken_icon = info.spoken_icons.get(spoken, "") 
        st.write(f"{spoken} {spoken_icon}")
skills(info.programming_data, info.spoken_data)

#Activities
def acts(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width = 250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullets in details:
                expander.write(bullet)
    st.write("---")
acts(info.leadership_data, info.activity_data)

