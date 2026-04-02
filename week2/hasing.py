#the problem with DAA is u is too large, can we still get same benefit of DAA but make u much
#smaller for space efficiency ->> HASHING ; m=O(n) hasing map: {1,2....u} - > {1,2,...,m}

#but u>m -> collide (pigeonhole principle)-> solution: CHAINING and OPEN Addressing(most hashtables are implemented)

#Chaining: problem: want small chain, if long chain -> linear time for searching -> need good hash function