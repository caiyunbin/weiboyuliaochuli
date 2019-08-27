# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:24:25 2019

@author: Administrator
"""
from datetime import datetime
import pandas as pd
import csv
import numpy as np

###对数据乱码进行处理
###对数据类型进行转换
#data.isnull().any() 


def get_month_data(data):
    KX5 = data[data['内容'].str.contains('新一代KX5')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    KX3 = data[data['内容'].str.contains('全新一代K3')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    KX3chadian = data[data['内容'].str.contains('全新一代k3插电混动')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    K5 = data[data['内容'].str.contains('K5')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    K5chadian = data[data['内容'].str.contains('K5插电混动')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    zhipao = data[data['内容'].str.contains('新一代智跑')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    yipao = data[data['内容'].str.contains('奕跑')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    quanxinKX3 = data[data['内容'].str.contains('全新一代KX3')][['收藏数','转发数','评论数','点赞数','计数']].sum()
    return pd.DataFrame({
            '收藏数':[KX5[0],KX3[0],KX3chadian[0],K5[0],K5chadian[0],zhipao[0],yipao[0],quanxinKX3[0]],
            '转发数':[KX5[1],KX3[1],KX3chadian[1],K5[1],K5chadian[1],zhipao[1],yipao[1],quanxinKX3[1]],
            '评论数':[KX5[2],KX3[2],KX3chadian[2],K5[2],K5chadian[2],zhipao[2],yipao[2],quanxinKX3[2]],
            '点赞数':[KX5[3],KX3[3],KX3chadian[3],K5[3],K5chadian[3],zhipao[3],yipao[3],quanxinKX3[3]],
            '计数':[KX5[4],KX3[4],KX3chadian[4],K5[4],K5chadian[4],zhipao[4],yipao[4],quanxinKX3[4]]
            },index=['新一代KX5','全新一代K3','全新K3混动','K5','K5混动','新智跑','奕跑','全新KX3'])
            

def save_to_csv(dics):
    with open('C:/Users/Administrator/Desktop/文件集合/weibohuizong.csv','a',encoding='GB18030',newline='') as csvfile:
        fieldnames = ['新一代KX5','全新一代K3','全新K3混动','K5','K5混动','新智跑','奕跑','全新KX3']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow(dics)



def main():
    path ='C:/Users/Administrator/Desktop/文件集合/weiboneirong.csv'
    data = pd.read_csv(path, sep=",",engine = "python",encoding="GB18030",header=None,names=['时间','收藏数','转发数','评论数','点赞数','内容'])
    data['时间'] = pd.to_datetime(data['时间'])
    data['计数'] = np.ones(len(data))
    data['转发数'].replace({'转发':'0'},inplace=True)
    data['评论数'].replace({'评论':'0'},inplace=True)
    data['点赞数'].replace({'赞':'0'},inplace=True)
    data['点赞数']=data['点赞数'].fillna('0')
    data['内容']=data['内容'].fillna('无')
    data[['收藏数', '转发数','评论数','点赞数']] = data[['收藏数', '转发数','评论数','点赞数']].astype(int)
    period = data[(data["时间"]>= datetime(2019,3,1)) & (data["时间"]<= datetime(2019,6,1))]    
    content = get_month_data(period)
    content.to_csv('C:/Users/Administrator/Desktop/文件集合/weibohuizong.csv')

    #for item in content:
        
    #save_to_csv(content)
    

if __name__ == '__main__':
    main()


