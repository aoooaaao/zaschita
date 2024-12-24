import random
class Voin(object):
    def __init__(self, a, b, c):
        self._unit = a #здоровье
        self._mana = b #выносливость
        self._armor = c #броня

    def hp(self):
        return self._unit
    
    def mana(self):
        return self._mana
    
    def armor(self):
        return self._armor
    
    def attack(self):
        if self._mana > 0:
            self._mana = self._mana - 10
            if self._mana < 0:
                self._mana = 0
    
    def defence(self, x):
        if self._armor > 0:
            self._armor = self._armor - x
            if self._armor < 0:
                self._armor = 0
    
    def damage(self, x):
        if self._unit > 10:
            self._unit = self._unit - x
            if self._unit < 0:
                self._unit = 0
                
    def situation(self,obj):
        print('Первый юнит:')
        print('Здоровье:', self.hp())
        print('Броня:', self.armor())
        print('Выносливость:', self.mana())
        print('Второй юнит:')
        print('Здоровье:', obj.hp())
        print('Броня:', obj.armor())
        print('Выносливость:', obj.mana())
    
    def fight(self,obj):
        print('Бой начался!')
        while self.hp() > 10 and obj.hp() > 10:
            a = random.randint(0,1) 
            b = random.randint(0,1)
            if a == 1 and b == 1:
                print('Оба юнита атакуют.')
                self.attack()
                if self.mana() > 0:
                    if obj.armor() > 0:
                        e = random.randint(0,20)
                    else:
                        e = random.randint(10,30)
                else:
                    e = random.randint(0,10)
                obj.damage(e)
                d = random.randint(0,10)
                obj.defence(d)
                obj.attack()
                if obj.mana() > 0:
                    if self.armor() > 0:
                        e = random.randint(0,20)
                    else:
                        e = random.randint(10,30)
                else:
                    e = random.randint(0,10)
                self.damage(e)
                d = random.randint(0,10)
                self.defence(d)
                self.situation(obj)
            if a == 1 and b == 0:
                print('Первый юнит атакует. Второй юнит защищается')
                self.attack()
                if self.mana() > 0:
                    if obj.armor() > 0:
                        e = random.randint(0,20)
                    else:
                        e = random.randint(10,30)
                else:
                    e = random.randint(0,10)
                obj.damage(e)
                d = random.randint(0,10)
                obj.defence(d)
                self.situation(obj)
            if a == 0 and b == 1:
                print('Первый юнит защищается. Второй юнит атакует')
                obj.attack()
                if obj.mana() > 0:
                    if self.armor() > 0:
                        e = random.randint(0,20)
                    else:
                        e = random.randint(10,30)
                else:
                    e = random.randint(0,10)
                self.damage(e)
                d = random.randint(0,10)
                self.defence(d)
                self.situation(obj)
        if obj.hp() <= 10:
            print('Победил первый юнит. Убить второго юнита? 0 - нет, 1 - да')
            while True:
                z = input()
                if z == 1:
                    print('Здоровье второго юнита: 0')
                    break
                if z == 0:
                    print('Второй юнит выжил')
                    break
        else:
            print('Победил второй юнит. Убить первого юнита? 0 - нет, 1 - да')
            while True:
                z = input()
                if z == 1:
                    print('Здоровье первого юнита: 0')
                    break
                if z == 0:
                    print('Первый юнит выжил')
                    break
class TestVoin(object):
    def setUp(self):
        self.u1 = Voin(100, 100, 100)
        self.u2 = Voin(100, 100, 100)
        
    def test_attack(self):
        self.u1.attack()
        self.assertEqual(self.u1.endurance(), 90)  

    def test_damage(self):
        self.u1.damage(20)
        self.assertEqual(self.u1.health(), 80)
        self.u1.damage(90)
        self.assertEqual(self.u1.health(), 0)  

    def test_defence(self): 
        self.u1.protection(10)
        self.assertEqual(self.u1.armor(), 90)
        self.u1.protection(100)
        self.assertEqual(self.u1.armor(), 0)

#unit1 = Voin(100, 100, 100)
#unit2 = Voin(100, 100, 100)
#unit1.fight(unit2)