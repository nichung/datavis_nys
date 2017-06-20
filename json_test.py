import itertools

"""
todo: hit the right sub dict 
"""
lst = sorted(itertools.chain(nyc_json__data,ny_json__data), key=lambda x:x['features'][1:]['properties']['pumace10'])
test_join = []
for k,v in itertools.groupby(lst, key=lambda x:x['geoid10']):
    d = {}
    for dct in v:
        d.update(dct)
    test_join.append(d)
