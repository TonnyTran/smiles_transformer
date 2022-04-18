# SMILES Transformer

## Requirements
This project requires the following libraries.
- Python3
- PyTorch > 1.2 # pip install torch
- NumPy # pip install numpy
- Pandas # pip install pandas
- tqdm # pip install tqdm
- RDKit # python -m pip install rdkit-pypi
- matplotlib # pip install matplotlib
- sklearn # pip install sklearn
- jupyter notebook # pip install notebook

## Dataset
Dataset for pretrain:
- Chembl24

Datasets for classification evaluation: (stored in folder `dataset`)
- HIV
- BBBP
- BACE

## 1. Data preparation
1. Download Chembl24 dataset and store it into `data` folder [Download here](https://drive.google.com/file/d/18aGDny6FQd7hNwK-0uV6mSH98JRa846-/view?usp=sharing)
2. Run `prepare_data.py`
```
$ python prepare_data.py 
```

## 2. Pre-training
After preparing the SMILES corpus for pre-training, run:

```
$ python pretrain_trfm.py --gpu 0 # pretrain smiles transformer model (Training process takes 7-10 hours)
$ python pretrain_rnn.py --gpu 0  # pretrain rnn model (Training process takes 20-25 hours)
```

Pre-trained models are stored in folder `pretrained_model`

## 3. Downstream Tasks
Run notebook in 3 files corresponding to 3 dataset
- `exp - HIV.ipynb` - experiment on HIV dataset
- `exp - BACE.ipynb` - experiment on BACE dataset
- `exp - BBBP.ipynb` - experiment on BBBP dataset

Note: you can generate directly the classification results using saved pretrained models. 