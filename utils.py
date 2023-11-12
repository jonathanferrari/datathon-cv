import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import cv2

def average_dataframe(df, n):
    return df.groupby(df.index // n).mean()

def process(data):
    df = data[["time[s]", "horizontal_motion[deg]", "vertical_motion[deg]"]]
    df.columns = ["time", "x", "y"]
    df = average_dataframe(df, 16)
    return df