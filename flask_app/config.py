# -*- coding: utf-8 -*-
# Where to store SQLite database
path_db = '/var/ttn_tracker/ttn_tracker_database.db'

# Period to download new data and display on the map (recommended not to go lower than 10 seconds)
refresh_period_seconds = 15

# Where the map initially loads
start_lat = 35.978781
start_lon = -77.855346

# TTN Application
application = "archie-gps-tracker"
app_key = "D92B57065E40ADABE34661D97429147D"

# Application devices
devices = [
    "eui-70b3d57ed0047e0e"
]

# Where to place gateway markers
gateway_locations = [

]

bing_api_key = 'Ahadal0at2YQ2IrKbvsgdJHY33DEVHDGndMa7ccJ7SPajyqlAsWbAeGslkaVoU-n'


def config_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=path_db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
