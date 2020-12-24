HW1

main_r08723067_pojui.py line 8 更改為from util_pattern import pattern
Detect_r08723067_pojui.py 新增 BigReverseV 及 BigCrash型態 並把部分原先型態先以註記方式不偵測
BigReverse為一個深V谷底反彈的型態，這在今年疫情使股市波動度加據下，小那、原油、黃金常常有此型態
BigCrash為一個大崩的反彈型態，這在今年疫情使股市波動度加據下，小那、原油、黃金常常有此型態


HW2
訓練MNIST的LSTM根CNN辨識模型準確度皆大於97%
LSTM改動:多加一層Dense，訓練參數epoch變2，batch_size縮小
CNN改動：訓練參數batch_size縮小

HW3
訓練LSTM與CNN模型辨識
LSTM多加一層Dense，batch_size縮小、hidden layer改一下成160，準確度提升至85趴
CNN模型batch_size縮小，準確度提升至85趴
