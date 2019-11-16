import sys
import os
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pprint

# Parse raw file
def parse(filepath):
    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

    with open(filepath) as fp:
        cnt = 0
        is_data = False
        card_list = []
        date_cardlist = []

        for line in fp:
            if line.strip():
                if line.strip() == '{':
                    is_data = True
                elif line.strip() == '}':
                    # print date
                    card_list.sort()
                    # print card_list
                    date_cardlist.append([date,card_list])
                    is_data = False
                    card_list = []
                elif is_data:
                    card = line.split(":")[0].strip()
                    card_list.append(card)
                    # print card
                else:   # date
                    # print line 
                    year  = int(line[0:4])
                    month = int(line[5:7])
                    day = int(line[8:10])
                    # print year, month, day
                    date = datetime.date(year, month, day)
                    # print date
    # print date_cardlist
    print "Total number of changes:", len(date_cardlist)
    return date_cardlist


def sum_by_month(date_cardlist):
    # date_numcard = {}
    dates_x = []
    numbers_y = []
    for date_cards in date_cardlist:
        date = date_cards[0]
        num_cards = len(date_cards[1])
        dates_x.append(date)
        numbers_y.append(num_cards)
        # print date
        # print num_cards



    index = np.arange(len(dates_x))
    plt.bar(index, numbers_y)
    plt.xlabel('Date', fontsize=20)
    plt.ylabel('Number of Card Changes', fontsize=20)
    plt.xticks(index, dates_x, fontsize=8, rotation=30)
    plt.title('Number of Card Changes Per Balance Update')
    plt.show()


def sum_by_year(date_cardlist):
    year_x = []
    numbers_y = []
    current_year = 2016
    current_no_sum = 0
    for date_cards in date_cardlist:
        # print date_cards
        date = date_cards[0]
        y = date.year
        # print y
        num_cards = len(date_cards[1])
        if y == current_year:
            current_no_sum = current_no_sum + num_cards
        else:
            year_x.append(current_year)
            numbers_y.append(current_no_sum)
            # print year_x
            # print numbers_y
            current_year = y
            current_no_sum = 0
    year_x.append(current_year)
    numbers_y.append(current_no_sum)
    # print year_x
    # print numbers_y

    ### plot
    index = np.arange(len(year_x))
    plt.bar(index, numbers_y)
    plt.xlabel('Year', fontsize=20)
    plt.ylabel('Number of Card Changes', fontsize=20)
    plt.xticks(index, year_x, fontsize=15, ha = 'left')
    plt.title('Number of Card Changes Per Year')
    plt.show()



def sum_by_card(date_cardlist):
    card_times = {}
    for date_cards in date_cardlist:
        cards = date_cards[1]
        for card in cards:
            if card in card_times:
                times = card_times[card]
                card_times[card] = times + 1
            else:
                card_times[card] = 1

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(card_times)

    for card, number in card_times.items():
    	print card, ",", number

    # Plot
    cards_y = []
    numbers_x = []
    for card in sorted (card_times.keys()):  
        # print card
        cards_y.append(card)
        numbers_x.append(card_times[card])

    y_pos = np.arange(len(cards_y))
    plt.barh(y_pos, numbers_x)
    plt.xlabel('Number of Changes', fontsize=20)
    plt.ylabel('Cards', fontsize=20)
    plt.yticks(y_pos, cards_y, fontsize=6)
    plt.show()

def main():
  filepath="/Users/yijizhang/coding/crcardhistory/data/history.txt"
  date_cardlist = parse(filepath)   # tested
  # sum_by_month(date_cardlist)   # tested
  # sum_by_year(date_cardlist)  # tested
  sum_by_card(date_cardlist)

  
if __name__== "__main__":
  main()