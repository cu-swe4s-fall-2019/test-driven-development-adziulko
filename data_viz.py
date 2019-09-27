import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math_lib




def boxplot(L, out_file_name):

    out_file = out_file_name
    X = []
    Y = []

    for l in sys.stdin:
        A = l.rstrip().split()
        X.append(float(A[0]))
        Y.append(float(A[1]))

    width=3
    height=3
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    title = ('mean = ' + mean + 'stdev = ' + stdev)

    fig = plt.figure(figsize=(width,height),dpi=300)
    ax = fig.add_subplot(1,1,1)
    ax.boxplot(L)
    plt.savefig(out_file,bbox_inches='tight')


def histogram(L, out_file_name):

    out_file = out_file_name
    D = []

    for l in sys.stdin:
        A = l.rstrip().split()
        D.append(float(A[0]))
        D.append(float(A[1]))

    width=3
    height=3
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    output = ('mean = ' + mean + 'stdev = ' + stdev)

    fig = plt.figure(figsize=(width,height),dpi=300)
    ax = fig.add_subplot(1,1,1)
    ax.hist(D)
    plt.savefig(out_file,bbox_inches='tight')


def combo(L, out_file_name):

    out_file = out_file_name
    X = []
    Y = []
    D = []

    for l in sys.stdin:
        A = l.rstrip().split()
        X.append(float(A[0]))
        Y.append(float(A[1]))
        D.append(float(A[0]))
        D.append(float(A[1]))

    width=5
    height=3
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    output = ('mean = ' + mean + 'stdev = ' + stdev)

    fig = plt.figure(figsize=(width,height),dpi=300)
    ax = fig.add_subplot(1,2,1)
    ax.boxplot(L)
    ax = fig.add_subplot(1,2,2)
    ax.hist(D)
    plt.savefig(out_file,bbox_inches='tight')
