# !/usr/bin/env python
# coding:utf-8
# author:liujian
import csv

import os


class Splitter:
    def __init__(self, in_path, out_path, keys=None):
        self.in_path = in_path
        self.out_path = out_path
        self.keys = keys

    def split(self):
        i = j = 1
        print self.in_path
        if not os.path.exists(self.out_path):
            os.makedirs(self.out_path)

        with open(self.in_path, "rU") as csv_in:
            reader = csv.DictReader(csv_in, fieldnames=self.keys)
            for row in reader:
                is_changed = False
                if i % 100001 == 0:
                    print u"CSV文件%s已生成成功" % (self.out_path + os.sep + j + "csv")
                    j = j + 1
                    is_changed = True

                out_file_path = self.out_path + "/" + str(j) + ".csv"
                # print out_file_path
                out_file = file(out_file_path, 'ab+')
                csv_write = csv.DictWriter(out_file, fieldnames=self.keys)
                # 写入数据
                csv_write.writerow(row)
                i += 1
                if is_changed:
                    out_file.close()


if __name__ == '__main__':
    keys = ['Name', 'CardNo', 'Descriot', 'CtfTp', 'CtfId', 'Gender', 'Birthday', 'Address', 'Zip',
            'Dirty', 'District1', 'District2', 'District3', 'District4', 'District5', 'District6',
            'FirstNm', 'LastNm', 'Duty', 'Mobile', 'Tel', 'Fax', 'EMail', 'Nation', 'Taste',
            'Education', 'Company', 'CTel', 'CAddress', 'CZip', 'Family', 'Version', 'id']
    sp = Splitter(u"F:/2000W/1-200W.csv", "F:/2000w/1-200W", keys)
    sp.split()
