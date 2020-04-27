import sys
import getopt
import logging

import train as train_script
import predict as predict_script

logging.basicConfig(level=logging.DEBUG)

def main(argv):
    try:
        opts, _ = getopt.getopt(argv, "tp:")
        if len(opts) != 1:
            raise getopt.GetoptError('Bad argument')

        opt, arg = opts[0]
        if opt == '-t':
            train_script.train(logging)
        elif opt == '-p':
            if len(sys.argv) < 3:
                raise getopt.GetoptError('Bad argument')
        
            predictions = predict_script.predict(logging, sys.argv[2:])
            for p in predictions:
                print(p)
        else:
            raise getopt.GetoptError('Bad argument')
    except getopt.GetoptError:
        print('Usage: main.py [-t] [-p "Text here"]')
        exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])