import pandas as pd
import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

url = 'https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-2/submit'
path_to_train = 'train.csv'
train_data = pd.read_csv(path_to_train)

submission = {}
submission['token'] = config['API']['token']
submission['email'] = config['API']['email']
submission['answer'] = list()

# TO-DO

print(submission)
r = requests.post(url, data=json.dumps(submission))
print(r)
