import logging

# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
def factorial(n):
    logging.debug('Start of factorial({})'.format(n))

    total = 1

    for i in range(1,n+1):
        total *= i
        logging.debug('i is {}, total is {}'.format(i,total))

    logging.debug('End of factorial({})'.format(n))
    return total

print(factorial(5))
logging.debug('End of program')
