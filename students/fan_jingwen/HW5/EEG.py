import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as itp

# load data into dataframe
df = pd.read_csv('EEG data.csv', header=None)
# rename the dataframe with the proper column names
df.columns = ['Sub_ID', 'Vid_ID', 'attention', 'meditation', 'raw', 'delta', 'theta', 'alpha1', 'alpha2',
              'beta1', 'beta2', 'gamma1', 'gamma2', 'pre_label', 'usr_label']
# correctly format the dataframe into floats
df[['Sub_ID', 'Vid_ID']] = df[['Sub_ID', 'Vid_ID']].apply(pd.to_numeric)


def plot_subject(df, sub_ID, freq, thresh):
    '''
    This function plots the EEG potential averaged over all video trials for each subject. It prints out the peak
    and trough potential values. This function can be used to detect artifacts.
    :param df: the accepted dataframe
    :param sub_ID: The subject's ID, ranging from 1~10
    :param freq: The form of data, drawing from ['raw', 'delta', 'theta', 'alpha1', 'alpha2',
             'beta1', 'beta2', 'gamma1', 'gamma2']
    :return: None
    '''
    # filtered dataframe for the specific subject
    df_ID = df[df['Sub_ID'] == sub_ID - 1]
    # get video its as a set
    vid_ID_set = {int(x) for x in set(df_ID['Vid_ID'])}
    # get the sizes of recorded EEG data for each video trial
    sizes = np.zeros(len(vid_ID_set))
    #     print (f'vid_ID_set:{vid_ID_set}')
    for ID in vid_ID_set:
        sizes[ID] = np.size(df_ID[df_ID.Vid_ID == ID].Sub_ID)
    sizes.astype(int)
    #     print (f'sizes:{np.max(sizes)}')

    # create a dataset for all EEG data and all video trials
    data_mat = np.zeros((int(np.max(sizes)), len(vid_ID_set)))
    # populate the dataset with the designated EEG data
    for ID in vid_ID_set:
        data_mat[:int(sizes[ID]), ID] = df_ID.loc[df_ID.Vid_ID == ID, freq]

    to_plot_mean = np.mean(data_mat, axis=1)
    errors = np.std(data_mat, axis=1)

    peak = np.max(to_plot_mean)
    trough = np.min(to_plot_mean)

    print(
        f'The peak mean voltage of {freq} data for subject {sub_ID} is {peak}mV, and the trough voltage is {trough}mV.')

    # check if there is need for eliminating artifact.
    if np.max(to_plot_mean) > thresh:
        print(
            f'The maximum of averaged potential is {np.max(to_plot_mean)}mV, which is greater than the threshold {thresh}mV. Check for artifacts.')
    else:
        print(f'The maximum of averaged potential is {np.max(to_plot_mean)}mV, within the threshold {thresh}.')

    # fit smooth lines for mean and upper and lower bounds of the mean EEG data
    xvec = np.arange(len(to_plot_mean)) * 0.5
    f = itp.interp1d(xvec, to_plot_mean)
    f_plus = itp.interp1d(xvec, to_plot_mean + errors)
    f_minus = itp.interp1d(xvec, to_plot_mean - errors)
    inter = f(xvec)
    inter_plus = f_plus(xvec)
    inter_minus = f_minus(xvec)

    # plotting
    plt.plot(xvec, inter, 'r-')
    plt.plot(xvec, inter_plus, 'g--')
    plt.plot(xvec, inter_minus, 'g--')
    plt.fill_between(xvec, inter_plus, inter_minus, facecolor="gray", alpha=0.15)
    #     plt.plot(x_vec, y_vec)
    plt.title(f'EEG for subject {sub_ID}: {freq} data', fontsize=20)
    plt.grid(b=True, which='major', color='0.65', linestyle='-')
    plt.xlabel(r'$t$ (s)')
    plt.ylabel('Voltage (mV)')
    plt.show()


plot_subject(df, 1, 'raw', 500)
plot_subject(df, 1, 'alpha1', 500)
plot_subject(df, 1, 'theta', 500)