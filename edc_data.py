import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Main_Condenser_Tripped_Very_Low.xlsx',sheet_name='Historical Data')
column_codes = ['PR1303','TR1310','ZR1300A','ZR1300B','ZR1309','ZR1328',\
                'VE1322AA','VE1322BA','KWHG1']
data_frames = ['df1','df2','df3','df4','df5','df6','df7','df8','df9']

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

trip = pd.DataFrame({'1-CVP' : df1.astype('float64'),\
                     '2-CWCT': df2.astype('float64'),\
                     '3-HDVP(1)': df3.astype('float64'),\
                     '4-HDVP(2)': df4.astype('float64'),\
                     '5-GCIVP': df5.astype('float64'),\
                     '6-CIVP': df6.astype('float64'),\
                     '7-HBV1': df7.astype('float64'),\
                     '8-HBV2': df8.astype('float64'),\
                     'GPO':df9.astype('float64')\
                     })

##trip = pd.DataFrame({'Cond. Vacuum Press' : df1.astype('float64'),\
##                     'Circ. Water to Cond. Temp': df2.astype('float64'),\
##                     'HWP Discharge Valve Position (1)': df3.astype('float64'),\
##                     'HWP Discharge Valve Position (2)': df4.astype('float64'),\
##                     'Gas Cooler Inlet Valve Position': df5.astype('float64'),\
##                     'Cond. Inlet Valve Position': df6.astype('float64'),\
##                     'HWP Bearing Vibration (pump side) 1': df7.astype('float64'),\
##                     'HWP Bearing Vibration (pump side) 2': df8.astype('float64'),\
##                     'Gross Power Output':df9.astype('float64')\
##                     })


##plt.plot(df3,'r',label='Pos 1')
##plt.plot(df4,'b',label='Pos 2')
##plt.title('HWP Discharge Valve Position (1,2)')
###plt.savefig('3_4.png')
##print 'HWP Discharge Valve Position (1,2): ', df3.astype('float64').corr(df4.astype('float64'))
##
##plt.clf()
##
##plt.plot(df7,'g',label='Pos 1')
##plt.plot(df8,'y',label='Pos 2')
##plt.title('HWP Bearing Vibration (pump side)')
###plt.savefig('7_8.png')
##print 'HWP Bearing Vibration (pump side): ', df7.astype('float64').corr(df8.astype('float64'))
##
##plt.clf()

##trip.plot(subplots=True)
##plt.savefig('subplots.png')
##
##plt.clf()




##f, ax = plt.subplots(figsize=(10, 8))
####corr = trip.corr()
####sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
####            square=True, ax=ax)
##cov = trip.cov()
##sns.heatmap(cov, mask=np.zeros_like(cov, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
##            square=True, ax=ax)
##plt.xticks(fontsize=6,rotation=45)
##plt.yticks(fontsize=6,rotation=45)
##print cov


##sns.pairplot(trip, kind="reg", size=3, vars=['1-CVP', '2-CWCT', '3-HDVP(1)','4-HDVP(2)'])
##
##plt.savefig('corr1-reg-1.png')
##plt.clf()

sns.pairplot(trip, kind="reg", size=3, vars=['1-CVP','5-GCIVP', '6-CIVP', '7-HBV1','8-HBV2','GPO'])
plt.savefig('cvp_inverse.png')
