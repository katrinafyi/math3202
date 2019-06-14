# Question 1 A

Academic license - for non-commercial use only
Optimize a model with 230 rows, 210 columns and 800 nonzeros
Variable types: 0 continuous, 210 integer (210 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e+02, 2e+03]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 6e+00]
Found heuristic solution: objective 29434.000000
Presolve time: 0.00s
Presolved: 230 rows, 210 columns, 800 nonzeros
Variable types: 0 continuous, 210 integer (210 binary)

Root relaxation: objective 1.542100e+04, 132 iterations, 0.00 seconds

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 15421.0000    0   65 29434.0000 15421.0000  47.6%     -    0s
H    0     0                    26528.000000 15421.0000  41.9%     -    0s
H    0     0                    19111.000000 15421.0000  19.3%     -    0s
H    0     0                    18916.000000 15421.0000  18.5%     -    0s
     0     0 15503.0000    0   64 18916.0000 15503.0000  18.0%     -    0s
H    0     0                    17357.000000 15503.0000  10.7%     -    0s
     0     0 15553.1000    0   83 17357.0000 15553.1000  10.4%     -    0s
     0     0 15560.9375    0   87 17357.0000 15560.9375  10.3%     -    0s
     0     0 15575.9634    0  100 17357.0000 15575.9634  10.3%     -    0s
     0     0 15582.9552    0  115 17357.0000 15582.9552  10.2%     -    0s
     0     0 15603.5532    0   98 17357.0000 15603.5532  10.1%     -    0s
     0     0 15603.7372    0  111 17357.0000 15603.7372  10.1%     -    0s
     0     0 15603.8789    0  112 17357.0000 15603.8789  10.1%     -    0s
     0     0 15611.0000    0  100 17357.0000 15611.0000  10.1%     -    0s
     0     0 15611.0276    0  101 17357.0000 15611.0276  10.1%     -    0s
     0     0 15614.8150    0  100 17357.0000 15614.8150  10.0%     -    0s
     0     0 15615.2883    0   85 17357.0000 15615.2883  10.0%     -    0s
     0     0 15617.8646    0  116 17357.0000 15617.8646  10.0%     -    0s
     0     0 15619.1098    0   96 17357.0000 15619.1098  10.0%     -    0s
     0     0 15621.4600    0  116 17357.0000 15621.4600  10.0%     -    0s
     0     0 15628.3108    0  120 17357.0000 15628.3108  10.0%     -    0s
     0     0 15630.0283    0  120 17357.0000 15630.0283  9.95%     -    0s
     0     0 15630.4579    0  120 17357.0000 15630.4579  9.95%     -    0s
     0     0 15630.4579    0  120 17357.0000 15630.4579  9.95%     -    0s
     0     2 15630.4579    0  120 17357.0000 15630.4579  9.95%     -    0s

Cutting planes:
  Gomory: 2
  MIR: 1
  Zero half: 17
  Mod-K: 1

Explored 242 nodes (4080 simplex iterations) in 0.25 seconds
Thread count was 4 (of 4 available processors)

Solution count 5: 17357 18916 19111 ... 29434

Optimal solution found (tolerance 1.00e-04)
Best objective 1.735700000000e+04, best bound 1.735700000000e+04, gap 0.0000%

MINIMUM COST: 17357.0
Factories built: [0, 3, 7, 9]
Assignments:
0 [9, 17, 19]
1 []
2 []
3 [5, 10, 11, 13, 14, 15]
4 []
5 []
6 []
7 [0, 2, 4, 6, 8, 16]
8 []
9 [1, 3, 7, 12, 18]

# Question 1 B

Optimize a model with 230 rows, 220 columns and 810 nonzeros
Variable types: 0 continuous, 220 integer (220 binary)
Coefficient statistics:
  Matrix range     [1e+00, 2e+00]
  Objective range  [5e+02, 2e+03]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 6e+00]
Found heuristic solution: objective 29434.000000
Presolve time: 0.00s
Presolved: 230 rows, 220 columns, 810 nonzeros
Variable types: 0 continuous, 220 integer (220 binary)

Root relaxation: objective 1.542100e+04, 132 iterations, 0.00 seconds

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 15421.0000    0   65 29434.0000 15421.0000  47.6%     -    0s
H    0     0                    26627.000000 15421.0000  42.1%     -    0s
H    0     0                    18611.500000 15421.0000  17.1%     -    0s
H    0     0                    17811.000000 15421.0000  13.4%     -    0s
     0     0 15503.0000    0   64 17811.0000 15503.0000  13.0%     -    0s
     0     0 15553.1000    0   83 17811.0000 15553.1000  12.7%     -    0s
     0     0 15560.9375    0   87 17811.0000 15560.9375  12.6%     -    0s
     0     0 15575.9634    0  100 17811.0000 15575.9634  12.5%     -    0s
     0     0 15582.9552    0  115 17811.0000 15582.9552  12.5%     -    0s
     0     0 15603.5532    0   98 17811.0000 15603.5532  12.4%     -    0s
     0     0 15603.7372    0  111 17811.0000 15603.7372  12.4%     -    0s
     0     0 15603.8789    0  112 17811.0000 15603.8789  12.4%     -    0s
     0     0 15611.0000    0  100 17811.0000 15611.0000  12.4%     -    0s
     0     0 15611.0276    0  101 17811.0000 15611.0276  12.4%     -    0s
     0     0 15614.8150    0  100 17811.0000 15614.8150  12.3%     -    0s
     0     0 15615.2883    0   85 17811.0000 15615.2883  12.3%     -    0s
     0     0 15617.8646    0  116 17811.0000 15617.8646  12.3%     -    0s
H    0     0                    17357.000000 15617.8646  10.0%     -    0s
     0     0 15620.2388    0  118 17357.0000 15620.2388  10.0%     -    0s
     0     0 15620.3947    0  119 17357.0000 15620.3947  10.0%     -    0s
     0     0 15620.3947    0  119 17357.0000 15620.3947  10.0%     -    0s
     0     2 15620.3947    0  119 17357.0000 15620.3947  10.0%     -    0s
*   19    13               9    17267.000000 15653.4903  9.34%  25.3    0s
H   29    20                    17251.000000 15936.2500  7.62%  26.0    0s
*   39    17              10    17186.000000 15936.2500  7.27%  22.7    0s
*   55    16               9    16993.000000 16131.1818  5.07%  20.9    0s

Cutting planes:
  Gomory: 2
  MIR: 1
  Zero half: 18
  Mod-K: 1

Explored 133 nodes (2630 simplex iterations) in 0.18 seconds
Thread count was 4 (of 4 available processors)

Solution count 9: 16993 17186 17251 ... 29434

Optimal solution found (tolerance 1.00e-04)
Best objective 1.699300000000e+04, best bound 1.699300000000e+04, gap 0.0000%

MINIMUM COST: 16993.0
Factories built: [0, 7, 9]
Big factories: [0]
Assignments:
0 [2, 5, 9, 10, 13, 14, 17, 19]
1 []
2 []
3 []
4 []
5 []
6 []
7 [0, 4, 6, 8, 11, 16]
8 []
9 [1, 3, 7, 12, 15, 18]

# Question 2 A

Profit: 533.0
Books bought: (20, 10, 10, 30, 10, 0)
[(14, 28), (8, 16), (17, 34), (22, 44), (12, 24), (6, 12)]

# Question 2 B

Profit: 1041.169629
Books bought: (30, (0, (30, (30, (0, (0, 'end', 'end'), (10, (), 'end')), (20, (), (10, (), 'end'))), (40, (), (30, (), (10, (), 'end')))), (40, (), (40, (), (20, (), (10, (), 'end'))))), (20, (), (30, (), (50, (), (20, (), (10, (), 'end'))))))

Graph
Format: (buy this week, next week if NO movie this week, next week if movie this week)
(30,
 (0,
  (30,
   (30, (0, (0, 'end', 'end'), (10, (), 'end')), (20, (), (10, (), 'end'))),
   (40, (), (30, (), (10, (), 'end')))),
  (40, (), (40, (), (20, (), (10, (), 'end'))))),
 (20, (), (30, (), (50, (), (20, (), (10, (), 'end'))))))

Movie released in week 1
Week 1 (MOVIE RELEASE)    bought: 30, sold: 28 / 28, stored:  2
Week 2 (after movie)      bought: 20, sold: 16 / 16, stored:  6
Week 3 (after movie)      bought: 30, sold: 34 / 34, stored:  2
Week 4 (after movie)      bought: 50, sold: 44 / 44, stored:  8
Week 5 (after movie)      bought: 20, sold: 24 / 24, stored:  4
Week 6 (after movie)      bought: 10, sold: 12 / 12, stored:  2

Movie released in week 2
Week 1 (before movie)     bought: 30, sold: 14 / 14, stored: 16
Week 2 (MOVIE RELEASE)    bought:  0, sold: 16 / 16, stored:  0
Week 3 (after movie)      bought: 30, sold: 30 / 34, stored:  0
Week 4 (after movie)      bought: 50, sold: 44 / 44, stored:  6
Week 5 (after movie)      bought: 20, sold: 24 / 24, stored:  2
Week 6 (after movie)      bought: 10, sold: 12 / 12, stored:  0

Movie released in week 3
Week 1 (before movie)     bought: 30, sold: 14 / 14, stored: 16
Week 2 (before movie)     bought:  0, sold:  8 /  8, stored:  8
Week 3 (MOVIE RELEASE)    bought: 30, sold: 34 / 34, stored:  4
Week 4 (after movie)      bought: 40, sold: 44 / 44, stored:  0
Week 5 (after movie)      bought: 30, sold: 24 / 24, stored:  6
Week 6 (after movie)      bought: 10, sold: 12 / 12, stored:  4

Movie released in week 4
Week 1 (before movie)     bought: 30, sold: 14 / 14, stored: 16
Week 2 (before movie)     bought:  0, sold:  8 /  8, stored:  8
Week 3 (before movie)     bought: 30, sold: 17 / 17, stored: 21
Week 4 (MOVIE RELEASE)    bought: 30, sold: 44 / 44, stored:  7
Week 5 (after movie)      bought: 20, sold: 24 / 24, stored:  3
Week 6 (after movie)      bought: 10, sold: 12 / 12, stored:  1

Movie released in week 5
Week 1 (before movie)     bought: 30, sold: 14 / 14, stored: 16
Week 2 (before movie)     bought:  0, sold:  8 /  8, stored:  8
Week 3 (before movie)     bought: 30, sold: 17 / 17, stored: 21
Week 4 (before movie)     bought: 30, sold: 22 / 22, stored: 29
Week 5 (MOVIE RELEASE)    bought:  0, sold: 24 / 24, stored:  5
Week 6 (after movie)      bought: 10, sold: 12 / 12, stored:  3

Movie released in week 6
Week 1 (before movie)     bought: 30, sold: 14 / 14, stored: 16
Week 2 (before movie)     bought:  0, sold:  8 /  8, stored:  8
Week 3 (before movie)     bought: 30, sold: 17 / 17, stored: 21
Week 4 (before movie)     bought: 30, sold: 22 / 22, stored: 29
Week 5 (before movie)     bought:  0, sold: 12 / 12, stored: 17
Week 6 (MOVIE RELEASE)    bought:  0, sold: 12 / 12, stored:  5

[(14, 28), (8, 16), (17, 34), (22, 44), (12, 24), (6, 12)]

