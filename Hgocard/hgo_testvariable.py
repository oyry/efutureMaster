# @Time    : 19-3-1
# @Author  : 欧阳
# @File    : hgo_testvariable.py
import random,datetime,string

"""单据编号-合法"""
def Billmoduleid():
    billmoduleid=random.randint(6666666,8888888)
    return billmoduleid
"""单据编号-英文"""
#等价类
def English():
    i=7
    english=''.join(random.sample(string.ascii_letters, i))
    return english
#边界值
def English_BJZ():
    i=6
    english=''.join(random.sample(string.ascii_letters, i))
    return english
def English_bjz():
    i=8
    english=''.join(random.sample(string.ascii_letters, i))
    return english

"""单据编号-符号"""
#等价类
def Notation():
    i=7
    notation=''.join(random.sample(string.punctuation, i))
    return notation
#边界值
def Notation_bjz():
    i=6
    notation=''.join(random.sample(string.punctuation, i))
    return notation
def Notation_BJZ():
    i=8
    notation=''.join(random.sample(string.punctuation, i))
    return notation

"""单据编号-整数"""
#边界值
def Number_BJZ():
    i=6
    number=''.join(random.sample(string.digits,i))
    return number
def Number_bjz():
    i=8
    number=''.join(random.choice("0123456789") for i in range(i))
    return number

"""单据编号-小数"""
#等价类
def Fractional():
    i=4
    fractional=round(random.uniform(10, 20),i)
    return fractional
#边界值
def Fractional_bjz():
    i=3
    fractional=round(random.uniform(10, 20),i)
    return fractional
def Fractional_BJZ():
    i=5
    fractional=round(random.uniform(10, 20),i)
    return fractional

"""单据编号-中文"""
#等价类
def Chinese():
    chinese=chr(random.randint(0x4e00,0x9fa5))
    return chinese

"""单据编号-表情"""
#等价类
def Emoji():
    EMOJI = ['☺', '☎', '♻', '☀', '☁', '❄', '☠', '✈', '✉', '✏', '✒', '✂', '♠', '♥', '♦', '♣', '♨', '✡', '✝', '☑', '✔',
             '✖', '✳', '✴', '❇', '©', '®', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓']
    emoji = random.choice(EMOJI)
    return emoji

"""SQL注入"""
#SQL注入代码汇总
def Sqlinfused():
    sqlcode = ["1=1 and 1=2", "admin' --", "admin' #", "admin'/*", "' or 1=1--", "' or 1=1#", "' or 1=1/*",
               "') or '1'='1--", "') or ('1'='1--", "'", "N/ A", "' OR '1' = '1", "') OR ('1' = '1",
               "value' OR '1' = '2", "value') OR ('1' = '2", "' AND '1' = '2", "') AND ('1' = '2", "' OR 'ab' = 'a''b",
               "') OR ('ab' = 'a''b", "'", "value + 1", "value - 1", "value + 0", "value - 0", "OR 1 = 1",
               ") OR (1 = 1", "value OR 1 = 2", "value) OR (1 = 2", "AND 1 = 2", ") AND (1 = 2", "' OR 'ab' = 'a''b",
               "value';--", "value');--", "value';update Users set Password=111111 where User='root';--",
               "value');update Users set Password=111111 where User='root';--", "value;--",
               "value);--", "value';#", "value');#", "value;#", "value);#", "' OR '1' = '1';--", "') OR '1' = '1';--",
               "OR 1 = 1;--", ") OR 1 = 1;--", "' AND '1' = '2';--", "') AND '1' = '2';--", "AND 1 = 2;--",
               ") AND 1 = 2;--", "value';", "value');", "value;", "value);"]
    infused=random.choice(sqlcode)
    return ("%s"% infused)

"""开始日期"""
def Sdate():
    i = datetime.datetime.now()
    sdate= ("%s-%s-%s" % (i.year,i.month,i.day))
    return sdate

"""结束日期"""
def Edate():
    i = (datetime.datetime.now()+datetime.timedelta(days=15))
    edate=("%s-%s-%s" % (i.year,i.month,i.day))
    return edate

"""制单时间"""
def Inputdate():
    inputdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return inputdate

"""手机号"""
# 合法
def Hfmobile():
    q3w = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
           "153", "155", "156", "157", "158", "159", "166", "185", "186", "187", "188", "198", "199"]
    randomq3w = random.choice(q3w)
    h8w = "".join(random.choice("0123456789") for i in range(8))
    mobile = randomq3w + h8w
    return mobile

# 非法-位数
def Ffmobile():
    q3w = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
           "153", "155", "156", "157", "158", "159", "166", "185", "186", "187", "188", "198", "199"]
    randomq3w = random.choice(q3w)
    h8w = "".join(random.choice("0123456789") for i in range(7))
    mobile = randomq3w + h8w
    return mobile
def Ffmobile1():
    q3w = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
           "153", "155", "156", "157", "158", "159", "166", "185", "186", "187", "188", "198", "199"]
    randomq3w = random.choice(q3w)
    h8w = "".join(random.choice("0123456789") for i in range(9))
    mobile = randomq3w + h8w
    return mobile
#调试
# test=Sqlinfused()
# print(test)