# 只是用来查看pkl 的

import pickle
path= '''SUMLL/show_pkl/nnUNetPlansv2.1_plans_3D.pkl'''
  #path='/root/……/aus_openface.pkl'   pkl文件所在路径
	   
f=open(path,'rb')
data=pickle.load(f)
 
print(data)
print(len(data))
