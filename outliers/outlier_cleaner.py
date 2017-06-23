#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    dataSize = len(predictions)
    output = []

    for i in range(dataSize):
        error = abs(predictions[i] - net_worths[i])
        output.append((ages[i], net_worths[i], error))

    output.sort(key=lambda tup: tup[2])
    cleaned_data = output[0:int(len(output)*0.9)]
    
    print "Data points without outliers", len(cleaned_data)

    return cleaned_data

