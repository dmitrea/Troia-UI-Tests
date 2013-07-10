from page import Page
from webDemoPage import WebDemoPage
from settings import Settings


class HomePage(Page):

    def __init__(self, driver):
        Page.__init__(self, driver)
        Page.navigate(self, Settings.url)

    def selectDemoApp(self, demoApp):
        if demoApp == 'GAL':
            self.clickButton('id', 'drop3')
            self.findElement('xpath', "id('menu3')/li[1]/a").click()
        else:
            self.clickButton('id', 'drop3')
            self.findElement('xpath', "id('menu3')/li[2]/a").click()
        return WebDemoPage(self.driver)


if __name__ == '__main__':
    homePage = HomePage()
    homePage.goToGALDemo()