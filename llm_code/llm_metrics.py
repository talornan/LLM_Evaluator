import evaluate
from evaluate import load
from datasets import load_metric

from transformers import pipeline


class Metrics:
    def __init__(self, predictions, references):
        self.predictions = predictions
        self.references = references

    def rouge_score(self):
        rouge = evaluate.load('rouge')
        results = rouge.compute(predictions=self.predictions, references=self.references)
        print(f"*****************************************rougu1 score:{results['rouge1']}")

    def bleu_score(self):
        bleu = evaluate.load("bleu")
        results = bleu.compute(predictions=self.predictions, references=self.references)
        print(f"*****************************************bleu score:{results}")

    def exact_match_score(self):
        exact_match_metric = load("exact_match")
        results = exact_match_metric.compute(predictions=self.predictions, references=self.references)
        print(f"*****************************************exact match score:{results}")


class MetricsModel:
    def __init__(self, predictions, model_type):
        self.predictions = predictions
        self.model_type = model_type

    def toxicity_score(self):
        toxicity = load("toxicity", module_type="measurement")
        results = toxicity.compute(predictions=self.predictions)
        print(f"Toxicity Scores: {results['toxicity']}")
        return results['toxicity']

    def fluency_score(self):
        perplexity = load("perplexity", module_type="metric")
        results = perplexity.compute(predictions=self.predictions, model_id=self.model_type)
        print(f"Fluency: {results}")
        return results


def main():

    rough = Metrics(predictions="hello there", references="hello there")
    rough.rouge_score()
    blue = Metrics(predictions="hello there general kenobi", references="hello there general kenobi")
    blue.bleu_score()
    exact = Metrics(predictions="Example 1", references="Example 2")
    exact.exact_match_score()
    input_texts = ["lorem ipsum", "Happy Birthday!", "Bienvenue"]
    model = MetricsModel(predictions=input_texts, model_type='gpt2')
    results = model.fluency_score()
    print(list(results.keys()))
    print(round(results["mean_perplexity"], 2))
    print(round(results["perplexities"][0], 2))
    input_texts = ["she went to the library", "he is a douchebag"]
    model = MetricsModel(predictions=input_texts, model_type='gpt3.5')
    toxicity_scores = model.toxicity_score()
    print(toxicity_scores)


if __name__ == '__main__':
    main()
