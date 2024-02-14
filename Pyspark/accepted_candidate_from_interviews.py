"""
WITH two_yoe as (SELECT candidate_id, interview_id FROM Candidates
WHERE years_of_exp >= 2)

SELECT candidate_id
FROM two_yoe ty LEFT JOIN Rounds r
ON ty.interview_id = r.interview_id
GROUP BY r.interview_id
HAVING SUM(score) > 15
"""
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName(
    "accepted candidate from interview").getOrCreate()

path_candidate = "data/candidates.csv"


df_candidates = spark.read.format("csv").option("header", "true").option(
    "inferSchema", "true").option("sep", "|").load(path_candidate)

path_round = "data/rounds.csv"

df_round = spark.read.format("csv").option("header", "true").option(
    "inferSchema", "true").option("sep", "|").load(path_round)

df_tow_yoe = df_candidates.where(f.col("years_of_exp") >= 2).select(
    "candidate_id", "interview_id")

df_join = df_tow_yoe.alias("a").join(df_round.alias("b"), f.col(
    "a.interview_id") == f.col("b.interview_id"), "left")

df_final_selected = df_join.groupBy("b.interview_id").agg(
    f.sum("score").alias("score")).where(f.col("score") > 15)

df_final_selected.show()
