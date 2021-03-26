#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
import time, requests
import random
from keys import username, password


# In[3]:


driver = webdriver.Chrome('/Users/nikkisalehi/downloads/chromedriver')
time.sleep(2)


# In[4]:


driver.get('https://www.github.com')
time.sleep(2)


# In[5]:


driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
time.sleep(2)


# In[6]:


driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
time.sleep(3)


# In[7]:


driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
time.sleep(2)


# In[1]:


num = random.randint(1,200)
time.sleep(2)


# In[2]:


driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(f"new-repo-{num}")
time.sleep(2)


# In[3]:


driver.find_element_by_xpath('//*[@id="repository_auto_init"]').click()
time.sleep(2)


# In[4]:


driver.find_element_by_xpath('//*[@id="new_repository"]/div[6]/button').click()
time.sleep(2)


# In[ ]:




