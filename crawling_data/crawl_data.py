#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 20:55:17 2019

@author: ikhwan
"""

import requests
from bs4 import BeautifulSoup

product = open('//Users/ikhwan/project_1/crawling_data/kca_data/kca_data_0218.txt', 'a', encoding='utf-8')
product_ewg = open('//Users/ikhwan/project_1/crawling_data/kca_data/ewg_data_0218.txt', 'a', encoding='utf-8')
for i in range(1,10):
    url = 'http://kcia.or.kr/cid/search/ingd_view.php?no='+str(i)
    req = requests.get(url=url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tr_list = soup.findAll('tr')
    ingre_name_kr='empty'
    ingre_name_en='empty'
    ingre_purpose='empty'
    for t in tr_list:
        head = t.find('th').text
        if head == "성분명":
            ingre_name_kr = t.find('p').find('b').text

        if head == "영문명":
            ingre_name_en = t.find('p').text

 
        if head == "배합목적":
            ingre_purpose = t.find('p').text

    product.writelines(str(i)+"*"+ingre_name_kr+"*"+ingre_name_en+"*"+ingre_purpose)
    #print(depth1+","+depth2+","+depth3+","+Brand_raw+","+prd_ref+","+prd_name+","+price+","+prd_img_url+","+prd_url)
    product.write('\n')
    
    if ingre_name_en is not 'empty':
        ingre_name_en = ingre_name_en.replace(" ","+")
        url_ewg = 'https://www.ewg.org/skindeep/search.php?query='+ingre_name_en
        req_ewg = requests.get(url=url_ewg)
        html_ewg = req_ewg.text
        soup = BeautifulSoup(html_ewg, 'html.parser')
        div_img = soup.find('div',{'id':"prod_cntr_score"})
        if div_img is not None:
            img = div_img.find('img').get('src')
            data_status = div_img.find('div',{'id':'score_style_small'}).find('span').text
            product_ewg.writelines(str(i)+"*"+img+"*"+data_status)
            product_ewg.write('\n')
    print(str(i)+"번째"+ingre_name_kr)
    
product.close()
product_ewg.close()
    
