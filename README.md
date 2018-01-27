# storyline
A story organization system

# running storyline

Here's how to run storyline locally
```
virtualenv env
source env/bin/activate
pip install -e .
export FLASK_APP=storyline
python -c 'from storyline import init_db; init_db()'
python -m flask run
```

Access storyline with your browser at http://localhost:5000