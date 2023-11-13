#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib> 
#include <ctime>

struct SecurityPersonnel {
    std::string name;
    std::string role;
    // Add other relevant details
};

struct SecurityCamera {
    std::string location;
    // Add other relevant details
};

struct SecurityIncident {
    std::string time;
    std::string location;
    std::string description;
    // Add other relevant details
};

struct VirtualCamera {
    std::string location;

    // Function to generate a random camera feed
    std::string generateCameraFeed() const {
        // Simulate a camera feed with random data
        return "Camera Feed from " + location + ": " + std::to_string(rand() % 100) + " people detected";
    }
};

class SecurityModule {
private:
    std::vector<SecurityPersonnel> personnelList;
    std::vector<SecurityCamera> cameraList;
    std::vector<SecurityIncident> incidentLog;
    std::vector<VirtualCamera> virtualCameraList;
public:
    // Function to add a virtual camera
    void addVirtualCamera(const VirtualCamera& camera) {
        virtualCameraList.push_back(camera);
        std::cout << "Virtual camera added successfully.\n";
    }

    // Function to display security personnel
    void displaySecurityPersonnel() const {
        std::cout << "Security Personnel:\n";
        for (const auto& personnel : personnelList) {
            std::cout << "Name: " << personnel.name << ", Role: " << personnel.role << "\n";
        }
        std::cout << "\n";
    }

    void displayAccessControl() {
        // Implement code to display access control information
    }

    // Function to display camera feeds
    void displayCameraFeeds() const {
        std::cout << "Camera Feeds:\n";
        for (const auto& camera : virtualCameraList) {
            std::cout << camera.generateCameraFeed() << "\n";
        }
        std::cout << "\n";
    }

    void displayIncidentList() {
        std::cout << "Incident Log:\n";
        for (const auto& incident : incidentLog) {
            std::cout << "Time: " << incident.time << ", Location: " << incident.location
                << ", Description: " << incident.description << "\n";
        }
        std::cout << "\n";
    }

    // Function to add security personnel
    void addSecurityPersonnel(const SecurityPersonnel& personnel) {
        personnelList.push_back(personnel);
        std::cout << "Security personnel added successfully.\n";
    }

    // Function to remove security personnel
    void removeSecurityPersonnel(const std::string& name) {
        auto it = std::remove_if(personnelList.begin(), personnelList.end(),
            [&name](const SecurityPersonnel& personnel) { return personnel.name == name; });

        if (it != personnelList.end()) {
            personnelList.erase(it, personnelList.end());
            std::cout << "Security personnel removed successfully.\n";
        }
        else {
            std::cout << "Security personnel not found.\n";
        }
    }

    void manageAccessControl() {
        // Implement code to manage access control
    }

    void addSecurityCamera(const SecurityCamera& camera) {
        cameraList.push_back(camera);
        std::cout << "Security camera added successfully.\n";
    }

    void viewIncidentLog() {
        displayIncidentList();
    }

    // Interface functions
    void saveSecurityPersonnelToFile() {
        std::ofstream file("security_personnel.txt");

        if (file.is_open()) {
            for (const auto& personnel : personnelList) {
                file << personnel.name << "," << personnel.role << "\n";
            }

            std::cout << "Security personnel data saved to file.\n";

            file.close();
        }
        else {
            std::cerr << "Error: Unable to open the file.\n";
        }
    }

    void loadSecurityPersonnelFromFile() {
        std::ifstream file("security_personnel.txt");

        if (file.is_open()) {
            personnelList.clear();

            std::string line;
            while (std::getline(file, line)) {
                size_t commaPos = line.find(',');
                if (commaPos != std::string::npos) {
                    SecurityPersonnel personnel;
                    personnel.name = line.substr(0, commaPos);
                    personnel.role = line.substr(commaPos + 1);
                    personnelList.push_back(personnel);
                }
            }

            std::cout << "Security personnel data loaded from file.\n";

            file.close();
        }
        else {
            std::cerr << "Error: Unable to open the file.\n";
        }
    }
};

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned>(std::time(0)));

    // List of predefined camera locations
    std::vector<std::string> cameraLocations = { "Entrance", "Lobby", "Hallway", "Conference Room", "Parking Lot" };

    // Instantiate the SecurityModule
    SecurityModule securitySystem;

    // Menu loop
    int choice;
    do {
        std::cout << "Menu:\n";
        std::cout << "1. Add Virtual Camera\n";
        std::cout << "2. Display Camera Feeds\n";
        std::cout << "3. Add Security Personnel\n";
        std::cout << "4. Remove Security Personnel\n";
        std::cout << "5. Display Security Personnel\n";
        std::cout << "6. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
        case 1: {
            // Add virtual camera
            std::cout << "Choose a location for the camera:\n";
            for (size_t i = 0; i < cameraLocations.size(); ++i) {
                std::cout << i + 1 << ". " << cameraLocations[i] << "\n";
            }

            int locationChoice;
            std::cout << "Enter the number corresponding to the location: ";
            std::cin >> locationChoice;

            if (locationChoice >= 1 && locationChoice <= static_cast<int>(cameraLocations.size())) {
                VirtualCamera newCamera = { cameraLocations[locationChoice - 1] };
                securitySystem.addVirtualCamera(newCamera);
            }
            else {
                std::cout << "Invalid location choice.\n";
            }
            break;
        }
        case 2:
            // Display camera feeds
            securitySystem.displayCameraFeeds();
            break;
        case 3: {
            // Add security personnel
            SecurityPersonnel newPersonnel;
            std::cout << "Enter personnel name: ";
            std::cin >> newPersonnel.name;
            std::cout << "Enter personnel role: ";
            std::cin >> newPersonnel.role;

            securitySystem.addSecurityPersonnel(newPersonnel);
            break;
        }
        case 4: {
            // Remove security personnel
            std::string personnelName;
            std::cout << "Enter the name of the personnel to remove: ";
            std::cin >> personnelName;

            securitySystem.removeSecurityPersonnel(personnelName);
            break;
        }
        case 5:
            // Display security personnel
            securitySystem.displaySecurityPersonnel();
            break;
        case 6:
            std::cout << "Exiting program.\n";
            break;
        default:
            std::cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 6);

    return 0;
}