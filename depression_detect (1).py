import pickle
import numpy as np
# import warnings
# warnings.warn('warnings.warn(')
with open('Depression_Model.pkl', 'rb') as file:
    Pickled_LR_Model = pickle.load(file)
# print(Pickled_LR_Model)
# a = np.array([1,5,0,1,1,0,1,0],ndmin=2)
# print(Pickled_LR_Model.predict(a))
print('\n Start of questions')
print('---------------------------')
print('Is there anyone in your life who can support you and be there for you?')
print('Type \n1.Yes \n0.No')
a = int(input())
print('How were you feeling lately?')
print('Type \n1.Overwhelmed 2.Satisfied 3.Confused 4.Disappointed 5.Frustrated')
b = int(input())
print('Have you been sleeping well?')
print('Type \n1.Yes \n0.No')
e=int(input())
print('Have you been feeling like you have a good support system in place?')
print('Type \n1.Yes \n0.No')
f=int(input())
print('Are you having any thoughts of self-harm or suicide?')
print('Type \n1.Yes \n0.No')
g=int(input())
print('How do you usually handle stress and negative emotions?')
print('Type \n1.Parents 2.Music 3.Sleep 4.Myself 5.Motivational videos')
h=int(input())
print('Have you talked to anyone about how you are feeling?')
print('Type \n1.Yes \n0.No')
i=int(input())
print('With whom do you share your feelings? ')
print('Type \n1.Family 2.Friends 3.No one ')
j=int(input())
result = np.array([a,b,c,d,e,f,g,i],ndmin=2)
# resultt = result[0]
resultt = Pickled_LR_Model.predict(result)
# if result==
# print(Pickled_LR_Model.predict(result))
if resultt==0:
    print('Major Depression')
elif resultt==1:
    print('Minor Depression')
elif resultt == 2:
    print('No Depression')
