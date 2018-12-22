@echo off
                   
pushd %cd%

c:\Python37\Scripts\virtualenv.exe virtualenv
rem call ./virtualenv/Scripts/activate.bat
rem pip install -i https://pypi.python.org/pypi --proxy http://10.100.192.1:3128/ -r ./requirements.txt
rem pip install -r ./requirements.txt
pip install ./requirements/Click-7.0-py2.py3-none-any.whl 
pip install ./requirements/Werkzeug-0.14.1-py2.py3-none-any.whl
pip install ./requirements/Jinja2-2.10-py2.py3-none-any.whl
pip install ./requirements/Flask-1.0.2-py2.py3-none-any.whl
pip install ./requirements/WTForms-2.2.1-py2.py3-none-any.whl
pip install ./requirements/Flask_WTF-0.14.2-py2.py3-none-any.whl
rem pip install -r ./requirements/dev.txt
rem pip install pypiwin32

popd
