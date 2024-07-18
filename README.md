# Kaggle_Happywhale Whale and Dolphin Identification
In this competition, you’ll develop a model to match individual whales and dolphins by unique—but often subtle—characteristics of their natural markings. You'll pay particular attention to dorsal fins and lateral body views in image sets from a multi-species dataset built by 28 research institutions. The best submissions will suggest photo-ID solutions that are fast and accurate.

### Preparation and Process

1. **Data Loading and Preprocessing**:
   - Load whale and dolphin images from Kaggle dataset.
   - Resize images to 512x512 pixels, standardize pixel values, and apply data augmentation techniques.
   - Encode labels using `LabelEncoder` and convert to one-hot encoding.

2. **Feature Extraction with EfficientNet**:
   - Use EfficientNet as a feature extractor with pre-trained weights.
   - Remove the top layers and add custom layers for classification.

3. **Training the Model**:
   - Train the model on TPU using Adam optimizer and ArcFace loss.
   - Evaluate performance on validation data.

4. **Prediction with KNN**:
   - Extract features from test images using trained EfficientNet model.
   - Train KNN on training features and predict test features' categories.

5. **Evaluation and Submission**:
   - Evaluate model performance on validation data.
   - Generate CSV file with test predictions for Kaggle submission.

## Citation:
If you find this code is useful in your research, please consider to cite:

    @misc{happy-whale-and-dolphin,
        author = {Ted Cheeseman, Ken Southerland, Walter Reade, Addison Howard},
        title = {Happywhale - Whale and Dolphin Identification},
        publisher = {Kaggle},
        year = {2022},
        url = {https://kaggle.com/competitions/happy-whale-and-dolphin}
    }