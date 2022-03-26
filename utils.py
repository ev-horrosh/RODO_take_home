import hashlib


def make_hash(filepath):
    '''
    returns the hash of the file
    '''

    with open(filepath, 'rb') as f:
        file = f.read()
        md5 = hashlib.md5()
        md5.update(file)
        return md5.hexdigest()
