Assignment: Type
enum NER: DataSet {
	UNER_Portuguese-Bosque 
	UNER_Chinese-GSDSIMP
	UNER_Swedish-Talbanken
	UNER_Serbian-SET
	UNER_Slovak-SNK
	UNER_Croatian-SET
	UNER_English-EWT 
	UNER_Danish-DDT
}


## mer 10 jan 2024 14:21:23 CET

I need to use hugging face
https://huggingface.co/docs/transformers/index


## mer 10 jan 2024 14:43:29 CET
Comme proposé dans le cours, je vais essayer Electra.

```rust
enum Encoder {
	Generator,
	Discriminator
}


Electra impl BERT;

Electra {
	Encoder::Discriminator,
	embedding_size: smaller
	hidden_size: bigger
}
```


