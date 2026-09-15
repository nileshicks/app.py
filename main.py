import streamlit as st

# ==========================================
# PAGE CONFIGURATION & CUSTOM STYLING (CSS)
# ==========================================
st.set_page_config(
    page_title="Niles Hicks | Cybersecurity Portfolio",
    page_icon="🛡️",
    layout="wide"
)

# Dark cybersecurity-themed CSS styling
st.markdown("""
<style>
    /* Dark Theme Backgrounds */
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }

    /* Headers Styling */
    h1, h2, h3 {
        color: #00FF66 !important; /* Cyber Green Accent */
        font-family: 'Courier New', Courier, monospace;
    }

    /* Custom Card Style for Sections */
    .css-card {
        background-color: #161B22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363D;
        margin-bottom: 20px;
    }

    /* Custom Badge for Skills */
    .badge {
        background-color: #21262D;
        color: #58A6FF;
        padding: 5px 10px;
        border-radius: 15px;
        border: 1px solid #30363D;
        font-size: 0.9em;
        margin-right: 5px;
        display: inline-block;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER / CONTACT INFORMATION
# ==========================================
st.title("🛡️ Niles Ashur Hicks")
st.subheader("Cybersecurity Undergraduate Student")
st.write("📍 Olive Branch, MS | ✉️ Ashurhicks@gmail.com | 🔗 [LinkedIn Profile](https://www.linkedin.com/in/nileshicks)")

st.divider()

# ==========================================
# PROFESSIONAL SUMMARY
# ==========================================
st.header("📋 Professional Summary")
st.write(
    "I am a junior cybersecurity undergraduate student with a strong academic foundation in network security and "
    "automation with Python. I have hands-on experience with helpdesk, SIEM tools, SQL, analyzing incident logs, "
    "and creating incident reports from academic projects and certification programs. I am highly coachable and eager "
    "to continue learning about the changing landscape of cybersecurity and leverage my technical and social skills "
    "to improve cybersecurity."
)

st.divider()

# ==========================================
# EDUCATION & CERTIFICATIONS
# ==========================================
col1, col2 = st.columns(2)

with col1:
    st.header("🎓 Education")
    st.markdown("""
    **Grambling State University** – Grambling, LA  
    *Bachelor of Science in Cybersecurity*  
    * **Expected Graduation:** May 2027  
    * **GPA:** 3.77  

    **Relevant Coursework:**  
    Foundations of Cybersecurity, Computer Science II, Information System Threats and Attacks, 
    Data Structures and Algorithms, Software Security, Applied Cryptography, Application Security, 
    Computer Organization/Architecture.
    """)

with col2:
    st.header("📜 Certifications")
    st.markdown("""
    * **Google Cybersecurity Professional Certificate (v.2)**
    """)

st.divider()

# ==========================================
# TECHNICAL SKILLS
# ==========================================
st.header("🛠️ Technical Skills")

st.subheader("Security Domains")
st.markdown("""
<span class="badge">Vulnerability Assessment</span>
<span class="badge">Incident Response</span>
<span class="badge">Log Analysis</span>
<span class="badge">Threat Intelligence</span>
<span class="badge">Network Defense</span>
""", unsafe_allow_html=True)

st.subheader("Tools & Platforms")
st.markdown("""
<span class="badge">Wireshark</span>
<span class="badge">Splunk</span>
<span class="badge">Nmap</span>
<span class="badge">Active Directory</span>
""", unsafe_allow_html=True)

st.subheader("Programming & Scripting")
st.markdown("""
<span class="badge">Python</span>
<span class="badge">PowerShell</span>
<span class="badge">SQL</span>
""", unsafe_allow_html=True)

st.subheader("Operating Systems")
st.markdown("""
<span class="badge">Kali Linux</span>
<span class="badge">Windows Server</span>
<span class="badge">Windows 10/11</span>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# ACCOMPLISHMENTS, AWARDS & LEADERSHIP
# ==========================================
st.header("🏆 Awards & Leadership")
st.markdown("""
* **4x** Dean's List
* **2x** Grambling Cybersecurity Scholarship Recipient
""")

st.divider()

# ==========================================
# PROJECTS (Placeholder for future updates)
# ==========================================
st.header("💻 Projects")
# To add future projects: Replace the string below with project details or code blocks!
st.info("No Info at this time")

st.divider()

# ==========================================
# EXPERIENCE / WORK HISTORY (Placeholder)
# ==========================================
st.header("💼 Work Experience")
st.info("No Info at this time")

st.divider()

# ==========================================
# SECURITY LABS & WRITEUPS (Placeholder)
# ==========================================
st.header("🧪 Security Labs & Writeups")
st.info("No Info at this time")

st.divider()

# ==========================================
# FOOTER
# ==========================================
st.caption("© 2026 Niles Hicks • Built with Python & Streamlit")