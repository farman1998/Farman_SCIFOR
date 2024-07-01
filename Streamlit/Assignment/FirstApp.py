import streamlit as sl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sl.header(':blue[MarkMate]', divider='rainbow')
sl.header('App for marks :blue[compression] :sunglasses:')
sl.image('result comp.jpg', caption='logo for the app')
sl.button("submit", type="primary")



marks = sl.slider("marks range?", 0, 100, 50)
sl.write("my marks is", marks)
#df=pd.read_csv('marksheet.csv')
#print(df.to_string())
#df.plot()
#plt.show()