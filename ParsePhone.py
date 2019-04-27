# !/usr/bin/env python
# encoding:utf-8
# author:liujian
import csv
import json

import requests

keys = ['Name', 'CardNo', 'Descriot', 'CtfTp', 'CtfId', 'Gender', 'Birthday', 'Address', 'Zip',
        'Dirty', 'District1', 'District2', 'District3', 'District4', 'District5', 'District6',
        'FirstNm', 'LastNm', 'Duty', 'Mobile', 'Tel', 'Fax', 'EMail', 'Nation', 'Taste',
        'Education', 'Company', 'CTel', 'CAddress', 'CZip', 'Family', 'Version', 'id']


def parse_mobile(phone, birth_day):
    url = "http://cx.shouji.360.cn/phonearea.php?number=%s" % phone

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2601.400'}
    r = requests.get(url=url, headers=headers)
    # f = urllib.urlopen(url)
    content = r.text
    res = json.loads(content)
    if res:
        if not res["code"] == 0:
            print "请求异常"
            return

        company = res["data"]["sp"]
        if company == "联通":
            with open(u"F:/2000W/uincom.txt", "ab+") as f:
                f.write(phone + "\n")

            if birth_day >= "19830118":
                with open(u"F:/2000W/1985_unicom.txt", "ab+") as f:
                    f.write(phone + "\n")
        elif company == "电信":
            with open(u"F:/2000W/telcom.txt", "ab+") as f:
                f.write(phone + "\n")

            if birth_day >= "19830118":
                with open(u"F:/2000W/1985_telcom.txt", "ab+") as f:
                    f.write(phone + "\n")
        elif company == "移动":
            with open(u"F:/2000W/chinaMobile.txt", "ab+") as f:
                f.write(phone + "\n")

            if birth_day >= "19830118":
                with open(u"F:/2000W/1985_chinaMobile.txt", "ab+") as f:
                    f.write(phone + "\n")


def parse_data(address):
    with open(address, "rU") as csvFile:
        reader = csv.DictReader(csvFile, fieldnames=keys)

        index = 0
        for row in reader:

            index = index + 1
            if index == 1:
                continue

            usr_mobile = row["Mobile"]

            if not len(str(usr_mobile)) == 11:
                index = index + 1
                print "无效", index
                continue

            parse_mobile(str(usr_mobile), row["Birthday"])


if __name__ == '__main__':
    parse_data(u"F:/2000W/1800w-2000w.csv")
