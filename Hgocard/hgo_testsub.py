# @Time    : 19-3-1
# @Author  : 欧阳
# @File    : hgo_testsub.py
from Hgocard import hgo_testvariable
from Hgocard import hgo_testmain
import string, random

"""变量-字段"""
#整数
number = hgo_testvariable.Billmoduleid()
number1 = hgo_testvariable.Number_BJZ()
number2 = hgo_testvariable.Number_bjz()
#小数
fractional = hgo_testvariable.Fractional()
fractional1 = hgo_testvariable.Fractional_bjz()
fractional2 = hgo_testvariable.Fractional_BJZ()
#时间
sdate = hgo_testvariable.Sdate()
edate = hgo_testvariable.Edate()
inputdate = hgo_testvariable.Inputdate()
#手机号
mobile = hgo_testvariable.Hfmobile()
mobile1 = hgo_testvariable.Ffmobile()
mobile2 = hgo_testvariable.Ffmobile1()
token1 = ''.join(random.sample(string.ascii_letters + string.punctuation + string.digits, 32))  # Token
chinese = hgo_testvariable.Chinese()  # 中文
english = hgo_testvariable.Emoji()  # 英文
notation = hgo_testvariable.Notation()  # 符号
emoji = hgo_testvariable.Emoji()  # Emoji
Sql = hgo_testvariable.Sqlinfused()  # Sql注入

"""变量-JSON类"""
class Jsonpayload(object):
#获取Token
    def Hqtoken(self):
        self.hqtoken = {"code": "1582944742277124566", "password": "j8ptrt", "tag": "mss"}
        return self.hqtoken
#购卡优惠
    def Gkyh(self):
        self.gkyh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": "9006666", "rebate_target": "1", "sdate": sdate,
                "inputer_name": "[admin]惠Go MSS 管理员", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.gkyh
#充值优惠
    def Czyh(self):
        self.czyh = {"flag": "I", "billmoduleid": "9006666", "billstatus": "N", "inputer": "admin", "sdate": sdate, "singlelimit": "22",
                "czk_rebate_det": [{"rebate_discount_money": "99",
                                    "flag": "I", "rebate_condition": "88", "_state": "added", "_id": 70, "_uid": 70}],
                "pagesize": "100", "rebate_type": "1", "edate": edate, "rebate_target": "1",
                "inputer_name": "[admin]惠Go MSS 管理员", "inputdate": inputdate, "totallimit": "0", "summary": "E"}
        return self.czyh
# 随机生成购卡模块号
    def Gkyh1(self):
        self.gkyh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": number, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.gkyh
# 随机生成充值模块号
    def Czyh1(self):
        self.czyh = {"flag": "I", "billmoduleid": number, "billstatus": "N", "inputer": "admin", "sdate": sdate, "singlelimit": "22",
                "czk_rebate_det": [{"rebate_discount_money": "99",
                                    "flag": "I", "rebate_condition": "88", "_state": "added", "_id": 70, "_uid": 70}],
                "pagesize": "100", "rebate_type": "1", "edate": edate, "rebate_target": "1",
                "inputer_name": "admin", "inputdate": inputdate, "totallimit": "0", "summary": "E"}
        return self.czyh
# 重复
    def Cfdh(self):
        self.cfdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": number, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.cfdh
# 空
    def Kdh(self):
        self.kdh = {"flag": "I", "billmoduleid": "", "billstatus": "N", "inputer": "admin", "sdate": sdate, "singlelimit": "12",
               "czk_rebate_det": [{"rebate_discount_money": "69",
                                   "flag": "I", "rebate_condition": "88", "_state": "added", "_id": 67, "_uid": 67}],
               "summary": "EC", "rebate_type": "1", "edate": edate, "rebate_target": "1",
               "inputer_name": "admin", "inputdate": inputdate, "totallimit": "0"}
        return self.kdh
# 英文
    def Endh(self):
        self.endh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": english, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.endh
# 符号
    def Fhdh(self):
        self.fhdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": notation, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.fhdh
# 小数
    def Xsdh(self):
        self.xsdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": fractional, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.xsdh
# 中文
    def Cndh(self):
        self.cndh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": chinese, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.cndh
# 表情
    def Bqdh(self):
        self.bqdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": emoji, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.bqdh
# 不传
    def Wdh(self):
        self.wdh = {"flag": "I", "billstatus": "N", "inputer": "admin", "sdate": sdate, "singlelimit": "12",
               "czk_rebate_det": [{"rebate_discount_money": "69",
                                   "flag": "I", "rebate_condition": "88", "_state": "added", "_id": 67, "_uid": 67}],
               "summary": "C", "rebate_type": "1", "edate": edate, "rebate_target": "1",
               "inputer_name": "admin", "inputdate": inputdate, "totallimit": "0"}
        return self.wdh
# SQL注入
    def Zrdh(self):
        self.zrdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": Sql, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.zrdh
#整数
    def Zsdh(self):
        self.zsdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": number1, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.zsdh
    def Zsdh1(self):
        self.zsdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": number2, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.zsdh
#小数
    def Xsdh1(self):
        self.xsdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": fractional1, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.xsdh
    def Xsdh2(self):
        self.xsdh = {"inputdate": inputdate, "czk_rebate_det": [
            {"flag": "I", "rebate_condition": "88", "rebate_discount_money": "99", "_state": "added", "_id": 66,
             "_uid": 66}],
                "rebate_type": "1", "inputer": "admin", "billmoduleid": fractional2, "rebate_target": "1", "sdate": sdate,
                "inputer_name": "admin", "singlelimit": "11",
                "flag": "I", "summary": "C", "totallimit": "0", "edate": edate, "billstatus": "N"}
        return self.xsdh
#会员认证
    def Getauth(self):
        self.auth = {"channel_id": "APP", "corp_id": "002", "mkt_id": "201", "id_type": "2",
                     "id_keyword": "13986106008", "id_password": "123456", "fields": "*,consumers_data"}
        return self.auth
#充值优惠信息
    def Getczyhxx(self):
        self.czyxxx = {"channel_id": "APP", "cid": getcid, "ctype": getctype, "summary": "E"}
        return self.czyxxx
#获取卡列表
    def Gethqklb(self):
        self.hqklb = {"page_no": 1, "page_size": 10, "can_deposit": "Y", "channel_id": "APP", "status": "Y",
                      "cid": getcid}
        return self.hqklb
#充值订单提交
    def Getczddtj(self):
        self.czddtj = {"UserAgreement": "免责声明", "market": "6206", "channel_id": "APP", "cid": getcid,
                       "ctype": getctype, "cflag": "04", "wxid": "", "mobile": getmobile,
                       "corp_id": "0", "cardno": cardno, "face_value": 1, "amount": 1, "discount": 0, "award": 0,
                       "summary": "E", "memo": "储值卡[" + cardno + "]充值1.00元"}
        return self.czddtj
#充值订单查询
    def Getczddcx(self):
        self.czddcx = {"page_no": 1, "page_size": 1, "billno": getbillno, "channel_id": "APP", "cid": getcid}
        return self.czddcx
#充值订单完成
    def Getczddwc(self):
        self.czddwc = {"channel_id": "APP", "billno": getbillno, "summary": "E", "eventtype": "02", "merchantid": "",
                       "transaction_id": "", "out_trade_no": "CHAG" + getbillno, "total_fee": 100,
                       "paycode": "debugpay", "payname": "模拟支付", "payref1": "", "payref2": "", "payref3": ""}
        return self.czddwc
#会员注册
    def Getreg(self):
        self.reg = {"channel_id": "WECHAT", "name": chinese, "nick_name": chinese, "reg_method": "2",
                    "reg_keyword": mobile, "reg_password": "", "mkt": "201", "invitedby": ""}
        return self.reg
#会员绑定
    def Getbind(self):
        self.bind = {"channel_id": "WECHAT", "reg_type": "5", "reg_keyword": mobile, "reg_password": "",
                     "name": chinese, "oper_type": "A", "id_type": "2",
                     "id_keyword": mobile, "id_password": ""}
        return self.bind
#可售卖清单查询
    def Getsdatemqdcx(self):
        self.sdatemqdcx = {"page_no": 1, "page_size": 1, "status": "%", "channel_id": "APP", "cid": zccid,
                        "ctype": zcctype, "cflag": "04", "wxid": "limin", "receiver_mobile": mobile}
        return self.sdatemqdcx
#购卡优惠信息
    def Getgkyxxx(self):
        self.gkyxxx = {"channel_id": "APP", "cid": zccid, "ctype": zcctype, "summary": "C"}
        return self.gkyxxx
#购卡订单提交
    def Getgkddtj(self):
        self.gkddtj = {"UserAgreement": "免责声明", "market": "6206", "channel_id": "APP", "cid": zccid,
                       "ctype": zcctype, "cflag": "04", "wxid": "limin", "mobile": mobile, "corp_id": "0",
                       "summary": "C", "card_num": 1, "memo": "购买100元面值储值卡1张", "amount": 89, "discount": 11, "award": 0,
                       "award_bill": gokaward_bill, "sale_price": 100, "face_value": 100, "cardtype": "468",
                       "cardtype_name": "HGO电子卡"}
        return self.gkddtj
#购卡订单查询
    def Getgkddcx(self):
        self.gkddcx = {"page_no": 1, "page_size": 1, "billno": gokbillno, "channel_id": "APP", "cid": zccid}
        return self.gkddcx
#购卡订单完成
    def Getgkddwc(self):
        self.gkddwc = {"channel_id": "APP", "billno": gokbillno, "summary": "C", "eventtype": "01", "merchantid": "",
                       "transaction_id": "", "out_trade_no": "PURH" + gokbillno, "total_fee": 8900,
                       "paycode": "debugpay", "payname": "模拟支付", "payref1": "", "payref2": "", "payref3": ""}
        return self.gkddwc
#调用
getjson = Jsonpayload()

if __name__ == '__main__':
    """获取Token"""
    hgo_testmain.HgoMain(url='/amp-auth-service/rest', querystring={'method': 'amp.auth.authentication.signInNoEnt'},
             payload=getjson.Hqtoken())
    token = hgo_testmain.Token()

    """新增购卡优惠"""
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600, 'token': token},
             payload=getjson.Gkyh())
    ph_key = hgo_testmain.Ph_key()

    """审核购卡优惠"""
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': 1582944742277124600, 'token': token},
             payload=ph_key)
    billno=hgo_testmain.Billno()
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': 1582944742277124600, 'token': token},
            payload={'billno':billno})

    """新增充值优惠"""
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600, 'token': token},
             payload=getjson.Czyh())
    ph_key1 = hgo_testmain.Ph_key()

    """审核充值优惠"""
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.rebate.get', 'ent_id': 1582944742277124600, 'token': token},
             payload=ph_key1)
    billno1 = hgo_testmain.Billno()
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.rebate.billaudit', 'ent_id': 1582944742277124600, 'token': token},
            payload={'billno':billno1})

    """会员认证+充值"""
    #认证
    hgo_testmain.HgoMain(port=':91', url='/ocm-info-webin/rest',
            querystring={'method': 'efuture.ocm.info.main.auth', 'ent_id': '1582944742277124566'},
            payload=getjson.Getauth())
    getcid = hgo_testmain.Getcid()
    getctype = hgo_testmain.Getctype()
    getmobile = hgo_testmain.Getmobile()
    #充值优惠信息
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.card.award', 'token': token},
            payload=getjson.Getczyhxx())
    #获取卡列表
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.card.getlist', 'token': token},
            payload=getjson.Gethqklb())
    cardno=hgo_testmain.Getcardno()
    #充值订单提交
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.card.deposit', 'token': token},
            payload=getjson.Getczddtj())
    getbillno=hgo_testmain.Getbillno()
    #充值订单查询
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.card.ordersearch', 'token': token},
            payload=getjson.Getczddcx())
    #充值订单完成
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.card.orderfinish', 'token': token},
            payload=getjson.Getczddwc())

    """会员注册+绑定+购卡"""
    #注册
    hgo_testmain.HgoMain(port=':91', url='/ocm-info-webin/rest',
            querystring={'method': 'efuture.ocm.info.main.fastregister', 'ent_id': '1582944742277124566'},
            payload=getjson.Getreg())
    zccid=hgo_testmain.Getcid()
    zcctype=hgo_testmain.Getctype()
    #绑定
    hgo_testmain.HgoMain(port=':91', url='/ocm-info-webin/rest',
            querystring={'method': 'efuture.ocm.info.main.bind', 'ent_id': '1582944742277124566'},
            payload=getjson.Getbind())
    #可售卖清单查询
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.card.salelist', 'token': token},
             payload=getjson.Getsdatemqdcx())
    #购卡优惠信息
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.card.award', 'token': token},
             payload=getjson.Getgkyxxx())
    gokaward_bill=hgo_testmain.Award_bill()
    #购卡订单提交
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
            querystring={'method': 'efuture.ocm.wallet.card.sale', 'token': token},
            payload=getjson.Getgkddtj())
    gokbillno=hgo_testmain.Getbillno()
    #购卡订单查询
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.card.ordersearch', 'token': token},
             payload=getjson.Getgkddcx())
    #购卡订单完成
    hgo_testmain.HgoMain( url='/ocm-wallet-webin/rest',
             querystring={'method': 'efuture.ocm.wallet.card.orderfinish', 'token': token},
             payload=getjson.Getgkddwc())

    """异常校验-Token"""
    # 空
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': ''},
                         payload=getjson.Gkyh())
    # emoji表情
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': emoji},
                         payload=getjson.Czyh())
    # 过期
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': '33c14c36-a01d-4f66-bf8f-a0273cc2e1ce'},
                         payload=getjson.Gkyh())
    # 中文
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': chinese},
                         payload=getjson.Czyh())
    # 符号
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': notation},
                         payload=getjson.Gkyh())
    # 不带Token
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600},
                         payload=getjson.Czyh())
    # 捏造的Token
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token1},
                         payload=getjson.Gkyh())
    # SQL注入
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': Sql}, payload=getjson.Czyh())

    """异常校验-单号"""
    # 随机购卡
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Gkyh1())
    # 随机充值
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Czyh1())
    # 中文
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Cndh())
    # 英文
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Endh())
    # 小数
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Xsdh())
    # 表情
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Bqdh())
    # 重复单号
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Cfdh())
    # 空
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Kdh())
    # 不传
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Wdh())
    # 整数边界值
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Zsdh())
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Zsdh1())
    # 小数边界值
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Xsdh1())
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Xsdh2())
    # SQL注入
    hgo_testmain.HgoMain(url='/ocm-wallet-webin/rest',
                         querystring={'method': 'efuture.ocm.wallet.rebate.save', 'ent_id': 1582944742277124600,
                                      'token': token},
                         payload=getjson.Zrdh())
