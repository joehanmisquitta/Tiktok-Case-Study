text = open("C:/Users/joeha/OneDrive/Desktop/Google Data Science/Tiktok/tiktok_dataset.csv", 'r')
txtfile = open("C:/Users/joeha/OneDrive/Desktop/Google Data Science/Tiktok/tiktok_dataset_2.csv", 'a')

output = []

for line in text:
    output.append(line.split('\\n'))


for line in output:
    for i in line:
        #print(i)
        txtfile.write(i)
        txtfile.write(",\n")
