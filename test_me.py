import sys

sys.path.insert(0, "/workspace/src")

from parseval.disprover import Disprover

# db = instantiate_db('SELECT * FROM t1 WHERE a>50;', 'CREATE TABLE t1(a INT PRIMARY KEY)', '/tmp', 'mydb')
# print(db)


def run_test(q1, q2, schema, dialect="calcite"):
    disprover = Disprover(q1, q2, schema, dialect=dialect)
    handler = disprover.run()

    if handler.state == "EQ":
        print("Given queries are equivalent")
    elif handler.state == "NEQ":
        print("Given queries are not equivalent! Counter example:")
        print(handler.q1_result.rows)
        print(handler.q2_result.rows)
    else:
        print("Error")
        print(handler.state)
        if handler.error_msg:
            print(handler.error_msg)
        if handler.q1_result and handler.q1_result.error_msg:
            print(handler.q1_result.error_msg)
        if handler.q2_result and handler.q2_result.error_msg:
            print(handler.q2_result.error_msg)


# run_test(
#     'SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.c GROUP BY d;',
#     'SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.c;',
#     'CREATE TABLE t1(a INT PRIMARY KEY, b INT); CREATE TABLE t2(c INT PRIMARY KEY, d INT);',
#     'sqlite')

# run_test(
#     q1_calc,
#     q2_calc,
#     base_schema,
#     'sqlite')

# with open('SQLSolver/sqlsolver_data/schemas/calcite_test.base.schema.sql') as schema_file:
#     schema = schema_file.read()

# with open('SQLSolver/sqlsolver_data/calcite/calcite_tests') as tests_file:
#     i = 1
#     while tests_file:
#         print('Test ' + str(i))
#         i += 1
#         q1 = tests_file.readline()
#         q2 = tests_file.readline()
#         run_test(q1, q2, schema, dialect='calcite')

# run_test(
#     'SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.c GROUP BY d;',
#     'SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.c;',
#     'CREATE TABLE t1(a INT PRIMARY KEY, b INT); CREATE TABLE t2(c INT PRIMARY KEY, d INT);',
#     'sqlite')

run_test(
    "SELECT * FROM t1 WHERE a > 50;",
    "SELECT * FROM t1 WHERE a > 60 ORDER BY b;",
    "CREATE TABLE t1(a INT PRIMARY KEY, b INT)",
    "sqlite",
)

# run_test('SELECT * FROM t1 WHERE a > 50;', 'SELECT * FROM t1 WHERE a > 60 ORDER BY b;', 'CREATE TABLE t1(a INT PRIMARY KEY, b INT)')
