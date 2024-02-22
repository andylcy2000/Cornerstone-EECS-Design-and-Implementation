import BT

# hint: You may design additional functions to execute the input command, which will be helpful when debugging :)

class BTinterface:
    def __init__(self):
        print("")
        print("Arduino Bluetooth Connect Program.")
        print("")
        self.ser = BT.bluetooth()
        port = input("PC bluetooth port name: ")
        while(not self.ser.do_connect(port)):
            if(port == "quit"):
                self.ser.disconnect()
                quit()
            port = input("PC bluetooth port name: ")

    def start(self):
        input("Press enter to start.")
        self.ser.SerialWriteString('s')

    def get_UID(self):
        while True:
            if self.ser.ser.in_waiting:
                return self.ser.SerialReadByte()

    def send_action(self,dirc):
        # TODO : send the action to car
        self.ser.SerialWriteString(dirc)
        return dirc

    def end_process(self):
        self.ser.SerialWriteString('e')
        self.ser.disconnect()

    def waiting(self) -> bool:
        return self.ser.ser.in_waiting

if __name__ == '__main__':
    test = BTinterface()
    test.start()
    test.end_process()