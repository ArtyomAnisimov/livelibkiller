deactivate
kill $(ps aux | grep '[p]ython manage.py runserver 0.0.0.0:8000' | awk '{print $2}')
virtualenv venv --python=python3 --prompt='(livelibkiller)'
source venv/bin/activate
pip install -r req.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
