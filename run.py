from taa.search_and_augment import augment_with_presearched_policy

# return the augmented train dataset in the form of torch.utils.data.Dataset
augmented_train_dataset = augment_with_presearched_policy(configfile="./taa/confs/english_data.yaml")