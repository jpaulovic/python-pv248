# Objekty

Na přednášce jsme si ukázali, jak v Pythonu vypadají objekty a třídy. 

Připravil jsem objekt `Runner` (viz [speedy_turtle.py][speedy_turtle]),
který reprezentuje želvu, která utíká náhodně po ploše. Objekt 
má atributy `x` a `y`.

## Úkol
             
Zkuste napsat vlastní objekt `Runner`, který bude pronásledovat 
utíkající objekt. 

V každém kroku se `Runner` podívá, kde je jeho cíl, nasměruje se 
směrem k němu a posune se. 


```python

from speedy_turtle import Runner

runner = Runner()

class Follower:
    def __init__(self, target, color='blue', speed=6):
        """:param target:    želva, kterou pronásledujeme
        """
        
        self.me = turtle.Turtle(color=color)        
        # ... sem patří další inicializace objektu

    def step(self):
        "posune mne směrem k utíkajícímu objektu"
        
        self.me.left(xxx)
        self.me.forward(self.speed)

```

Hlavní program pak bude vypadat nějak takhle:

```python

def run_demo():
    speedy = Runner()
    follower = Follower(target=speedy)
    for i in range(1000):
        speedy.step()
        follower.step()
    turtle.exitonclick()

```

## Potřebné moduly

* [math]

[speedy_turtle]: https://github.com/VerosK/python-pv248/blob/master/03-moving-turtle/speedy_turtle.py
[math]: https://docs.python.org/3/library/math.html