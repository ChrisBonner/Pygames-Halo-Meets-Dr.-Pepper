# Sets up and handles conf file for UI
import ConfigParser

Conf = ConfigParser.SafeConfigParser({"author_name": 'My Name', 'author_email': 'address@email.com'})

try:
    Conf.read('pyg.conf')
except: pass