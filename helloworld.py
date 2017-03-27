#!/usr/bin/python
import logging
import time

FORMAT = '[%(asctime)s] level="%(levelname)s" clientip="%(clientip)s" user="%(user)-8s" \
action="%(action)s" message="%(message)s" build="%(build)s" '

logging.basicConfig(format=FORMAT, level=logging.INFO)



def hello_world():
	test_data = {'clientip': '192.168.0.23','user': 'Chris Yang','action':'Running', 'build':'2.3.5'}
	logging.warning('Hello_World_Only', extra=test_data)


#FORMAT = '[%(asctime)s] clientip="%(clientip)s" user="%(user)-8s" action="%(action)s" message="%(message)s" build="%(build)s" '
FORMAT = '[%(asctime)s] clientip=%(clientip)s user=%(user)-8s action=%(action)s message=%(message)s build=%(build)s '


logging.basicConfig(format=FORMAT, level=logging.INFO)


test_data = {'clientip': '192.168.0.24','user': 'Chris Yang','action':'Running', 'build':'2.3.5'}

while(1):
#	print "[%s]" % time.ctime(),
#	hello_world_only()
    time.sleep(10)
    hello_world()

    time.sleep(10)
    logging.info('hello one', extra=test_data)
#	get_module_logger(__name__).info("HELLO WORLD!")

#	hello_world_with_time()
    time.sleep(10)
    test_data['clientip'] = '192.168.0.28'
    test_data['user'] = 'Cheyne Gillooly'
    logging.warning('hello two', extra=test_data)
#	get_module_logger(__name__).info("HELLO WORLD second!")

#	hello_world_with_time_and_greeting("from Chris@GKC")
    time.sleep(10)
    test_data['clientip'] = '192.168.0.28'
    test_data['user'] = 'Cheyne Gillooly'
    test_data['action'] = 'shopping'
    logging.error('hello three', extra=test_data)

    time.sleep(10)
    logging.debug('hello four', extra=test_data)


