## 1. INSTRUCTIONS FOR RUNNING THE SCRIPTS

If you have make:
just run make:
```bash
make
```

Otherwise:

just run:
```bash
python3 main.py
```

The script will just run the spacy and the python-crf implementations and fill their results into the corresponding files:

- `spacy_reports.txt` for spacy
- `crf_reports.txt` for python-crf

The datasets are in the `datasets` folder:

- da_ddt-ud-test.iob2
- da_ddt-ud-train.iob2
- en_ewt-ud-test.iob2
- en_ewt-ud-train.iob2
- hr_set-ud-test.iob2
- hr_set-ud-train.iob2
- pt_bosque-ud-test.iob2
- pt_bosque-ud-train.iob2
- sk_snk-ud-test.iob2
- sk_snk-ud-train.iob2
- sr_set-ud-test.iob2
- sr_set-ud-train.iob2
- sv_talbanken-ud-test.iob2
- sv_talbanken-ud-train.iob2
- zh_gsdsimp-ud-test.iob2
- zh_gsdsimp-ud-train.iob2

## 2. RUNNING TIME FOR BOTH SCRIPTS 

-

## 3. OPTIONS SELECTED FOR RUNNING SPACY

I choose those model for each language:
- danish -> "da_core_news_sm"
- chinese -> "zh_core_web_sm"
- portuguese -> "pt_core_news_sm"
- english -> "en_core_web_sm"
- french -> "fr_core_news_sm"
- otherwise -> "xx_ent_wiki_sm"

