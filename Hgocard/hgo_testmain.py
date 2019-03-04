# @Time    : 19-3-1
# @Author  : 欧阳
# @File    : hgo_testmain.py
import requests, json, traceback
from Hgocard import hgo_testlog

logging = hgo_testlog.get_logger()
res = None

"""定义Post"""
def HgoPost(host, port, url, querystring, payload, header=None):
    global response
    if header != None:
        try:
            res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   headers=header, timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", response)
    else:
        try:
            res = requests.request("Post", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", response)
    logging.info("接口请求url" + "-" * 20 + ">" * 2 + " %s", res.url)
    logging.info("接口请求data" + "-" * 20 + ">" * 2 + " %s", payload)
    Returncode()

"""定义Get"""
def HgoGet(host, port, url, querystring, payload, header=None):
    if header != None:
        try:
            res = requests.request("Get", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   headers=header, timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", response)
    else:
        try:
            res = requests.request("Get", url=host + port + url, params=querystring, data=json.dumps(payload),
                                   timeout=8, verify=False)
            response = res.content.decode('utf-8')
        except:
            logging.error("接口异常" + "-" * 20 + ">" * 2 + " %s", response)
    logging.info("接口请求url" + "-" * 20 + ">" * 2 + " %s", res.url)
    logging.info("接口请求data" + "-" * 20 + ">" * 2 + " %s", payload)
    logging.info("接口返回data" + "-" * 20 + ">" * 2 + " %s", response)

"""定义主体"""
def HgoMain(url, querystring, method='post',payload=None, header={'content-type': "application/json"}, host='http://172.17.13.74',
             port=':80'):
    if method == 'Post' or 'post':
        try:
            response = HgoPost(host, port, url, querystring, payload, header)
        except:
            traceback.print_exc()
    else:
        try:
            response = HgoGet(host, port, url, querystring, payload, header)
        except:
            traceback.print_exc()
    return response

"""获取token"""
def Token():
    token = json.loads(response)
    return token['data']['token']
"""获取ph_key"""
def Ph_key():
    ph_key = json.loads(response)
    return ph_key['data'][0]
"""获取billno"""
def Billno():
    billno=json.loads(response)
    return billno['data']['czk_rebate_hd']['billno']
"""获取cid"""
def Getcid():
    cid=json.loads(response)
    return cid['data']['cid']
"""获取cutype"""
def Getctype():
    ctype=json.loads(response)
    return ctype['data']['cust_type']
"""获取mobile"""
def Getmobile():
    mobile=json.loads(response)
    return mobile['data']['custmember']['cmmobile1']
"""获取award_bill"""
def Award_bill():
    award_bill=json.loads(response)
    return award_bill['data']['awardset'][0]['award_bill']
"""获取billno"""
def Getbillno():
    billno=json.loads(response)
    return billno['data']['billno']
"""获取cardno"""
def Getcardno():
    cardno=json.loads(response)
    return cardno['data']['datalist'][0]['cardno']

"""断言returncode"""
def Returncode():
    returncode=json.loads(response)
    code=returncode['returncode']
    if code == 0 or code == '0':
        logging.info("接口请求成功" + "-" * 20 + ">" * 2 + " %s", response)
    else:
        logging.debug("接口请求失败" + "-" * 20 + ">" * 2 + " %s", response)