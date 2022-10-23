import file

from classes.PriceElement import PriceElement
from classes.Pro100Element import Pro100Element
from classes.ReportElement import ReportElement


def PRO100_data(dir:str) -> list:
    data = file.txt_to_tuple(dir)
    result=[]
    for tuple in data:
        row = Pro100Element(tuple[0],tuple[1])
        result.append(row)
    return result

def search_in_price(price_data:list, pro100_element:Pro100Element) -> int:
    for price_element in price_data:
        if price_element.name == pro100_element.name:
            return price_element.price

price_data = (PriceElement('test',400), PriceElement('test1', 600))
pro100_data = PRO100_data('files/pro100.txt')

report = []
final_sum = 0
for pro100_string in pro100_data:
    price = search_in_price(price_data, pro100_string)
    report_string = ReportElement(pro100_string.name, 
                                  pro100_string.count,
                                  price)
    report.append(report_string)
    final_sum += report_string.sum

print(report, final_sum)
