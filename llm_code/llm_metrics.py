import evaluate
from evaluate import load
from datasets import load_metric

from transformers import pipeline
import asyncio
import sys
from rouge_score import rouge_scorer, scoring

sys.path.append('../..')


class Metrics:
    def __init__(self, predictions, references):
        self.predictions = predictions
        self.references = references

    def rouge_score(self):
        rouge = evaluate.load('rouge')
        results = rouge.compute(predictions=self.predictions, references=self.references)
        print(f"*****************************************rougu1 score:{results['rouge1']}")
        return results['rouge1']

    def bleu_score(self):
        bleu = evaluate.load("bleu")
        results = bleu.compute(predictions=self.predictions, references=self.references)
        print(f"*****************************************bleu score:{results['bleu']}")
        return results["bleu"]

    def exact_match_score(self):
        exact_match_metric = load("exact_match")
        results = exact_match_metric.compute(predictions=self.predictions, references=self.references)
        print(f"*****************************************exact match score:{results['exact_match']}")
        return results['exact_match']

    def chrf_score(self):
        chrf = evaluate.load("chrf")
        results = chrf.compute(predictions=self.predictions, references=self.references)
        print(f"'chrf': {results['score']}")
        return results['score']


class MetricsModel:
    def __init__(self, predictions, model_type):
        self.predictions = predictions
        self.model_type = model_type

    def toxicity_score(self):
        toxicity = load("toxicity", module_type="measurement")
        results = toxicity.compute(predictions=self.predictions)
        print(f"Toxicity Scores: {results['toxicity'][0]}")
        return results['toxicity'][0]





def main():
    rough = Metrics(predictions="hello there", references="hello there")
    rough.rouge_score()
    blue = Metrics(predictions="hello there general kenobi", references="hello there general kenobi")
    blue.bleu_score()
    exact = Metrics(predictions="Example 1", references="Example 2")
    exact.exact_match_score()
    input_texts = ["lorem ipsum", "Happy Birthday!", "Bienvenue"]
    me = Metrics(predictions="hello there general kenobi", references="hello there general kenobi")
    input_texts = ["she went to the library", "he is a douchebag"]
    model = MetricsModel(predictions=input_texts, model_type='gpt3.5')
    toxicity_scores = model.toxicity_score()
    print(toxicity_scores)
    me.chrf_score()


if __name__ == '__main__':
    main()