import os
import nimbbl
import helpers

def mock_file(filename):
    if not filename:
        return ''
    file_dir = os.path.dirname(__file__)
    file_path = "{}/mocks/{}.json".format(file_dir, filename)
    with open(file_path) as f:
        mock_file_data = f.read()
    return mock_file_data
  
class TestClientOrder(helpers.ClientTestCase):

    def setUp(self):
        super(TestClientOrder, self).setUp()
        
    def test_verify_signature(self):
        signature={
            'nimbbl_signature':'41547fa353e7e01dd6cb85715fa323fa35e3f76bf383d4041c371daff7adb645',
            'nimbbl_transaction_id':'order_BmO74B5pZQJ4W3qx-20211018144400',
            'order_amount':14.0,
            'order_currency':'INR',
            'merchant_order_id':'order_BmO74B5pZQJ4W3qx'
        }
        util=nimbbl.Utility(self.client)
        hmac=util.validate_signature(signature)
        self.assertEqual(True,hmac)