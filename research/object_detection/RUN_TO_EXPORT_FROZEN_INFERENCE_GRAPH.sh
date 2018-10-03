$export PYTHONPATH=$PYTHONPATH:$YOUR_PATH_HERE/TensorFlow-BeersDetection-Semana-i-2018:$YOUR_PATH_HERE/TensorFlow-BeersDetection-Semana-i-2018/research:$YOUR_PATH_HERE/TensorFlow-BeersDetection-Semana-i-2018/research/slim

python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-LAST_CHECKPOINT --output_directory inference_graph
