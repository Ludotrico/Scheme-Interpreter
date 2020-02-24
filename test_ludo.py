#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dematicadmin
#
# Created:     02/08/2019
# Copyright:   (c) dematicadmin 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from scheme import *


def main():

    env = create_global_frame()
    scheme_eval(read_line("(define (enumerate s)(define (tailer s index)(if (null? (car s)) nil(cons(list index (car s)) (tailer (cdr s) (+ 1 index)))))(tailer s 0))"), env)
    r = read_line("(enumerate '(1 2 3))")
    a=scheme_eval(r,env)
    print(a)


if __name__ == '__main__':
    main()
