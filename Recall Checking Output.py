import glob, random, csv,re


# sets filepath for where to extract files from (parsed corpus)
path = 'C:/Users/brett/Desktop/Language Data/Parsed Longman Corpus Sample/*'
outfolder = 'C:/Users/brett/Desktop/dr egbert work/the grammar project/Stuff for accuracy checkers/'


# randomly selects twenty texts for recall checking

# creates the list from which it will randomly draw
filelist = []
for files in glob.glob(path):
    filelist.append(files)

# generates the names of the random files to sample
random_20 = random.sample(filelist,10)

# checks the files to see if they are in the list of files to sample from
# if the file is in the list, then it copies it to the outputfolder
for files in glob.glob(path):

    if files in random_20:
        # creates the outfile
        file = re.sub('C:/Users/brett/Desktop/Language Data/Parsed Longman Corpus Sample\\\\','',files)
        file = re.sub('.txt|.TXT','',file)
        fileout = outfolder + file + '.csv'
        fileout = open(fileout, 'w+')
        # enables the writer to work on a csv
        wr = csv.writer(fileout, dialect='excel', lineterminator='\n')
        # reads in the infile by lines
        with open(files, encoding = 'utf-8', errors = 'ignore') as sample:
            lines = sample.readlines()
            # splits up each element in the list into words, tags, and tags
            for line in lines:
                line = line.split(' ^')
                # writes it to the out csv
                wr.writerow(line)
                print(line)
        # shutil.copy(files,outfolder)