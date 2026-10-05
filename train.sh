

CUDA_VISIBLE_DEVICES=0 \ python train.py \ 
  --model dynamic_gaussian_graph \
  --config configs/UASR/uncertainty_dinov2_fpn.yaml \
  --batch_size 2 \ --epochs 40 \ --accum_iter 1 \ 
  --samples_num 1 \ --num_workers 4 \ 
  --output_dir ./results_train \ 
  --warmup_epochs 4 \ --blr 0.0001 \ --device cuda


