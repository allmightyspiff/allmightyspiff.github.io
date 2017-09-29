# Database Pitfalls and Gotchas

## Intro
+ Who I am

```terminal
josh@brick ~/repos/aha $ git log -2
<span style="color:yellow;">commit 08d10fe4d88ae13103373452a294330a22c0e254</span>
Author: allmightyspiff &lt;chrisagallo@gmail.com&gt;
Date:   Tue Sep 26 16:55:30 2017 -0500

    updated order bare metal example

<span style="color:yellow;">commit 03e1654a8446794b1ab1aa0f7e6743e1e7adca79</span>
Author: allmightyspiff &lt;chrisagallo@gmail.com&gt;
Date:   Tue Sep 26 16:51:01 2017 -0500

    more advanced quotes

```

---

## NoSQL v SQL
+ Different types of NoSQL
+ Differences between SQLs
+ When to use NoSQL
    * LARGE DATA
    * variety of columns in a data set
    * documents

---

## Indexes
+ Explain explain
+ Dont over index
+ NULLS
    * use anything else to indicate the absense of a value
+ Appropriate use of datatypes
    * varchar for date or ip is bad

---

## Over Normalization
+ It is OK to have un-normalized data

---

## TRIGGERS and constraints
+ obscurity - trigger logic should be in application
+ complexity - a good source of unexpected behavior, aka bugs

---

## What not to store
+ Images
+ unstructured data you want to search

---

## Sensitive data
+ hash AND salt passwords
+ dont use MD5
+ understand your engines encryption 

---

## JOINs
+ Joins > subquery
+ join venn diagram

---

## Performance Tuning
+ acquire connection only when needed, and immediately close
+ db files should live on their own storage
+ understand the query cache

---

## Big data and scaling up
+ table partition based on timestamp
    * only partition on something else if it REALLY makes sense
+ sharding
+ multi master setups
+ having a read sql string and a write sql string


http://sql-info.de/mysql/gotchas.html
http://allyouneedisbackend.com/blog/2017/09/24/the-sql-i-love-part-1-scanning-large-table/