#include <iostream>
#include <vector>
#include <fstream>

class Hardware {
public:
    std::string name;
    int requiredProcessingSpeed;

    Hardware(const std::string& n, int speed) : name(n), requiredProcessingSpeed(speed) {}
};

class Rack {
private:
    std::vector<Hardware> hardwareList;
    int requiredPerformanceSpeed;  // Cumulative required performance speed based on added hardware

public:
    Rack() : requiredPerformanceSpeed(0) {}

    void addHardware(const Hardware& hardware) {
        hardwareList.push_back(hardware);
        requiredPerformanceSpeed += hardware.requiredProcessingSpeed;
    }

    void removeHardware() {
        if (!hardwareList.empty()) {
            requiredPerformanceSpeed -= hardwareList.back().requiredProcessingSpeed;
            hardwareList.pop_back();
            std::cout << "Hardware removed from the rack.\n";
        }
        else {
            std::cout << "No hardware to remove from the rack.\n";
        }
    }

    void displayHardware() const {
        std::cout << "Hardware in the rack:\n";
        for (const auto& hardware : hardwareList) {
            std::cout << hardware.name << " (Required Speed: " << hardware.requiredProcessingSpeed << ")\n";
        }
    }

    bool empty() const {
        return hardwareList.empty();
    }

    const Hardware& back() const {
        return hardwareList[size() - 1];
    }

    size_t size() const {
        return hardwareList.size();
    }

    int getRequiredPerformanceSpeed() const {
        return requiredPerformanceSpeed;
    }

    // Non-const version for non-const access
    std::vector<Hardware>& getHardwareList() {
        return hardwareList;
    }

    // Const version for const access
    const std::vector<Hardware>& getHardwareList() const {
        return hardwareList;
    }
};

class Server {
private:
    int processingSpeed; // Represents the processing speed of the server
    int temperature;     // Represents the temperature of the server
    std::vector<Rack> rackList;

public:
    Server(int initialSpeed, int initialTemp) : processingSpeed(initialSpeed), temperature(initialTemp) {
        // Assuming each server starts with 4 racks
        for (int i = 0; i < 4; ++i) {
            addRack();
        }
    }

    void adjustPerformance(int newSpeed) {
        processingSpeed = newSpeed;
        // Adjust temperature based on the new processing speed
        temperature = calculateNewTemperature();
    }

    void displayStatus() const {
        std::cout << "Server Performance: " << processingSpeed << "\n";
        std::cout << "Server Temperature: " << temperature << "\n";
        displayRacks();
    }

    const std::vector<Rack>& getRackList() const {
        return rackList;
    }

    int getTemperature() const {
        return temperature;
    }

    int getProcessingSpeed() const {
        return processingSpeed;
    }

    const std::vector<Hardware>& getHardwareList(int rackIndex) const {
        if (rackIndex >= 0 && rackIndex < rackList.size()) {
            return rackList[rackIndex].getHardwareList();
        }
        else {
            std::cerr << "Invalid rack index.\n";
            return std::vector<Hardware>();
        }
    }

    void addRack() {
        rackList.emplace_back();
        checkRequiredPerformanceSpeed();
    }

    void removeRack() {
        if (!rackList.empty()) {
            rackList.pop_back();
            std::cout << "Rack removed from the server.\n";
            checkRequiredPerformanceSpeed();
        }
        else {
            std::cout << "No rack to remove from the server.\n";
        }
    }

    void addHardwareToRack(int rackIndex, const Hardware& hardware) {
        if (rackIndex >= 0 && rackIndex < rackList.size()) {
            rackList[rackIndex].addHardware(hardware);
            checkRequiredPerformanceSpeed();
        }
        else {
            std::cout << "Invalid rack index.\n";
        }
    }

    void removeHardwareFromRack(int rackIndex) {
        if (rackIndex >= 0 && rackIndex < rackList.size()) {
            rackList[rackIndex].removeHardware();
            checkRequiredPerformanceSpeed();
        }
        else {
            std::cout << "Invalid rack index.\n";
        }
    }

    void displayRacks() const {
        std::cout << "Racks in the server:\n";
        for (int i = 0; i < rackList.size(); ++i) {
            std::cout << "Rack " << i + 1 << " (Required Speed: " << rackList[i].getRequiredPerformanceSpeed() << "):\n";
            rackList[i].displayHardware();
        }
    }

private:
    int calculateNewTemperature() const {
        // Implement your temperature adjustment logic based on processing speed
        // This is a placeholder, replace it with your actual logic
        return processingSpeed * 2;
    }

    void checkRequiredPerformanceSpeed() {
        int totalRequiredSpeed = 0;
        for (const auto& rack : rackList) {
            totalRequiredSpeed += rack.getRequiredPerformanceSpeed();
        }

        if (processingSpeed != totalRequiredSpeed) {
            std::cout << "Warning: Current server performance speed does not match the required speed based on added hardware.\n";
            std::cout << "Adjusting server performance speed to the required speed: " << totalRequiredSpeed << "\n";
            adjustPerformance(totalRequiredSpeed);
        }
    }
};


void saveState(const std::vector<Server>& servers, int selectedServerIndex) {
    std::ofstream outFile("server_state.txt", std::ios::out);

    if (outFile.is_open()) {
        for (size_t i = 0; i < servers.size(); ++i) {
            const Server& server = servers[i];

            outFile << server.getProcessingSpeed() << " " << server.getTemperature() << "\n";
            const auto& rackList = server.getRackList();
            for (const auto& rack : rackList) {
                const auto& hardwareList = rack.getHardwareList();
                for (const auto& hardware : hardwareList) {
                    outFile << hardware.name << " " << hardware.requiredProcessingSpeed << "\n";
                }
                outFile << "-1\n"; // Separator for racks
            }
            outFile << "-1\n"; // Separator for servers

            // Save the selected server index
            if (i == selectedServerIndex) {
                outFile << i << "\n";
            }
        }

        outFile.close();
        std::cout << "State saved successfully.\n";
    }
    else {
        std::cerr << "Unable to open file for saving.\n";
    }
}

void loadState(std::vector<Server>& servers, int& selectedServerIndex) {
    std::ifstream inFile("server_state.txt", std::ios::in);

    if (inFile.is_open()) {
        servers.clear();

        int processingSpeed, temperature;
        while (inFile >> processingSpeed >> temperature) {
            Server server(processingSpeed, temperature);

            int rackIndex = 0;
            while (true) {
                std::string hardwareName;
                int requiredProcessingSpeed;
                inFile >> hardwareName;
                if (hardwareName == "-1") {
                    break; // End of rack
                }
                inFile >> requiredProcessingSpeed;

                Hardware hardware(hardwareName, requiredProcessingSpeed);
                server.addHardwareToRack(rackIndex, hardware);
            }

            servers.push_back(server);
        }

        // Load the selected server index
        if (inFile >> selectedServerIndex) {
            if (selectedServerIndex < 0 || selectedServerIndex >= static_cast<int>(servers.size())) {
                selectedServerIndex = 0; // Default to the first server if the loaded index is invalid
            }
        }

        inFile.close();
        std::cout << "State loaded successfully.\n";
    }
    else {
        std::cerr << "Unable to open file for loading. Starting with default state.\n";
    }
}
int main() {
    std::vector<Server> servers;
    for (int i = 0; i < 4; ++i) {
        servers.emplace_back(100, 50); // Initial processing speed: 100, Initial temperature: 50
    }

    int selectedServerIndex = 0; // Default to the first server

    loadState(servers, selectedServerIndex);
    const Hardware presetHardware[] = { {"CPU", 20}, {"RAM", 10}, {"Storage", 15}, {"Network Card", 5}, {"GPU", 30} };

    int choice;
    do {
        std::cout << "\nMenu:\n";
        std::cout << "1. Select Server\n";
        std::cout << "2. Adjust Performance\n";
        std::cout << "3. Display Status\n";
        std::cout << "4. Add Rack\n";
        std::cout << "5. Remove Rack\n";
        std::cout << "6. Add Hardware to Rack\n";
        std::cout << "7. Remove Hardware from Rack\n";
        std::cout << "8. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
        case 1: {
            std::cout << "Enter server index (1-4): ";
            std::cin >> selectedServerIndex;
            if (selectedServerIndex < 1 || selectedServerIndex > 4) {
                std::cout << "Invalid server index. Please select a server between 1 and 4.\n";
                selectedServerIndex = 0; // Reset to default
            }
            else {
                selectedServerIndex -= 1; // Adjust index to vector indexing (starting from 0)
            }
            break;
        }
        case 2: {
            int newSpeed;
            std::cout << "Enter new processing speed: ";
            std::cin >> newSpeed;
            servers[selectedServerIndex].adjustPerformance(newSpeed);
            break;
        }
        case 3:
            servers[selectedServerIndex].displayStatus();
            break;
        case 4:
            servers[selectedServerIndex].addRack();
            std::cout << "Rack added to the server.\n";
            break;
        case 5:
            servers[selectedServerIndex].removeRack();
            break;
        case 6: {
            int rackIndex;
            std::cout << "Enter rack index: ";
            std::cin >> rackIndex;

            // Display preset hardware options
            std::cout << "Preset Hardware Options:\n";
            for (int i = 0; i < sizeof(presetHardware) / sizeof(presetHardware[0]); ++i) {
                std::cout << i + 1 << ". " << presetHardware[i].name << " (Required Speed: " << presetHardware[i].requiredProcessingSpeed << ")\n";
            }

            int hardwareChoice;
            std::cout << "Enter hardware choice: ";
            std::cin >> hardwareChoice;

            if (hardwareChoice >= 1 && hardwareChoice <= sizeof(presetHardware) / sizeof(presetHardware[0])) {
                servers[selectedServerIndex].addHardwareToRack(rackIndex, presetHardware[hardwareChoice - 1]);
            }
            else {
                std::cout << "Invalid hardware choice.\n";
            }

            break;
        }
        case 7: {
            int rackIndex;
            std::cout << "Enter rack index: ";
            std::cin >> rackIndex;
            servers[selectedServerIndex].removeHardwareFromRack(rackIndex);
            break;
        }
        case 8:
            saveState(servers, selectedServerIndex);
            std::cout << "Exiting...\n";
            break;
        default:
            std::cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 8);

    return 0;
}