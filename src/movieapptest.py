from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.imdb.com")


def MovieAppTest():


	#search_field = driver.find_element_by_id("suggestion-search")
	search_field = driver.find_element_by_xpath("//input[@class='imdb-header-search__input searchTypeahead__input react-autosuggest__input']")
	search_field.clear()
	search_field.send_keys("Avatar")
	search_button = driver.find_element_by_id("suggestion-search-button")
	search_button.click()

	return


if __name__ == "__main__":
	MovieAppTest()