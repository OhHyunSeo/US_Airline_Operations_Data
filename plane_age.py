#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:00:44 2025

@author: oh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.rcParams['font.family'] = 'AppleGothic'

# 데이터 읽기 (1987 ~ 1999)
df_1987 = pd.read_csv('./dataverse_files_1987-1999/1987.csv')
df_1988 = pd.read_csv('./dataverse_files_1987-1999/1988.csv')
df_1989 = pd.read_csv('./dataverse_files_1987-1999/1989.csv')
df_1990 = pd.read_csv('./dataverse_files_1987-1999/1990.csv')
df_1991 = pd.read_csv('./dataverse_files_1987-1999/1991.csv')
df_1992 = pd.read_csv('./dataverse_files_1987-1999/1992.csv')
df_1993 = pd.read_csv('./dataverse_files_1987-1999/1993.csv')
df_1994 = pd.read_csv('./dataverse_files_1987-1999/1994.csv')
df_1995 = pd.read_csv('./dataverse_files_1987-1999/1995.csv')
df_1996 = pd.read_csv('./dataverse_files_1987-1999/1996.csv')
df_1997 = pd.read_csv('./dataverse_files_1987-1999/1997.csv')
df_1998 = pd.read_csv('./dataverse_files_1987-1999/1998.csv')
df_1999 = pd.read_csv('./dataverse_files_1987-1999/1999.csv')

# 데이터 읽기 (2000  ~ 2008)
df_2000 = pd.read_csv('./dataverse_files_2000-2008/2000.csv')
df_2001 = pd.read_csv('./dataverse_files_2000-2008/2001.csv', encoding= 'latin1')
df_2002 = pd.read_csv('./dataverse_files_2000-2008/2002.csv', encoding= 'latin1')
df_2003 = pd.read_csv('./dataverse_files_2000-2008/2003.csv')
df_2004 = pd.read_csv('./dataverse_files_2000-2008/2004.csv')
df_2005 = pd.read_csv('./dataverse_files_2000-2008/2005.csv')
df_2006 = pd.read_csv('./dataverse_files_2000-2008/2006.csv')
df_2007 = pd.read_csv('./dataverse_files_2000-2008/2007.csv')
df_2008 = pd.read_csv('./dataverse_files_2000-2008/2008.csv')

plt.rcParams['font.family'] = 'AppleGothic'
