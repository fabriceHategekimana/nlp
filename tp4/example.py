##TODO Run this example
from transformers import AutoTokenizer, ElectraForTokenClassification
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "bhadresh-savani/electra-base-discriminator-finetuned-conll03-english"
)
model = ElectraForTokenClassification.from_pretrained(
    "bhadresh-savani/electra-base-discriminator-finetuned-conll03-english"
)

input_text = "HuggingFace is a company based in Paris and New York"
print("input_text:", input_text)

inputs = tokenizer(
    input_text,
    add_special_tokens=False,
    return_tensors="pt",
)

with torch.no_grad():
    logits = model(**inputs).logits

predicted_token_class_ids = logits.argmax(-1)

# Note that tokens are classified rather then input words which means that
# there might be more predicted token classes than words.
# Multiple token classes might account for the same word
predicted_tokens_classes = [
    model.config.id2label[t.item()] for t in predicted_token_class_ids[0]
]
predicted_tokens_classes
print("predicted_tokens_classes:", predicted_tokens_classes)

labels = predicted_token_class_ids
loss = model(**inputs, labels=labels).loss
loss_res = round(loss.item(), 2)
print("loss_res:", loss_res)
