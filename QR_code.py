import qrcode

cool=True
while cool:
    qr_url=input("Paste Link Here to get started: ")
    qr_name=input("QR Code filename")
    qr_format=input("File Format(jpg,jpeg,img,png): ")
    categories=["file","link"]
    recap=[qr_url,qr_format+qr_name]
    print("Review:")
    for cat_name,rec_name in categories,recap:
        print(cat_name," : ",rec_name)
    check=input("Is everything correct?")
    if check == "no":
        print("What do you need to edit?")
        print("Link? Filename? File format?")
        px={"Link":qr_url,"Filename":qr_name,"File format":qr_format}
        problem=input("- ")
        correction=input("Enter correct value:")
        new={problem:correction}
        px.update(new)
        print(new)
        res=input("Correct? :")
        if res=="yes":
            break
        else:
            continue
    else:        
        break
print("Creating")
img =qrcode.make(qr_url)
type(img)
img.save(qr_name+"."+qr_format)
print("Complete!!")