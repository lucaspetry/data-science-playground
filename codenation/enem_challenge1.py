import pandas as pd
import math
import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

url = 'https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-1/submit'
path_to_train = 'train.csv'
train_data = pd.read_csv(path_to_train)

submission = {}
submission['token'] = config['API']['token']
submission['email'] = config['API']['email']
submission['answer'] = list()

scores_dict = {}

for idx, row in train_data.iterrows():
    score_math = 0.3 * row['NU_NOTA_MT']
    score_nat = 0.2 * row['NU_NOTA_CN']
    score_lang = 0.15 * row['NU_NOTA_LC']
    score_hum = 0.1 * row['NU_NOTA_CH']
    score_essay = 0.3 * row['NU_NOTA_REDACAO']

    nu_inscricao = row['NU_INSCRICAO']
    nota_final = score_math + score_nat + score_lang + \
        score_hum + score_essay

    if not math.isnan(nota_final):
        scores_dict[nu_inscricao] = nota_final

selected = sorted(scores_dict.keys(),
                  key=scores_dict.__getitem__,
                  reverse=True)
count = 20

for nu_inscricao in selected:
    submission['answer'].append({'NU_INSCRICAO': nu_inscricao,
                                 'NOTA_FINAL': scores_dict[nu_inscricao]})
    count -= 1

    if count == 0:
        break

print(submission)
r = requests.post(url, data=json.dumps(submission))
print(r)
