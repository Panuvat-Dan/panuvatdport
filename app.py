from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    job_experiences = [
        {"title": "Senior Technical Consultant (Contractor)", "company": "Celebal Technologies", "duration": "Oct 2024 - Present"},
        {"title": "Senior ETL Developer (Contractor)", "company": "Generali life insurance", "duration": "Apr 2024 - Present"},
        {"title": "Senior Data Engineer (Contractor)", "company": "R-system Consultant", "duration": "Sep 2023 - Mar 2024"},
        {"title": "Data Engineer consultant (Contractor)", "company": "Adastra Thailand", "duration": "Aug 2022- Jun 2023"},
        {"title": "Data Engineer (Contractor)", "company": "Lotus's CP AXTRA", "duration": "Aug 2021 - Jul 2022"},
        {"title": "Project Engineer (Full Time)", "company": "Toyota Motor Thailand", "duration": "Jul 2019 - Jul 2021"}
    ]

    capstone_projects = [
        {"name": "AI Model Developemnt and Deployment", "description": "Built an machine learning model with sklearn to predict heart disease and publish to opensource streamlit platform  ", "image": "project1.png", "repo": "https://github.com/Panuvat-Dan/mldeployment-65130700332/tree/main","website" : "https://panuvat-dan-mldeployment-6513070033-app-main-65130700332-xdteva.streamlit.app/"},
        {"name": "ETL Modules Pipeline", "description": "Developed a ETL modules (config manager, log handler, ingestion, cleansing, transformation modules) and dynamic data pipeline with  these tech stacks .. Apache Airflow, Apache Spark,  ,Docker, Pytest ,Pandas ", "image": "project2.png", "repo": "https://deproject-cj2llr8mehkwxcaqjacz74.streamlit.app/","website" :"https://deproject-cj2llr8mehkwxcaqjacz74.streamlit.app/"},
        {"name": "Siam ETL Flow Python Package", "description": "Created a UAV flight sim for training.", "image": "project3.png", "repo": "https://github.com/Panuvat-Dan/siamflowetl","website":"https://pypi.org/project/siamflowetl/"},
        {"name": "Predictive Analysis with BI Tool (Tableau)", "description": "To explore, analyse and identify the overview from starbuck_world_stat data set on Tablaeu file.However, to deep dive on analysis", "image": "project4.png", "repo": "https://github.com/Panuvat-Dan/Stabuck_analysis_loyalprediction","website":"https://public.tableau.com/app/profile/panuvat.danvorapong/viz/Stabuckanalysis/Overviewstory"}
    ]

    certifications = [
        {"name": "Apache Kafka Confluent Fundamentals Accreditation" ,"link":"https://www.credential.net/57ec2ca0-3415-433b-aa6f-4945268cc68f#acc.DaXsVUCl"},
        {"name": "Azure Databricks Platform Architect", "link": "https://credentials.databricks.com/642a17a3-fd68-428a-a900-7bb5d31477c1#acc.RNpDrMT6/"},
        {"name": "Databricks Certified Data Engineer Associate", "link": "https://credentials.databricks.com/e0873fd3-f2ae-427d-a900-eb53ba5c17a3#acc.XtqnTMAo"},
        {"name": "AWS Partner: Accreditation (Technical)", "link": "https://www.credential.net/4d8fa0ca-2c37-4e5d-8984-fba0c3010f38?username=panuvatdanvorapong146095#gs.s2fox6"},
        {"name": "Microsoft Certified: Azure Data Engineer Associate" ,"link":"https://www.credly.com/badges/50cb9b23-3723-4500-ba40-d3dc4d3f2a86/linked_in_profile"},
        {"name": "Microsoft Certified: Security, Compliance, and Identity Fundamentals" ,"link":"https://www.credly.com/badges/4a5b20b6-2d85-4b8c-823c-97d3b8e6c513/linked_in_profile"},
        {"name": "Microsoft Certified: Azure Data Fundamentals" ,"link":"https://www.credly.com/badges/4460634c-c8f6-46b8-b40b-b56aa3ca8cd0/linked_in_profile"},
        {"name": "Oracle Database Foudations" ,"link":"https://drive.google.com/file/d/1hBb48kqcsy2Bu5XtwzEDvE2s80mHAjuH/view"},
        {"name": "Talend Data Fabric Explorer", "link": "https://www.credly.com/badges/fd3cb24c-fbc8-47f9-8c69-8e53dcd9f625/linked_in_profile"},
        {"name": "Tableau Desktop Specialist","link": "https://www.credly.com/badges/4d4d321e-082c-4228-8cef-3ff58dfbcff1/linked_in_profile"},
        {"name": "Data Virtualization Architech","link":"https://drive.google.com/file/d/1HZi6BGJ2Q8EMgJ5qnvtMyBK8PtzFz62l/view"}     
    ]

    about_me = {
        "name": "Panuvat Danvorapong",
        "master_degree": "Master of Science - MS, Information Technology, King Mongkut's University of Technology Thonburi (2021 - 2023)",
        "bachelor_degree": "Bachelor of Engineering - Aerospace Engineering (IDDP Program), Royal Melbourne Insitude University - Kasetsart University (2014-2018)",
        "linkedin": "https://www.linkedin.com/in/panuvat-danvorapong/",
        "website": "https://yourportfolio.com",
        "github": "https://github.com/Panuvat-Dan",
        "email": "dpanuvatz2m1994@gmail.com",
        "phone": "+66-957390898"
    }

    return render_template("index.html", jobs=job_experiences, projects=capstone_projects, certifications=certifications, about_me=about_me)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render’s assigned PORT
    app.run(host="0.0.0.0", port=port)