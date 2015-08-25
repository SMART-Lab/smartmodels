from smartmodels import rnn
from projects.timeSeries.run_script import *

def train_sequence_rnn():
    trainset, validset, testset = create_synthetic_datasets()

    model = create_model(rnn.RNN, trainset)
    optimizer = create_optimizer(model, trainset)
    trainer = create_trainer(model, optimizer, trainset, validset)
    training(trainer)


if __name__ == "__main__":
    train_sequence_rnn()
