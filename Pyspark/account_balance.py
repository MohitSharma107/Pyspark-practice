"""
# Write your MySQL query statement below
SELECT account_id, day, 
SUM(CASE WHEN type = "Withdraw" THEN -amount ELSE amount END) OVER(partition by account_id order by day) as balance
FROM Transactions
"""

from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("account balance").getOrCreate()

# Give relative path of account balance.csv file in data folder and store it in path variable.
path = "data/account balance.csv"


df = spark.read.format("csv").option("header","true").option("sep","|").load(path)

window1 = Window.partitionBy("account_id").orderBy(f.asc("day"))

df = df.withColumn("balance", f.sum(f.when(f.col("type")=="Withdraw",-1 * f.col("amount")).otherwise(f.col("amount"))).over(window1))

df_balance = df.select("account_id","day","type","balance")

df_balance.show()
