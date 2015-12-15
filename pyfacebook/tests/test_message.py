import unittest

from .. import Message 

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.data = {
                "from": {
                    "name": "Jim",
                }, 
                "message": "Hello", 
                "created_time": "2015-12-12T22:22:22+0000",
        }
        self.conversation = None 
        self.msg = Message(self.data, self.conversation) 

    def test_comp(self):
        msg = Message(self.data, self.conversation) 
        data1 = self.data
        data1["from"]["name"] = "Parsons" 
        msg1 = Message(data1, self.conversation)
        self.assertTrue(msg == self.msg) 
        print(msg1.get_sender())
        print(self.msg.get_sender())
        self.assertFalse(msg1 == self.msg) 
