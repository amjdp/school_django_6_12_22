echo " BUILD START"
python3.10.4 pip install -r requirements.txt
python3.10.4 manage.py collectstatic

echo " BUILD END"