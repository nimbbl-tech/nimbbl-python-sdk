import hmac
import hashlib
import sys
import hmac

from ..errors import SignatureVerificationError


class Utility(object):
    def __init__(self, client=None):
        self.client = client

    # Taken from Django Source Code
    # Used in python version < 2.7.7
    # As hmac.compare_digest is not present in prev versions
    # def compare_string(self, expected_str, actual_str):
    #     """
    #     Returns True if the two strings are equal, False otherwise
    #     The time taken is independent of the number of characters that match
    #     For the sake of simplicity, this function executes in constant time only
    #     when the two strings have the same length. It short-circuits when they
    #     have different lengths
    #     """
    #     if len(expected_str) != len(actual_str):
    #         return False
    #     result = 0
    #     for x, y in zip(expected_str, actual_str):
    #         result |= ord(x) ^ ord(y)
    #     return result == 0
    
    def generate_nimbbl_header(self,submerchent_id,token):
        hash=hashlib.md5(bytes(token, 'utf-8'))
        return str(submerchent_id) +"-"+ hash.hexdigest()

    def validate_signature(self,attributes):
        actualSignature = attributes['nimbbl_signature'];
        transactionId = attributes['nimbbl_transaction_id'];
        order_amount = attributes['order_amount'];
        order_amount="{:.2f}".format(order_amount)
        order_currency = attributes['order_currency'];
        if "merchant_order_id" in attributes:
            orderId = attributes['merchant_order_id'];
            payload = orderId + '|' + transactionId+'|'+order_amount  +"|"+order_currency ;
        else:
            raise SignatureVerificationError("merchant_order_id must be present")
        print(payload)
        secret=self.client.secret;
        return self.verifySignature(payload, actualSignature, secret);
    
    def verifySignature(self,payload,actualSignature,secret):
        expectedSignature=self._hmac_sha256(payload, secret)
        print(expectedSignature)
        verified = hash(expectedSignature) == hash(actualSignature)
        return verified

    def _hmac_sha256(self,signature_data, secret_key):
        raw = signature_data.encode("utf-8")
        key = secret_key.encode('utf-8')
        return hmac.new(key=key, msg=raw, digestmod=hashlib.sha256).hexdigest()
    
        