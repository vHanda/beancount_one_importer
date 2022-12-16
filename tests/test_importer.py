from beancount_one_importer import *


def test_1():
    input_str = "44715.0,44715.0,BIZUM ENVIADO,,-30.0,2097.06"
    output_str = """
2022-06-03 * "BIZUM ENVIADO"
    Assets:Personal:Spain:LaCaixa  -30.0 EUR
"""
    assert build_importer(input_str, output_str) != None


def test_2():

    input_str = """
404-7319078-6347502,3 Scale Home Brew Hydrometer Wine Beer Cider Alcohol Testing Making Tester; ,Vishesh Handa,2019-06-24,"EUR 2,34",N/A,N/A,N/A,N/A,
"""
    input_str = input_str.replace("N/A", "")
    output_str = """
2019-06-24 * "3 Scale Home Brew Hydrometer Wine Beer Cider Alcohol Testing Making Tester;"
  orderId: "404-7319078-6347502"
  Expenses:Personal:Amazon  2.34 EUR
"""
    assert build_importer(input_str, output_str) != None


def test_3():
    input_str = """
01-Feb-2011,31-Jan-2011, ,Credit Interest Capitalised,"","787.00","5,898.20"
"""
    output_str = """
2011-02-01 * "Credit Interest Capitalised"
  Assets:Personal:India:CanaraBank  787.0 INR
"""
    assert build_importer(input_str, output_str) != None


def test_4():
    input_str = """
Dividend (Ordinary),2022-04-06 07:39:19,IE00B3XXRP09,VUSA,"Vanguard S&P 500 ETF",10.0000000000,0.20,GBP,Not available,2.36,-0.00,GBP,,,,
"""
    output_str = """
2022-04-06 * "Dividend (Ordinary)" "Vanguard S&P 500 ETF"
  isin: "IE00B3XXRP09"
  Assets:N26  2.36 EUR
"""
    assert build_importer(input_str, output_str) != None