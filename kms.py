
import boto3
from os import environ
from base64 import b64decode

# if used on an aws service which role has permissions to use kms no keys are needed, otherwise you will need to provide an appropriate user keys to the client constructor
client = boto3.client('kms')


def getPasswordsFromKMS(client, KMSKey):
    """
    Takes a boto3 KMS client and returns the decrypted string of the stored value
    """
    plainBytes = client.decrypt(
        CiphertextBlob=b64decode(environ[KMSKey]))['Plaintext']
    plainStringValue = plainBytes.decode()
    return plainStringValue


# For EC2, you will have to encrypt your passwords beforehand and use the cipher in the functon below


def decrypt(client, cipher):
    valueBytes = client.decrypt(CiphertextBlob=b64decode(cipher))
    plainText = valueBytes.decode()
    return plainText
