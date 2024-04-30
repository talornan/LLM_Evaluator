import evaluate
from datasets import load_metric

from transformers import pipeline


class Metrics:
    def __init__(self):
        self.predictions = None
        self.references = None

    def rouge_score(self):
        rouge_metric = load_metric("rouge")

        # Compute ROUGE scores
        scores = rouge_metric.compute(predictions=[self.predictions], references=[self.references])

        # Extract ROUGE-1 F1 score
        rouge1_f1 = scores["rouge1"].mid.fmeasure
        print(f"ROUGE-1 F1 Score: {rouge1_f1}")

        return rouge1_f1

    def bleu_score(self):
        # bleu = evaluate.load("bleu")
        # results = bleu.compute(predictions=self.predictions, references=self.references)
        # print(f"*****************************************bleu score:{results}")
        # return results
        pass

    def fluency_score(self):
        return 0.7

    def coherence_score(self):
        return 0.4

    def toxicity_score(self):
        return 0.9
