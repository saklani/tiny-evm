import json
import unittest
from tinyevm.evm import EVM

class TestOps(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        f = open("tests/evm.json", "r")
        self.data = json.load(f)
        f.close()

    def test_evm(self):
        evm = EVM()
        for i in range(30):
            data = self.data[i]
            with self.subTest(data=data):
                print(data['name'])
                expected = data['expect']['stack']
                result = evm.execute(code=data['code']['bin'])
                stack = [hex(x) for x in evm.context.stack.data]
                stack.reverse()
                self.assertEqual(stack, expected)
               
            
