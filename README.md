# 2021 AI
## D1：Python 專題實作介紹：房價預測
- Numpy, Pandas, SciPy, Matplotlib, Scikit-learn
## D2：資料視覺化（Data Visualization）
- 使用 Matplotlib，Seaborn 繪製統計圖表
- EDA：資料處理流程、缺失值分析、連續型特徵、離散型特徵
## D3：資料清洗（Data Cleaning）
- 五項指標：
    1. Validity (每筆資料是否與 data 格式相符)
    2. Accuracy (每筆資料的正確性)
    3. Completeness (資料是否完整)
    4. Consistency (資料的關聯性是否矛盾)
    5. Uniformity (單位是否統一)
- 缺失值情形：Missing at Random, Missing Completely at Random, Missing not an Random
- 填補方法：
    1. Delete：當一筆資料或特徵有 60% 以上的缺失值，才考慮刪除法！
    2. 統計式填補：平均數、中位數、眾數
    3. 將缺失值作為新標籤加入
    4. 利用機器學習演算法填補缺失值：(Xgboost, regression等…)來預測並填補缺失值
    5. 尋找相似度：使用 KNN 演算法，找與某比含缺失值的資料最近的 K 筆資料，並使用這些資料的平均值來填補。
## D4：特徵工程（Feature Engineering）
- Feature transformation：Label encoding, One-hot encoding, Box-cox transformation, Binarization, Binning
    - Label encoding：有順序性 (Ex. 年齡)、只會佔用一個欄位、sklearn.preprocessing.LabelEncoder、Series.map
    - One-hot encoding：無順序性 (Ex. 國家、地點)、會佔用多個欄位，常會造成過多特徵、pandas.get_dummies
- Feature scaling：Standarization, Normalization
- Feature combination & construction：在一個專案中，特徵數量不宜太多，特徵太多往往會使學習難度更加困難，Feature combination 即是一個縮減特徵的方式。
- Feature Extraction：Dimension reduction (降維), Autoencoder
## D5：基本建模&評估（Basic Modeling & Evaluation）
- Over-fitting & Under-fitting
- Linear regression：sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None, positive=False)
- Tree-based Algorithm：Decision Tree, Random Forest...
    - Decision Tree：sklearn.tree.DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=None, max_features=None, random_state=None, ccp_alpha=0.0)
    - Random Forest：sklearn.ensemble.RandomForestClassifier()
- 兩種衡量好切分的方式：Imformation gain, Gini gain