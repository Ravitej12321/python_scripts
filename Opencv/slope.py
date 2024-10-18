def get_coeff(x,y):
    x_avg = sum(x)/x.__len__()
    y_avg = sum(y)/y.__len__()
    numerator = sum([(a - x_avg)*(b-y_avg) for a,b in zip(x,y)])
    denominator = sum([(a - x_avg)**2 for a in x])
    return round(numerator/denominator, 3)

if __name__ == '__main__':
    feature_1 = "15  12  8   8   7  7   7   6   5   3"
    feature_2 = "10  25  17  11  13  17  18  13  9   15"
    feature_1 = [int(x) for x in feature_1.split()]
    feature_2 = [int(x) for x in feature_2.split()]
    print(str(get_coeff(feature_1,feature_2)))