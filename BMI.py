#!/usr/bin/env python
# coding: utf-8

# In[21]:


weight = float(input('請輸入體種是多少(公斤)?'))
height = float(input('請輸入身高是多少(公分)?'))
height = height / 100 
BMI = weight / height / height  
BMI = round(BMI,2)
if BMI >= 35 :
    print('BMI= ',BMI, ',重度肥胖')
elif BMI >= 30 and BMI < 35 :
    print('BMI= ',BMI, ',中度肥胖')
elif BMI >= 27 and BMI < 30 :
    print('BMI= ',BMI, ',輕度肥胖')   
elif BMI >= 24 and BMI < 27 :
    print('BMI= ',BMI, ',過重') 
elif BMI >= 18.5 and BMI < 24 :
    print('BMI= ',BMI, ',正常') 
else:
    print('BMI= ',BMI, ',過輕')


# In[ ]:





# In[ ]:




