import os
import pandas as pd
from tqdm import tqdm
from random import sample 

from Process_r08723067_pojuiyu import Process
from Detect_r08723067_pojuiyu import Detect
from util_pattern import pattern

pd.set_option('display.max_columns', 1000)
class Main(object):
    def __init__(self, filename_raw, filename_pro, filename_rule, pattern_path, timeScale):
        self.data_pro_df = None
        self.data_rule_df = None
        self.filename_raw = filename_raw
        self.filename_pro = filename_pro
        self.filename_rule = filename_rule
        self.pattern_path = pattern_path
        self.timeScale = timeScale
    

    def save(self, data, filename, file_format):
        # 儲存csv和pickle檔
        if file_format == 'csv':
            data.to_csv(filename, index = False)
        elif file_format == 'pickle':
            with open(filename, 'wb+') as f:
                pickle.dump(data, f)


    def load(self, filename, file_format):
        # 載入csv和pickle檔
        if file_format == 'csv':
            data = pd.read_csv(filename)
            return data
        elif file_format == 'pickle':
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            return data


    def process(self):
        # 呼叫process.py檔，做資料前處理
        Pro = Process(self.filename_raw, self.timeScale)
        Pro.preprocessing()
        Pro.timeConvert()
        self.data_pro_df = Pro.addFeature()
        self.save(self.data_pro_df, self.filename_pro, 'csv')
    

    def detect(self):
        # 呼叫Detect.py檔，做rule-base偵測
        Det = Detect(self.filename_pro)
        Det.process()
        Det.trend()
        self.data_rule_df = Det.signal()
        Det.result()
        self.save(self.data_rule_df, self.filename_rule, 'csv')
    

    def graph(self, signal, num_pattern = 1):
        # 繪出符合交易訊號的pattern
        data_df = self.load(self.filename_rule, 'csv')
        idx_signal_ls = list(data_df.loc[data_df[signal] == 1].index)
        idx_signal_sample_ls = sample(idx_signal_ls, num_pattern)
        for idx in tqdm(idx_signal_sample_ls):
            idx_start, idx_end = (idx - 9), idx
            df = data_df.loc[idx_start:idx_end]
            path = self.pattern_path + '/' + str(signal)
            pattern(df, signal, self.timeScale, path)