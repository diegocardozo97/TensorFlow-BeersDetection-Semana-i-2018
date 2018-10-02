$export PYTHONPATH=$PYTHONPATH:$YOUR_PATH_HERE/TensorFlow-BeersDetection-Semana-i-2018:$YOUR_PATH_HERE/TensorFlow-BeersDetection-Semana-i-2018/research:$YOUR_PATH_HERE/TensorFlow-BeersDetection-Semana-i-2018/research/slim

python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
