# HybridFrameworkUpdated
This is the hybrid framework of python with html report

Steps for creation:
Create new prject - "Hybrid framework"
Create following folders
	Configurations(Directory)
	Logs(Directory)
	pageObjects(python package)
	Reports(Directory)
	Screenshots(Directory)
	testCases(python package)
	TestData(python package)
	utilities (Directory)
	
Create new Loginpage.py file under pageObjects
	capture xpath and initialize variables
Create new test_login.py file under testCases
Write test cases and call them using appropriate function
	update the conf test file for repetitive tasks (invoking browser)
call the screenshot function for taking screenshot

Run: pytest -v -s TestCases/test_login.py

Read common values from .ini file
Adding logs to all the class ***** needs to be implemented

add multiple browsers in conftest file
 pytest -v -s TestCases/test_login.py --browser edge

multiple browsers  parellel run 
pytest -v -s -n=4 TestCases/test_login.py --browser chrome

configure hook file in config file 
pytest -v -s -n=2 --html=Reports\reports.html TestCases/test_login.py --browser chrome

****run.bat**** file
pytest -v -s --html=Reports\reports.html TestCases/test_login_ddt.py --browser chrome
rem pytest -v -s -m "sanity or regression" --html=./Reports/reports.html TestCases/ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/reports.html TestCases/ --browser chrome
rem pytest -v -s -m "regression" --html=./Reports/reports.html TestCases/ --browser chrome

rem firefox
pytest -v -s -m "sanity" --html=./Reports/reports.html TestCases/ --browser firefox
rem pytest -v -s -m "sanity or regression" --html=./Reports/reports.html TestCases/ --browser firefox
rem pytest -v -s -m "sanity and regression" --html=./Reports/reports.html TestCases/ --browser firefox
rem pytest -v -s -m "regression" --html=./Reports/reports.html TestCases/ --browser firefox

****

***github commands**
git init
git remote add origin git@github.com:harishwarc/HybridFramework.git


