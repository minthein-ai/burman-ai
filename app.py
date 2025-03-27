# !pip3 install -U transformers
# !pip3 install -U datasets
# !pip3 install -U seaborn
# !pip3 install -U bertviz
# !pip3 install -U umap-learn

from datasets import load_dataset

dataset = load_dataset('dair-ai/emotion')
