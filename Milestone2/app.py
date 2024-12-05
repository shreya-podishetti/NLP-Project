from flask import Flask, render_template, request, redirect, session
from gensim.models.fasttext import FastText
import pickle
import os
from bs4 import BeautifulSoup
import numpy as np

"""
Note: a faster version of `gen_docVecs`.
"""
def docvecs(embeddings, docs):
    vecs = np.zeros((len(docs), embeddings.vector_size))
    for i, doc in enumerate(docs):
        valid_keys = [term for term in doc if term in embeddings.key_to_index]
        docvec = np.vstack([embeddings[term] for term in valid_keys])
        docvec = np.sum(docvec, axis=0)
        vecs[i,:] = docvec
    return vecs

def read_job_description(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        title = None
        description = None
        for line in lines:
            if line.startswith("Title:"):
                title = line.split(': ', 1)[1].strip()
            elif line.startswith("Description:"):
                description = line.split(': ', 1)[1].strip()
            if title and description:
                break
    return title, description

def get_job_data(category):
    job_data = []
    folder_path = os.path.join(app.root_path, 'templates', category)
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            title, description = read_job_description(file_path)
            job_data.append({'title': title, 'description': description})
    return job_data


app = Flask(__name__)
app.secret_key = os.urandom(16) 

@app.route('/')
def home():
    engineering_data = get_job_data('Engineering')
    sales_data = get_job_data('Sales')
    healthcare_nursing_data = get_job_data('Healthcare_Nursing')
    accounting_finance_data = get_job_data('Accounting_Finance')
    return render_template('home.html', engineering_data=engineering_data, sales_data=sales_data, healthcare_nursing_data=healthcare_nursing_data, accounting_finance_data=accounting_finance_data)

@app.route('/accounting_finance')
def accounting_finance():
    accounting_finance_folder = os.path.join(app.root_path, 'templates', 'accounting_finance')
    accounting_finance_files = [f for f in os.listdir(accounting_finance_folder) if f.endswith('.txt')]
    accounting_finance_data = []
    for filename in accounting_finance_files:
        file_path = os.path.join(accounting_finance_folder, filename)
        title, description = read_job_description(file_path)
        accounting_finance_data.append({'title': title, 'description': description})
    return render_template('accounting_finance.html', accounting_finance_data=accounting_finance_data)

@app.route('/engineering')
def engineering():
    engineering_folder = os.path.join(app.root_path, 'templates', 'engineering')
    engineering_files = [f for f in os.listdir(engineering_folder) if f.endswith('.txt')]
    engineering_data = []
    for filename in engineering_files:
        file_path = os.path.join(engineering_folder, filename)
        title, description = read_job_description(file_path)
        engineering_data.append({'title': title, 'description': description})
    return render_template('engineering.html', engineering_data=engineering_data)

@app.route('/healthcare_nursing')
def healthcare_nursing():
    healthcare_nursing_folder = os.path.join(app.root_path, 'templates', 'healthcare_nursing')
    healthcare_nursing_files = [f for f in os.listdir(healthcare_nursing_folder) if f.endswith('.txt')]
    healthcare_nursing_data = []
    for filename in healthcare_nursing_files:
        file_path = os.path.join(healthcare_nursing_folder, filename)
        title, description = read_job_description(file_path)
        healthcare_nursing_data.append({'title': title, 'description': description})
    return render_template('healthcare_nursing.html', healthcare_nursing_data=healthcare_nursing_data)

@app.route('/sales')
def sales():
    sales_folder = os.path.join(app.root_path, 'templates', 'sales')
    sales_files = [f for f in os.listdir(sales_folder) if f.endswith('.txt')]
    sales_data = []
    for filename in sales_files:
        file_path = os.path.join(sales_folder, filename)
        title, description = read_job_description(file_path)
        sales_data.append({'title': title, 'description': description})
    return render_template('sales.html', sales_data=sales_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<category>/<filename>')
def article(category, filename):
    try:
        # Define the file path based on the category and filename
        file_path = f'templates/{category}/{filename}.txt'

        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        # Extract title and description from the file content
        title = content[0].replace('Title: ', '').strip()
        description = content[1].replace('Description: ', '').strip()

        return render_template('job_post.html', title=title, description=description)
    except FileNotFoundError:
        return "Job posting not found", 404


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'username' in session:
        if request.method == 'POST':

            # Read the content
            f_title = request.form['title']
            f_content = request.form['description']

            # Classify the content
            if request.form['button'] == 'Classify':

                # Tokenize the content of the .txt file so as to input to the saved model
                tokenized_data = f_content.split(' ')

                # Load the FastText model
                bbcFT = FastText.load("desc_FT.model")
                bbcFT_wv= bbcFT.wv

                # Generate vector representation of the tokenized data
                bbcFT_dvs = docvecs(bbcFT_wv, [tokenized_data])

                # Load the LR model
                pkl_filename = "descFT_LR.pkl"
                with open(pkl_filename, 'rb') as file:
                    model = pickle.load(file)

                # Predict the label of tokenized_data
                y_pred = model.predict(bbcFT_dvs)
                y_pred = y_pred[0]

                return render_template('admin.html', prediction=y_pred, title=f_title, description=f_content)
            
            elif request.form['button'] == 'Save':
                # First check if the recommended category is empty
                cat_recommend = request.form['category']
                if cat_recommend == '':
                    return render_template('admin.html', prediction=cat_recommend,
                                        title=f_title, description=f_content,
                                        category_flag='Recommended category must not be empty.')

                elif cat_recommend not in ['Engineering', 'Healthcare_Nursing', 'Accounting_Finance', 'Sales']:
                    return render_template('admin.html', prediction=cat_recommend,
                                        title=f_title, description=f_content,
                                        category_flag='Recommended category must belong to: Engineering, Healthcare_Nursing, Accounting_Finance, Sales.')

                else:
                    # Define the filename based on the title and category
                    filename_list = f_title.split()
                    filename = '_'.join(filename_list) + ".txt"
                    directory = "templates/" + cat_recommend  # Use existing directories in 'templates'

                    # Write the title and description to a new .txt file
                    file_path = os.path.join(directory, filename)
                    with open(file_path, "w", encoding='utf-8', newline='\n') as file:
                        file.write(f"Title: {f_title}\n")
                        file.write(f"Description: {f_content}\n")

                    # Manually construct the redirect URL
                    redirect_url = f'/{cat_recommend}/{filename.replace(".txt", "")}'
                    return redirect(redirect_url)
            # If not a POST request, render the admin page
        return render_template('admin.html')
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/admin')
    else:
        if request.method == 'POST':
            if (request.form['username'] == 'admin') and (request.form['password'] == 'secret'):
                session['username'] = request.form['username']
                return redirect('/admin')
            else:
                return render_template('login.html', login_message='Username or password is invalid.')
        else:
            return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)

    return redirect('/')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        search_string = request.form["searchword"]

        # Search over all the txt files in templates to find the search_string
        article_search = []
        dir_path = 'templates'
        for category in ['Engineering', 'Healthcare_Nursing', 'Accounting_Finance', 'Sales']:
            category_path = os.path.join(dir_path, category)
            if os.path.isdir(category_path):
                for filename in sorted(os.listdir(category_path)):
                    if filename.endswith('.txt'):
                        with open(os.path.join(category_path, filename), encoding="utf8") as file:
                            file_content = file.read()
                            # Search for the string within the file
                            if search_string.lower() in file_content.lower():
                                title, description = file_content.split('\n', 1)
                                article_search.append({
                                    'category': category,
                                    'filename': filename.replace('.txt', ''),
                                    'title': title.replace('Title: ', ''),
                                    'description': description.replace('Description: ', '')
                                })

        # Generate the right format for the Jquery script in search.html
        num_results = len(article_search)

        return render_template('search.html', num_results=num_results, search_string=search_string,
                               article_search=article_search)
    else:
        return render_template('home.html')
