# Hw08
## 解題步驟：
1. 讀取 x_train.npy, y_train.npy, x_test.npy, y_test.npy
3. 先以上課的知識或 default hyperparameter 調整出一個不會 over-fitting 太多的 XGBoost 模型
4. 以該組超參數為基準，搜尋附近的參數(可以用自己偏好的搜尋策略)
5. 將最終調整結果與一開始的模型做比較，誤差是否有降低
6. 請比較 Random Forest, XGBoost(有時間的同學可以增加 GBDT, Adaboost) 的超參數搜尋時間與誤差(記得要控制 n_estimators 等會影響到時間的超參數，比較會較客觀)
   



## 檔案解說：

4. HW_08.ipynb:
   * 同學需撰寫的程式作業
5. HW_08_ans.ipynb:
   * 作業的正確答案
5. *.npy: 同學需要讀取的訓練及測試資料