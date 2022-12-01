from taa.search_and_augment import search_and_augment

# return the augmented train dataset in the form of torch.utils.data.Dataset
augmented_train_dataset = search_and_augment(configfile="./taa/confs/bert_imdb_example.yaml")