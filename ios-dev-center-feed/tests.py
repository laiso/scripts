import urllib2
import json
import unittest

class FeedActivityTest(unittest.TestCase):

    def setUp(self):
        self.sampleCodeJSON = urllib2.urlopen('http://pipes.yahoo.com/pipes/pipe.run?_id=2e692378a03f70e68eeaefbd75927624&_render=json').read()
        self.documentationJSON = urllib2.urlopen('http://pipes.yahoo.com/pipes/pipe.run?_id=265d351456e157e65ba1df00baf8c10d&_render=json').read()

    def testSomepleCodeCount(self):
        sampleCode = json.loads(self.sampleCodeJSON)
        self.assertEqual(sampleCode['count'], 20)

    def testDocumantationCount(self):
        documentation = json.loads(self.documentationJSON)
        self.assertEqual(documentation['count'], 20)

