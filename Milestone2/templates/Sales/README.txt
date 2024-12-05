=== Contributor ===
Author : Shreya Podishetti
Student ID : s4040881
Title : Job Seek Website
Requirements : 
	* Python
	* Flask
	* Gensim
	* numpy
	* os
OneDrive link to the project folder: https://rmiteduau-my.sharepoint.com/:u:/g/personal/s4040881_student_rmit_edu_au/Edet8azrnOFLoTnq4CGXIFMBK7QW5VuKNnAF-oVnmIL5vw
			
=== Overview ===
This project is a job-seeking website developed by using Flask named as ‘Job Seek’. This website allows job seekers to search through job listings and view the detailed job descriptions posted by employers. The website also allows the employer to login to the portal and create new job listings. By leveraging NLP in this project, the website will also recommend job categories for each of the new listings. The categories available include ‘Accounting and Finance’, ‘Engineering’, ‘Healthcare and Nursing’, and ‘Sales’.

=== Features ===
For Job Seekers

* Job Search : Job seekers can search for particular job listings based on keywords. The search results displays the top 4 job titles and descriptions directly on the search results page.

For Employers

* Creating New Job Listings : Employers can login to the admin portal with their username and password and then create new job listings by entering the job title, description, and category details.
* Category Recommendation : The website recommends suitable job categories based on the job description provided by the employer. If the employer is not happy with the generated category he has the option to rewrite and save it.

=== Directory Structure ===

* static
	** images
	** jQuery-3.6.0.js
	** style_advance.css
* templates
	** Accounting_Finance
	** Engineering
	** Healthcare_Nursing
	** Sales
	** about.html
	** accounting_finance.html
	** admin.html
	** article_template.html
	** base.html
	** engineering.html
	** healthcare_nursing.html
	** home.html
	** job_post.html
	** login.html
	** sales.html
	** search.html
* app.py
* desc_FT.model
* desc_FT.model.wv.vectors_ngram.npy
* descFT_LR.pkl

=== Setup and Installation ===

1. Setup Visual Studio Code by changing base to conda

```
Ctrl + Shift + P -> python: Select Interpreter -> base : conda

```

2. Set the path to folder created for the project

```
cd milestone2

```

3. Run the application

```
export FLASK_APP= app.py
export FLASK_ENV = development
flask run

```

4. Open the browser and navigate to `http://127.0.0.1:5000`.
