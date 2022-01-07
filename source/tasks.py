from celery_settings import celery


@celery.task
def sum_of_numbers(number1, number2):
   f = open("logs.txt", "a+")
   f.write(f"The sum of the numbers {number1} + {number2} = {number1 + number2}")
   f.close()