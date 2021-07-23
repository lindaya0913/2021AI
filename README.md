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
## D6：引數調整（Hyperparameters Tuning）
1. Ensemble Learning
- Bootstrap：Bootstrap是一種抽樣方法，藉由多次可放回採樣（resampling），就能透過觀察每個 Bootstrap 估算出母體的分配及變異。
- Bagging(袋算法)：藉由 Bootstrap 的方法使每個模型的訓練資料有差異性，使模型進行有效的投票。
    - Bagging：sklearn.ensemble.BaggingClassifier(base_estimator=None, n_estimators=10, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=False, oob_score=False, warm_start=False, n_jobs=None, random_state=None, verbose=0)
    - RandomForest：sklearn.ensemble.RandomForestClassifier(n_estimators=100, criterion='gini’, max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None, ccp_alpha=0.0, max_samples=None)
- Boosting(提升法)：Boosting 強迫每次產生新的 Weak Learner 時都要觀察其他 Learner 的輸出結果，針對分類錯誤的資料增加其權重後再次學習。Ex. AdaBoost, Gradient Boost, XGBoost, LightGBM
    - AdaBoost：sklearn.ensemble.AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R’, random_state=None)
- Stacking(堆疊法)：融合多種機器學習模型，以過濾單一模型的誤差，使模型的泛化能力更好，不使用 Bootstrap ，使用 Cross Validation，以減輕 Over-fitting 的狀況
    - Stacking：sklearn.ensemble.StackingClassifier(estimators, final_estimator=None, cv=None, stack_method='auto’n_jobs=None, passthrough=Falseverbose=0)
2. Hyperparameter Tuning
- 控制模型架構的參數即為 Hyperparameter (超參數)
    1. Grid Searching (貪婪搜尋)：理論上在無限的時間中可以找到最佳解，但時間不是無限的，可能剛好在低點白做工
        - GridSearchCV(estimator, param_grid, scoring=None, n_jobs=None,refit=True, cv=None, verbose=0, return_train_score=False)
    2. Random Searching (隨機搜尋)：有機會脫離低點達到最佳解
        - RandomizedSearchCV(estimator, param_distributions, n_iter=10, scoring=None, n_jobs=None, refit=True, cv=None, verbose=0, random_state=None, return_train_score=False)
    3. Successive halving (繼承減半)
        - Coarse-to-fine Searching：假設模型參數對精準度的影響是和緩的，先大範圍搜尋，再從較佳的區域細部搜尋
        - Multi-fidelity searching：配合 Coarse-to-fine searching 及 Random searching 使用，一開始以比較小的時間成本(ex. 資料量、n_estimators) 來搜尋，之後在良好區域內提昇時間成本，提高調參精準度
        - HalvingRandomSearchCV(estimator, param_distributions, n_candidates='exhaust', factor=3, resource='n_samples', cv=5, scoring=None, refit=True, random_state=None, n_jobs=None, verbose=0)