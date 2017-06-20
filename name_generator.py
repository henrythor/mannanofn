# -*- coding: utf-8 -*-
import random
import requests
from lxml import html


class NameGenerator(object):
    def __init__(self):
        self.kk_page = requests.get('https://is.wikipedia.org/wiki/Listi_yfir_íslensk_eiginnöfn_karlmanna')
        self.kvk_page = requests.get('https://is.wikipedia.org/wiki/Listi_yfir_%C3%ADslensk_eiginn%C3%B6fn_kvenmanna')

        self.kk_tree = html.fromstring(self.kk_page.content)
        self.kvk_tree = html.fromstring(self.kvk_page.content)

        self.kk_nofn = self.kk_tree.xpath('//div[@id="mw-content-text"]/div/ul/li/a/text()')[0:-2]
        self.kvk_nofn = self.kvk_tree.xpath('//div[@id="mw-content-text"]/div/ul/li/a/text()')[0:-2]

        self.nofn = []
        self.nofn.append(self.kk_nofn)
        self.nofn.append(self.kvk_nofn)

        self.KYN_KK = 0
        self.KYN_KVK = 1

    def get_fodurnafn(self, kyn):
        fodurnafn_url = 'https://is.wikipedia.org'
        fodurnafn_fj = len(self.nofn[0])
        fodurnafn_i = random.randint(0, fodurnafn_fj - 1)
        nafn = self.nofn[0][fodurnafn_i]
        url_search = '//div[@id="mw-content-text"]/ul/li/a[@title="{}"]/@href'.format(nafn)
        fodurnafn = self.kk_tree.xpath(url_search)
        if len(fodurnafn) > 0:
            fodurnafn_url += fodurnafn[0]
            fodurnafn_page = requests.get(fodurnafn_url)
            fodurnafn_tree = html.fromstring(fodurnafn_page.content)
            trs = fodurnafn_tree.xpath('//table/tr')
            for tr in trs:
                tds = tr.getchildren()
                if tds[0].text_content() == 'Eignarfall':
                    ef_nafn = tds[1].text_content().split(' ')
                    output = ef_nafn[0]
                    if kyn == self.KYN_KVK:
                        output += 'dóttir'
                    elif kyn == self.KYN_KK:
                        output += 'son'
                    return output
        return self.get_fodurnafn(kyn)

    def get_name(self):
        output = ''
        kyn = random.randint(0, 1)
        nafn_fj = len(self.nofn[kyn])
        nafn = random.randint(0, nafn_fj - 1)
        output += self.nofn[kyn][nafn]
        # Athuga hvort við ætlum að hafa miðnafn
        if random.randint(0, 2) in [0, 1]:
            output += ' '
            midnafn = random.randint(0, nafn_fj - 1)
            output += self.nofn[kyn][midnafn]
        output += ' '
        output += self.get_fodurnafn(kyn)
        return output
