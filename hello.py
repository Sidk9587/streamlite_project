import streamlit as st


st.set_page_config(
    page_title="Siddharth Kharat | AI & Flutter Developer",
    page_icon="SK",
    layout="wide",
    initial_sidebar_state="collapsed",
)


PROFILE = {
    "name": "Siddharth Kharat",
    "role": "AI & Data Science Engineer | Flutter Developer",
    "location": "Pune, India",
    "email": "siddharthkharat881@gmail.com",
    "phone": "+91-9011711894",
    "linkedin": "https://www.linkedin.com/in/siddharth-kharat-4a752a257",
    "github": "https://github.com/Sidk9587",
}

SKILLS = {
    "Languages": ["Python", "C++", "Dart", "MySQL"],
    "Mobile & UI": ["Flutter", "Responsive UI", "UI/UX", "SQFlite"],
    "Data & ML": ["Machine Learning", "Pandas", "NumPy", "Matplotlib", "scikit-learn"],
    "Platforms": ["Git", "GitHub", "GitLab", "AWS EC2", "AWS S3"],
    "Core CS": ["Data Structures", "Algorithms", "OOP", "REST APIs"],
}

PROJECTS = [
    {
        "title": "PAN Card Tampering Detector",
        "time": "Jul 2025",
        "type": "Computer Vision",
        "description": (
            "Flask-based verification app that detects tampering in PAN card images "
            "using SSIM comparison, OpenCV contours, PIL, and scikit-image."
        ),
        "impact": "Highlights altered regions with visual feedback for clearer fraud review.",
        "tech": ["Python", "Flask", "OpenCV", "SSIM", "PIL"],
        "link": "https://github.com/Sidk9587/pancard-tampering",
    },
    {
        "title": "Sales Prediction Using Python",
        "time": "Mar 2024",
        "type": "Machine Learning",
        "description": (
            "Linear regression model for predicting sales from advertising spend, "
            "supported by exploratory charts and performance visualization."
        ),
        "impact": "Turns raw campaign spend into a simple forecasting workflow.",
        "tech": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
        "link": "https://github.com/Sidk9587/CodeAlpha",
    },
    {
        "title": "Quiz App",
        "time": "Apr 2025",
        "type": "Flutter App",
        "description": (
            "Responsive mobile quiz app for machine learning knowledge checks with "
            "real-time validation, score tracking, and dynamic UI updates."
        ),
        "impact": "Creates a fast and polished learning loop for mobile users.",
        "tech": ["Flutter", "Dart", "Mobile UI"],
        "link": "https://github.com/Sidk9587/QuizApp",
    },
    {
        "title": "DailySync",
        "time": "Oct 2025",
        "type": "Productivity App",
        "description": (
            "Unified life-management Flutter app with modules for health, finance, "
            "tasks, and routine scheduling."
        ),
        "impact": "Combines Firebase services with local SQFlite storage for offline use.",
        "tech": ["Flutter", "Dart", "Firebase", "SQFlite"],
        "link": "https://github.com/Sidk9587/Dailysync",
    },
]

EDUCATION = [
    {
        "degree": "B.E. in Artificial Intelligence & Data Science",
        "school": "Dr. D. Y. Patil Institute of Technology",
        "place": "Pune, India",
        "result": "CGPA 8.45 / 10",
        "year": "2026",
    },
    {
        "degree": "12th HSC",
        "school": "Smt. Kasturbai Walchand College",
        "place": "Sangli, India",
        "result": "78.83%",
        "year": "2022",
    },
    {
        "degree": "10th SSC",
        "school": "Bethesda School",
        "place": "Miraj, India",
        "result": "88.40%",
        "year": "2020",
    },
]


def chips(items):
    return "".join(f"<span class='chip'>{item}</span>" for item in items)


def metric(label, value):
    return f"""
    <div class="metric">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
    """


STYLE = """
<style>
:root {
  --ink: #f8fafc;
  --muted: #a8b3c7;
  --line: rgba(148, 163, 184, 0.2);
  --panel: rgba(11, 18, 32, 0.78);
  --panel-strong: rgba(15, 23, 42, 0.94);
  --cyan: #38bdf8;
  --green: #34d399;
  --amber: #f59e0b;
  --rose: #fb7185;
  --bg: #050914;
}

html {
  scroll-behavior: smooth;
}

[data-testid="stAppViewContainer"] {
  background:
    linear-gradient(rgba(148, 163, 184, 0.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(148, 163, 184, 0.045) 1px, transparent 1px),
    linear-gradient(135deg, #050914 0%, #07111f 45%, #0b1220 100%);
  background-size: 44px 44px, 44px 44px, auto;
  color: var(--ink);
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"] {
  background: transparent;
}

.main .block-container {
  padding-top: 1.4rem;
  padding-bottom: 2rem;
  max-width: 1180px;
}

h1, h2, h3, h4, p, li, span, label {
  color: var(--ink);
}

a {
  color: inherit;
  text-decoration: none;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  padding: 0.8rem 1rem;
  margin-bottom: 1.4rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(5, 9, 20, 0.84);
  backdrop-filter: blur(18px);
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-weight: 800;
}

.brand-mark {
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border: 1px solid rgba(56, 189, 248, 0.45);
  border-radius: 8px;
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.18), rgba(52, 211, 153, 0.12));
  color: #e0f2fe;
}

.navlinks {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 0.35rem;
}

.navlinks a,
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  padding: 0.62rem 0.88rem;
  border: 1px solid transparent;
  border-radius: 8px;
  color: var(--muted);
  font-size: 0.92rem;
  font-weight: 700;
  transition: color 180ms ease, border-color 180ms ease, background 180ms ease, transform 180ms ease;
}

.navlinks a:hover,
.btn:hover {
  color: var(--ink);
  border-color: rgba(56, 189, 248, 0.4);
  background: rgba(56, 189, 248, 0.09);
  transform: translateY(-1px);
}

.btn.primary {
  color: #04111f;
  border-color: rgba(56, 189, 248, 0.7);
  background: linear-gradient(135deg, #38bdf8, #34d399);
}

.section {
  margin: 2.4rem 0;
  scroll-margin-top: 110px;
}

.section-title {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1rem;
}

.eyebrow {
  margin: 0 0 0.55rem;
  color: var(--green);
  font-size: 0.82rem;
  font-weight: 800;
  text-transform: uppercase;
}

.section-title h2 {
  margin: 0;
  font-size: clamp(1.7rem, 3vw, 2.5rem);
  line-height: 1.1;
}

.section-title p,
.muted {
  color: var(--muted);
}

.hero {
  position: relative;
  overflow: hidden;
  min-height: 640px;
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(340px, 0.9fr);
  gap: 2rem;
  align-items: center;
  padding: 3rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background:
    linear-gradient(120deg, rgba(56, 189, 248, 0.11), transparent 34%),
    linear-gradient(240deg, rgba(52, 211, 153, 0.12), transparent 38%),
    rgba(8, 13, 28, 0.82);
  box-shadow: 0 24px 90px rgba(0, 0, 0, 0.34);
}

.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
  background-size: 80px 100%;
  opacity: 0.55;
  pointer-events: none;
}

.hero-copy,
.hero-stage {
  position: relative;
  z-index: 2;
}

.hero h1 {
  max-width: 760px;
  margin: 0;
  font-size: clamp(3rem, 6vw, 5.8rem);
  line-height: 1.02;
  font-weight: 900;
}

.hero h1 span {
  background: linear-gradient(90deg, #e0f2fe, #38bdf8 42%, #34d399 74%, #f59e0b);
  -webkit-background-clip: text;
  color: transparent;
}

.hero-lede {
  max-width: 680px;
  margin: 1.3rem 0 0;
  color: #cbd5e1;
  font-size: 1.08rem;
  line-height: 1.8;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-top: 1.6rem;
}

.hero-proof {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.7rem;
  max-width: 660px;
  margin-top: 1.7rem;
}

.metric {
  min-height: 92px;
  padding: 0.9rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.72);
}

.metric span {
  display: block;
  color: var(--muted);
  font-size: 0.83rem;
}

.metric strong {
  display: block;
  margin-top: 0.45rem;
  font-size: 1.35rem;
}

.hero-stage {
  min-height: 460px;
  perspective: 1100px;
}

.orbit-scene {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  transform-style: preserve-3d;
  animation: sceneFloat 8s ease-in-out infinite;
}

.cube {
  position: relative;
  width: 190px;
  height: 190px;
  transform-style: preserve-3d;
  animation: cubeSpin 16s linear infinite;
}

.face {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border: 1px solid rgba(125, 211, 252, 0.52);
  border-radius: 8px;
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.88), rgba(56, 189, 248, 0.18));
  box-shadow: inset 0 0 38px rgba(56, 189, 248, 0.14), 0 22px 60px rgba(0, 0, 0, 0.32);
  color: #e0f2fe;
  font-size: 1.05rem;
  font-weight: 900;
}

.front { transform: translateZ(95px); }
.back { transform: rotateY(180deg) translateZ(95px); }
.right { transform: rotateY(90deg) translateZ(95px); }
.left { transform: rotateY(-90deg) translateZ(95px); }
.top { transform: rotateX(90deg) translateZ(95px); }
.bottom { transform: rotateX(-90deg) translateZ(95px); }

.ring {
  position: absolute;
  inset: 42px;
  border: 1px solid rgba(52, 211, 153, 0.38);
  border-radius: 50%;
  transform-style: preserve-3d;
}

.ring.one { transform: rotateX(72deg) rotateZ(12deg); animation: ringA 12s linear infinite; }
.ring.two { transform: rotateY(70deg) rotateZ(36deg); animation: ringB 14s linear infinite; }
.ring.three { transform: rotateX(20deg) rotateY(58deg); animation: ringA 18s linear infinite reverse; }

.node-card {
  position: absolute;
  width: 154px;
  padding: 0.75rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.9);
  box-shadow: 0 18px 55px rgba(0, 0, 0, 0.32);
  backdrop-filter: blur(18px);
}

.node-card strong {
  display: block;
  margin-bottom: 0.25rem;
}

.node-card span {
  color: var(--muted);
  font-size: 0.82rem;
}

.node-card.a { top: 28px; left: 10px; animation: cardFloat 6s ease-in-out infinite; }
.node-card.b { right: 2px; top: 170px; animation: cardFloat 7s ease-in-out infinite 700ms; }
.node-card.c { left: 28px; bottom: 30px; animation: cardFloat 8s ease-in-out infinite 300ms; }

@keyframes cubeSpin {
  from { transform: rotateX(-18deg) rotateY(0deg) rotateZ(2deg); }
  to { transform: rotateX(-18deg) rotateY(360deg) rotateZ(2deg); }
}

@keyframes sceneFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-16px); }
}

@keyframes ringA {
  from { rotate: 0deg; }
  to { rotate: 360deg; }
}

@keyframes ringB {
  from { rotate: 360deg; }
  to { rotate: 0deg; }
}

@keyframes cardFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.panel,
.project-card,
.timeline-card,
.edu-card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  box-shadow: 0 18px 55px rgba(0, 0, 0, 0.24);
}

.panel {
  padding: 1.4rem;
}

.panel p,
.panel li,
.project-card p,
.timeline-card li,
.edu-card p {
  color: #cbd5e1;
  line-height: 1.75;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

.skill-group {
  min-height: 156px;
  padding: 1rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.72);
}

.skill-group h3 {
  margin: 0 0 0.8rem;
  font-size: 1.05rem;
}

.chip {
  display: inline-flex;
  align-items: center;
  min-height: 31px;
  margin: 0 0.36rem 0.42rem 0;
  padding: 0.35rem 0.58rem;
  border: 1px solid rgba(148, 163, 184, 0.22);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.045);
  color: #dbeafe;
  font-size: 0.82rem;
  font-weight: 700;
}

.timeline {
  position: relative;
  display: grid;
  gap: 1rem;
}

.timeline-card {
  position: relative;
  padding: 1.3rem 1.4rem 1.3rem 1.6rem;
  overflow: hidden;
}

.timeline-card::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: linear-gradient(#38bdf8, #34d399, #f59e0b);
}

.timeline-card h3,
.project-card h3,
.edu-card h3 {
  margin: 0;
}

.timeline-meta,
.project-meta {
  margin: 0.3rem 0 0.8rem;
  color: var(--green);
  font-weight: 800;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.project-card {
  display: flex;
  flex-direction: column;
  min-height: 330px;
  padding: 1.25rem;
  transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
}

.project-card:hover {
  transform: translateY(-5px);
  border-color: rgba(56, 189, 248, 0.46);
  background: rgba(15, 23, 42, 0.9);
}

.project-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  margin-top: auto;
  padding-top: 1rem;
}

.project-link {
  color: #7dd3fc;
  font-weight: 900;
}

.edu-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

.edu-card {
  min-height: 210px;
  padding: 1.2rem;
}

.result {
  display: inline-flex;
  margin-top: 0.7rem;
  padding: 0.38rem 0.62rem;
  border-radius: 8px;
  background: rgba(52, 211, 153, 0.12);
  color: #bbf7d0;
  font-weight: 900;
}

.contact-band {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 1rem;
  align-items: stretch;
}

.contact-card {
  padding: 1.35rem;
  border: 1px solid rgba(56, 189, 248, 0.32);
  border-radius: 8px;
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.13), rgba(52, 211, 153, 0.08)), var(--panel-strong);
}

.contact-row {
  display: grid;
  grid-template-columns: 92px 1fr;
  gap: 0.8rem;
  padding: 0.65rem 0;
  border-bottom: 1px solid rgba(148, 163, 184, 0.16);
}

.contact-row:last-child {
  border-bottom: 0;
}

.contact-row span {
  color: var(--muted);
  font-weight: 800;
}

.footer {
  margin: 3rem 0 1rem;
  color: var(--muted);
  text-align: center;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
  border: 1px solid rgba(148, 163, 184, 0.28);
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.75);
  color: var(--ink);
}

.stButton > button {
  width: 100%;
  min-height: 45px;
  border: 1px solid rgba(56, 189, 248, 0.62);
  border-radius: 8px;
  background: linear-gradient(135deg, #38bdf8, #34d399);
  color: #04111f;
  font-weight: 900;
}

@media (max-width: 980px) {
  .hero,
  .contact-band {
    grid-template-columns: 1fr;
  }

  .hero {
    padding: 2rem;
    min-height: auto;
  }

  .hero-stage {
    min-height: 390px;
  }

  .feature-grid,
  .edu-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .topbar {
    position: relative;
    align-items: flex-start;
    flex-direction: column;
  }

  .navlinks {
    justify-content: flex-start;
  }

  .hero {
    padding: 1.25rem;
  }

  .hero h1 {
    font-size: 3rem;
  }

  .hero-proof,
  .feature-grid,
  .project-grid,
  .edu-grid {
    grid-template-columns: 1fr;
  }

  .node-card {
    position: relative;
    width: auto;
    margin: 0.5rem 0;
    inset: auto;
  }

  .hero-stage {
    min-height: 330px;
  }
}
</style>
"""


st.markdown(STYLE, unsafe_allow_html=True)

st.markdown(
    f"""
    <nav class="topbar">
      <a class="brand" href="#home">
        <span class="brand-mark">SK</span>
        <span>{PROFILE["name"]}</span>
      </a>
      <div class="navlinks">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Projects</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>
      </div>
    </nav>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section id="home" class="hero">
      <div class="hero-copy">
        <p class="eyebrow">Portfolio website - Streamlit, animated, resume-driven</p>
        <h1>Building <span>mobile-first AI products</span> with clean engineering.</h1>
        <p class="hero-lede">
          I am {PROFILE["name"]}, an AI & Data Science engineering student and Flutter developer
          focused on practical machine learning, responsive mobile UI, and product-ready software.
          My work spans computer vision, prediction systems, Firebase-backed apps, and polished
          interfaces that stay fast and clear.
        </p>
        <div class="hero-actions">
          <a class="btn primary" href="mailto:{PROFILE["email"]}">Email Me</a>
          <a class="btn" href="{PROFILE["github"]}" target="_blank">GitHub</a>
          <a class="btn" href="{PROFILE["linkedin"]}" target="_blank">LinkedIn</a>
        </div>
        <div class="hero-proof">
          {metric("Core Degree", "AI & DS")}
          {metric("CGPA", "8.45 / 10")}
          {metric("Featured Projects", "4")}
        </div>
      </div>
      <div class="hero-stage" aria-label="Animated 3D technology scene">
        <div class="orbit-scene">
          <div class="ring one"></div>
          <div class="ring two"></div>
          <div class="ring three"></div>
          <div class="cube">
            <div class="face front">Flutter</div>
            <div class="face back">AWS</div>
            <div class="face right">Python</div>
            <div class="face left">ML</div>
            <div class="face top">Data</div>
            <div class="face bottom">Apps</div>
          </div>
        </div>
        <div class="node-card a"><strong>Computer Vision</strong><span>PAN tampering detector</span></div>
        <div class="node-card b"><strong>Mobile UI</strong><span>Flutter and Dart apps</span></div>
        <div class="node-card c"><strong>Prediction</strong><span>Regression analytics</span></div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section id="about" class="section">
      <div class="section-title">
        <div>
          <p class="eyebrow">About</p>
          <h2>Developer with a product mindset.</h2>
        </div>
        <p>Focused on useful AI, clean UI, and reliable delivery.</p>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

about_left, about_right = st.columns([1.5, 1], gap="large")
with about_left:
    st.markdown(
        """
        <div class="panel">
          <h3>Professional summary</h3>
          <p>
            I build practical software across AI, data science, and mobile development.
            My resume shows a strong foundation in Python, Flutter, Dart, machine learning,
            UI development, and cloud platforms. I enjoy taking an idea from model or data
            exploration all the way to a usable app experience.
          </p>
          <p>
            During my Mobile Application Development internship at Incubators, I worked on
            cross-platform Flutter applications, responsive UI/UX, debugging, testing, and
            performance-focused development workflows.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with about_right:
    st.markdown(
        f"""
        <div class="panel">
          <h3>Snapshot</h3>
          <div class="contact-row"><span>Location</span><strong>{PROFILE["location"]}</strong></div>
          <div class="contact-row"><span>Role</span><strong>AI & Flutter Developer</strong></div>
          <div class="contact-row"><span>Focus</span><strong>ML, CV, Mobile Apps</strong></div>
          <div class="contact-row"><span>Tools</span><strong>Python, Dart, AWS</strong></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <section id="skills" class="section">
      <div class="section-title">
        <div>
          <p class="eyebrow">Skills</p>
          <h2>Technical stack shaped from the resume.</h2>
        </div>
      </div>
      <div class="feature-grid">
    """
    + "".join(
        f"""
        <div class="skill-group">
          <h3>{group}</h3>
          <div>{chips(items)}</div>
        </div>
        """
        for group, items in SKILLS.items()
    )
    + """
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section id="experience" class="section">
      <div class="section-title">
        <div>
          <p class="eyebrow">Experience</p>
          <h2>Hands-on mobile application development.</h2>
        </div>
      </div>
      <div class="timeline">
        <div class="timeline-card">
          <h3>Mobile Application Development Intern</h3>
          <p class="timeline-meta">Incubators - Pune, India - Jun 2025 to Dec 2025</p>
          <ul>
            <li>Developed and maintained cross-platform mobile applications using Flutter and Dart.</li>
            <li>Built responsive UI/UX and robust app functionality for smooth mobile experiences.</li>
            <li>Assisted with debugging, testing, and app performance improvements during development workflows.</li>
          </ul>
        </div>
        <div class="timeline-card">
          <h3>Leadership and activities</h3>
          <p class="timeline-meta">S4DS Club and sports representation</p>
          <ul>
            <li>Member of the Marketing Team at S4DS Club.</li>
            <li>Represented Sangli District in the Basketball Championship, 2018.</li>
          </ul>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section id="projects" class="section">
      <div class="section-title">
        <div>
          <p class="eyebrow">Projects</p>
          <h2>Selected work with practical engineering depth.</h2>
        </div>
      </div>
      <div class="project-grid">
    """
    + "".join(
        f"""
        <article class="project-card">
          <p class="project-meta">{project["type"]} - {project["time"]}</p>
          <h3>{project["title"]}</h3>
          <p>{project["description"]}</p>
          <p><strong>Impact:</strong> {project["impact"]}</p>
          <div>{chips(project["tech"])}</div>
          <div class="project-footer">
            <span class="muted">Resume project</span>
            <a class="project-link" href="{project["link"]}" target="_blank">Open repository</a>
          </div>
        </article>
        """
        for project in PROJECTS
    )
    + """
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section id="education" class="section">
      <div class="section-title">
        <div>
          <p class="eyebrow">Education</p>
          <h2>Academic foundation.</h2>
        </div>
      </div>
      <div class="edu-grid">
    """
    + "".join(
        f"""
        <div class="edu-card">
          <p class="project-meta">{item["year"]} - {item["place"]}</p>
          <h3>{item["degree"]}</h3>
          <p>{item["school"]}</p>
          <span class="result">{item["result"]}</span>
        </div>
        """
        for item in EDUCATION
    )
    + """
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section id="contact" class="section">
      <div class="section-title">
        <div>
          <p class="eyebrow">Contact</p>
          <h2>Ready for internships, projects, and collaboration.</h2>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

contact_left, contact_right = st.columns([1.2, 0.8], gap="large")
with contact_left:
    with st.container():
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Message", height=150)
        submitted = st.button("Send message")
        if submitted:
            if name and email and message:
                st.success("Thanks. Your message is ready to be sent to Siddharth.")
            else:
                st.warning("Please fill in your name, email, and message.")
        st.markdown("</div>", unsafe_allow_html=True)

with contact_right:
    st.markdown(
        f"""
        <div class="contact-card">
          <h3>Direct contact</h3>
          <div class="contact-row"><span>Email</span><a href="mailto:{PROFILE["email"]}">{PROFILE["email"]}</a></div>
          <div class="contact-row"><span>Phone</span><a href="tel:{PROFILE["phone"].replace(" ", "")}">{PROFILE["phone"]}</a></div>
          <div class="contact-row"><span>GitHub</span><a href="{PROFILE["github"]}" target="_blank">Sidk9587</a></div>
          <div class="contact-row"><span>LinkedIn</span><a href="{PROFILE["linkedin"]}" target="_blank">Siddharth Kharat</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <p class="footer">
      Built in the current Streamlit project with animated 3D CSS, resume-based content, and a professional portfolio layout.
    </p>
    """,
    unsafe_allow_html=True,
)
