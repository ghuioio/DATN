import torch
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)  # For 3 sentiment classes: positive, negative, neutral

from torch.utils.data import DataLoader
from transformers import AdamW
from tqdm import tqdm
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file
data = pd.read_csv('btc_tweets_data.csv', encoding='utf-8')

# Replace this line with the actual column name containing the text of the tweets
data['text'] = data['content']

# Replace this line with the actual column name containing the sentiment labels
# Assuming sentiment labels are already encoded as integers (0, 1, or 2)
data['label'] = data['sentiment']

# Split the data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Extract the text and labels from the training and test sets
train_texts = train_data['text'].tolist()
train_labels = train_data['label'].tolist()

test_texts = test_data['text'].tolist()
test_labels = test_data['label'].tolist()

# Define a dataset class
class SentimentDataset(torch.utils.data.Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        inputs['labels'] = torch.tensor(label)
        return inputs

    def __len__(self):
        return len(self.texts)

# Create DataLoader
train_dataset = SentimentDataset(train_data['text'], train_data['label'], tokenizer)
train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)

# Fine-tuning loop
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
optimizer = AdamW(model.parameters(), lr=2e-5)

for epoch in range(3):  # Train for 3 epochs
    model.train()
    for batch in tqdm(train_loader):
        optimizer.zero_grad()
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

test_texts = [...]  # List of test tweets
test_labels = [...]  # List of ground truth sentiment labels (0, 1, or 2) for test tweets

test_dataset = SentimentDataset(test_texts, test_labels, tokenizer)
test_loader = DataLoader(test_dataset, batch_size=8, shuffle=False)

# Evaluation loop
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for batch in tqdm(test_loader):
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        predictions = torch.argmax(outputs.logits, dim=-1)
        correct += (predictions == batch['labels']).sum().item()
        total += len(predictions)

accuracy = correct / total
print("Accuracy:", accuracy)
