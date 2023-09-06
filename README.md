# Developer Workflow
## [One Time] Clone Repo
```
cd ~/src/indieagi
git clone git@github.com:indieagi/website.git
```

## [One Time] Create Venv
This will create a Python virtual environment in the directory ``./iagi-venv`
```
python -m venv iagi-venv
```

## Update Repo
```
cd ~/src/indieagi/website
git pull
```

## Activate `iagi_venv` In Your Active Terminal Session
This will make it so installed packages etc don't interfere with your local system, and so your local system's packages don't interfere with this dev environment. If you don't do this, unexpected things may break while you develop.
```
source iagi-venv/bin/activate
```
Your terminal prompt should change to say `(iagi-venv)`.

## Copy Branch Name
Copy the branch name from the Linear Issue you are developing for by clicking the branch button or pressing `ctrl + shift + .` It should look something like this: `toby/agi-315-iagi-jug-island-meetup-invite`

If there is no Linear Issue for the task you are doing, please make one first.

## Create Branch
```
git checkout -b toby/agi-315-iagi-jug-island-meetup-invite
git push --set-upstream origin toby/agi-315-iagi-jug-island-meetup-invite
```
## Sanity Check Your Flask Server
Test the website using your local server, following the instructions given in this README.

## Make Your Edits and Commit Changes
Edit the files you intend to change. Commit your changes along the way.
```
subl {file-to-edit}
git commit -m "changed xyz about {file-to-edit}"
git push
```

## Test Your Changes
Test the website using your local server, following the instructions given in this README.

## Make Pull Request
Navigate to this repo in your web browser. Go to Pull Requests. Github should prompt you to make a Pull Request from your branch.

## Request Pull Request Review
Go to the [IndieAGI XFN project board on Linear](https://linear.app/indieagi/team/AGI/cycle/active). Change your issue's status to "In Review". At the next XFN Standup, the standup emcee will ask to review your pull request.

## Pull Request Approved + Deployment
Your request is now approved. The site automatically deploys to Railway when the PR is merged to `main` branch.

## Test indieagi.org Live Website
Navigate to the pages you changed on indieagi.org. Make sure they work.

## You're Done!
Congrats!

# Run Server Locally
## Venv Setup
- If you haven't aleady, create your venv `create_venv.sh`
- Activate your venv `source venv/bin/activate`
- Install Python requirements `pip install -r requirements.txt`
## Run Server
- Start the server for development `python main.py`
- Navigate to `127.0.0.1:5000`

# Selenium Tests
## Install ChromeDriver for Selenium on Ubuntu
- Download the latest version of ChromeDriver
- Run the following:
```
unzip chromedriver_linux64.zip
cd chromedriver_linux64.zip
sudo mv chromedriver /usr/bin
sudo chmod +x /usr/bin/chromedriver
```
- Test the installation
```
chromedriver --port=4444
# Navigate to http://localhost:4444 in your browser
# Success is if you see something like the following:
{"value":{"error":"unknown command","message":"unknown command: unknown command: ","stacktrace":"#0 0x5643a3570783 \u003Cunknown>\n#1 0x5643a329c917 \u003Cunknown>\n#2 0x5643a32f78de \u003Cunknown>\n#3 0x5643a32f75f5 \u003Cunknown>\n#4 0x5643a3269da3 \u003Cunknown>\n#5 0x5643a3531e98 \u003Cunknown>\n#6 0x5643a3535d67 \u003Cunknown>\n#7 0x5643a354032c \u003Cunknown>\n#8 0x5643a3536993 \u003Cunknown>\n#9 0x5643a3505827 \u003Cunknown>\n#10 0x5643a32682d1 \u003Cunknown>\n#11 0x7f5520e23a90 \u003Cunknown>\n"}}
```

## How to test
- `python tests/test_smoke_selenium.py`