from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

data = {
  "score_card": {
        "ats": {
            "score": 78,
            "description": "Strong ATS compatibility potential.",
            "reason": "Good use of relevant keywords and proper formatting.",
            "improvementTip": "Further refine keywords and optimize layout for ATS readability."
        },
        "jd": {
            "score": 2,
            "description": "High alignment with job description.",
            "reason": "Resume closely matches key job requirements.",
            "improvementTip": "Highlight specific achievements that directly relate to job requirements."
        },
        "overall": {
            "score": 75,
            "description": "Good overall resume quality.",
            "reason": "Well-structured with relevant content.",
            "improvementTip": "Add more quantifiable achievements to strengthen impact."
        },
        "ranking": {
            "score": 80,
            "description": "Above average compared to peers.",
            "reason": "Strong performance against common resumes in your field.",
            "improvementTip": "Tailor experience section to industry-specific expectations."
        },
        "keywords": {
            "score": 85,
            "description": "Excellent keyword optimization.",
            "reason": "Includes many relevant keywords for target position.",
            "improvementTip": "Incorporate a few more advanced technical terms in your field."
        }
    },

    

            "project_impact": {
                "impact": {
                    "AI-Driven Analytics Platform": 35,
                    "Cloud Migration Project": 25,
                    "Blockchain-based Supply Chain": 70,
                    "DevOps Pipeline Optimization": 50,
                    "IoT Data Processing System": 100
                },
                "advice": "Highlight the business impact of your AI-Driven Analytics Platform. Emphasize the scale and challenges overcome in your Cloud Migration Project.",

                "suggestion1": "what needs to be done to get selected for this job description Highlight the business impact of your AI-Driven Analytics Platform. Emphasize the scale and challenges overcome in your Cloud Migration",
                "suggestion2":"which project is not making any sense for this job description Highlight the business impact of your AI-Driven Analytics Platform. Emphasize the scale and challenges overcome in your Cloud Migration",
                "suggestion3": "what keywords you should add in this projects Highlight the business impact of your AI-Driven Analytics Platform. Emphasize the scale and challenges overcome in your Cloud Migration ",
                
                
            },



            "skill_Score": {
                "skills_ratio": {
                    "Machine Learning": 75,
                    "Data Analysis": 60,
                    "Cloud Computing": 45,
                    "DevOps": 30,
                    "Blockchain": 20

                },
                "advice": "Consider deepening your knowledge in Cloud Computing and DevOps to align better with industry demands. Stay updated with the latest Machine Learning techniques.",
              
                },

                  "recommendations": [
                "Pursue advanced certifications in Cloud Computing to address the skill gap.",
                "Contribute to open-source DevOps projects to gain practical experience.",
                "Write technical blog posts about your ML projects to showcase expertise.",
                "Attend industry conferences to network and stay updated on trends.",
                "Mentor junior data scientists to demonstrate leadership skills."
            ],








          
            "course_impact":{ 
                "impt":{
                "Advanced Machine Learning Specialization": 50,
                "Cloud Architect Certification": 100,
                "DevOps Engineering on AWS": 20,
                "Blockchain Technology Fundamentals": 70,
                "IoT & Big Data Analytics": 10
            },

            "course_advice": "Relate your Advanced Machine Learning Specialization to specific projects. Demonstrate how your Cloud Architect Certification enhances your ability to design scalable solutions.",

             "suggestion1": "what needs to be done to get selected for this job description ",
                "suggestion2":"which project is not making any sense for this job description",
                "suggestion3": "what keywords you should add in this projects "
            },
 
          
    
             "Strengths":{
                    "Relevant Education":" The candidate is pursuing a Bachelor's degree in AI & DS, which aligns with the job requirements.",
                    "AI/ML Experience":"The candidate has experience in AI/ML through various projects, internships, and certifications, which is a significant strength for this role.",
                    "Technical Skills":"The candidate has a good foundation in technical skills required for the job, including ML, NLP, LLM, Python, SciKit Learn, Pandas, and Matplotlib.",
                    },
                "Weaknesses":{
                    "Lack of Direct Experience": "Although the candidate has experience in AI/ML, they lack direct experience in Gen AI development, deployment, and pipeline creation, which is a critical requirement for the job.",
                    "Limited Industry Experience" : "The candidate's experience is mostly limited to internships and personal projects, which may not be sufficient to meet the job's requirements.",
                    "No Mention of Model Development or Evaluation" : "The candidate's resume does not explicitly mention experience in model development, evaluation, or deployment, which are essential skills for the job."
                },

    
     "recommended_People_linkdin": [
    {
      "name": " Doe",
      "title": "Senior Soft... ",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "John Doe",
      "title": "Senior Soft....",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "John Doe",
      "title": "Senior Software Engineer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },

    
  ],

  
     "recommendedPeople_twitter": [
    {
      "name": "John Doe",
      "title": "Senior Soft... ",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "John Doe",
      "title": "Senior Soft....",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "John Doe",
      "title": "Senior Software Engineer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    
    
  ],
   "recommendedPeople_instagram": [
    {
      "name": "John ",
      "title": "Senior Soft... ",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "John Doe",
      "title": "Senior Soft....",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "John Doe",
      "title": "Senior Software Engineer",
      "link": "https://example.com/john-doe"
    },
    {
      "name": "Jane Smith",
      "title": "UX Designer",
      "link": "https://example.com/john-doe"
    },
    
    
  ],
  "Actionable Recommendations": [
    "Pursue advanced certifications in Cloud Computing to address the skill gap.",
    "Contribute to open-source DevOps projects to gain practical experience.",
    "Write technical blog posts about your ML projects to showcase expertise.",
    "Attend industry conferences to network and stay updated on trends.",
    "Mentor junior data scientists to demonstrate leadership skills."
  ]
,
  "experience_relevance": {
      "imp":{
    "expeience1": 50,
    "ex2": 100,
    "ex3": 20,
    "ex4": 7,
    "ex5": 10
  },
  "advice": " deepening your knowledge in Cloud Computing and DevOps to align better with industry demands. Stay updated with the latest Machine Learning techniques."
        },
}

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')
    # return send_from_directory(os.path.join(app.root_path, 'static'), 'peoples.html')


@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)