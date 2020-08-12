# allproducts = self.driver.find_elements_by_css_selector('div[class="card h-100"]')

        # allelements=driver.find_elements_by_xpath("//h4[@class='card-title']/a")
        listofproducts = ['Samsung Note 8', 'Nokia Edge', 'Blackberry']
        self.driver.execute_script("window.scrollTo(0,0);")
     #   gotocheckoutpage_meth().click()


   #     for i in allproducts:
            productname = i.checkout.get_productnames().text

            # productname = i.find_element_by_xpath("div/h4/a").text
            for selecteachproduct in listofproducts:
                if (productname == selecteachproduct):
                    time.sleep(1)
                    i.find_element_by_xpath("div[2]/button").click()

   #     verifyselecteditem = (self.driver.find_elements_by_class_name("media-body"))
        list = []
        for y in verifyselecteditem:
            name = y.find_element_by_xpath("h4").text
            list.append(name)
        print(list)
        print(listofproducts)
        assert (list == listofproducts)

        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()

        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)
        # driver.find_element_by_xpath("//a[contains(text(),'India')]").click()
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        time.sleep(1)
        # driver.find_element_by_id("checkbox2").click()
        self.driver.find_element_by_link_text("term & Conditions").click()
        self.driver.find_element_by_css_selector("button[class='btn btn-info']").click()
        # obj=driver.switch_to.alert
        # obj.dismiss()
        # driver.switch_to.default_content()
        # driver.find_element_by_css_selector("input[value='Purchase']").click()
        # driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
        time.sleep(1)
        # driver.find_element_by_class_name("btn btn-success btn-lg").click()
        self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        Stringsuccess = (
            self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)
        assert ("Success! Thank you!" in Stringsuccess)
        self.driver.get_screenshot_as_file("screenshot.png")

        # driver.close
