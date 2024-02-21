from pyspark.sql import SparkSession
import pyspark.sql.functions as f 

spark = SparkSession.builder.appName("employees with missing info").getOrCreate()

emp_path = 'data/employees_w_m_info.csv'

df_employees = spark.read.format("csv").option("header","true").option("sep","|").load(emp_path)

sal_path = 'data/salaries_w_m_info.csv'

df_salaries = spark.read.format("csv").option("header","true").option("sep","|").load(sal_path)

df_join = df_employees.alias("e").join(df_salaries.alias("s"), f.col("e.employee_id") == f.col("s.employee_id"), "fullouter")

df_final = df_join.where(f.col("salary").isNull() | f.col("name").isNull()).select(f.coalesce("e.employee_id","s.employee_id").alias("employee_id"))

df_final.orderBy(f.asc(f.col("employee_id"))).show()

spark.stop()