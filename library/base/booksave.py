from .serializers import BookSerializer
def BookSave(items):
    print(len(items))
    for i in items:
        authors=i["volumeInfo"]["authors"].copy()
        mydata={
            "external_id": i["id"],
            "title": i["volumeInfo"]["title"],
            "authors": authors,
            "acquired": False,
            "published_year": i["volumeInfo"]["publishedDate"],
            "thumbnail": i["volumeInfo"]["imageLinks"]["thumbnail"]
        }
        serializer = BookSerializer(data=mydata)
        if serializer.is_valid():
            serializer.save()
