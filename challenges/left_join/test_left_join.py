import pytest
from left_join import left_join, right_join, HashTable

def test_left_join_happy_test():
    t_1 = HashTable()
    t_1.add('fond','enamored')        
    t_1.add('wrath', 'anger')          
    t_1.add('diligent', 'employed')    
    t_1.add('outfit', 'garb')           
    t_1.add('guide', 'usher')           

    t_2 = HashTable()
    t_2.add('fond', 'averse')
    t_2.add('wrath', 'delight')
    t_2.add('diligent', 'idle')
    t_2.add('guide', 'follow')
    t_2.add('flow', 'jam')

    assert left_join(t_1, t_2) == [
        ['diligent', 'employed', 'idle'], 
        ['wrath', 'anger', 'delight'], 
        ['guide', 'usher', 'follow'], 
        ['fond', 'enamored', 'averse'], 
        ['outfit', 'garb', None]
        ]

def test_left_join_all_different():
    t_1 = HashTable()
    t_1.add('james','agent')        
    t_1.add('bond', 'surname')          
    t_1.add('gun', 'tool')    
    t_1.add('girl', 'bondgirl')           
    t_1.add('car', 'speed')           

    t_2 = HashTable()
    t_2.add('fond', 'averse')
    t_2.add('wrath', 'delight')
    t_2.add('diligent', 'idle')
    t_2.add('guide', 'follow')
    t_2.add('flow', 'jam')

    assert left_join(t_1, t_2) == [
        ['gun', 'tool', None],
        ['james', 'agent', None], 
        ['bond', 'surname', None], 
        ['girl', 'bondgirl', None], 
        ['car', 'speed', None], 
            
    ]

def test_right_join_happy_test():
    t_1 = HashTable()
    t_1.add('fond','enamored')        
    t_1.add('wrath', 'anger')          
    t_1.add('diligent', 'employed')    
    t_1.add('outfit', 'garb')           
    t_1.add('guide', 'usher')           

    t_2 = HashTable()
    t_2.add('fond', 'averse')
    t_2.add('wrath', 'delight')
    t_2.add('diligent', 'idle')
    t_2.add('guide', 'follow')
    t_2.add('flow', 'jam')

    assert right_join(t_1, t_2) == [
        ['diligent', 'idle', 'employed'], 
        ['wrath', 'delight', 'anger'], 
        ['guide', 'follow','usher'], 
        ['fond', 'averse', 'enamored'], 
        ['outfit', None, 'garb']
        ]

def test_right_join_all_different():
    t_1 = HashTable()
    t_1.add('james','agent')        
    t_1.add('bond', 'surname')          
    t_1.add('gun', 'tool')    
    t_1.add('girl', 'bondgirl')           
    t_1.add('car', 'speed')           

    t_2 = HashTable()
    t_2.add('fond', 'averse')
    t_2.add('wrath', 'delight')
    t_2.add('diligent', 'idle')
    t_2.add('guide', 'follow')
    t_2.add('flow', 'jam')

    assert right_join(t_1, t_2) == [
        ['gun', None, 'tool'],
        ['james', None, 'agent'], 
        ['bond', None, 'surname'], 
        ['girl', None, 'bondgirl'], 
        ['car', None, 'speed' ], 
            
    ]