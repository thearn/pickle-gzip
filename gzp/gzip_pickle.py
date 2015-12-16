import pickle
import gzip

def save(object, filename, protocol = 0):
        """Saves a compressed object to disk
        """
        fil = gzip.GzipFile(filename, 'wb')
        fil.write(pickle.dumps(object, protocol))
        fil.close()

def load(filename):
        """Loads a compressed object from disk
        """
        fil = gzip.GzipFile(filename, 'rb')
        buffer = ""
        while True:
                data = fil.read()
                if data == "":
                        break
                buffer += data
        object = pickle.loads(buffer)
        fil.close()
        return object
