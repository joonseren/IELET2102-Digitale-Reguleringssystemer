from threading import Thread, Lock, currentThread
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

sensor_finished = False
actuator_finished = False

communication_lock = Lock()

def sensor():
    global actuator_finished, sensor_finished
    while(not sensor_finished):
        communication_lock.acquire()
        
        if not actuator_finished:
            communication_lock.release()
            logging.debug('Yielding lock to actuator thread')
            logging.debug('Sleeping 1 second')
            sleep(1)
        else:
            logging.debug('Sensor transmitted information')
            sensor_finished = True
            communication_lock.release()
        
    
def actuator():
    global actuator_finished, sensor_finished
    while(not actuator_finished):
        communication_lock.acquire()
        
        if not sensor_finished:
            communication_lock.release()
            logging.debug('Yielding lock to sensor thread')
            logging.debug('Sleeping 1 second')
            sleep(1)
        else:
            logging.debug('Actuator recieved information')
            actuator_finished = True
            communication_lock.release()
    
def main():
    sensor_thread = Thread(name='Sensor', target=sensor, args=[])
    actuator_thread = Thread(name='Actuator', target=actuator, args=[])
    
    sensor_thread.start()
    actuator_thread.start()
    
main()
