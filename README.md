# Adaptive Bi-Encoder for Named Entity Recognition via Contrastive Learning

## Introduction
This is the repository for **ada-binder** - extended version of [**microsoft/binder**](https://openreview.net/forum?id=9EAQVEINuum).



## Reference

Check out [original microsoft/binder paper](https://openreview.net/forum?id=9EAQVEINuum) for the details. 

[Original microsoft/binder repository](https://github.com/microsoft/binder)


```bib
@article{zhang-etal-2022-binder,
  title={Optimizing Bi-Encoder for Named Entity Recognition via Contrastive Learning},
  author={Zhang, Sheng and Cheng, Hao and Gao, Jianfeng and Poon, Hoifung},
  journal={arXiv preprint arXiv:2208.14565},
  year={2022}
}
```


## Quick Start
### 1. Data Preparation

Follow the instructions [README.md](https://github.com/microsoft/binder/blob/main/data_preproc/README.md) in the data_preproc folder of original repository [microsoft/binder](https://github.com/microsoft/binder).


### 2. Environment Setup
```bash
conda create -n binder -y python=3.9
conda activate binder
conda install pytorch==1.13 pytorch-cuda=11.6 -c pytorch -c nvidia
pip install transformers==4.24.0 datasets==2.6.1 wandb==0.13.5 seqeval==1.2.2
```

### 3. Experiment Run
Assuming you have prepared data for [Nerel-BIO](https://github.com/nerel-ds/NEREL-BIO/tree/master) and finished environment setup, below is the command to run an experiment:
```bash
python run_ner.py conf/nerel-bio.json
```

To run experiments on other datasets, simply change the config.
