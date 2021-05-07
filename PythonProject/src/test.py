import numpy as np
# x = (2,3)
# x[0] = 5
# print(x)


# y = np.arange(0,9).reshape(3,3)
# print(y)

# z = (y > 5) & (y < 8) # mask
# # # need to get indexes where z evaluates to true
# print(z)
# print(y[z])
# y[z] = 0 # threshold
# print(y)
# # print(y)
# # y[y > 5] = 0
# # print(y)




# def mask_applier(img, mins, maxs, curr_index):
#     if curr_index == len(mins):
#         return (img > 100 ) & (img < 100)

#     return (mins[curr_index] <= img) & (img <= maxs[curr_index]) | mask_applier(img, mins, maxs, curr_index+1)

def change_data(img):
    img[img > 3] = 0


img = np.arange(0,9).reshape(3,3)
change_data(img)
print(img)
# mask_mins = [2,5,5, 0, 15]
# mask_maxs = [3,5,7, 0, 12]
# curr_index = 0

# result = mask_applier(img ,mask_mins, mask_maxs, curr_index)
# indexes = np.where(result == True)
# print(img[indexes])

# x = []
# x.pop()
