import re

text="""[locale: "zh"
description: "2\n3\n4\n5\n6\n7\n1\n14\n16\n17\n.\344\272\206\n"
bounding_poly {
  vertices {
    x: 721
    y: 366
  }
  vertices {
    x: 3307
    y: 366
  }
  vertices {
    x: 3307
    y: 516
  }
  vertices {
    x: 721
    y: 516
  }
}
, description: "2"
bounding_poly {
  vertices {
    x: 816
    y: 366
  }
  vertices {
    x: 855
    y: 366
  }
  vertices {
    x: 855
    y: 411
  }
  vertices {
    x: 816
    y: 411
  }
}
, description: "3"
bounding_poly {
  vertices {
    x: 878
    y: 394
  }
  vertices {
    x: 912
    y: 394
  }
  vertices {
    x: 912
    y: 441
  }
  vertices {
    x: 878
    y: 441
  }
}
, description: "4"
bounding_poly {
  vertices {
    x: 1153
    y: 369
  }
  vertices {
    x: 1192
    y: 369
  }
  vertices {
    x: 1192
    y: 413
  }
  vertices {
    x: 1153
    y: 413
  }
}
, description: "5"
bounding_poly {
  vertices {
    x: 1213
    y: 397
  }
  vertices {
    x: 1248
    y: 397
  }
  vertices {
    x: 1248
    y: 444
  }
  vertices {
    x: 1213
    y: 444
  }
}
, description: "6"
bounding_poly {
  vertices {
    x: 1493
    y: 374
  }
  vertices {
    x: 1525
    y: 374
  }
  vertices {
    x: 1525
    y: 418
  }
  vertices {
    x: 1493
    y: 418
  }
}
, description: "7"
bounding_poly {
  vertices {
    x: 1549
    y: 402
  }
  vertices {
    x: 1579
    y: 403
  }
  vertices {
    x: 1577
    y: 446
  }
  vertices {
    x: 1547
    y: 445
  }
}
, description: "1"
bounding_poly {
  vertices {
    x: 2103
    y: 381
  }
  vertices {
    x: 2137
    y: 381
  }
  vertices {
    x: 2137
    y: 426
  }
  vertices {
    x: 2103
    y: 426
  }
}
, description: "14"
bounding_poly {
  vertices {
    x: 2856
    y: 394
  }
  vertices {
    x: 2928
    y: 388
  }
  vertices {
    x: 2931
    y: 427
  }
  vertices {
    x: 2859
    y: 433
  }
}
, description: "16"
bounding_poly {
  vertices {
    x: 3160
    y: 395
  }
  vertices {
    x: 3232
    y: 389
  }
  vertices {
    x: 3236
    y: 437
  }
  vertices {
    x: 3164
    y: 443
  }
}
, description: "17"
bounding_poly {
  vertices {
    x: 3242
    y: 420
  }
  vertices {
    x: 3306
    y: 423
  }
  vertices {
    x: 3304
    y: 469
  }
  vertices {
    x: 3240
    y: 466
  }
}
, description: "."
bounding_poly {
  vertices {
    x: 721
    y: 451
  }
  vertices {
    x: 739
    y: 450
  }
  vertices {
    x: 739
    y: 458
  }
  vertices {
    x: 721
    y: 459
  }
}
, description: "\344\272\206"
bounding_poly {
  vertices {
    x: 737
    y: 451
  }
  vertices {
    x: 830
    y: 447
  }
  vertices {
    x: 833
    y: 511
  }
  vertices {
    x: 740
    y: 515
  }
}
]
"""
############## To get the description from the JSON output #############
text_description=[]
for i in text.splitlines():
    if 'description' in i:
        #print (len(i))
        num1=re.findall(r'"([^"]*)"', i)
        text_description.append(num1)
print (text_description)

#print (len(text_description))

############## To get the vertices from the JSON output #############
ver=re.finditer('vertices',text)
#print (ver)
count=0
ver_list=[]
for i in ver:
    ver_list.append((i.start(),i.end()))
    count=count+1
#print ('Count is ',count)
                    
#print(ver_list)

abc=[(76, 84), (115, 123), (155, 163), (195, 203),(271, 279), (310, 318), (349, 357), (388, 396)]
ver_list1=[]
ver_list2=[]

text_boundary_box=[]
                   
for num,data in enumerate(ver_list):
    if num%2==0:
        ver_list1.append((ver_list[num],ver_list[num+1]))
        #ver_list1_count=ver_list1_count+1
#print ('ver_list1 ',ver_list1)
ver_list1_count=0 
for num,i in enumerate(ver_list1):
    #print('##### i[0][1] and i[0][1] #########' )
    #print (i[0][1],' ',i[1][1])
    text_extracted=text[i[0][1]:i[1][1]]
    needed_text=re.findall(r'\d+',text_extracted)
    #print (needed_text)
    ver_list2.append(needed_text)
    ver_list1_count=ver_list1_count+1
    if ver_list1_count%2==0:
        text_boundary_box.append(ver_list2)
        ver_list2=[]

print ('############ Text text_boundary_box ###########')
print (text_boundary_box)
print ('Legnth of text_boundary_box is: ',len(text_boundary_box))
print ('############ Description text_boundary_box ###########')
print (text_description)
print ('Legnth of text_description is: ',len(text_description))

text_desc_bounding_box={}
for i in range(0,len(text_description)):
    if i!=0 :
        #print(text_description[i])
        #print (text_boundary_box[i])
        text_desc_bounding_box[str(text_description[i])]=text_boundary_box[i]
#print (text_desc_bounding_box)


###### Object detection #####
'''
object_bound_list=[ ((427, 143), (593, 268)),
 ((329, 247), (482, 400)),
   ((9, 61), (197, 252)),
  ((179, 66), (350, 245)) ,
((264, 68), (431, 249)) ,
((312, 70), (498, 257)) ,
((864, 67), (999, 256)) ,
((878, 251), (999, 412)),
((0, 258), (135, 475)) , 
((163, 243), (331, 466)),
((641, 259), (851, 451))
    ]
'''
object_bound_list=[
((660, 387), (1065, 681)) ,
((3075, 410), (3301, 650)),
((548, 514), (1175, 732)), 
((1392, 467), (1882, 789))
]
#cv2.rectangle(img,(816, 366),(855, 411),(255,0,0),4)
import cv2
img=cv2.imread('test.jpg')
cv2.namedWindow("output", cv2.WINDOW_NORMAL)   
for key,value in text_desc_bounding_box.items():
    #print (value[0], '  ',value[1])
    cv2.rectangle(img,(int(value[0][0]),int(value[0][1]))  ,  (int(value[1][0]),int(value[1][1])) , (255,0,0),2 )
for i in object_bound_list:
     cv2.rectangle(img,(int(i[0][0]),int(i[0][1]))  ,  (int(i[1][0]),int(i[1][1])) , (255,0,0),2 )
cv2.imshow('output',img)

################## To check the overlap ########################################
def dooverlap(l1,r1,l2,r2):
    if (l1[0] > r2[0] or l2[0] > r1[0]):
        return False
    if (l1[1] > r2[1] or l2[1] > r1[1]):
        return False
    return True
l1=(816, 366)
r1=(855, 411)
l2=(660, 387)
r2=(1065, 681)  
#print (dooverlap(l1,r1,l2,r2))
#816,366,855,411

'''
object_bound_dict={'((427, 143), (593, 268))': 'Empty',
 '((329, 247), (482, 400))': 'Empty',
 '((9, 61), (197, 252))': 'occupied',
 '((179, 66), (350, 245))': 'occupied',
 '((264, 68), (431, 249))': 'Empty',
 '((312, 70), (498, 257))': 'occupied',
 '((864, 67), (999, 256))': 'occupied',
 '((878, 251), (999, 412))': 'Empty',
 '((0, 258), (135, 475))':  'occupied',
 '((163, 243), (331, 466))': 'occupied',
 '((641, 259), (851, 451))': 'occupied'
 }
'''
object_bound_dict={
'((660, 387), (1065, 681))' : 'Empty', 
'((3075, 410), (3301, 650))': 'Empty',
'((548, 514), (1175, 732))' : 'Empty',
'((1392, 467), (1882, 789))':'Empty'
}
def same_axes(l1,r1,l2,r2):
    if (l1[0]>l2[0] and l1[1]<l2[1]) and ( r1[0]<r2[0] and r1[1]<r2[1]):
        return True
text_bound_box=[]#To store the overlap and same axes text and bound box
for key,value in text_desc_bounding_box.items():
    #if key=="['2']":
    for i in range(0,len(object_bound_list)):
        #print (object_bound_list[0][0])
        l2=object_bound_list[i][0]
        #print (l2)
        r2=object_bound_list[i][1]
        #print (r2)
        l1=((int(value[0][0]),int(value[0][1])))
        #print (l1)
        r1=(int(value[1][0]),int(value[1][1]))
        if dooverlap(l1,r1,l2,r2):
            print ('Overlap ',key,' ',object_bound_list[i])
            #print (key,' ',object_bound_dict[str(object_bound_list[i])])
            text_bound_box.append(('O',key,object_bound_list[i]))
        if same_axes(l1,r1,l2,r2):
            print ('Same axis ',key,' ',object_bound_list[i])
            text_bound_box.append(('S',key,object_bound_list[i]))
#print (text_bound_box)
#print ('Count is ',len(text_bound_box))
########## To get the unique values ###########
def unique(list_value):
    unique_values=[]
    for i in list_value:
        if i not in unique_values:
            unique_values.append(i)
    return unique_values
#print (unique(text_bound_box))
#print ('Count is ',len(unique(text_bound_box)))

######## To get the text and corresponding label value
Text_and_object_bounding_box=[]#TO store the text and  object bounding box values
textdesc_axis_label_objbndbox=[]


top_bottom=[]# text with object bounding box co ordinates
for i in unique(text_bound_box):
    text_desc=re.findall(r'\w+',i[1])
    #print (object_bound_dict[str(i[1])])
    print (text_desc,'  ' ,i[0],' ',object_bound_dict[str(i[2])],' ',i[2])
    textdesc_axis_label_objbndbox.append((text_desc,i[0],object_bound_dict[str(i[2])],i[2]))
    top_bottom.append((text_desc,i[2]))

############## print text boundary box ############
#print (text_desc_bounding_box)
print (top_bottom)

########################################################################
######## To get the bounding boxes co ordinates that are existing in the same axis ###########

top_bottom_list=[]# To store the top and bottom bounding box
def bounding_box_same_axes(l1,r1,l2,r2):
    if l1[0]<l2[0] and l1[1]<l2[1] and r1[0]<r2[0] and r1[1]<r2[1]:
        #print (1)
        top_bottom_list.append(((l1,r1),'top'))
        top_bottom_list.append(((l2,r2),'bottom'))
        
        
    #elif l1[0]<l2[0] and l1[1]<l2[1] and r1[0]>r2[0] and r1[1]<r2[1]:
    #print (2)
    #elif l1[0]>l2[0] and l1[1]<l2[1] and r2[0]>r1[0] and r1[1]<r2[1]:
    #print (3)
    else:
        print ('not in same axis')
#To get the top and bottom object bounding box 
for num,data in enumerate(top_bottom):
    if num!=0:
        #If same text consists of two bounding box
        if top_bottom[num-1][0]==top_bottom[num][0]:
            print (num-1,' ',num)
            print (top_bottom[num][1][0])
            print (top_bottom[num][1][1])
            bounding_box_same_axes(top_bottom[num-1][1][0],top_bottom[num-1][1][1],
                                   top_bottom[num][1][0],top_bottom[num][1][1])

print (top_bottom_list)
print (unique(top_bottom_list))

print (text_desc_bounding_box)


filtered_text_list=[]

def filter_text(top_bottom): 
    for i in top_bottom:
        if  re.findall('X',str(i[0])):
            pass
        else:
            filtered_text_list.append(i)
filter_text(top_bottom)
print ('######## filtered_text_list ########')
print (filtered_text_list)    
print ('####To get the left and right text bounding box ######')
def left_or_right(l1,r1,l2,r2):
    if int(l1[0])<int(l2[0]) and int(r1[0])<int(r2[0]):
        print ('Left')
        return 'Left'
    else:
        print ('Right')
        return 'Right'
left_or_right_list=[]    
i_num=0
for i in range(0,len(filtered_text_list)):
    
    j_num=i_num+1
    for j in range(0,len(filtered_text_list)):
        if j_num<=len(filtered_text_list)-1:
            if filtered_text_list[i_num][1]==filtered_text_list[j_num][1]:
                   print (filtered_text_list[i_num][0],'  ',filtered_text_list[j_num][0])
                   print ('i_num :',i_num,'  ','j_num: ',j_num)
                   b1=text_desc_bounding_box[str(filtered_text_list[i_num][0])]
                   b2=text_desc_bounding_box[str(filtered_text_list[j_num][0])]
                   print (b1)
                   print (b2)
                   if left_or_right(b1[0],b1[1],b2[0],b2[1])=='Left':
                       left_or_right_list.append((filtered_text_list[i_num][0],'Left'))
                       left_or_right_list.append((filtered_text_list[j_num][0],'Right'))
                   else:
                       left_or_right_list.append((filtered_text_list[j_num][0],'Left'))
                       left_or_right_list.append((filtered_text_list[i_num][0],'Right'))
                       
                   print ('#####')
            j_num=j_num+1
        if j_num==len(filtered_text_list):
            pass
            #print ('Something')
    i_num=i_num+1
    #print ('Single for loop end ',i_num)

#print (text_desc_bounding_box)


print ('######################################################################')
#print(unique(left_or_right_list))
#print (unique(top_bottom_list))
list1=unique(left_or_right_list)
list2=unique(top_bottom_list)
topbottom_leftright={}

for i in list1:
    topbottom_leftright[str(i[0])]=i[1]
for i in list2:
    topbottom_leftright[str(i[0])]=i[1]
    
print (textdesc_axis_label_objbndbox)
print (topbottom_leftright)


final_text_obj=[]
for i in textdesc_axis_label_objbndbox:
    try:
        if topbottom_leftright[str(i[0])] and topbottom_leftright[str(i[3])]:
            final_text_obj.append((i[0],i[2],i[3],topbottom_leftright[str(i[0])],topbottom_leftright[str(i[3])]))
    except KeyError:
            pass
            
print(final_text_obj)

###### Generating the report
import csv
final_text_obj_dict={}
for data in final_text_obj:
    if data[3]=='Left' and data[4]=='top':
        #wr.writerow(zip(data[0],data[1]))
        final_text_obj_dict[str(data[0])]=data[1]
        print (data[0],data[1])
    if data[3]=='Right' and data[4]=='bottom':
        #wr.writerow(zip(data[0],data[1]))
        print (data[0],data[1])
        final_text_obj_dict[str(data[0])]=data[1]

keyList1 = final_text_obj_dict.keys()
valueList1 = final_text_obj_dict.values()
rows = zip(keyList1,valueList1 )
with open('report.csv','w+') as f:
    writer = csv.writer(f)
    for row in rows:
         writer.writerow(row)

