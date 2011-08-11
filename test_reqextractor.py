import unittest
import reqextractor
import json
from cStringIO import StringIO

class ReqExtractorTests(unittest.TestCase):
    def setUp(self):
        self.fake_yaml_string = """--- #YAML:1.0
name:               ShiftJIS-CP932-MapUTF
version:            1.03
abstract:           transcode between Microsoft CP932 and Unicode
author:
    - SADAHIRO Tomoyuki <SADAHIRO@cpan.org>
license:            perl
distribution_type:  module
configure_requires:
    ExtUtils::MakeMaker:  0
build_requires:
    ExtUtils::MakeMaker:  0
requires:
    bytes:       0
    Carp:        0
    DynaLoader:  0
    Exporter:    0
    File::Copy:  0
    strict:      0
    vars:        0
no_index:
    directory:
        - t
        - inc
generated_by:       ExtUtils::MakeMaker version 6.57_05
meta-spec:
    url:      http://module-build.sourceforge.net/META-spec-v1.4.html
    version:  1.4
""" 
        expected_json_dict = {
            'success' : True,
            'data' : { 'name' : 'ShiftJIS-CP932-MapUTF',
                       'version' : '1.03',
                       'configure_requires' :
                            { 'ExtUtils::MakeMaker' :  '0' },
                        'build_requires' :
                           {    'ExtUtils::MakeMaker' :  '0' },
                        'requires' :
                           {  'bytes' : '0',
                              'Carp' :  '0',
                              'DynaLoader' :  '0',
                              'Exporter' : '0',
                              'File::Copy' :  '0',
                              'strict' : '0',
                              'vars' : '0' } } }
                                            

        self.fake_yaml_file = StringIO(self.fake_yaml_string)

    def _test_extract_from_stringio(self):
        jsonresponse = reqextractor.extract_requirements(self.fake_yaml_file)
        self.assertEqual(type(''), type(jsonresponse))
        dictresponse = json.loads(jsonreponse)
        self.assertEqual(2, len(dictresponse.keys()))

    def test_extract_from_string(self):
        jsonresponse = reqextractor.extract_requirements(self.fake_yaml_string)
        self.assertEqual(type(''), type(jsonresponse))
        dictresponse = json.loads(jsonresponse)
        import ipdb; ipdb.set_trace()
        self.assertTrue(dictresponse['success'])
        

if __name__=='__main__':
    unittest.main()
