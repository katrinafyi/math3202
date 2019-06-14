from gurobipy import *
from functools import lru_cache
from itertools import product

# To run this code, import the file then use the run() function like
# run(1, "a") for question 1, part a.

def bigcorp(part_b=0):
    from Prac2019Stub import Factories, Customers, Build, Assign
    
    # transform data structure
    AssignCosts = {(f,c): Assign[c][f] for f in Factories for c in Customers}
    
    m = Model('BigCorp Factories')

    # factory built variable
    X = m.addVars(Factories, name='X', vtype=GRB.BINARY, obj=Build)
    # factory assignment variable
    Y = m.addVars(Factories, Customers, name='Y', vtype=GRB.BINARY, obj=AssignCosts)
    if part_b:
        BigCosts = [0.5*x for x in Build]
        # factory upgrade variable
        Z = m.addVars(Factories, name='Z', vtype=GRB.BINARY, obj=BigCosts)
    else:
        # if part a, all factories are not upgraded.
        Z = (0,)*len(Factories)

    m.setAttr(GRB.Attr.ModelSense, GRB.MINIMIZE)

    # customers can only be assigned if factory built
    m.addConstrs(Y[f,c] <= X[f] for f in Factories for c in Customers)
    # factory serves at most 6 or 8 if upgraded
    m.addConstrs(Y.sum(f, '*') <= 6 + 2*Z[f] for f in Factories)
    # every customer must be assigned to a factory
    m.addConstrs(Y.sum('*', c) >= 1 for c in Customers)

    m.optimize()
    print()
    print('MINIMUM COST:', m.objVal)
    print('Factories built:', [f for f in Factories if X[f].x])
    if part_b:
        print('Big factories:', [f for f in Factories if Z[f].x])

    print('Assignments:')
    for f in Factories:
        print(f, [c for c in Customers if Y[f,c].x])

def classic_book(part_b=0):
    # range of weeks
    Weeks = range(6)
    # expected sales each week
    Sales = [14, 8, 17, 22, 12, 6]
    # actions: books bought, in lots of 10
    Actions = [10*x for x in range(11)]

    @lru_cache(None)
    def V_a(t, s):
        # Part A
        # stage: t = weeks elapsed
        # state: s = books in storage from previous week
        if t >= len(Weeks):
            return (s, ()) # profit $1 per book at end of 6 weeks
        return max( 
            (
                # subtract $5 per book and $0.5 per stored book
                -5*a -0.5*(a+s-min(Sales[t], s+a))
                # add $12 profit per sold book, limited by expected sales
                # and available books
                + 12*min(Sales[t], s+a)
                # add profit of later stages
                + V_a(t+1, max(a+s-Sales[t], 0))[0]
            , (a,) + V_a(t+1, max(a+s-Sales[t], 0))[1])
            for a in Actions
        )

    # sales are doubled
    MovieSales = [2*x for x in Sales]
    # Sales2[t][m] gives sales at time t with movie state m. 
    # m=1 indicated movie released.
    Sales2 = list(zip(Sales, MovieSales))
    # probability of each m state.
    MovieProbs = [0.3, 0.7]

    get_sales2 = lambda t, c, m, movie: min(Sales2[t][max(m, movie)], c)

    @lru_cache(None)
    def V_b(t, s, movie):
        # Part B
        # stage: t = weeks elapsed
        # state: s = books in storage from previous week
        #        movie = whether book has been turned into movie before this week.
        if t >= len(Weeks):
            # profit $1 per book at end of 6 weeks
            return (s, 'end') 
        return max( 
            (sum( 
                p*(
                    # m is 1 if this is the case where the movie has been released, 
                    # 0 otherwise. max(m, movie) means if the movie has 
                    # already been released, it continues to be released.
                    #
                    # other parts of value function are the same.
                    -5*a - 0.5 * (a+s - get_sales2(t, s+a, m, movie))
                    + 12 * get_sales2(t, s+a, m, movie)
                    + V_b(t+1, s+a - get_sales2(t, s+a, m, movie), max(m, movie))[0]
                )
                for m, p in enumerate(MovieProbs)
            ), (a, V_b(t+1, s+a - get_sales2(t, s+a, 0, movie), max(0, movie))[1] if not movie else (),
                    V_b(t+1, s+a - get_sales2(t, s+a, 1, movie), max(1, movie))[1]
                )
            )
            for a in Actions
        )

    max_p, max_a = V_a(0, 0) if not part_b else V_b(0, 0, 0)
    print('Profit:', max_p)
    print('Books bought:', max_a)

    if part_b:
        import pprint
        print()
        print('Graph')
        print('Format: (buy this week, next week if NO movie this week, next week if movie this week)')
        pprint.pprint(max_a, indent=1)

        print()
        for t in Weeks: # what if the movie started in week t
            print('Movie released in week', t+1)
            s = 0
            for m, weeks in enumerate((range(0, t+1), range(t+1, 6))):
                for t_ in weeks:
                    sol = V_b(t_, s, m)
                    bought = sol[1][0]
                    sales = Sales2[t_][m or (t_ >= t)]
                    sold = min(s+bought, sales)
                    s = s+bought - sold
                    week_type = ('(before movie)', '(after movie)')[m]
                    if t_ == t: week_type = '(MOVIE RELEASE)'
                    print('Week', t_+1, week_type.ljust(18),
                        'bought: {:>2}, sold: {:>2} / {:>2}, stored: {:>2}'.format(bought, sold, sales, s))
            print()

def run(question, part):
    from sys import stderr
    q = question-1
    p = 'ab'.index(part.lower())
    print('#', 'Question', question, part.upper())
    print()
    (bigcorp, classic_book)[q](p)
    print()
    print('This was question', question, 'part', part + '.', file=stderr)


if __name__ == "__main__":
    from sys import argv 
    if len(argv) < 3:
        for q in (1, 2):
            for p in 'ab':
                run(q, p)
    else:
        question = int(argv[1])
        part = argv[2]
        run(question, part)