#!/usr/bin/env python3
import psycopg2

dbname = "news"
question1 = " === The most popular three articles of all time are : === "
quaryQ1 = """
select articles.title , COUNT(*) as num FROM log,
articles WHERE log.path LIKE ('%'||articles.slug)
GROUP BY articles.title ORDER BY num desc LIMIT 3;
"""

question2 = " === The most popular authors are : === "

quaryQ2 = """
select authors.name, count(*) as views
from authors
join articles on articles.author = authors.id
join log on log.path LIKE ('%'||articles.slug)
group by authors.name order by views desc  """

question3 = " === Days with greater than 1% errors are: === "

quaryQ3 = """
with visits as (select count(status),
cast(time as date) as day from log group by day),
error as (select cast(time as date) as day,
count(*) as count from log where status!='200 OK' group by day),
error_pre as (select error.count*100.0/visits.count as error2,
error.day as day from error join visits on error.day = visits.day)
select * from error_pre where error2 > 1.0 order by day;

"""

db = psycopg2.connect(database=dbname)
c = db.cursor()


c.execute(quaryQ1)
results = c.fetchall()
print(" ")
print question1
i = 1
for result in results:
    print(
        " " + str(i) + "- ( " + result[0] + " ) with " +
        str(result[1]) + " views.")
    i = i + 1
print(" ")


c.execute(quaryQ2)
results = c.fetchall()
print(" ")
print question2
i = 1
for result in results:
    print(
        " " + str(i) + "- (" + result[0] + ") with " +
        str(result[1]) + " views.")
    i = i + 1
print(" ")


c.execute(quaryQ3)
results = c.fetchall()
print(" ")
print question3
i = 1
for result in results:
    print(
        " " + str(i) + "- " + str(result[1]) + " with " +
        "%.2f" % round(result[0], 2) + "% of error.")
    i = i + 1
print(" ")

db.close()
