# !/usr/bin/env python
# encoding:utf-8
# author:liujian
import csv

import MySQLdb

keys = ['Name', 'CardNo', 'Descriot', 'CtfTp', 'CtfId', 'Gender', 'Birthday', 'Address', 'Zip',
        'Dirty', 'District1', 'District2', 'District3', 'District4', 'District5', 'District6',
        'FirstNm', 'LastNm', 'Duty', 'Mobile', 'Tel', 'Fax', 'EMail', 'Nation', 'Taste',
        'Education', 'Company', 'CTel', 'CAddress', 'CZip', 'Family', 'Version', 'id']
total_count = 0


def parse_data(address):
    db = MySQLdb.Connect("localhost", "root", "123456", "HomeInData", charset='utf8')
    cursor = db.cursor()
    with open(address, "rU") as csvFile:
        reader = csv.DictReader(csvFile, fieldnames=keys)

        index = 0
        print reader
        for row in reader:


            index = index + 1
            if index == 1:
                continue

            usr_ctf_id = row["CtfId"]
            usr_name = row["Name"]
            usr_gender = row["Gender"]
            usr_birth_day = row["Birthday"]
            usr_address = row["Address"]
            usr_duty = row["Duty"]
            usr_mobile = row["Mobile"]
            usr_tel = row["Tel"]
            usr_fax = row["Fax"]
            usr_email = row["EMail"]
            usr_nation = row["Nation"]
            usr_education = row["Education"]
            usr_company = row["Company"]
            usr_cTel = row["CTel"]
            usr_cAddress = row["CAddress"]
            usr_cZip = row["CZip"]
            global total_count
            # print usr_ctf_id,usr_name,usr_gender,usr_birth_day,usr_address,usr_duty,usr_mobile,usr_tel,usr_fax,usr_email,usr_nation,usr_education,usr_company,usr_cTel,usr_cAddress,usr_cZip
            if not (
                                        usr_mobile and usr_tel and usr_email and usr_gender and usr_name and usr_ctf_id):

                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue

            if len(usr_ctf_id) > 50:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_name) > 40:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_gender) > 5:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_birth_day) > 12:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_address) > 120:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_duty) > 20:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_mobile) > 20:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_tel) > 50:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_fax) > 50:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_email) > 50:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_nation) > 40:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_education) > 40:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_company) > 50:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_cTel) > 50:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_cAddress) > 50:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue
            if len(usr_cZip) > 40:
                total_count = total_count + 1
                print "无效数据个数：", total_count
                continue

            query_sql = "select total from homein_tab_last WHERE ctf_id = %s"
            result = cursor.execute(query=query_sql, args=usr_ctf_id)

            if result == 0:
                insert_sql = "INSERT INTO homein_tab_last(ctf_id, name, gender, birth_day, address,duty,mobile,tel,fax,email,nation,education, company, cTel, cAddress, cZip,total) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s)"
                cursor.execute(insert_sql, (
                    usr_ctf_id, usr_name, usr_gender, usr_birth_day, usr_address,
                    usr_duty, usr_mobile, usr_tel,
                    usr_fax, usr_email,
                    usr_nation, usr_education, usr_company, usr_cTel, usr_cAddress,
                    usr_cZip, 0))
                print "insert"
            else:
                update_sql = "UPDATE homein_tab_last set total = total + 1 WHERE ctf_id = %s"
                cursor.execute(update_sql, args=usr_ctf_id)
                print "update"
            db.commit()

        cursor.close()


if __name__ == '__main__':
    parse_data(u"F:/2000W/最后5000.csv")
