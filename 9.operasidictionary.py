# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung" 
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get

print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("ipo", ("key tidak ditemukan"))) # cek key massage tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asek kesapek"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"teng":"siateng"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["teng"]
print(data_dict)
