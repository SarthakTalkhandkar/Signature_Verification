from src.train import train

if __name__ == "__main__":
    print("🚀 Starting Training...")
    
    train()
    
    print("✅ Training Completed!")

# from src.verify import verify_signature


# def test_case(img1, img2, case_name):
#     print(f"\n🔹 {case_name}")

#     score = verify_signature(img1, img2)

#     print("Similarity Score:", score)

#     if score > 0.5:
#         print("Prediction: ✅ Genuine")
#     else:
#         print("Prediction: ❌ Forged")


# if __name__ == "__main__":

#     # ✅ Test 1: Genuine (same person)
#     test_case(
#         "data/CEDAR/CEDAR/1/original_1_1.png",
#         "data/CEDAR/CEDAR/1/original_1_2.png",
#         "Test 1: Genuine (Same Person)"
#     )

#     # ❌ Test 2: Forgery
#     test_case(
#         "data/CEDAR/CEDAR/1/original_1_1.png",
#         "data/CEDAR/CEDAR/1/forgeries_1_1.png",
#         "Test 2: Forged Signature"
#     )

#     # ❌ Test 3: Different person
#     test_case(
#         "data/CEDAR/CEDAR/1/original_1_1.png",
#         "data/CEDAR/CEDAR/2/original_2_1.png",
#         "Test 3: Different Person"
#     )