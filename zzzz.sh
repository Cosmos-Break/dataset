python scripts/subword-nmt/subword_nmt/learn_joint_bpe_and_vocab.py --input data/task1/tok/train.lc.norm.tok.en data/task1/tok/train.lc.norm.tok.de -s 5000 -o codes --write-vocabulary vocab.en vocab.de

python scripts/subword-nmt/subword_nmt/apply_bpe.py -c codes --dropout 0.9 --vocabulary vocab.en --vocabulary-threshold 50 < data/task1/tok/train.lc.norm.tok.en > train.lc.norm.tok.bpe.en

python scripts/subword-nmt/subword_nmt/apply_bpe.py -c codes --dropout 0.01 --vocabulary vocab.en --vocabulary-threshold 50 < data/task1/tok/train.lc.norm.tok.en > train.lc.norm.tok.bpe.en

python scripts/subword-nmt/subword_nmt/apply_bpe.py -c codes --dropout 0.1 --vocabulary vocab.en < data/task1/tok/train.lc.norm.tok.en > train.lc.norm.tok.bpe.en