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
        self.expected_json_dict = {
            'success' : True,
            'data' : { 'name' : 'ShiftJIS-CP932-MapUTF',
                       'version' : 1.03,
                       'configure_requires' :
                            { 'ExtUtils::MakeMaker' :  0 },
                        'build_requires' :
                           {    'ExtUtils::MakeMaker' :  0 },
                        'requires' :
                           {  'bytes' : 0,
                              'Carp' :  0,
                              'DynaLoader' :  0,
                              'Exporter' : 0,
                              'File::Copy' :  0,
                              'strict' : 0,
                              'vars' : 0 } } }
                                            

        self.fake_yaml_file = StringIO(self.fake_yaml_string)
        self.non_yaml_string = 'not actually yaml'

    def _test_extract_from_stringio(self):
        jsonresponse = reqextractor.extract_requirements(self.fake_yaml_file)
        self.assertEqual(type(''), type(jsonresponse))
        dictresponse = json.loads(jsonresponse)
        self.assertEqual(2, len(dictresponse.keys()))
        self.assertEqual(type({}), type(dictresponse['data']))
        self.assertEqual(5, len(dictresponse['data'].keys()))
        self.assertEqual(self.expected_json_dict, dictresponse)
        for key in dictresponse['data']:
            for key in self.expected_json_dict['data']:
                self.assertEqual(dictresponse['data'][key], self.expected_json_dict['data'][key])


    def _test_extract_from_string(self):
        jsonresponse = reqextractor.extract_requirements(self.fake_yaml_string)
        self.assertEqual(type(''), type(jsonresponse))
        dictresponse = json.loads(jsonresponse)
        self.assertTrue(dictresponse['success'])
        self.assertEqual(2, len(dictresponse.keys()))
        self.assertEqual(type({}), type(dictresponse['data']))
        self.assertEqual(5, len(dictresponse['data'].keys()))
        self.assertEqual(self.expected_json_dict, dictresponse)
        for key in dictresponse['data']:
            for key in self.expected_json_dict['data']:
                self.assertEqual(dictresponse['data'][key], self.expected_json_dict['data'][key])

    def test_non_yaml_string(self):
        jsonresponse = reqextractor.extract_requirements(self.non_yaml_string)
        self.assertEqual(type(''), type(jsonresponse))
        dictresponse = json.loads(jsonresponse)
        self.assertTrue(dictresponse['success'])
        self.assertEqual(2, len(dictresponse.keys()))
        self.assertEqual(type({}), type(dictresponse['data']))
        self.assertEqual(5, len(dictresponse['data'].keys()))

if __name__=='__main__':
    unittest.main()
