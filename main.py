from classes.PriceElement import PriceElement
from classes.Pro100Element import Pro100Element
from classes.ReportElement import ReportElement

price_data = (PriceElement('test',400), PriceElement('test1', 600))
pro100_data = (Pro100Element('test', 3),Pro100Element('test1', 6))

result = []
final_sum = 0
for pro100_string in pro100_data:
    for price_string in price_data:
        if pro100_string.name is price_string.name:
            result_string = ReportElement(pro100_string.name, pro100_string.count, price_string.price)
            result.append(result_string)
            final_sum += result_string.sum
            print(result_string)

print(result, final_sum)
