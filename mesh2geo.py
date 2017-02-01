#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

def conversion(code):
    """
    メッシュコードを緯度経度に変換
    :param code: メッシュコード
    """
    code = str(code)
    
    c1 = float(code[0:2])
    c2 = float(code[2:4])
    c3 = float(code[4:5])
    c4 = float(code[5:6])
    c5 = float(code[6:7])
    c6 = float(code[7:8])
    
    lat = (((c1 / 1.5) * 3600) + ((c3 * 5) * 60) + (c5 * 30)) / 3600
    lng = (((c2 + 100) * 3600) + ((c4 * 7.5) * 60) + (c6 * 45)) / 3600
    
    return lat, lng


def write_csv(geos, file_name):
    """
    csv形式で出力
    :param geos: 南端緯度および西端経度のリスト
    :param file_name: ファイル名
    """
    with open(file_name + '.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(geos)


def m2g(code, num, file_name):
    """
    メッシュを分割し，南端緯度および西端経度のリストをリターン
    :param code: メッシュコード
    :param num: 分割数
    :param file_name: ファイル名
    """
    
    len_lat = 30 / 3600.0 / num
    len_lng = 45 / 3600.0 / num
    
    geos = []
    
    lat, lng = conversion(code)
        
    for y in range(num):
        for x in range(num):
            geo = []
            geo.append(lat + len_lat * y)
            geo.append(lng + len_lng * x)
            geos.append(geo)
                
    write_csv(geos, file_name)


if __name__ == '__main__':
    argv = sys.argv

    if len(argv) != 4:
        print("Usage: python " + argv[0] + " query number")
        sys.exit()

    m2g(argv[1], int(argv[2]), argv[3])
