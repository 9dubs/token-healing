import sparknlp
from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.base import *
from .pipeline import createPipeline, grammerCheck

spark = sparknlp.start()

def tokenHealing(text):

    pipeline = createPipeline()
    empty_ds = spark.createDataFrame([[""]]).toDF("text")
    lp = LightPipeline(pipeline.fit(empty_ds))

    result = lp.annotate(text)

    corrected_text = ' '.join([' '.join(strings) for strings in result.values()])

    result = grammerCheck(corrected_text)

    return result

text = "anyy inputt txt with intentionnally misspelled wordds"

result = tokenHealing(text)

print(result)