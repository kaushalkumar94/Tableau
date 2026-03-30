import kagglehub

# Download latest version
path = kagglehub.dataset_download("alexanderfreberg/airbnb-listings-2016-dataset")

print("Path to dataset files:", path)
