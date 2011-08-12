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

    req = dict(
            data = dict(),
            success = True,
                )
    for key in doc:
        if 'requires' in key or key == 'version' or key == 'name':
            req['data'][key] = doc[key]
    
    return json.dumps(req)
    

if __name__=='__main__':
    print extract_requirements('META.yml')

