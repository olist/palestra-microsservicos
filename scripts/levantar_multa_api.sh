echo "Levantando multa-api venv"
source ../multa-api/.venv/bin/activate
python ../multa-api/multa-api/manage.py runserver 127.0.0.1:8001
