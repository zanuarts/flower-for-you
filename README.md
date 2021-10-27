# Flowers Classification - Demo Deployment

## Installation

1. Clone repository

```git clone https://github.com/zanuarts/flower-for-you.git```

2. Install Virtual Environemnt

```virtualenv env```

3. Install Requirements

```pip install -r requirements.txt```

4. Import Flask App & Run

```
export FLASK_APP=app.py
flask run
```
---

## Deploy Machine Learning Model with Flask on Heroku

1. Create account in Heroku: https://id.heroku.com/login

2. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install

3. Login to Heroku from Terminal


```
# go to project folder
cd
your-path\flower-for-you

# activate virtual environment
source env\lib\activate

# login to heroku account
heroku login
```

5. Install Gunicorn

```pip install gunicorn```

6. Create Procfile

Enter this code to Procfile:

```web:gunicorn app:app```

7. Create Heroku app, add files to Git and deploy

```
heroku create 'your-heroku-app-name'

# add files to git
git add .
git commit -m "Deploy to heroku"
git push heroku master
```

---

Credits & Full Tutorial: [Deploy Machine Learning Model with Flask on Heroku](https://medium.com/@nutanbhogendrasharma/deploy-machine-learning-model-with-flask-on-heroku-cd079b692b1d)
