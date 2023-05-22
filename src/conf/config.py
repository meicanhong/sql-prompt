import os
import yaml


current_path = os.path.dirname(__file__)

with open(current_path + '/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

DATABASE_CONF = config['database']
CHATGPT_CONF = config['chatgpt']


if __name__ == '__main__':
    print(config)
