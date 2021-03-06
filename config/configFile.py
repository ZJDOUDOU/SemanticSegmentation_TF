# Model
model_type                  = 'DenseNetFCN'
model_blocks                = 5               # Number of block densenetFCN_Custom only
model_layers                = 4               # Number of layers per block densenetFCN_Custom only
model_growth                = 12              # Growth rate per block (k) densenetFCN_Custom only
model_upsampling            = 'deconv'        # upsampling types available: 'upsampling' , 'subpixel', 'deconv'
model_dropout               = 0.0             # Dropout rate densenetFCN_Custom only
model_compression           = 0.0             # Compression rate for DenseNet densenetFCN_Custom only
pretrained_model			= False			  # True to use a pretrained model or restore experiment
load_model	                = 'tensorflow'    # Load model from 'tensorflow' or 'keras'
weight_only					= False
model_name                  = 'densenetFCN_Custom'
model_path                  = None #'/home/jlgomez/Repositories/TensorFlow/tensorflow_model/' # None uses experiment path by default if pretrained_model is True


# General parameters

train_samples               = 10
valid_samples				= 5
test_samples				= 5
train_batch_size            = 1
valid_batch_size            = 1
test_batch_size             = 1
train                       = True
validation                  = False
test                        = False
predict_test				= False	# True when you want only predictions without GT on test
predict_output				= None # None uses the default output in the experiment folder /predictions

# Image properties
size_image_train			= (960, 1280)
size_image_valid			= (960, 1280)
size_image_test				= (960, 1280)
resize_image_train          = (480, 640)
resize_image_valid          = (480, 640)
resize_image_test           = (480, 640)
crop_train					= (320, 320)
image_channels              = 3
grayscale                   = False

# Dataset properties
train_dataset_path          = '/home/jlgomez/Datasets/Audi_10classes/train/'
valid_dataset_path          = '/home/jlgomez/Datasets/Audi_10classes/valid/'
test_dataset_path			= '/home/jlgomez/Datasets/Audi_10classes/test/'
train_folder_names          = ['images/','masks/']
valid_folder_names			= ['images/','masks/']
test_folder_names			= ['images/','masks/']
labels						= ['person', 'car', 'truck', 'drivable', 'nondrivable', 'blocker', 
															'info', 'sky', 'buildings', 'nature'] 
num_classes                 = 10
shuffle                     = True
void_class                  = 10

#Training
epochs                      = 1
valid_samples_epoch			= 5
is_training                 = True
optimizer                   = 'adam'
learning_rate               = 0.0001
weight_decay				= 0.01
save_condition				= 'valid_mIoU'		  # ['always','(x)_loss','(x)_mAcc','(x)_mIoU'] x = train/valid
early_stopping 				= True
patience					= 5

# Image preprocess
rescale                     = 1/255.
mean                        = [0.37296272, 0.37296272, 0.37296272]
std                         = [0.21090189, 0.21090189, 0.21090189]

# Metrics


# TensorBoard
log_path					= 'logs/'