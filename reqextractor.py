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
    
    for key in doc:
        if 'requires' in key or key == 'version' or key == 'name':
            req['data'][key] = doc[key]
    if len(req['data'].keys()) != 5:
        req['success'] = False
        if 'name' not in req['data']:
            req['errors'].append('name not found')
        if 'version' not in req['data']:
            req['errors'].append('version not found')
        if 'requires' not in req['data']:
            req['errors'].append('requires not found')
        if 'configure_requires' not in req['data']:
            req['errors'].append('configure_requires not found')
        if 'build_requires' not in req['data']:
            req['errors'].append('build_requires not found')
    
    return json.dumps(req)
    

if __name__=='__main__':
    print extract_requirements('META.yml')

