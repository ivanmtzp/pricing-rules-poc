@echo off
                   
pushd %cd%

c:\Python37\Scripts\virtualenv.exe virtualenv
call ./virtualenv/Scripts/activate.bat
rem pip install -i https://pypi.python.org/pypi --proxy http://10.100.192.1:3128/ -r ./requirements.txt
rem pip install -r ./requirements.txt
pip install Click-7.0-py2.py3-none-any.whl 
pip install Werkzeug-0.14.1-py2.py3-none-any.whl
pip install Jinja2-2.10-py2.py3-none-any.whl
pip install Flask-1.0.2-py2.py3-none-any.whl
pip install WTForms-2.2.1-py2.py3-none-any.whl
pip install Flask_WTF-0.14.2-py2.py3-none-any.whl
rem pip install -r ./requirements/dev.txt
rem pip install pypiwin32

popd
