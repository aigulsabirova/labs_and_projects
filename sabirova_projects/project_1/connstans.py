#удельные теплоемкости (Дж/(кг*С))
c_water: float = 4200.0 #вода
c_oil: float = 2000.0   #масло
c_steel: float = 500.0  #сталь

#допустимые диапазоны входных данных
m_min: float = 0.1
m_max: float = 1000.0

t1_min: float = -50.0
t1_max: float = 100.0

t2_min: float = 0.0
t2_max: float = 1000.0

#пороговые значения для классификации нагрева (t = t2 - t1)
t_small_limit: float = 10.0
t_normal_limit: float = 100.0

#файл журнала ошибок
log_file: str = 'input_errors.log'