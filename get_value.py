#coding=utf-8

#import urllib
#import urllib.request
import re
import random
import time
import tushare as ts  



date_now='2018-03-09'
### 读取list 
fp_in=open('ttt.txt');
fp_out=open('tmp', 'w');
for id in fp_in:

    id=id.strip(); ## 300491

    f = ts.get_k_data(id, start='2018-03-09',end='2018-03-09')
    fp_out.write("%s\n"%(f));

fp_in.close();
fp_out.close();


ii=0;
fp_in=open('tmp');
fp_out=open('ttt_out.txt','w');
for line in fp_in:
    line=line.strip();
    if line == 'Empty DataFrame':
        continue;
    ii += 1;
    if ii %2 == 0:
        vec = line.split(); 
        if len(vec)<8:
            print('error:%s\n'%(line));
        else:
            fp_out.write("%s\t%s\n"%(vec[7], vec[3]));


fp_in.close();
fp_out.close();

