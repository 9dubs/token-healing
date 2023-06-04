import sparknlp

from gingerit.gingerit import GingerIt

from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.base import *

spark = sparknlp.start()

def createPipeline():
  documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

  tokenizer = RecursiveTokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")\
    .setPrefixes(["\"", "(", "[", "\n"])\
    .setSuffixes([".", ",", "?", ")","!", "'s"])

  spellModel = ContextSpellCheckerModel\
    .pretrained()\
    .setInputCols("token")\
    .setOutputCol("checked")

  finisher = Finisher()\
    .setInputCols("checked")

  pipeline = Pipeline(stages = [
      documentAssembler,
      tokenizer,
      spellModel,
      finisher
  ])

  return pipeline

def grammerCheck(text):
  ginger = GingerIt()

  result = ginger.parse(text)

  return result['result']