import collections
# 从序列中随机抽取一个元素
from random import choice
# namedtuple是继承自tuple的子类。
# namedtuple创建一个和tuple类似的对象，而且对象拥有可以访问的属性。
# 这对象更像带有数据属性的类，不过数据属性是只读的
# 创建card类型，带属性rank，suit
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    #print(ranks)
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')

deck = FrenchDeck()
print(len(deck))
print(beer_card)
print(deck[0],deck[-1])
print(choice(deck))
print(deck[0:3])
# 先找到索引是12的位置，然后每隔13取一张
print(deck[12::13])

for card in deck:
    print(card)

# 反向迭代

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)

# sort
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    # card.rank返回2，3...A,rank_value返回索引值0-12
    rank_value = FrenchDeck.ranks.index(card.rank)
    #print(len(suit_values))
    #len(suit_values)返回列表长度4，
    #card.suit返回spades，hearts,diamonds,clubs
    # suit_values[card.suit]返回，对应的数值，3，2，1，0
    return rank_value * len(suit_values) + suit_values[card.suit]

# sorted(a. b)函数，输入a, 以b排序
for card in sorted(deck, key=spades_high):
    print(card)
