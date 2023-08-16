# hr-prof-test
Test for HR-Prof

Install libraries
pip install -r requirements.txt

Run ./prepare_data.py:
This will generate a file test_data_clean.csv in ./data folder

Run docker-compose up -d
This will create a container with postgresql and grafana
Connection postgresql to grafana:
https://grafana.com/docs/grafana/latest/administration/data-source-management/?utm_source=grafana_gettingstarted

Run ./init_db.py
This will initialize the database with the following file test_data_clean.csv

