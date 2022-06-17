'''
# ######################   ДЗ 1часть ######################################### #
# Напишите классы сериализации контейнеров с данными Python в json, bin файлы. #
# Сами классы должны соответствовать общему интерфейсу (абстрактному базовому  #
# классу) SerializationInterface.                                              #
# ############################################################################ #
'''
from abc import ABCMeta, abstractmethod
import json
import pickle

class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def serialization(self):
        raise NotImplementedError()


class SerializationBin(SerializationInterface):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
    
    def serialization(self):
        with open(self.filename + '.bin', 'wb') as file:
            pickle.dump(self.data, file)
        


class SerializationJson(SerializationInterface):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
    
    def serialization(self):
       with open(self.filename + '.json', 'w') as file:
            json.dump(self.data, file,indent=4, ensure_ascii=False )


obj = {"name": "Misha", "age": 21,"brothers": ["Andrii","Alise"], "susters": ("Alise","Albina")}

# with open('file_bin.bin', 'rb') as file:
#         r = pickle.load(file)
# print(r) 
serializJson = SerializationJson('json_file', obj)      
serializJson.serialization()

#   2
'''
Напишите класс метакласс Meta, который всем классам, для кого он будет 
метаклассом, устанавливает порядковый номер. Код для проверки правильности 
решения:
'''
class Meta(type):
    children_number = 0
    
    def __new__(*args):
        inseance = type.__new__(*args)
        inseance.class_number = Meta.children_number
        Meta.children_number +=1
        return inseance


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

print((Cls1.class_number, Cls2.class_number) == (0, 1))
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
