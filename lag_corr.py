import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

df = pd.read_excel('Main_Condenser_Tripped_Very_Low.xlsx',sheet_name='Historical Data')
column_codes = ['PR1303','TR1310','ZR1300A','ZR1300B','ZR1309','ZR1328',\
                'VE1322AA','VE1322BA','KWHG1']
data_frames_str = ['df1','df2','df3','df4','df5','df6','df7','df8','df9']

##for code, frame in zip(column_codes, data_frames):
##    for i in xrange(len(df)):
##        if df[code][i] == '#######': df[code][i] = 0

df1 = df.xs('PR1303', axis=1) #Cond. Vacuum Press
df2 = df.xs('TR1310', axis=1) #Circ. Water to Cond. Temp
df3 = df.xs('ZR1300A', axis=1) #HWP Discharge Valve Position (1)
df4 = df.xs('ZR1300B', axis=1) #HWP Discharge Valve Position (2)
df5 = df.xs('ZR1309', axis=1) #Gas Cooler Inlet Valve Position
df6 = df.xs('ZR1328', axis=1) #Cond. Inlet Valve Position
df7 = df.xs('VE1322AA', axis=1) #HWP Bearing Vibration (pump side)
df8 = df.xs('VE1322BA', axis=1) #HWP Bearing Vibration (pump side)
df9 = df.xs('KWHG1', axis=1) #Gross Power Output

data_frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9]

trip = pd.DataFrame({'1-CVP' : df1.astype('float64'),\
                     '2-CWCT': df2.astype('float64'),\
                     '3-HDVP(1)': df3.astype('float64'),\
                     '4-HDVP(2)': df4.astype('float64'),\
                     '5-GCIVP': df5.astype('float64'),\
                     '6-CIVP': df6.astype('float64'),\
                     '7-HBV1': df7.astype('float64'),\
                     '8-HBV2': df8.astype('float64'),\
                     '9-GPO':df9.astype('float64')\
                     })


##for label_df in trip:
##    first_df = trip[label_df]
##    for df_ in t##        df = trip[df_]
##        corr_lag = []
##        lag_hours = xrange(1000)
##        for lag in lag_hours:
##            corr_lag.append(first_df.corr(df.shift(lag)))
##        plt.plot(lag_hours, corr_lag, label=df_)
##    plt.legend()
##    plt.xlabel('Lag in number f hours')
##    plt.ylabel('Correlation')
##    plt.title('Correlation against '+label_df+' with lag up to 1000 hours')
##    plt.savefig(label_df+'_1000.png')
##    plt.clf()


r = trip.corr()
s = r**2
sns.heatmap(s, annot=True, fmt=".2f")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
##plt.show()
##print r

print pearsonr(df6,df7)
print pearsonr(df7,df8)



