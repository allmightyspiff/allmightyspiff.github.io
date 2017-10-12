Disassembly of sort:
 14           0 LOAD_CONST               1 (False)
              3 STORE_FAST               2 (is_sorted)

 15           6 SETUP_LOOP             167 (to 176)
        >>    9 LOAD_FAST                2 (is_sorted)
             12 POP_JUMP_IF_TRUE       175

 16          15 LOAD_GLOBAL              0 (len)
             18 LOAD_FAST                1 (to_sort)
             21 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             24 STORE_FAST               3 (array_len)

 17          27 LOAD_CONST               2 (True)
             30 STORE_FAST               4 (jobs_done)

 19          33 SETUP_LOOP             124 (to 160)
             36 LOAD_GLOBAL              1 (range)
             39 LOAD_CONST               3 (0)
             42 LOAD_FAST                3 (array_len)
             45 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             48 GET_ITER
        >>   49 FOR_ITER               107 (to 159)
             52 STORE_FAST               5 (i)

 21          55 LOAD_FAST                5 (i)
             58 LOAD_CONST               4 (1)
             61 BINARY_ADD
             62 LOAD_FAST                3 (array_len)
             65 COMPARE_OP               2 (==)
             68 POP_JUMP_IF_FALSE       74

 22          71 JUMP_ABSOLUTE           49

 24     >>   74 LOAD_FAST                1 (to_sort)
             77 LOAD_FAST                5 (i)
             80 BINARY_SUBSCR
             81 LOAD_FAST                1 (to_sort)
             84 LOAD_FAST                5 (i)
             87 LOAD_CONST               4 (1)
             90 BINARY_ADD
             91 BINARY_SUBSCR
             92 COMPARE_OP               4 (>)
             95 POP_JUMP_IF_FALSE      146

 25          98 LOAD_CONST               1 (False)
            101 STORE_FAST               4 (jobs_done)

 26         104 LOAD_FAST                1 (to_sort)
            107 LOAD_FAST                5 (i)
            110 BINARY_SUBSCR
            111 STORE_FAST               6 (temp)

 27         114 LOAD_FAST                1 (to_sort)
            117 LOAD_FAST                5 (i)
            120 LOAD_CONST               4 (1)
            123 BINARY_ADD
            124 BINARY_SUBSCR
            125 LOAD_FAST                1 (to_sort)
            128 LOAD_FAST                5 (i)
            131 STORE_SUBSCR

 28         132 LOAD_FAST                6 (temp)
            135 LOAD_FAST                1 (to_sort)
            138 LOAD_FAST                5 (i)
            141 LOAD_CONST               4 (1)
            144 BINARY_ADD
            145 STORE_SUBSCR

 29     >>  146 LOAD_FAST                5 (i)
            149 LOAD_CONST               4 (1)
            152 BINARY_ADD
            153 STORE_FAST               5 (i)
            156 JUMP_ABSOLUTE           49
        >>  159 POP_BLOCK

 31     >>  160 LOAD_FAST                4 (jobs_done)
            163 POP_JUMP_IF_FALSE        9

 32         166 LOAD_CONST               2 (True)
            169 STORE_FAST               2 (is_sorted)
            172 JUMP_ABSOLUTE            9
        >>  175 POP_BLOCK

 33     >>  176 LOAD_FAST                1 (to_sort)
            179 RETURN_VALUE