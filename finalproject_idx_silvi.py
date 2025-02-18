# -*- coding: utf-8 -*-
"""finalproject_idx_silvi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mtbcnNq7n1dpEv5SiQy24swXOfqfwpfZ

# RAKAMIN ID/X DATA SCIENTIST

# PREPARATION
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""# preproces Dataset"""

df = pd.read_csv("/content/drive/MyDrive/loan_data_2007_2014.csv", dtype={'desc' : str})

from google.colab import drive
drive.mount('/content/drive')

"""jumlah baris dan kolom dari dataset"""

print("Dataset shape:", df.shape)

"""mengatur jumlah maksimum kolom yang ditampilkan"""

pd.set_option("display.max_columns", 500)

"""mencari/menampilkan data duplikat"""

df.duplicated().sum()

print(df.head())

df.info()

"""mencari tahu jumlah missing value pada setiap kolom"""

df.isnull().sum()

plt.figure(figsize=(10,6))
sns.heatmap(df.isna().transpose(),
            cmap="YlGnBu",
            cbar_kws={'label': 'Miss data'})

df.corr()

df.drop(columns=['Unnamed: 0', 'annual_inc_joint', 'dti_joint', 'verification_status_joint',
       'open_acc_6m', 'open_il_6m', 'open_il_12m', 'open_il_24m',
       'mths_since_rcnt_il', 'total_bal_il', 'il_util', 'open_rv_12m',
       'open_rv_24m', 'max_bal_bc', 'all_util', 'inq_fi', 'total_cu_tl',
       'inq_last_12m'], axis=1)

df.loan_status.value_counts()

"""# Label"""

unsure = ['Current', 'In Grace Period']
good_loan =  ['Fully Paid', 'Does not meet the credit policy. Status:Fully Paid']

df = df[df.loan_status.isin(unsure) == False]

df['loan_type'] = np.where(df['loan_status'].isin(good_loan), 'good', 'bad')

leakages = ['issue_d', 'loan_status', 'pymnt_plan', 'out_prncp', 'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv',
                   'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee',
                   'last_pymnt_d', 'last_pymnt_amnt', 'next_pymnt_d']

df.drop(columns=leakages, axis=1, inplace=True)

df.drop(columns=['funded_amnt', 'funded_amnt_inv', 'id', 'member_id', 'url', 'desc'], axis=1, inplace=True)

df.loan_type.value_counts()

plt.title('Loan Type')
sns.barplot(x=df.loan_type.value_counts().index,y=df.loan_type.value_counts().values)

"""data baik dan buruk peminjam,sangat jauh jaraknya membuat data menjadi imbalance

mengubah nilai tipe data kategorikal (string atau objek) menjadi tipe data numerik
"""

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df["loan_type"] = label_encoder.fit_transform(df["loan_type"])
df["loan_type"]

df.loan_type.value_counts()

df.corr()

df.dtypes

df.isnull().sum()

"""menghapus data yang tidak meiliki kontribusi"""

df.drop(columns=['annual_inc_joint', 'dti_joint', 'verification_status_joint', 'open_acc_6m', 'open_il_6m', 'open_il_12m', 'open_il_24m', 'mths_since_rcnt_il', 'total_bal_il', 'il_util', 'open_rv_12m', 'open_rv_24m', 'max_bal_bc', 'all_util', 'inq_fi',  'total_cu_tl', 'inq_last_12m'], axis=1, inplace=True)

df.isnull().sum()

df.emp_title.value_counts()

df.earliest_cr_line.value_counts()

plt.boxplot(df['loan_amnt'], vert=False)
plt.title("Boxplot jumlah pinjaman")
plt.xlabel('jumlah pinjaman')

df.last_credit_pull_d.value_counts()

plt.boxplot(df['int_rate'], vert=False)
plt.title("Int rate Boxplot")
plt.xlabel('Int rate')

df.emp_length.value_counts()

"""mengubah value emp length menjadi numerik"""

df.emp_length = df.emp_length.astype('str')

df.emp_length.dtypes

df.dtypes

""" menghilangkan semua karakter kecuali angka dari kolom emp length"""

import re
df.emp_length = [re.sub('[^0-9]', '', x) for x in df.emp_length]

df.emp_length.value_counts()

df.emp_length = pd.to_numeric(df.emp_length)

"""menangani missing value dalam data dengan menggantikannya dengan nilai yang lebih representatif, dalam hal ini menggunakan rata-rata dari masing-masing kolom"""

df.emp_length.replace(np.nan, df.emp_length.astype("float").mean(axis=0), inplace=True)
df.annual_inc.replace(np.nan, df.annual_inc.astype("float").mean(axis=0), inplace=True)
df.delinq_2yrs.replace(np.nan, df.delinq_2yrs.astype("float").mean(axis=0), inplace=True)
df.inq_last_6mths.replace(np.nan, df.inq_last_6mths.astype("float").mean(axis=0), inplace=True)
df.mths_since_last_delinq.replace(np.nan, df.mths_since_last_delinq.astype("float").mean(axis=0), inplace=True)
df.mths_since_last_record.replace(np.nan, df.mths_since_last_record.astype("float").mean(axis=0), inplace=True)
df.open_acc.replace(np.nan, df.open_acc.astype("float").mean(axis=0), inplace=True)
df.pub_rec.replace(np.nan, df.pub_rec.astype("float").mean(axis=0), inplace=True)
df.revol_util.replace(np.nan, df.revol_util.astype("float").mean(axis=0), inplace=True)
df.total_acc.replace(np.nan, df.total_acc.astype("float").mean(axis=0), inplace=True)
df.collections_12_mths_ex_med.replace(np.nan, df.collections_12_mths_ex_med.astype("float").mean(axis=0), inplace=True)
df.mths_since_last_major_derog.replace(np.nan, df.mths_since_last_major_derog.astype("float").mean(axis=0), inplace=True)
df.acc_now_delinq.replace(np.nan, df.acc_now_delinq.astype("float").mean(axis=0), inplace=True)
df.tot_coll_amt.replace(np.nan, df.tot_coll_amt.astype("float").mean(axis=0), inplace=True)
df.tot_cur_bal.replace(np.nan, df.tot_cur_bal.astype("float").mean(axis=0), inplace=True)
df.total_rev_hi_lim.replace(np.nan, df.total_rev_hi_lim.astype("float").mean(axis=0), inplace=True)

"""handling missing data dengan menggantikannya dengan nilai yang paling sering muncul, sehingga mempertahankan karakteristik distribusi data yang ada."""

df.emp_title.replace(np.nan, df.emp_title.value_counts().idxmax(), inplace=True)
df.title.replace(np.nan, df.title.value_counts().idxmax(), inplace=True)
df.earliest_cr_line.replace(np.nan, df.earliest_cr_line.value_counts().idxmax(), inplace=True)
df.last_credit_pull_d.replace(np.nan, df.last_credit_pull_d.value_counts().idxmax(), inplace=True)

df.isnull().sum()

df.purpose.value_counts()

df.addr_state.value_counts()

df.dtypes

df.grade.value_counts()

plt.figure(figsize=(9,9))
plt.pie(x=df['grade'].value_counts(), startangle=90, autopct='%1.0f%%')
plt.legend(title="grade presentase", loc="upper right", labels=["B", "C", "D", "A", "E", "F", "G"])
plt.show()

"""membuat DataFrame baru, df_plot_grade, dengan menghitung jumlah peminjam berdasarkan kombinasi grade dan loan_type dari DataFrame asli df.Ini memanfaatkan operasi grup dan pivot pada pandas untuk mengorganisir data"""

df_plot_grade = df.groupby(['grade', 'loan_type']).size().reset_index().pivot(columns='grade', index='loan_type', values=0)

df_plot_grade.plot(title="Grade to Loan Type", kind='bar', stacked=True)

""" menggunakan LabelEncoder dari library scikit-learn untuk mengkodekan variabel kategori dalam DataFrame menjadi nilai numerik"""

df.term = label_encoder.fit_transform(df.term)
df.grade = label_encoder.fit_transform(df.grade)
df.emp_title = label_encoder.fit_transform(df.emp_title)
df.home_ownership = label_encoder.fit_transform(df.home_ownership)
df.sub_grade = label_encoder.fit_transform(df.sub_grade)
df.verification_status = label_encoder.fit_transform(df.verification_status)
df.purpose = label_encoder.fit_transform(df.purpose)
df.zip_code = label_encoder.fit_transform(df.zip_code)
df.addr_state = label_encoder.fit_transform(df.addr_state)
df.earliest_cr_line = label_encoder.fit_transform(df.earliest_cr_line)
df.initial_list_status = label_encoder.fit_transform(df.initial_list_status)
df.last_credit_pull_d = label_encoder.fit_transform(df.last_credit_pull_d)
df.application_type = label_encoder.fit_transform(df.initial_list_status)
df.title = label_encoder.fit_transform(df.title)

""" membuat plot distribusi kernel (KDE) dari kolom loan_amnt dalam DataFrame. Ini memberikan gambaran visual tentang sebaran nilai loan_amnt"""

sns.displot(data=df, x="loan_amnt", kind="kde", bw_adjust=2)

"""memberikan gambaran visual tentang sebaran probabilitas pendapatan tahunan peminjam, dengan parameter"""

sns.displot(data=df, x="annual_inc", kind="kde", bw_adjust=2)

df.dtypes

df.corr().loan_type

"""menghapus data yang tidak memiliki korelasi dengan loan_type"""

uncorrelated = ['loan_amnt', 'installment', 'emp_title', 'emp_length', 'home_ownership', 'annual_inc',
                'verification_status', 'purpose', 'title', 'zip_code', 'addr_state', 'delinq_2yrs',
                'earliest_cr_line', 'inq_last_6mths', 'mths_since_last_delinq', 'mths_since_last_record',
                'open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'initial_list_status',
                'last_credit_pull_d', 'collections_12_mths_ex_med', 'mths_since_last_major_derog', 'policy_code',
                'application_type', 'acc_now_delinq', 'tot_coll_amt', 'tot_cur_bal', 'total_rev_hi_lim']
df.drop(columns=uncorrelated, axis=1, inplace=True)

df.corr().loan_type

plt.boxplot(df['term'], vert=False)
plt.title("Term Boxplot")
plt.xlabel('term')

plt.boxplot(df['int_rate'], vert=False)
plt.title("Int rate Boxplot")
plt.xlabel('Int rate')

plt.boxplot(df['grade'], vert=False)
plt.title("Grade Boxplot")
plt.xlabel('grade')

plt.boxplot(df['sub_grade'], vert=False)
plt.title("Sub Grade Boxplot")
plt.xlabel('sub_grade')

plt.boxplot(df['dti'], vert=False)
plt.title("Dti Boxplot")
plt.xlabel('dti')

sns.pairplot(data=df)

from scipy import stats

"""menghapus outlier dari DataFrame"""

df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

"""memberikan nilai 1 dan 0 pada loan type

*   1 = GOOD
*   0 = BAD


"""

df_class_0 = df[df.loan_type == 0]
df_class_1 = df[df.loan_type == 1]

count_class_1, count_class_0 = df.loan_type.value_counts()

count_class_1, count_class_0

"""menangani imbalance kelas dalam dataset loan_type"""

df_balance_1 = pd.concat([df_class_1[0:count_class_0], df_class_0], axis = 0)

df_balance_1.info()

print(df_balance_1.head())

"""# MODEL&TRAIN

# LOGISTIC REGRESION
"""

from sklearn.model_selection import RandomizedSearchCV

X = df_balance_1.drop("loan_type", axis = "columns")
y = df_balance_1["loan_type"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

"""melakukan tuning parameter pada model Logistic Regression menggunakan pendekatan Randomized Search Cross Validation untuk mencari kombinasi parameter yang memberikan kinerja terbaik"""

lgc = LogisticRegression(n_jobs = -1)
param_grid =  {'C': [0.1,0.6,0.8],
              'fit_intercept': [True,False],
              'solver': ['lbfgs','liblinear', 'sag', 'saga']}

clf_lg = RandomizedSearchCV(lgc, param_distributions = param_grid, n_iter = 20, cv = 3, verbose = 2)
tuned_lg = clf_lg.fit(x_train, y_train)

"""Evaluasi"""

print("Accuracy:", accuracy_score(y_test, y_pred1))
y_pred1 = tuned_lg.predict(x_test)
print(classification_report(y_test, y_pred1))

"""# ROC"""

from sklearn.metrics import roc_curve, auc

"""Training"""

y_score = tuned_lg.predict_proba(x_test)[:, 1]

fpr, tpr, _ = roc_curve(y_test, y_score)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('(ROC) Curve')
plt.legend(loc='lower right')
plt.show()

"""TESTING"""

y_score_test = tuned_lg.predict_proba(x_test)[:, 1]

fpr_test, tpr_test, _ = roc_curve(y_test, y_score_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Menghitung skor probabilitas prediksi untuk kelas positif pada data uji
y_score_test = tuned_lg.predict_proba(x_test)[:, 1]

# Menghitung kurva ROC untuk data uji
fpr_test, tpr_test, _ = roc_curve(y_test, y_score_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Plot kurva ROC untuk data uji
plt.figure()
plt.plot(fpr_test, tpr_test, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc_test))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Testing')
plt.legend(loc='lower right')
plt.show()

"""Confusion Matrix"""

cm = confusion_matrix(y_test, y_pred1)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=tuned_lg.classes_)
disp.plot()

"""hasil prediksi"""

y_pred1[9]

y_pred1[6]

"""Hasil dari model pertama adalah akurasi 80%

# DECISION TREE
"""

X = df_balance_1.drop("loan_type", axis = "columns")
y = df_balance_1["loan_type"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

"""Model Decision Tree"""

dtc = DecisionTreeClassifier(criterion='entropy', random_state=42)

"""Training model"""

dtc.fit(x_train, y_train)

y_pred = dtc.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""Confusion Matrix"""

cm1 = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,6))
sns.heatmap(cm1, annot=True, fmt=".0f", linewidths=.5, square=True, cmap='Blues')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Confusion matrix')
plt.show()

"""hasil prediksi"""

y_pred[6]

y_pred1[10]

y_pred1[9]

"""Hasil dari model kedua adalah akurasi 83%

# EDA

STATUS LOAN
"""

plt.figure(figsize=(10,5))
sns.countplot(y= "loan_status", data = df)
plt.show()

value_counts = df["loan_status"].value_counts()
percentage = value_counts / value_counts.sum()
percentage = percentage.apply("{:.2%}".format)
print(percentage)

"""membagi yang berhasil dan gagal lalu di kategorikan 1 dan 0"""

succes = ["Fully Paid"]
fail = ["Charged Off",
        "Default",
        "Does not meet the credit policy. Status:Charged off",
        "Does not meet the credit policy. Status:Fully Paid"]

def loan(status):
    if status in fail:
        return 0
    return 1

"""1 berhasil membayar,0 gagal membayar"""

df = df[df["loan_status"].isin(succes + fail)].copy()
df["loan_status"] = df["loan_status"].apply(loan)

plt.figure(figsize=(10,5))
sns.countplot(y= "loan_status", data = df)
plt.show()

value_counts = df["loan_status"].value_counts()
percentage = value_counts / value_counts.sum()
percentage = percentage.apply("{:.2%}".format)
print(percentage)

"""jumlah pinjaman"""

x = "loan_status"
y = "loan_amnt"

plt.figure(figsize=(10,10))
sns.boxplot(data = df, x=x , y=y)
plt.title("jumlah pinjaman")
plt.ylabel("")
plt.show()

df.groupby(x)[y].describe()

"""jumlah pinjaman terbanyak adalah oleh client yang telah membayar tetapi untuk rata ratanya masih tinggi di client yang belum membayar

tujuan peminjaman
"""

plt.figure(figsize=(10,10))
sns.countplot(y= "purpose",order=value_counts.index, data = df)
plt.show()

value_counts = df["purpose"].value_counts()
percentage = value_counts / value_counts.sum()
percentage = percentage.apply("{:.2%}".format)
print(percentage)

"""paling banyak client meminjam uang untuk menutup hutang sebelumnya

negara peminjam
"""

plt.figure(figsize=(10,10))
sns.countplot(y= "addr_state",order=value_counts.index, data = df)
plt.show()

value_counts = df["addr_state"].value_counts()
percentage = value_counts / value_counts.sum()
percentage = percentage.apply("{:.2%}".format)
print(percentage)

"""peminjam terbanyak dari california

pemilikan rumah
"""

plt.figure(figsize=(10,10))
sns.countplot(y= "home_ownership", data = df)
plt.show()

value_counts = df["home_ownership"].value_counts()
percentage = value_counts / value_counts.sum()
percentage = percentage.apply("{:.2%}".format)
print(percentage)

"""sebagian besar peminjam adalah client yang tidak mempunyai rumah dan masih memiliki tagihan untuk membayar rumahnya

# KESIMPULAN

*   Dataset: Setelah melakukan proses preprocessing pada dataset, diperoleh dataset dengan jumlah 466285 baris dan 75 kolom. Seluruh kolom dalam dataset telah diobservasi dan diolah dengan mengeliminasi kolom-kolom yang tidak relevan, mengisi nilai missing value, dan mengubah tipe data dari kolom-kolom yang diperlukan.
*   Data Imbalance: Seluruh dataset memiliki jumlah kelas yang tidak seimbang, yaitu jumlah 'good' lebih banyak dibandingkan kelas 'bad' dari pengelompokan kolom loan_status.Untuk mengatasi masalah data imbalance dalam pengolahan data credit risk, saya menggunakan metode undersampling. Metode ini menggabungkan data kelas 'bad' sebanyak kelas 'good'. Hal ini dapat dikategorikan sebagai proses undersampling, karena jumlah data kelas 'bad' ditekan ke bawah sehingga menjadi sejumlah yang sama dengan kelas 'good'.
*   Logistic Regression: Setelah melakukan tuning parameter pada model Logistic Regression, didapatkan kombinasi parameter yang memberikan kinerja terbaik dengan akurasi sebesar 80%. Kurva ROC dan Confusion Matrix dapat digunakan sebagai indikator untuk menilai kinerja model.
*   Decision Tree: Selain Logistic Regression, kita juga menggunakan model Decision Tree dengan metrik entropy dan menemukan bahwa model ini memiliki akurasi sebesar 83%.
*   EDA: Seluruh proses EDA menunjukkan bahwa dataset memiliki beberapa insight menarik, seperti jumlah pinjaman yang lebih tinggi pada client yang belum membayar, tujuan peminjaman yang paling tinggi adalah untuk menutup hutang sebelumnya, dan peminjam terbanyak berasal dari California. Selain itu, sebagian besar peminjam tidak memiliki rumah dan masih memiliki tagihan untuk membayar rumahnya.
"""