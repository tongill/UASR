

CUDA_VISIBLE_DEVICES=0 \ python train.py \ 
  --model vrp_sam_dino_uncertainty_graph_deterministic_contrastive \
  --config configs/unicl_sam/vrp_sam_dinov2_large_vitdet_fpn_uncertainty.yaml \
  --input_size 518 \ 
  --batch_size 2 \ --epochs 40 \ --accum_iter 1 \ 
  --samples_num 1 \ --num_workers 4 \ 
  --output_dir ./output_train \ 
  --warmup_epochs 4 \ --blr 0.0001 \ --device cuda


