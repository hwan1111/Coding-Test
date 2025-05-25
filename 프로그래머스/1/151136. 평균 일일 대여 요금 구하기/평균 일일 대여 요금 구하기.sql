select round(avg(c.DAILY_FEE), 0) as AVERAGE_FEE
from car_rental_company_car as c
where c.car_type = 'SUV'