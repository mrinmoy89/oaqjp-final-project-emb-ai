from EmotionDetection import emotion_detector

def test_emotion_detection():
    
    # Test cases
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for text, expected_emotion in test_cases:
        result = emotion_detector(text)
        dominant_emotion = result["dominant_emotion"]

        print(f"Text: {text}")
        print(f"Expected: {expected_emotion}, Got: {dominant_emotion}")

        assert dominant_emotion == expected_emotion, f"Test failed for: {text}"

    print("\nAll tests passed!")

# Run tests
if __name__ == "__main__":
    test_emotion_detection()
