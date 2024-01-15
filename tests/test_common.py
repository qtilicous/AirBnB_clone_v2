import unittest
import os

skip_if_not_db = unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Skipping test for non-DB storage")
