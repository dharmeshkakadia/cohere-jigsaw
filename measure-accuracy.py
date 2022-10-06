import os
import cohere

from datasets import load_dataset
from sklearn.metrics import classification_report

dataset = load_dataset("jigsaw_toxicity_pred", data_dir='.', split='test', streaming=True)
co = cohere.Client(os.environ.get('COHERE_API_KEY'))

inputs = []
true_labels = []
predicted_labels = []

for i,d in enumerate(dataset):
    if i >= 100: break
    true_labels.append(d['toxic'])
    inputs.append(d['comment_text'])

response = co.classify(model='cohere-toxicity',inputs=inputs)

for c in response.classifications:
    predicted_labels.append(1 if c.prediction=='TOXIC' else 0)

print(classification_report(y_pred=predicted_labels, y_true=true_labels))