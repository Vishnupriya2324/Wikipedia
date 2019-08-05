from selenium.webdriver.support.ui import Select
import time
import requests

class wikipediaPage():
    def __init__(self,driver):
        self.driver=driver
        self.oxygen="//span[.='O']"
        self.featuredArticle="//img[contains(@alt,'featured article')]"
        self.infobox="//table[@class='infobox']"
        self.pdf_count="//span[.='(PDF)']"
        self.search="searchInput"
        self.second_suggestion="(//div[@class='suggestions-results']/a)[2]"
        self.externalLinks="(//h2/span[@id='External_links']/../../ul)[2]/li/a"

    def verify_ExternalLinks(self):
        links=self.driver.find_elements_by_xpath(self.externalLinks)
        counter=1
        for link in links:
            #print(link)
            self.driver.find_element_by_xpath("(//h2/span[@id='External_links']/../../ul)[2]/li"+'['+str(counter)+"]/a")
            #print("(//h2/span[@id='External_links']/../../ul)[2]/li"+'['+str(counter)+"]/a"+'['+str(counter)+']')
            counter=counter+1
            href=link.get_attribute("href")
            #print(href)
            try:
                r = requests.head(href)
                if r.status_code == 200:
                    print(str(href) + " - is Valid.")
                else:
                    print(str(href) + " - Invalid.")
            except:
                print(str(href) + " - Not Responding")
        #self.driver.find_element_by_id(self.productlist).click()
        #1. Open the page https://en.wikipedia.org/wiki/...
# 2. Verify that the external links in “External links“ section work


# 3. Click on the “Oxygen” link on the Periodic table at the bottom of the page
# 4. Verify that it is a “featured article”
# 5. Take a screenshot of the right hand box that contains element properties
# 6. Count the number of pdf links in “References“
# 7. In the search bar on top right enter “pluto” and verify that the 2 nd suggestion
# is “Plutonium”




    def isFeaturedArticle(self):
        self.driver.find_element_by_xpath(self.oxygen).click()
        self.driver.find_element_by_xpath(self.featuredArticle).is_displayed()

    def take_screenshot(self):
        image=self.driver.find_element_by_xpath(self.infobox).screenshot_as_png
        print(type(image))
        fobj = open("C:\\Users\\Dell\\PycharmProjects\\submit\\some_image.jpg", "wb")
        fobj.write(image)
        fobj.close()

    def get_PDFCount(self):
        count=self.driver.find_elements_by_xpath(self.pdf_count)
        print(type(count))
        print("# of PDF Links is {0}".format(len(count)))


    def verify_plutonium(self):
        self.driver.find_element_by_id(self.search).send_keys("pluto")
        second_sugg=self.driver.find_element_by_xpath(self.second_suggestion).text
        print(second_sugg)
        assert second_sugg == "Plutonium"







