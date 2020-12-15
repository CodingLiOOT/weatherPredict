#coding=utf-8
import json, os, re


def csv_to_json(place):
    data1 = '{'
    data2 = '"weather": ['
    data3 = ']'
    data4 = '}'
    data5 = ','
    data6 = '    "token":"1"'
    data7 = '    "Id":"' + place + '"'
    data8 = '"data":['

    source_file = 'prediction/predict_data-' + place + '.csv'
    json_file_result = 'prediction/' + place + '.json'
    zd_key = ["Date", "tmax", "tmin", "mobile", "status", "thirdUserId", "a", "b", "c", "e", "d"]
    # 判断文件是否存在，并清空文件内容
    if os.path.exists(json_file_result):
        with   open(json_file_result, "r+") as f:
            f.truncate()

    with open(json_file_result, 'a+', encoding='utf-8') as c:
        c.write(data1 + '\n')
        c.write(data8 + '\n')
        # Token部分
        c.write(data1 )
        c.write(data6 )
        c.write(data4 )
        c.write(data5 + '\n')
        # Id部分
        c.write(data1 )
        c.write(data7 )
        c.write(data4 )
        c.write(data5 + '\n')
        # weather部分
        c.write(data1 )
        c.write(data2 )

    if os.path.isfile(source_file):
        with open(source_file, 'r', encoding='gbk') as f:
            lines = f.readlines()
            for i in lines:
                l = i.strip("\n").split(",")
                zd = dict(zip(zd_key, l))
                data_json = json.dumps(zd, ensure_ascii=False, sort_keys=False)

                # 将JSON格式的数据存储到txt文件中，便于使用
                with open(json_file_result, 'a+', encoding='utf-8') as f:
                    if (i==lines[-1]):
                        f.write(data_json)

                    else:
                        f.write(data_json)
                        f.write(data5)
                        f.close()



        print("写入完成", "\n""文件路径是：%s" % (os.path.abspath(json_file_result)))
    else:
        print("文件不存在")


    with open(json_file_result, 'a+', encoding='utf-8') as d:
        d.write(data3)
        d.write(data4 + '\n')
        d.write(data3)
        d.write(data4+ '\n')

if __name__ == '__main__':
    PLACE = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']

    for place in PLACE:
        csv_to_json(place)