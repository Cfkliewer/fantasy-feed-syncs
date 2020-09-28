from flask import Flask
import requests
from sync import Sync

app = Flask(__name__)

s = Sync()
s.SyncTimeframe()
s.SyncTeam()
s.SyncSchedule()
s.SyncStanding()

if __name__ == '__main__':
    app.run()