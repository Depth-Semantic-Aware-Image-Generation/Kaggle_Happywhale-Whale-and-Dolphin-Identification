import csv
import pandas as pd 

sub_files = [
                #'/kaggle/input/20230301rwz-mlhw1/pred.csv',
                '/kaggle/input/20230329rwz-mlhw/Vgg.csv',
                '/kaggle/input/20230329rwz-mlhw/Vgg13.csv',
                '/kaggle/input/20230329rwz-mlhw/resnet18.csv',
                '/kaggle/input/20230329rwz-mlhw2/cnn.csv',
                #'/kaggle/input/20230329rwz-mlhw3/submission.csv',
                '/kaggle/input/20230329rwz-mlhw4/submission (1).csv',
                '/kaggle/input/20230329rwz-mlhw4/submission.csv',
]

# Weights of the individual subs
sub_weight = [
                #0.81685**3,
                0.846**2,
                0.84066**2,
                0.86066**2,
                0.64466**9,
                #0.87333**3,
                0.794**6.5,
                0.77133**7,
            ]




Hlabel = 'Id' 
Htarget = 'Category'
npt = 1
place_weights = {}
for i in range(npt):
    place_weights[i] = (1 / (i + 1))

print(place_weights)

lg = len(sub_files)
sub = [None]*lg
for i, file in enumerate( sub_files ):   
    print("Reading {}: w={} - {}". format(i, sub_weight[i], file))
    reader = csv.DictReader(open(file,"r"))
    sub[i] = sorted(reader, key=lambda d: str(d[Hlabel]))

out = open("submission.csv", "w", newline='')
writer = csv.writer(out)
writer.writerow([Hlabel,Htarget])

for p, row in enumerate(sub[0]):
    target_weight = {}
    for s in range(lg):
        row1 = sub[s][p]
        for ind, trgt in enumerate(row1[Htarget].split(' ')):
            target_weight[trgt] = target_weight.get(trgt,0) + (place_weights[ind]*sub_weight[s])
    tops_trgt = sorted(target_weight, key=target_weight.get, reverse=True)[:npt]
    writer.writerow([row1[Hlabel], " ".join(tops_trgt)])
out.close()
