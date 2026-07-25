import pickle

model = pickle.load(open("ridge.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

temp = float(input("Temperature: "))
rh = float(input("RH: "))
ws = float(input("Wind Speed: "))
rain = float(input("Rainfall: "))
ffmc = float(input("FFMC: "))
dmc = float(input("DMC: "))
isi = float(input("ISI: "))
classes = int(input("Classes (0=Not Fire, 1=Fire): "))
region = int(input("Region (0=Bejaia, 1=Sidi-Bel Abbes): "))

sample = [[
    temp,
    rh,
    ws,
    rain,
    ffmc,
    dmc,
    isi,
    classes,
    region
]]

sample_scaled = scaler.transform(sample)

prediction = model.predict(sample_scaled)

print(f"\nPredicted FWI: {prediction[0]:.2f}")