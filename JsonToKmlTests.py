from JsonToKml import JsonToKml

def main():
    # Verify if program works correctly
    for i in range(1, 6):
        JsonToKml(f"traj{i}.json")
        # Display success message
        print(f"traj{i}.json a été converti avec succès !")

if __name__ == "__main__":
    main()
