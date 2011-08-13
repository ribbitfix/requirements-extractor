import yaml
import json

def extract_requirements(yaml_file, return_format='json'):
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
    
    for item in useful_data:
        if item in doc:
            req['data'][item] = doc[item]
        else:
            req['success'] = False
            req['errors'].append(item + ' not found')
    
    if return_format == 'dict':
        return req
    else:
        return json.dumps(req)
    

if __name__=='__main__':
    print extract_requirements('META.yml')

