def get_headers(data):
    t1 = data[3]
    t2 = "{} {}".format(data[6], data[12])
    t3 = "{}{}{} {}".format(data[0], data[2], data[7], data[12])
    t4 = "{} {} {}".format(data[3], data[8], data[12])
    t5 = "{}{} {} {}".format(data[1].split('/')[0]+'/', data[4], data[9], data[12])
    t6 = "{}{}{}{}".format(data[1].split('/')[0]+'/', data[5], data[10], data[12])

    headers = [t1, t2, t3, t4, t5, t6]
    return headers

def make_chunks(l, n):
    '''
    Helper function to create vectors (sets) from list
    '''
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def get_csv_fields(data, headers):
    return list(make_chunks(data, len(headers)))