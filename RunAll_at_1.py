import unittest
import HtmlTestRunner
import os  

os.makedirs("Reports", exist_ok=True)
os.makedirs("Screenshots", exist_ok=True)


# Import your test case classes
from Effect_on_Agent import EffectonAgent_1Class
from TestCase3_CompleteFlow import TestCase3_CompleteFlowFunction

if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestSuite()
    
    # Add both test cases to the suite using the updated loader
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestCase3_CompleteFlowFunction))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(EffectonAgent_1Class))
    
    # Run the suite
    runner = HtmlTestRunner.HTMLTestRunner(
        output="Reports",
        report_title="Combined Selenium Test Report",
        combine_reports=True
    )
    runner.run(suite)
