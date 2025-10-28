from concrete import fhe

# Define FHE function for BMI calculation
@fhe.compiler({"weight": "encrypted", "height": "encrypted"})
def encrypted_bmi(weight, height):
    return weight / (height * height)

# Compile and save model
def build_model():
    inputset = [(70, 1.75), (80, 1.8), (60, 1.6)]
    compiler = encrypted_bmi.compile(inputset)
    compiler.save("bmi_fhe.zip")
    print("FHE model built and saved!")

if __name__ == "__main__":
    build_model()
