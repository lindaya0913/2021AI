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
- Linear regression：`sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None, positive=False)`
- Tree-based Algorithm：Decision Tree, Random Forest...
    - Decision Tree：`sklearn.tree.DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=None, max_features=None, random_state=None, ccp_alpha=0.0)`
    - Random Forest：`sklearn.ensemble.RandomForestClassifier()`
- 兩種衡量好切分的方式：Imformation gain, Gini gain
## D6：引數調整（Hyperparameters Tuning）
1. Ensemble Learning
- Bootstrap：Bootstrap是一種抽樣方法，藉由多次可放回採樣（resampling），就能透過觀察每個 Bootstrap 估算出母體的分配及變異。
- Bagging(袋算法)：藉由 Bootstrap 的方法使每個模型的訓練資料有差異性，使模型進行有效的投票。
    - Bagging：`sklearn.ensemble.BaggingClassifier(base_estimator=None, n_estimators=10, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=False, oob_score=False, warm_start=False, n_jobs=None, random_state=None, verbose=0)`
    - RandomForest：`sklearn.ensemble.RandomForestClassifier(n_estimators=100, criterion='gini’, max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None, ccp_alpha=0.0, max_samples=None)`
- Boosting(提升法)：Boosting 強迫每次產生新的 Weak Learner 時都要觀察其他 Learner 的輸出結果，針對分類錯誤的資料增加其權重後再次學習。Ex. AdaBoost, Gradient Boost, XGBoost, LightGBM
    - AdaBoost：`sklearn.ensemble.AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R’, random_state=None)`
- Stacking(堆疊法)：融合多種機器學習模型，以過濾單一模型的誤差，使模型的泛化能力更好，不使用 Bootstrap ，使用 Cross Validation，以減輕 Over-fitting 的狀況
    - Stacking：`sklearn.ensemble.StackingClassifier(estimators, final_estimator=None, cv=None, stack_method='auto’n_jobs=None, passthrough=Falseverbose=0)`
2. Hyperparameter Tuning
- 控制模型架構的參數即為 Hyperparameter (超參數)
    1. Grid Searching (貪婪搜尋)：理論上在無限的時間中可以找到最佳解，但時間不是無限的，可能剛好在低點白做工
        - `GridSearchCV(estimator, param_grid, scoring=None, n_jobs=None,refit=True, cv=None, verbose=0, return_train_score=False)`
    2. Random Searching (隨機搜尋)：有機會脫離低點達到最佳解
        - `RandomizedSearchCV(estimator, param_distributions, n_iter=10, scoring=None, n_jobs=None, refit=True, cv=None, verbose=0, random_state=None, return_train_score=False)`
    3. Successive halving (繼承減半)
        - Coarse-to-fine Searching：假設模型參數對精準度的影響是和緩的，先大範圍搜尋，再從較佳的區域細部搜尋
        - Multi-fidelity searching：配合 Coarse-to-fine searching 及 Random searching 使用，一開始以比較小的時間成本(ex. 資料量、n_estimators) 來搜尋，之後在良好區域內提昇時間成本，提高調參精準度
        - `HalvingRandomSearchCV(estimator, param_distributions, n_candidates='exhaust', factor=3, resource='n_samples', cv=5, scoring=None, refit=True, random_state=None, n_jobs=None, verbose=0)`
## D7：整合方法（Ensemble Methods）
- Feature Selection：最主要的目的是減少特徵數量，使模型訓練及預測的效能更好。某些情況下甚至能提升測試的準確度或降低測試誤差，通常會配合"刪除法"及 "Feature Extraction" 一起使用
    1. Feature Selection：選擇特徵的子集合
    - Unsupervised：在選擇特徵的演算法中，並沒有使用預測目標
    - Supervised：在選擇特徵的演算法中，有使用預測目標
        - Wrapper：設立多個特徵組合，從中尋找最佳解(RFE，RFECV)
        - Filter：透過分析特徵與預測目標間的關係，來篩選特徵(Statistical Methods、Feature Importance Methods – Permutation Importance)
        - Intrinsic：演算法內有內建選擇特徵的方法(Linear regression、Decision Trees)
    2. Dimensionality Reduction：Project input data into a lower-dimensional feature space
- 我們可以將特徵分為 continual (連續型) 及 discrete (離散型)；而預測目標分為兩種：regression (回歸) 及 classification (分類)
    1. Filter method
    - ANOVA for regression：`f_regression()`
    - ANOVA for classification：`f_classif()`
    - Chi-Squared：`chi2()`
    - Mutual Information：`mutual_info_classif()` and `mutual_info_regression()`
    - SelectKBest：`sklearn.feature_selection.SelectKBest(score_func=<function f_classif>, k=10)`
    - Permutation Importance：`sklearn.inspection.permutation_importance(estimator, X, y, scoring=None, n_repeats=5, n_jobs=None, random_state=None, sample_weight=None)`
    2. Intrinsic：某些機器學習演算法再進行訓練時，本身就會帶有特徵重要性的性質在其中，如 tree-based algorithm, Linear regression 即為 Feature Importance Intrinsic Model
    - Mean Decrease Impurity
    3. Wrapper method
    - RFE(Recursive Feature Elimination)：每回合透過特徵重要性將一定數量的特徵刪除，直到剩下 k 個特徵。
    - RFE：`sklearn.feature_selection.RFE(estimator, n_features_to_select=None, step=1, verbose=0, importance_getter='auto’)`
    - RFECV(RFE Cross Validation)：每回合透過特徵重要性將一定數量的特徵刪除，且以交叉驗證的方式分析特徵對 score 的影響，直到剩下 k 個特徵。
    - RFECV：`sklearn.feature_selection.RFECV(estimator, step=1, min_features_to_select = 1, cv=None, scoring=None, verbose=0, n_jobs=None, importance_getter='auto’)`
## D8：XGBoost
- 樹型演算法 – 架構
    - Random Forest = Bagging + Decision tree
    - Boosting Tree = AdaBoost + Decision tree，使 adaboost 可以解決回歸問題
    - GBDT  = Gradient Boost + Decision tree，提升運行速度及準確度
    - XGBoost is an upgrade of GBDT
- XGBoost vs GBDT vs Decision Tree
    - 基礎的決策樹使用 information gain, gini factor 來選擇最佳分割點
    - 而 GBDT 透過決策樹本身的演算法來擬合殘差
    - 與前兩者相比，XGBoost 定義了自己的函數：gain function 來決定最佳分割點
- 平行運算：無法平行建樹，因為 boosting 家族的演算法都是 sequential structure，然而，XGBoost 為了更快速的計算，將資料集分成好幾個 block，將計算過的 gain 等中間計算結果暫存在記憶體，使演算法在尋找最佳分割點或 sub-sampling 的時候可以快速存取運算結果；並將尋找最佳分割點這項工作平行化再次加速運行速度，使其訓練速度逼近 Random Forest 的結果
- XGBoost：XGBoost 本身是獨立模組，但透過 xgboost.sklearn 可以讓使用者以相近 sklearn 的風格使用 XGBoost 演算法。
    - `from xgboost.sklearn import XGBClassifier`
    - `Model = XGBClassifier(eta, gamma, max_depth, min_child_weight, min_child_weight, subsample, lambda,alpha, colsample_by*,importance_type,  objective, scale_pos_weight)`
## D10：爬蟲實戰教學 (一)
- 爬蟲的意義：自動、即時性、需要更多未被整理過的資料 
## D11：爬蟲實戰教學 (二)