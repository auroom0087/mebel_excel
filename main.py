price_data = ({'name':'test', 'price':150},{'name':'test1', 'price':400})
pro100_data = ({'name':'test', 'count':4}, {'name':'test1', 'count':3})

result = []
final_sum = 0
for pro100_string in pro100_data:
    for price_string in price_data:
        if pro100_string.get('name') is price_string.get('name'):
            result_string =  {'name':pro100_string.get('name'),
                            'count':pro100_string.get('count'),
                            'price':price_string.get('price'),
                            'sum':pro100_string.get('count')*price_string.get('price')}
            result.append(result_string)
            final_sum += result_string.get('sum')

print(result, final_sum)
