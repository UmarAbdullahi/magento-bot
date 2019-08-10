from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import autoit
import time
import urllib.request
import os, sys

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def scrape(self):
        bot = self.bot
        for v in range(17, 26):
            bot.get('http://genuss.ng/computer-accessories.html?p='+str(v))
            time.sleep(15)

            for n in range (1, 21):
                product = "product"+str(n)
                pro = "pro"+str(n)
                product = bot.find_element_by_xpath('//html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[3]/ul/li['+str(n)+']/div/a')
                pro = product.get_attribute('href')
                # print(pro)

                bot.get(pro)
                title = "title"+str(n)
                title = bot.find_element_by_xpath('//html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[4]/div[1]/form/div[4]/div[1]/h1').text
                print(title)

                price = "price"+str(n)
                price = bot.find_element_by_xpath('//html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[4]/div[1]/form/div[4]/div[2]/div[1]/div/span/span').text
                #print(price)
                pprice = price[1:]
                ppprice = pprice.replace(',','')
                #print(ppprice)

                sku = 'sku'+str(n)
                sku = bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[4]/div[1]/form/div[4]/div[2]/div[2]/p[1]/span').text
                #print(sku)

                sdesc = "short-desc"+str(n)
                sdesc = bot.find_element_by_xpath('//html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[4]/div[1]/form/div[4]/div[4]/div').text
                #print(sdesc)

                ldesc = "long-desc"+str(n)
                ldesc = bot.find_element_by_xpath('//html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[4]/div[2]/div[1]/div').text
                #print(ldesc)

                img = "image"+str(n)
                img = bot.find_element_by_xpath('//html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[4]/div[1]/form/div[3]/div[1]/div/a/img').get_attribute('src')
                urllib.request.urlretrieve(img, "image{}.png".format(str(n)))

                if v == 17:
                    bot.execute_script("window.open('');")
                bot.switch_to.window(bot.window_handles[1])
                time.sleep(2)

                if v == 17:
                    bot.get('http://emd.genuss.ng/admin_q0n5jd/')
                    time.sleep(5)
                    email = bot.find_element_by_name('login[username]')
                    password = bot.find_element_by_name('login[password]')
                    email.clear()
                    password.clear()
                    email.send_keys(self.username)
                    password.send_keys(self.password)
                    password.send_keys(Keys.RETURN)
                    time.sleep(10)
                    bot.refresh()
                    time.sleep(15)
                    catalog = bot.find_element_by_xpath("//div[1]/nav/ul/li[2]/a")
                    catalog.click()
                    time.sleep(5)
                    product = bot.find_element_by_xpath('//div[1]/nav/ul/li[2]/div/ul/li/div/ul/li/a')
                    product.click()
                    time.sleep(10)
                    addproduct = bot.find_element_by_id("add_new_product-button").click()
                    time.sleep(15)

                
                time.sleep(5)
                bot.find_element_by_name("product[sku]").send_keys(sku)
                bot.find_element_by_name("product[name]").send_keys(title)
                bot.find_element_by_name("product[price]").send_keys(ppprice)
                
                bot.execute_script("scroll(0, 390);")
                #categories
                bot.find_element_by_xpath('//html/body/div[2]/main/div[2]/div/div/div/div[2]/div[1]/div/fieldset/fieldset[4]/div/div[1]/div[2]/div/div[1]').click()
                bot.find_element_by_xpath('//html/body/div[2]/main/div[2]/div/div/div/div[2]/div[1]/div/fieldset/fieldset[4]/div/div[1]/div[2]/div/div[2]/ul/li/ul/li[9]/div').click()
                bot.find_element_by_xpath('//html/body/div[2]/main/div[2]/div/div/div/div[2]/div[1]/div/fieldset/fieldset[4]/div/div[1]/div[2]/div/div[2]/div[2]/button').click()
                # click and upload descriptions
                bot.find_element_by_xpath('//html/body/div[2]/main/div[2]/div/div/div/div[2]/div[3]/div[1]').click()
                time.sleep(4)
                bot.execute_script("scroll(390, 1220);")
                desc = bot.find_element_by_id('product_form_description_ifr')
                desc.click()
                time.sleep(2)
                desc.send_keys(ldesc)
                bot.execute_script("scroll(1220, 1620);")
                time.sleep(2)
                shortdesc = bot.find_element_by_id('product_form_short_description_ifr')
                shortdesc.click()
                time.sleep(2)
                shortdesc.send_keys(sdesc)
                # bot.find_element_by_xpath('//div/div[2]/div[5]/div[1]').click()
                # time.sleep(1)
                # continue from here,
                bot.execute_script("scroll(1620, 2990);")
                
                bot.find_element_by_xpath('//html/body/div[2]/main/div[2]/div/div/div/div[2]/div[5]/div[1]').click()
                time.sleep(2)
                bot.find_element_by_xpath('//html/body/div[2]/main/div[2]/div/div/div/div[2]/div[5]/div[2]/fieldset/div/div[2]/div[1]/div[1]/div[1]').click()
                filepath = "C:\\Users\\Umar\\Desktop\\Code\\magento-bot\\image"+str(n)+".png"
                autoit.win_wait_active("File Upload", 6)
                if autoit.win_exists("File Upload"):
                    autoit.control_send("File Upload","Edit1", filepath+"{ENTER}")
                
                # bot.find_element_by_id('fileupload').send_keys(os.getcwd()+"\image"+str(n)+".png")
                time.sleep(19)
                bot.find_element_by_id('save-button').click()
                time.sleep(30)
                bot.execute_script("window.history.go(-1)")
                time.sleep(19)
                    
                    #drv.find_element_by_id("IdOfInputTypeFile").send_keys(os.getcwd()+"/image.png")

                bot.switch_to.window(bot.window_handles[0])
                time.sleep(4)
                bot.execute_script("window.history.go(-1)")
                time.sleep(16)

            




           # /html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/a

        # products = bot.find_element_by_id("product-original-image-970")
        # pro = products.get_attribute('src')
        # print(pro)

        # name = bot.find_element_by_xpath("//html/body/div[3]/div/div[2]/div[1]/div/div[1]/div/div[3]/ul/li[1]/div/div[1]/h2/a")
        # proname = name.get_attribute()
        # print(proname)

        # for pro in products:
        #     print(pro.get_attribute('src'))

ed =  TwitterBot('umar','Mku4?MQ5=83oV4E>qu9:KrWBY8uG*786')
ed.scrape()
# ed.login()
# ed.addProduct()
# ed.like_tweet('i love you')