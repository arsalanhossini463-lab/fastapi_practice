from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

mylist = [10, 20, 30, 40, 50, 60]


@app.get("/")
def get_index():
    return {"Hellp": "Python"}

@app.get("/home/")
def get_index():
    return {"Welcome": "Home"}

@app.get("/getitem/")
def get_all_item():
    return {"Mylist": mylist}


@app.post("/add/{new_item}")
def add_item(new_item: int):
    mylist.append(new_item)
    return {"new mylist" : mylist}


@app.post("/addindex/")
def add_item_by_index(index:int, newitem:int):
    if index < len(mylist):
        mylist.insert(index, newitem)
        return {"new mylist" : mylist}
    else:
        return ("Index out of range")


@app.delete("/deleteitem/")
def delete_item(item:int):
    if item in mylist:
        mylist.remove(item)
        return(f"{item} Removed from mylist")
    else:
        return(f"{item} Not Found")


@app.delete("/deleteindex/")
def delete_item(index:int = -1):
    if len(mylist) > 0 and index < len(mylist):
        mylist.pop(index)
        return {"new mylist" : mylist}
    else:
        return("index out of range")

@app.put("/update/")
def update_item(old_item:int, new_item:int):
    if old_item in mylist:
        index = mylist.index(old_item)
        mylist[index] = new_item
        return (f"{old_item} Replaced by {new_item}")
    else:
        return(f"{old_item} Not Found")


@app.put("/updateindex/")
def update_item(index:int, new_item:int):
    if index < len(mylist):
        mylist[index] = new_item
        return (f"Index{index} Replaced by {new_item}")
    else:
        return(f"Index Not Found")
        
             

