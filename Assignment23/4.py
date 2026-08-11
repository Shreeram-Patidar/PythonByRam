"""
Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data
"""
text=input("Enter text: ")
text=text.split()
final=""
for word in text: 
    if word not in final:
       final=final+word+" "
    else:
       count=final.count(word)
       final+=f'{word}({count}) '
print(final)


