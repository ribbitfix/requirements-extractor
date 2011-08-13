import yaml
import json

def extract_requirements(yaml_file):
    #import ipdb; ipdb.set_trace()
    try:
        fin = open(yaml_file)
        doc = yaml.safe_load(fin)
    except IOError:
        doc = yaml.load(yaml_file)
    except TypeError:
        doc = yaml.load(yaml_file)

    req = dict(data = dict(), success = True, errors = [])
    useful_data = ['name', 'version', 'configure_requires', 'build_requires', 'requires']
    
    for key in doc:
        if key in useful_data:
            req['data'][key] = doc[key]

    if len(req['data'].keys()) != 5:
        req['success'] = False
        for item in useful_data:
            if item not in req['data']:
                req['errors'].append(item + ' not found')
    
    return json.dumps(req)
    

if __name__=='__main__':
    print extract_requirements('META.yml')

