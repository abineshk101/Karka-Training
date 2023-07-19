mark_list=[{"name":"Abinesh","sslc":{"tamil":80,"english":90,"maths":91,"science":88,"social":100}},
           {"name":"Dhanraj","sslc":{"tamil":99,"english":77,"maths":99,"science":80,"social":100}},
           {"name":"Dhanush","sslc":{"tamil":100,"english":89,"maths":77,"science":96,"social":91}},
           {"name":"Bhuvanesh","sslc":{"tamil":88,"english":88,"maths":100,"science":88,"social":90}},
           {"name":"Gowtham","sslc":{"tamil":71,"english":99,"maths":88,"science":79,"social":89}}]

for detail in mark_list:
    total=0
    for marks in detail["sslc"]:
        total=detail["sslc"][marks]+total
    percentage=(total/500)*100
    print("Name:",detail["name"] ,f"\t The total is: {total}\tThe percentage is:{percentage}")
    if percentage>90 or percentage>75 and detail["sslc"]["maths"]>=98:
        print("\tYou are eligible for biology and computer")
    elif percentage>80 or percentage>70 and detail["sslc"]["maths"]>=98 :
         print("\tYou are eligible for computer only")