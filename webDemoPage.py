from page import Page
import time


class WebDemoPage(Page):

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.waitUntilElementIsPresent('id', 'id_data_choose')

    def setAlgorithm(self, algorithm):
        self.selectListValue('id', 'id_algorithm_choose', algorithm)

    def setDataSet(self, dataSet):
        self.selectListValue('id', 'id_data_choose', dataSet)
        time.sleep(5)

    def processData(self):
        self.clickButton('id', 'send_data')
        self.waitUntilDataIsProcessed()

    def waitUntilDataIsProcessed(self):
        wait = 1
        while (wait == 1):
            self.waitUntilElementIsPresent('xpath', "id('result')")
            spinningImg = self.findElement('xpath', "id('result')/img")
            if spinningImg != None:
                imgStyleAttribute = spinningImg.get_attribute('style')
                if imgStyleAttribute == 'display: none;':
                    wait = 0

    def getResults_Summary_GAL(self):
        res = {}
        table = self.findElement('xpath', "id('summary_list')/tbody")
        res['no_workers'] = table.find_element_by_xpath('tr[1]/td[2]').text
        res['no_objects'] = table.find_element_by_xpath('tr[2]/td[2]').text
        res['assigned_labels'] = table.find_element_by_xpath('tr[3]/td[2]').text
        res['gold_labels'] = table.find_element_by_xpath('tr[4]/td[2]').text
        res['est_data_quality'] = table.find_element_by_xpath('tr[5]/td[2]/a').text
        res['est_workers_quality'] = table.find_element_by_xpath('tr[6]/td[2]/a').text
        res['eval_data_quality'] = table.find_element_by_xpath('tr[7]/td[2]').text
        res['eval_workers_quality'] = table.find_element_by_xpath('tr[8]/td[2]').text
        return res

    def getResults_Labels_GAL(self):
        self.clickButton('xpath', "id('resultsTab')/li[2]/a")
        return len(self.findElements('xpath', "id('objects_table')/table/tbody/tr"))

    def getResults_Workers_GAL(self):
        self.clickButton('xpath', "id('resultsTab')/li[3]/a")
        return len(self.findElements('xpath', "id('workers_table')/table/tbody/tr"))

    def getResults_Summary_GALC(self):
        self.waitUntilDataIsProcessed()
        res = {}
        table = self.findElement('xpath', "id('summary_list')/tbody")
        res['no_workers'] = table.find_element_by_xpath('tr[1]/td[2]').text
        res['no_objects'] = table.find_element_by_xpath('tr[2]/td[2]').text
        res['assigned_labels'] = table.find_element_by_xpath('tr[3]/td[2]').text
        res['gold_labels'] = table.find_element_by_xpath('tr[4]/td[2]').text
        return res

    def getResults_Labels_GALC(self):
        self.clickButton('xpath', "id('resultsTab')/li[2]/a")
        return len(self.findElements('xpath', "id('objects_table')/tbody/tr"))

    def getResults_Workers_GALC(self):
        self.clickButton('xpath', "id('resultsTab')/li[3]/a")
        return len(self.findElements('xpath', "id('workers_table')/tbody/tr"))

    def getResultsUrl(self):
        self.clickButton('xpath', "id('resultsTab')/li[1]/a")
        url = self.findElement('xpath', "id('url')/pre").text
        print url
        return url

    def downloadResults(self):
        self.clickButton('id', 'download_zip_btn')
