"""
# Write your MySQL query statement below
SELECT a.team_id,a.name,
CAST(ROW_NUMBER() OVER(ORDER BY points DESC,name ASC) AS SIGNED)-
CAST(ROW_NUMBER() OVER(ORDER BY points+points_change DESC,name ASC) as SIGNED) as rank_diff
FROM TeamPoints as a
JOIN PointsChange as b
ON a.team_id=b.team_id
"""

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Change in global ranking").getOrCreate()

df_prev = spark.read.format("csv").option("header", "true").option(
    "sep", "|").load("data/TeamPoints.csv")

df_new = spark.read.format("csv").option("header", "true").option(
    "sep", "|").load("data/points_change.csv")


df = df_new.join(df_prev, df_new.team_id == df_prev.team_id, "inner")

df = df.withColumn("points", F.col("points").cast("int")).withColumn(
    "points_change", F.col("points_change").cast("int"))


window1 = Window.orderBy(F.desc("points"), F.desc("name"))
window2 = Window.orderBy(
    F.desc((df["points"] + df["points_change"])), F.col("name").asc())


df = df.withColumn("prev_rank", F.row_number().over(window1)).withColumn(
    "new_rank", F.row_number().over(window2))

df_ranking = df.select(df_prev["team_id"], "name", (F.col("prev_rank") -
          F.col("new_rank")).alias("rank_diff"))

df_ranking.show()
