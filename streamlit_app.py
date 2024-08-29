import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Shah Ahmad
##### *Resume* 
''')

image = Image.open('ShahAhmadNoBackground.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Application Developer and Architect with twenty years plus of experience in healthcare applications architecture, design, and development. 
- Deep background and interest in AI Technologies such as Neural Networks. Strong knowledge of frameworks like Pytorch, Langchain, and Data Science libraries.
- Worked on several prototype multimodal AI projects using AI models. 
- In-depth experience in agile methodologies and software quality management.
- Analytical mind with a passion for building quality within code.
- Strong verbal and written communication skills with the ability to lead by example and establish trust among teams.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#key-skills">Key Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#tools-worked-on">Tools worked on</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


#####################
st.markdown('''
## Key Skills
''')
txt3('Languages', '`Python`, `C#`, `JavaScript`, `Qlikview`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`PyTorch`')
txt3('Web development', '`Flask`, `Streamlit`, `HTML`, `CSS`')
txt3('Frameworks for Model deployment', '`LangChain`,`Hugging Face`,`streamlit`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')

#####################
st.markdown('''
## Tools Worked on
''')
txt4('MultiPdf Chat', 'A web server that allows you to chat with multiple PDF documents', 'https://shah109-ask-multiple-pdfs.streamlit.app/')
txt4('Chat with Websites', 'A web server that allows you to chat with websites', 'https://chat-with-websites-shah.streamlit.app/')
txt4('Mortgage Application', 'Calculates monthly re-payments, total re-payments, total interest and principle balance for a mortgage ', 'https://shah109-mortgage-app.streamlit.app/')
# txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
# txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
# txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
# txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
# txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
# txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
# txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
# txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
# txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
# txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
# txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')

#####################
st.markdown('''
## Work Experience
''')
txt('**Professional Development Sabbatical**, *Retired Software Developer/Architect*',
'2021-current')
st.markdown('''
- Focused on advancing expertise in Artificial Intelligence, specializing in deep learning and neural networks.
- Independently developed and implemented several AI projects and applications, demonstrating practical skills and creativity. Frameworks and libraries used are OpenAI API, LangChain, Hugging Face, Numpy, Pandas, Matplotlib. All work is done in Python, VSCode, Google Colab and Git/GitHub.  
- Kept pace with industry trends, attending workshops, and staying connected with the ever-evolving AI community.
-	Looking forward to adding a splash of excitement to my career journey with Artificial Intelligence.
''')

txt('**Senior Software Engineer/ Architect, Medical Systems Group**, Olympus Corporation, Center Valley, Pennsylvania',
'2008-2021')
st.markdown('''
- Responsible for design and development activities for Olympus UE, a web-based health-care workflow and asset management system at hospitals. Project life cycle is managed via an agile environment using MS Team Foundation Server. This system is a large endeavor towards managing the business processes and safety around Olympus assets in hospital environments. 
- Further details of the platform are available at:
https://medical.olympusamerica.com/customer-resources/cleaning-disinfection-sterilization/reprocessing-products/unifia#

-	Development of the next generation software solutions to integrate and track Olympus devices, interface with other hospital systems to provide data analysis features for decision making for management. Unifia is a highly modular and efficient web application for admin tasks, dashboards of hospital locations and real time device statuses, infection prevention monitoring and Asset Management. All back-end communication is handled via web services on the UE Server. 
- I was involved in both front-end and back-end development of Unifia. The back end involved Microsoft based technologies such as ASP.NET MVC, Entity Framework, C#, Signal R, LINQ, MS Unity, Team Foundation Server, MS SQL Server among others. The front-end involved several JS frameworks and libraries such as jQuery, Bootstrap, Knockout, JsGrid, AngularJS etc. 
- Enforcing best practices for unit tests across the team for UE Server, a large and critical .NET based back-end on IIS receiving messages from Olympus devices via RabbitMQ and android based mobile RFID and barcode scanners. It handles all business logic and communicates with the front end via web services.
- Improved UI performance by nearly 15x for a Qlikview website embedded in Olympus UE for BI reporting in various tabular and graphic formats.  Improvements prevented the team from considering a Qlikview replacement, which would have caused major delays and re-work. 
- Built IOS /Android mobile application for RFID and barcode scanning functionality for Olympus assets using Xamarin Forms. Designed as MVVM architecture with highly modular and extensible code. Later also developed a android mobile app that interfaced with Unifia. 
''')

txt('**Team Lead and Consultant, ENGINE Factory Test Automation**, Novartis Pharmaceuticals, NJ' ,
'2000-2008')
st.markdown('''
- Managed and improved the development, quality assurance and testing activities of application portfolio management system across the corporation.
- **Environment:** VBA, VBScript, c#, QA Center, QA Run, Visual Studio 2003/2005, MS Test, ADO.NET, ASP.NET, NetInstall.
''')


# txt('**Content Creator**, [Data Professor YouTube Channel](https://youtube.com/dataprofessor/)',
# '2019-Present')
# st.markdown('''
# - `100,000+` subscribers on YouTube
# - Created `261` educational videos on data science, machine learning and bioinformatics as well as hosted several podcast episodes with data scientists.
# - Created `3` sponsored videos for Notion, Gradio and Classpert.
# ''')

# txt('**Content Creator**, [Coding Professor YouTube Channel](https://youtube.com/codingprofessor/)',
# '2019-Present')
# st.markdown('''
# - `3,200+` subscribers on YouTube
# - Created `38` educational videos on Python and R programming.
# ''')

# txt('**Technical Writer**, [Data Professor Blog](https://data-professor.medium.com/) on Medium.com',
# '2019-Present')
# st.markdown('''
# - `4,100+` subscribers on Medium
# - Written `68` technical blogs on data science, machine learning and bioinformatics.
# ''')




#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/shah109')
txt2('Twitter', 'https://twitter.com/shah1090')
txt2('GitHub', 'https://github.com/shah109/')
#txt2('', 'https://github.com/chaninlab/')
#txt2('', 'https://github.com/dataprofessor')
#txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
#txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
#txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
#txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
#txt2('Publons', 'https://publons.com/a/303133/')

#####################
st.markdown('''
## Education
''')

txt('**Masters in Computer Science**, *Preston University*, Pakistan', '1999')
st.markdown('''
- Graduated with First Class Honors
''')

txt('**Masters in Systems Engineering**, *Quaid-e-Azam University*, Pakistan',
'1982')
st.markdown('''
- Graduated with First Division.
''')















