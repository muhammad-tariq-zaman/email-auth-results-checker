import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check

class TestAuthResults(unittest.TestCase):
    def test_all_pass_trusted(self):
        _, trusted = check("spf=pass dkim=pass dmarc=pass")
        self.assertTrue(trusted)
    def test_one_fail_not_trusted(self):
        _, trusted = check("spf=pass dkim=fail dmarc=pass")
        self.assertFalse(trusted)
    def test_missing_not_trusted(self):
        results, trusted = check("spf=pass")
        self.assertEqual(results["dkim"], "NOT FOUND")
        self.assertFalse(trusted)
    def test_case_insensitive(self):
        results, _ = check("SPF=PASS DKIM=PASS DMARC=PASS")
        self.assertEqual(results["spf"], "PASS")
