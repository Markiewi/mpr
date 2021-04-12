
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local", "PySpark Word Count")
    lines = sc.textFile("txt")
    counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    print(counts.collect())