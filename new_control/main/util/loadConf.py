# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : loadConf.py
# @Soft    : tomato_farm
import configparser
import os
import re
import sys

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class config:
    def __init__(self, key=')_9-+klo@c4t$k$w'):
        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.dirs = self.path + "/config/"
        self.fileName = "config.ini"

    def remove_BOM(self, config_path):
        content = open(config_path).read()
        content = re.sub(r"\xfe\xff", "", content)
        content = re.sub(r"\xff\xfe", "", content)
        content = re.sub(r"\xef\xbb\xbf", "", content)
        open(config_path, 'w').write(content)

    # 读取配置文件
    def readConfig(self):
        config = configparser.ConfigParser()
        if not os.path.exists(self.dirs):
            os.makedirs(self.dirs)
        if not os.path.exists(self.dirs + self.fileName):
            f = open(self.dirs + self.fileName, 'w')
            f.close()
        try:
            config_path = self.dirs + self.fileName
            self.remove_BOM(config_path)
            config.read(config_path, encoding="utf-8")
        except Exception as e:
            pass
        else:
            return config

    # 写入配置文件
    def writeConfig(self, config):
        try:
            config.write(open(self.dirs + self.fileName, "w", encoding='utf-8'))
        except Exception as e:
            pass

    # 新增section
    def addSection(self, section):
        config = self.readConfig()
        if not config.has_section(section):  # 检查是否存在section
            config.add_section(section)
        self.writeConfig(config)

    # 新增option
    def addoption(self, section, option, word):
        config = self.readConfig()
        config.set(section, option, word)
        self.writeConfig(config)

    # 删除配置文件
    def delSection(self, section):
        config = self.readConfig()
        if config.has_section(section):
            config.remove_section(section)  # 整个section下的所有内容都将删除
        self.writeConfig(config)

    # 获得配置
    def getOption(self, section, option):
        config = self.readConfig()
        if config.has_section(section):
            word = config.get(section, option)
        else:
            word = ''
        return word

    # 获得配置
    def getSection(self):
        config = self.readConfig()
        word = config.sections()
        return word

    # 字符串切割成数组
    def splitword(self, word):
        if word != '':
            list = word.split(',')
        else:
            list = []
        return list

    # 数组转成字符串
    def split(self, list):
        if len(list) > 0:
            word = ','.join(list)
        else:
            word = ''
        return word

    # aes加密
    def encrypt(self, text):
        try:
            cryptor = AES.new(self.key, self.mode, self.key)
            length = 16
            count = len(text)
            add = 0
            if count < length:
                add = (length - count)
            elif count > length:
                add = (length - (count % length))
            text_new = (text + ('\0' * add)).encode('utf-8')
            self.ciphertext = cryptor.encrypt(text_new)
            return bytes.decode(b2a_hex(self.ciphertext), encoding='utf8')
        except Exception as e:
            return ''

    # aes解密
    def decrypt(self, text):
        try:
            cryptor = AES.new(self.key, self.mode, self.key)
            plain_text = bytes.decode(cryptor.decrypt(a2b_hex(bytes(text, encoding='utf8'))), encoding='utf8')
            return plain_text.rstrip('\0')
        except Exception as e:
            return ''


if __name__ == '__main__':
    con = config()
    con.readConfig()
    print(con.encrypt("False"))
