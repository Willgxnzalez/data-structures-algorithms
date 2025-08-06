from math import sqrt

#color codes
BLUE = "\033[35m"
RESET = "\033[0m"

data1 = [5,9,2,8,1] # independant variable
data2 = [12,17,7,22,12] # dependant variable X:[9,4,9,4,14]
data1_label = "Z"
data2_label = "Y"

def mean(data, label):
    m = sum(data) / len(data)
    print(f"{BLUE}{label}-mean: {m}{RESET}")
    return m

def getSumSqrs(data, mean, label):
    squared_diffs = []
    diffs = []
    print(f"({label}-{label}mean) |  ({label}-{label}mean)^2")
    for value in data:
        diff = value - mean
        squared_diff = diff ** 2
        squared_diffs.append(squared_diff)
        diffs.append(diff)
        print(f"  {diff:>7.4f} | {squared_diff:>7.4f}")
    sum_squares = sum(squared_diffs)
    print(f"{BLUE}Sum of Squares for {label}: {sum_squares}\n{RESET}")
    return sum_squares, diffs

def getStdDev(SS, n, label):
    std_dev = sqrt(SS / n)
    print(f"{BLUE}Standard Deviation {label} (SD{label}): {std_dev}\n{RESET}")
    return std_dev

def getStandardizedValue(val, mean, SDv, label):
    std_val = (val - mean) / SDv
    print(f"{BLUE}Standardized {label} for value {val}: {std_val}\n{RESET}")
    return std_val
    
def covariance(Xdiffs, Ydiffs, label1, label2):
    cov = 0
    for x, y in zip(Xdiffs, Ydiffs):
        product = x * y
        print(f"{product:>10.4f}")
        cov += product
    print(f"{BLUE}Covariance {label1}-{label2}: {cov}\n{RESET}")
    return cov

def getRegEqn(mean1, mean2, cov, SS1, label1, label2):
    slope = cov/SS1
    y_intercept = mean2 - (slope * mean1)
    print(f"{BLUE}Regression Line: {label2} = {slope:.4f}{label1} + {y_intercept:.4f}\n{RESET}")
    return slope, y_intercept

def predict(data, slope, y_int, label):
    out = []
    print(f"Predicted {label} values: ")
    for x in data:
        predicted = (slope*x) + y_int
        print(f"{predicted:>10.4f}")
        out.append(predicted)
    print()
    return out

def predict2x(data1, data2, slope1, slope2, y_int):
    out = []
    print("Predicted Y values: ")
    for x1, x2 in zip(data1, data2):
        yhat = (slope1*x1) + (slope2*x2) + y_int
        print(f"{yhat:>10.4f}")
        out.append(yhat)
    print()
    return out
    
def getSumSqrErr(data2, data2_hat, label):
    squared_diffs = []
    diffs = []
    print(f"({label}-{label}hat) |  ({label}-{label}hat)^2")
    for data, predicted in zip(data2, data2_hat):
        diff = data - predicted
        squared_diff = diff ** 2
        squared_diffs.append(squared_diff)
        diffs.append(diff)
        print(f" {diff:>7.4f} | {squared_diff:>7.4f}")
    sum_sqr_err = sum(squared_diffs)
    print(f"{BLUE}Sum of Squared Error: {sum_sqr_err}\n{RESET}")
    return sum_sqr_err

def getSumSqrReg(data2_hat, data2_mean, label):
    squared_diffs = []
    diffs = []
    print(f"{label}hat-{label}mean | ({label}hat-{label}mean)^2")
    for predicted in data2_hat:
        diff = predicted - data2_mean
        squared_diff = diff ** 2
        squared_diffs.append(squared_diff)
        diffs.append(diff)
        print(f"  {diff:>7.4f} | {squared_diff:>7.4f}")
    print()
    sum_sqr_reg = sum(squared_diffs)
    print(f"{BLUE}Sum of Squares Regression: {sum_sqr_reg}\n{RESET}")
    return sum_sqr_reg

def pearsons_r(cov, SS1, SS2):
    r = cov / sqrt(SS1 * SS2)
    print(f"{BLUE}Pearson's r (Correlation coefficient): {r}")
    print(f"Coefficient of Determination (r^2): {r ** 2}\n{RESET}")
    return r

def getStdErrEst(SSe, n):
    std_err_est = sqrt(SSe / (n - 2))
    print(f"{BLUE}Standard Error Estimate / Residual Standard Error: {std_err_est}\n{RESET}")
    return std_err_est

def getStdDevEst(SS, n):
    std_dev_est = sqrt(SS / (n - 1))
    print(f"{BLUE}Estimated Standard Deviation: {std_dev_est}\n{RESET}")
    return std_dev_est
    

def getObtF(SSr, SSe, n, k):
    MSr = SSr / k
    MSe = SSe / (n - k - 1)
    print(f"MSr: {MSr} | MSe: {MSe}")
    obt_f = MSr / MSe
    print(f"{BLUE}Obtained F ratio: {obt_f}\n{RESET}")
    return obt_f


mean1 = mean(data1, data1_label)
mean2 = mean(data2, data2_label)

SS1, diffs1 = getSumSqrs(data1, mean1, data1_label)

SS2, diffs2 = getSumSqrs(data2, mean2, data2_label)

SD1 = getStdDev(SS1, len(data1), data1_label)
SD2 = getStdDev(SS2, len(data2), data2_label)

IDinput1 = 13
IDinput2 = 20

Std1 = getStandardizedValue(IDinput1, mean1, SD1, data1_label)
Std2 = getStandardizedValue(IDinput2, mean2, SD2, data2_label)

getStandardizedValue(232, 250, 12, "X")

cov12 = covariance(diffs1, diffs2, data1_label, data2_label)

slope, Yint = getRegEqn(mean1, mean2, cov12, SS1, data1_label, data2_label)


predictions = predict(data1, slope, Yint, data2_label)

    
"""
xdata1 = [8, 7, 9, 7, 12]
xdata2 = [7, 5, 7 ,10, 11]
slope1 = 0.2589
slope2 = 0.2455
y_int = 2.0089
Yhat = predict2x(xdata1, xdata2, slope1, slope2, y_int)
"""


SSe = getSumSqrErr(data2, predictions, data2_label)
SSr = getSumSqrReg(predictions, mean2, data2_label)

r = pearsons_r(cov12, SS1, SS2)

StdErrEst = getStdErrEst(SSe, len(data1)) 
StdDevEst = getStdDevEst(SS2, len(data1))

SSt = SSr + SSe
print(f"Sum of Squares Total: {SSt}\n")

obtF = getObtF(SSr, SSe, len(data1), 1)

