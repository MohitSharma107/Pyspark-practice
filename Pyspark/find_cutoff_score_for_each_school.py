"""
select school_id, ifnull(min(score),-1) as score
from Schools left join exam
on capacity >= student_count
group by school_id
"""
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName(
    "accepted candidate from interview").getOrCreate()

path_school = "data/schools.csv"
path_exam = "data/exam.csv"

df_school = spark.read.format("csv").option(
    "header", "true").option("sep", "|").option("inferSchema","true").load(path_school)
df_exam = spark.read.format("csv").option(
    "header", "true").option("sep", "|").option("inferSchema","true").load(path_exam)


df_join = df_school.join(df_exam, f.col("capacity") >= f.col("student_count"), "left")

df_join.groupBy(f.col("school_id")).agg(f.coalesce(
    f.min(f.col("score")).cast("int"), f.lit(-1)).alias("score")).show()

