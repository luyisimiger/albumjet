
def toBoolean(value):
    
    result = None
    
    result = True if value in ['true', 'True', 'y', 'yes', '1'] else result
    result = False if value in ['false', 'False', 'n', 'no', '0'] else result
    
    return result
