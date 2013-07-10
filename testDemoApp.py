import unittest
from homepage import HomePage
from selenium import webdriver
from webDemoPage import WebDemoPage


class TestDemoApplications(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()

        def tearDown(self):
            self.driver.quit()

        def scenario_GAL(self, algorithm, dataset):
            homePage = HomePage(self.driver)
            webDemo = homePage.selectDemoApp('GAL')
            webDemo.setAlgorithm(algorithm)
            webDemo.setDataSet(dataset)
            webDemo.processData()

        def scenario_GALC(self, dataset):
            homePage = HomePage(self.driver)
            webDemo = homePage.selectDemoApp('GALC')
            webDemo.setDataSet(dataset)
            webDemo.processData()

        def checkResultsLink(self):
            webDemo = WebDemoPage(self.driver)
            resultsUrl = webDemo.getResultsUrl()
            webDemo.navigate(resultsUrl)
            webDemo.waitUntilDataIsProcessed()

        def checkResults(self, algType, expectedSummary, expectedLabelsCount, expectedWorkersCount):
            webDemo = WebDemoPage(self.driver)
            if algType == 'GAL':
                self.assertDictEqual(expectedSummary, webDemo.getResults_Summary_GAL())
                self.assertEqual(expectedLabelsCount, webDemo.getResults_Labels_GAL())
                self.assertEqual(expectedWorkersCount, webDemo.getResults_Workers_GAL())
            else:
                self.assertDictEqual(expectedSummary, webDemo.getResults_Summary_GALC())
                self.assertEqual(expectedLabelsCount, webDemo.getResults_Labels_GALC())
                self.assertEqual(expectedWorkersCount, webDemo.getResults_Workers_GALC())

        def test_GALDemo_EM_SmallDataset(self):
            self.scenario_GAL('EM Algorithm', 'Small: 25 assigned labels, 1 gold')
            expectedSummary = {'no_workers':u'5', 'no_objects':u'5','assigned_labels':u'25', 'gold_labels':u'1', 'est_data_quality':u'100%', 'est_workers_quality':u'73%', 'eval_data_quality':u'100%', 'eval_workers_quality':u'73%'}
            self.checkResults('GAL', expectedSummary, 5, 5)
            self.checkResultsLink()
            self.checkResults('GAL', expectedSummary, 5, 5)

        def test_GALDemo_MV_SmallDataset(self):
            self.scenario_GAL('Majority Vote', 'Small: 25 assigned labels, 1 gold')
            expectedSummary = {'no_workers':u'5', 'no_objects':u'5','assigned_labels':u'25', 'gold_labels':u'1', 'est_data_quality':u'52%', 'est_workers_quality':u'25%', 'eval_data_quality':u'60%', 'eval_workers_quality':u'73%'}
            self.checkResults('GAL', expectedSummary, 5, 5)
            self.checkResultsLink()
            self.checkResults('GAL', expectedSummary, 5, 5)

        def test_GALDemo_EM_LargeDataSet(self):
            self.scenario_GAL('EM Algorithm', 'Large: 5000 assigned labels, 30 golds')
            expectedSummary = {'no_workers':u'83', 'no_objects':u'1000','assigned_labels':u'5000', 'gold_labels':u'30', 'est_data_quality':u'79%', 'est_workers_quality':u'39%', 'eval_data_quality':u'48%', 'eval_workers_quality':u'42%'}
            self.checkResults('GAL', expectedSummary, 200, 83)
            self.checkResultsLink()
            self.checkResults('GAL', expectedSummary, 200, 83)

        def test_GALDemo_MV_LargeDataSet(self):
            self.scenario_GAL('Majority Vote', 'Large: 5000 assigned labels, 30 golds')
            expectedSummary = {'no_workers':u'83', 'no_objects':u'1000','assigned_labels':u'5000', 'gold_labels':u'30', 'est_data_quality':u'73%', 'est_workers_quality':u'44%', 'eval_data_quality':u'41%', 'eval_workers_quality':u'42%'}
            self.checkResults('GAL', expectedSummary, 200, 83)
            self.checkResultsLink()
            self.checkResults('GAL', expectedSummary, 200, 83)

        def test_GALCDemo(self):
            self.scenario_GALC('200 assigned labels, 10 golds')
            expectedSummary = {'no_workers':u'2', 'no_objects':u'100','assigned_labels':u'200', 'gold_labels':u'10'}
            self.checkResults('GALC', expectedSummary, 100, 2)
            self.checkResultsLink()
            self.checkResults('GALC', expectedSummary, 100, 2)