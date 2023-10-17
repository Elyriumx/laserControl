import grpc
import laserControl_pb2
import laserControl_pb2_grpc
from colorama import init, Fore, Style

def printGreen(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def printRed(text):
    print(Fore.RED + text + Style.RESET_ALL)

def run():
    init()
    print("starting client")

    while True:
        
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = laserControl_pb2_grpc.LaserControlServiceStub(channel)
            print("1. EnableLaser")
            print("2. DisableLaser")
            print("3. SetBiasVoltage")
            print("4. GetLaserStatus")
            print("5. Exit program")
            user_input = input("Enter your choice: ")

            if user_input == "1":
                enableLaserRequest = laserControl_pb2.EnableLaserRequest()
                enableLaserResponse = stub.EnableLaser(enableLaserRequest)
                if enableLaserResponse.success:
                    printGreen("Laser enabled")
                else:
                    printRed("Laser enable failed")

            elif user_input == "2":
                disableLaserRequest = laserControl_pb2.DisableLaserRequest()
                stub.DisableLaser(disableLaserRequest)
                printGreen("Laser disabled")
                
            elif user_input == "3":
                voltage = float(input("Enter voltage: "))
                setBiasVoltageRequest = laserControl_pb2.SetBiasVoltageRequest()
                setBiasVoltageRequest.voltage = voltage
                setBiasVoltageResponse = stub.SetBiasVoltage(setBiasVoltageRequest)

                if setBiasVoltageResponse.success:
                    printGreen("Set bias voltage succeeded")
                else:
                    printRed("Set bias voltage failed")

            elif user_input == "4":
                getLaserStatusRequest = laserControl_pb2.GetLaserStatusRequest()
                getLaserStatusResponse = stub.GetLaserStatus(getLaserStatusRequest)
                status = getLaserStatusResponse.status
                if status == laserControl_pb2.GetLaserStatusResponse.ON:
                    printGreen("Laser is on")
                elif status == laserControl_pb2.GetLaserStatusResponse.OFF:
                    printRed("Laser is off")
                else:
                    printRed("Invalid status")
            
            elif user_input == "5":
                print("Exiting program")
                break

            else:
                print("Invalid choice")
        
        print("")
        continue

if __name__ == '__main__':  
    run()

