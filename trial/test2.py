

words = ['before', 'was', 'was', 'was', 'was', 'was', 'is']
mat = {}

# assigning rows:
for i in range(len(words)-1):
    if not words[i] in mat:
        mat.update({f'{words[i]}' : None})
    else:
        continue

# assigning cols

col = True
i = 0





for i in range(len(words)-1):
    if not words[i] == words[i+1]:
        mat.update({f'{words[i]}' : {f'{words[i+1]}' : None}})
    else:
        try:
            if words[i+1] in mat[words[i]]:
                continue
        except KeyError as e:
            mat.update({f'{words[i]}' : {f'{words[i+1]}' : None}})
    # print(mat[words[i]])


# while(i<=len(words)):
#     if i < len(words)-1:
#         if words[i] == words[i+1]:
#             mat.update({f'{words[i]}' : {f'{words[i+1]}' : None}})
#             while words[i] == words[i+1]:
#                 i += 1
#         else:
#             mat.update({f'{words[i]}' : {f'{words[i+1]}' : None}})
#     else:
#         continue
    
#     i += 1


# for i in range(len(words)):
#     if i < len(words)-1:
#         if words[i] == words[i+1]:
#             mat.update({f'{words[i]}' : {f'{words[i+1]}' : None}})
#             if mat[words[i]] is None:
        # print(words[i], words[i+1])

# for i in range(len(words)):
#     if i < len(words)-1:
#         mat.update({f'{words[i]}':{f'{words[i+1]}' : None}})

print(mat)

