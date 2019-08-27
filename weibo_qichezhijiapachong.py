# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:59:25 2019

@author: Administrator
"""
import re 
import time
import csv
from lxml import etree
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
USERNAME = 'yuedaqiya2008'
PASSWORD = '********'
browser = webdriver.Chrome()


def log_in(username,password):
    url = 'https://weibo.com/p/1006061348898682/home?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop'
    browser.get(url)
    browser.maximize_window()
    print('请输入账号')
    time.sleep(45)
    

def scroll_to_bottom():
    # 最多尝试 20 次滚屏
    print ("开始滚屏")
    for i in range(0,50):       
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        html = browser.page_source
        tr = etree.HTML(html)
        next_page_url = tr.xpath('//a[contains(@class,"page next")]')
        if len(next_page_url) > 0:
            return next_page_url[0].get('href')
        if len(re.findall('点击重新载入', html)) > 0:
            print ('滚屏失败了，请刷新')
            browser.find_element_by_link_text('点击重新载入').click()
        time.sleep(1.6)

def get_page_source(page):
    url = 'https://weibo.com/p/1006061348898682/home?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page='+str(page)+'&pagebar=1'
    browser.get(url)
    scroll_to_bottom()
    return browser.page_source

def parse_one_page(content):
    doc = pq(content)
    weiboit = doc('.WB_cardwrap.WB_feed_type.S_bg2.WB_feed_like').items()
    for item in weiboit:
        yield{
                '时间':item('.WB_detail .WB_from.S_txt2 a').attr('title').strip()[0:10],
                '收藏数':item('.WB_row_line.WB_row_r4.clearfix.S_line2 li').eq(0).find('.line.S_line1 i').attr('title')[9:-1],
                '转发数':item('.WB_row_line.WB_row_r4.clearfix.S_line2 li').eq(1).find('em').eq(1).text(),
                '评论数':item('.WB_row_line.WB_row_r4.clearfix.S_line2 li').eq(2).find('em').eq(1).text(),
                '点赞数':item('.WB_row_line.WB_row_r4.clearfix.S_line2 li').eq(3).find('em').eq(1).text(),
                '内容':item('.WB_detail .WB_text.W_f14').text()
                }



def save_to_csv(dics):
    with open('C:/Users/Administrator/Desktop/文件集合/weiboneirong.csv','a',encoding='GB18030',newline='') as csvfile:
        fieldnames = ['时间','收藏数','转发数','评论数','点赞数','内容']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow(dics)


def main():
    log_in(USERNAME,PASSWORD)
    for page in range(1,100):
        a = get_page_source(page)
        b = parse_one_page(a)
        for item in b:
            save_to_csv(item)
            
    
if __name__ == '__main__':
    main()


