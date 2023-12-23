import numpy as np

poses_arr = np.load(r'E:\GitHub\data\new\severe_blur_exp_clear\poses_bounds.npy')
exp_list = [-2,0,2]
exp_key=[0,1,1,1,2,0,0,1,1,1,
     2,2,1,1,1,1,1,0,1,1,
     0,1,1,1,2,2,1,1,1,1,
     0,1,1,2
     ]
exp=[]
for i in range(34):
    exp.append(exp_list[exp_key[i]])
exp_array = np.array(exp)

result_array = np.hstack((poses_arr, exp_array.reshape(-1, 1)))

print(result_array)

# np.save(r'E:\GitHub\data\new\severe_blur_exp_clear\poses_bounds_exp.npy',result_array)