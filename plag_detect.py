import re

def plag_detect(t1, t2):
   L = [[0] * (1 + len(t2)) for i in range(1 + len(t1))]
   len_match, x_len_match = 0, 0
   for x in range(1, 1 + len(t1)):
       for y in range(1, 1 + len(t2)):
           if t1[x - 1] == t2[y - 1]:
               L[x][y] = L[x - 1][y - 1] + 1
               if L[x][y] > len_match:
                   len_match = L[x][y]
                   x_len_match = x
           else:
               L[x][y] = 0
   return t1[x_len_match - len_match: x_len_match]

def create_measures(tunes):
    measures = []
    for i in tunes:
        measures.append(re.split(r'(?<=\|\s)', i))
    return measures
        
 
if __name__ == "__main__":
    
    source = open("data_v2_withtitles_ONeillsJigs", "r") #SourceFile
    destination = open("rmsprop_samples_b4_50","r") #DestinationFile

    all_tunes_source_temp = source.readlines()
    all_tunes_destination = destination.readlines()

    all_tunes_source = []

    for i in all_tunes_source_temp:
        all_tunes_source.append(i[:-1])

    measures_source = create_measures(all_tunes_source)
    measures_destination = create_measures(all_tunes_destination)

    count = 0

    
    for i in measures_source:
        for j in measures_destination:
            matched_sequence = plag_detect(i,j[:-1])
            if len(matched_sequence) >= 1:
                count = count+1
                print("Source Tune : ")
                print(i)
                print("Destination Tune: ")
                print(j[:-1])
                print("Matched Sequence:")
                print(matched_sequence)
                print(" ")
    
    print(count)



