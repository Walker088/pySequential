#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from logger.logger import cmd_logger as log
from shutil import copyfile
import os

src = '{}/source'.format(os.getcwd())
dest = '{}/destination'.format(os.getcwd())

class sequentailMaker():
    def __init__(self):
        self.sequential = 1

    def makeSequentailNumbers(self):
        log.info('making numbers.....')
        for root, _, files in os.walk(src, topdown=False):
            for srtFile in files:
                srtfile = os.path.join(root, srtFile)
                outputFile = '{}_with_index.srt'.format(os.path.join(dest, srtFile))
                log.info('Target srt file: %s' % srtfile)
                with open(srtfile, 'r', encoding='utf-8') as sf:
                    sfLst = [row for row in sf.readlines() if row != '\n']
                with open(outputFile, 'w+') as csf:
                    for id in range(len(sfLst)):
                        if id%2 == 0 :
                            csf.write('{}\n'.format(self.sequential))
                            self.sequential += 1
                            csf.write('{}'.format(sfLst[id]))
                        else:
                            csf.write('{}\n'.format(sfLst[id]))
                copyfile(outputFile, outputFile.replace('.srt', '.txt'))
                self.sequential = 1

if __name__ == '__main__':
    log.info('Welcom to srt sequential number maker ヽ(́◕◞౪◟◕‵)ﾉ')
    sm = sequentailMaker()
    sm.makeSequentailNumbers()