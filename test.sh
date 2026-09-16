

CUDA_VISIBLE_DEVICES=0 python /root/autodl-tmp/UASR-main/test.py     
-cfg ./checkpoint.pth    
-d fss1000     -s 518     -b 4     
-val "test_splits-test"     -n 1



