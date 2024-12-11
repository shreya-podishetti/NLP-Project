# NLP-Project ( NLP Web-Based Job Category Prediction Project)

![image](https://github.com/user-attachments/assets/1a5ef0a9-3361-45a8-ac4d-1a66b2e30046)

Project Overview
-----------------

Nowadays there are many job hunting websites including seek.com.au and au.indeed.com. These job hunting
sites all manage a job search system, where job hunters could search for relevant jobs based on keywords,
salary, and categories. In previous years, the category of an advertised job was often manually entered by the
advertiser (e.g., the employer). There were mistakes made for category assignment. As a result, the jobs in the
wrong class did not get enough exposure to relevant candidate groups.

With advances in text analysis, automated job classification has become feasible; and sensible suggestions for
job categories can then be made to potential advertisers. This can help reduce human data entry error,
increase the job exposure to relevant candidates, and also improve the user experience of the job hunting site.
In order to do so, we need an automated job ads classification system that helps to predict the categories of
newly entered job advertisements.

This project includes two milestones. The first milestone (NLP) concerns the pipeline from basic text
preprocessing to building text classification models for predicting the category of a given job advertisement.
Then, the second milestone will adopt one of the models that we built in the first milestone, and develop a job
hunting website that allows users to browse existing job advertisements, as well as for employers to create
new job advertisements

Milestone-1
-------------
-------------

This milestone, requires to pre-process a collection of job advertisement documents, build machine
learning models for document classification (i.e., classifying the category of a given job advertisement), and
perform evaluation and analysis on the built models.

The Data:
----------

Inside the data folder you will see 4 different subfolders, namely: 
- Accounting_Finance,
- Engineering,
- Healthcare_Nursing, and
- Sales

Each folder name is a job category.
The job advertisement text documents of a particular category are located in the corresponding subfolder.
Each job advertisement document is a txt file, named as "Job_<ID>.txt". It contains the title, the webindex,
(some will also have information on the company name, some might not), and the full description of the job
advertisement


Task 1: Basic Text Pre-processing
------------

In this task, we focus on
pre-processing the description only. We perform the following:
1. Extract information from each job advertisement. Perform the following pre-processing steps to the
description of each job advertisement
2. Tokenize each job advertisement description. The word tokenization must use the following regular
expression, r"[a-zA-Z]+(?:[-'][a-zA-Z]+)?"
3. All the words must be converted into the lower case
4. Remove words with length less than 2.
5. Remove stopwords using the provided stop words list (i.e, stopwords_en.txt). It is located inside the
same downloaded folder.
6. Remove the word that appears only once in the document collection, based on term frequency.
7. Remove the top 50 most frequent words based on document frequency.
8. Save all job advertisement text and information in txt file(s) (you have flexibility to choose what format
you want to save the preprocessed job ads, and you will need to retrieve the pre-processed job ads
text in Task 2 & 3)
9. Build a vocabulary of the cleaned job advertisement descriptions, save it in a txt file

Output of Task 1:

vocab.txt This file contains the unigram vocabulary, one each line, in the following format:
word_string:word_integer_index. Very importantly, words in the vocabulary must be sorted in
alphabetical order, and the index value starts from 0. 

Task 2: Generating Feature Representations for Job Advertisement Descriptions 
---

In this task, you are required to generate different types of feature representations for the collection of
job advertisements. Note that in this task, we will only consider the description of the job
advertisement. The feature representation that you need to generate includes the following:

- Bag-of-words model: Generate the Count vector representation for each job advertisement description, and save
them into a file. Note, the generated Count vector
representation is based on the generated vocabulary in Task 1 (as saved in vocab.txt).

- Models based on word embeddings: You are required to generate feature representation of job advertisement description based on
the following language models, respectively: Any 1 embedding language model, e.g., FastText, GoogleNews300, or other
Word2Vec pretrained models, or Glove. (Here we have used the Glove embedding language model)

In this part, we build the weighted (i.e., TF-IDF weighted) and unweighted vector
representation for each job advertisement description using the chosen language model.
To summarize, there are 3 different types of feature representation of documents that you need to
build in this task, including count vector, two document embeddings (one TF-IDF weighted, and one
unweighted version).

Output of Task 2:

count_vectors.txt This file stores the sparse count vector representation of job advertisement
descriptions in the following format. Each line of this file corresponds to one advertisement. It starts
with a ‘#’ key followed by the webindex of the job advertisement, and a comma ‘,’. The rest of the line
is the sparse representation of the corresponding description in the form of
word_integer_index:word_freq separated by comma.

Task 3: Job Advertisement Classification
-----

In this task, we are required to build machine learning models for classifying the category of a job
advertisement text. A simple model that you can consider is the logistic regression model from sklearn as
demonstrated in the activities.

Milestone-2
-------------
-------------

In Milestone, we built various machine learning models using different document vector representations to
classify job adverts. In Milestone II, we will develop a job search website based on the Flask web
framework. The website allows job seekers to browse existing job adverts and lets employers create new
job adverts. This website will make use of one machine learning model that you trained in Milestone I. It
will be used to recommend job categories for employers to assign to newly created job adverts. This
feature will help to reduce human error, increase the job exposure to relevant candidates, and improve the
user experience of the job seeking website

Minimum Functional Requirements
---------
There are minimum functional requirements of the developed website for job hunters and
employers, respectively. 

- Functionality for Job seekers
1. Job Search: The Job hunting website will allow job hunters to effectively search for job listings that are of their
interest.
2. The search could be based on keywords.
3. Upon user entering a keyword string, the develop
system should return a message saying how many matched job advertisements, and it also returns a
list of job advertisement previews that are relevant to the keyword string.
4. When users click on a job ad
preview, they can see the full description of the job.
5. You need to design a search algorithm that: support to search keyword strings in similar forms. For example, if users enter the keyword
strings “work” or “works” or “worked”, the search results from these two keyword strings will
be the same.
6. Apart from the above requirement, you have the flexibility to use simple string matching based
methods, or any other language models, or build your own models to evaluate the relevance
of a job advertisement to the entered keyword string.

- Functionality for Employers
1. Create New Job Listing: The Job seeking website allows employers to create new job listings.
2. When creating a new job listing
employers can enter information such as title, description, salary, etc.
3. When a new job advert is created, using the job description (and/or job title), the website should
recommend a list of categories for selection to assign to the job advert.
4. The employer should be able to
select other categories if the recommendation does not suit, that is, they can override the categories
suggested by the website.
5. Upon
confirmation, the created job advert should be included in the job data and be accessible via URL and
relevant search.
6. You have the flexibility to choose the language model and the classification model for the job category
recommendation task.
7. You do not need to create any employer login for the job website.

Feedback and Contact
--------------------
I would love to hear you feedback, suggestions, or answer any questions regarding th projects of this repository. Feel free to reach out to me via email at shreyapodishetti30@gmail.com

Have a great time exploring this repository. Thank you!
