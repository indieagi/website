# Setup
## System Setup
### Ubuntu
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
## Python Setup
- If you haven't aleady, create your venv `create_venv.sh`
- Activate your venv `source dev_venv/bin/activate`
- Install Python requirements `pip install -r requirements.txt`
# How to run
- Start the server for development `python main.py`
- Navigate to `127.0.0.1:5000`

# How to test
- `python tests/test_smoke_selenium.py`