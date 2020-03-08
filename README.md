# The functional automated tests of simple form.
This tests require Python 3.* and pytest framework. Tests work on Chrome browser.

If you use PyCharm, you need to change test runner first:

Open the Settings/Preferences | Tools | Python Integrated Tools settings dialog.
In the Default test runner field select pytest.

*How to run tests*

1. Install project on a local machine:

cd <projects_folder>
git clone https://github.com/whyNat/Formularz_testy_automat.git


2. Create virtualenv and activate it:

$ pip install virtualenv
$ cd project_folder
$ virtualenv venv
$ source venv/bin/activate


3. In your project directory:

C:\Users\SomeUser\project_folder> venv\Scripts\activate

install packages using the pip command:

pip install -U pytest
pip install selenium


4. Download Chromedriver from https://chromedriver.chromium.org/downloads and add it to the path.
