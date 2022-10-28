import telnetlib
import time
from tkinter import *
import re


class OpticalSwitch:
    def __init__(self):
        self.root = Tk()
        self.root.title('OpticalSwitchGUI')
        self.root.geometry('570x300')
        self.root.resizable(0, 0)
        self.inputPort = 0
        self.outputPort = 0

        # Empty Columns
        self.root.columnconfigure(0, minsize=30)
        self.root.columnconfigure(3, minsize=30)
        self.root.columnconfigure(5, minsize=30)
        self.root.columnconfigure(12, minsize=30)

        # Empty Rows
        self.root.rowconfigure(2, minsize=60)
        self.root.rowconfigure(6, minsize=30)

        # IP
        self.textIP = Label(self.root, text='Switch IP')
        self.textIP.grid(row=0, column=1)

        self.ip = Entry(self.root, width=18)
        self.ip.grid(row=0, column=2, columnspan=2, pady=10)

        # Port
        self.textPort = Label(self.root, text='Port')
        self.textPort.grid(row=1, column=1)

        self.port = Entry(self.root, width=18)
        self.port.grid(row=1, column=2, columnspan=2)

        with open('Config.txt', 'r', encoding='utf8') as f:
            config = f.read().split('\n')
            try:
                self.port.insert(0, config[1])
                self.ip.insert(0, config[0])
            except:
                self.ip.insert(0, '255.255.255.255')
                self.port.insert(0, '10001')

        # Background for message
        self.output = Label(self.root, width=42, text=f'Input Port {self.inputPort}\t\tOutput Port {self.outputPort}',
                            bg='gray', fg='white')
        self.output.grid(row=0, column=6, columnspan=6)

        # Execute
        self.execute = Button(self.root, text='Acivate', width=15, command=self.switch_ports)
        self.execute.grid(row=1, column=6, columnspan=3)

        # Show
        self.show = Button(self.root, text='Show active', width=15, command=self.check_ports)
        self.show.grid(row=1, column=9, columnspan=3)

        # Exit
        self.exit = Button(self.root, text='Exit', command=lambda: self.root.quit(), width=15)
        self.exit.grid(row=7, column=1, columnspan=2)

        # Input Ports
        self.textIN = Label(self.root, text='Input')
        self.textIN.grid(row=2, column=2, columnspan=3)

        self.IN1 = Button(self.root, text='1', activebackground='green', command=lambda: [self.chooseInput(1)])
        self.IN1.grid(row=3, column=2, ipadx=10, ipady=10, rowspan=3)

        self.IN2 = Button(self.root, text='2', activebackground='green', command=lambda: [self.chooseInput(2)])
        self.IN2.grid(row=3, column=3, ipadx=10, ipady=10, rowspan=3)

        # Output Ports
        self.textOUT = Label(self.root, text='Output')
        self.textOUT.grid(row=2, column=6, columnspan=6)

        self.OUT1 = Button(self.root, text='1', activebackground='green', command=lambda: [self.chooseOutput(1)])
        self.OUT1.grid(row=3, column=6, ipadx=15, ipady=15)

        self.OUT2 = Button(self.root, text='2', activebackground='green', command=lambda: [self.chooseOutput(2)])
        self.OUT2.grid(row=3, column=7, ipadx=15, ipady=15)

        self.OUT3 = Button(self.root, text='3', activebackground='green', command=lambda: [self.chooseOutput(3)])
        self.OUT3.grid(row=3, column=8, ipadx=15, ipady=15)

        self.OUT4 = Button(self.root, text='4', activebackground='green', command=lambda: [self.chooseOutput(4)])
        self.OUT4.grid(row=3, column=9, ipadx=18, ipady=15)

        self.OUT5 = Button(self.root, text='5', activebackground='green', command=lambda: [self.chooseOutput(5)])
        self.OUT5.grid(row=3, column=10, ipadx=18, ipady=15)

        self.OUT6 = Button(self.root, text='6', activebackground='green', command=lambda: [self.chooseOutput(6)])
        self.OUT6.grid(row=3, column=11, ipadx=18, ipady=15)

        self.OUT7 = Button(self.root, text='7', activebackground='green', command=lambda: [self.chooseOutput(7)])
        self.OUT7.grid(row=5, column=6, ipadx=15, ipady=15)

        self.OUT8 = Button(self.root, text='8', activebackground='green', command=lambda: [self.chooseOutput(8)])
        self.OUT8.grid(row=5, column=7, ipadx=15, ipady=15)

        self.OUT9 = Button(self.root, text='9', activebackground='green', command=lambda: [self.chooseOutput(9)])
        self.OUT9.grid(row=5, column=8, ipadx=15, ipady=15)

        self.OUT10 = Button(self.root, text='10', activebackground='green', command=lambda: [self.chooseOutput(10)])
        self.OUT10.grid(row=5, column=9, ipadx=15, ipady=15)

        self.OUT11 = Button(self.root, text='11', activebackground='green', command=lambda: [self.chooseOutput(11)])
        self.OUT11.grid(row=5, column=10, ipadx=15, ipady=15)

        self.OUT12 = Button(self.root, text='12', activebackground='green', command=lambda: [self.chooseOutput(12)])
        self.OUT12.grid(row=5, column=11, ipadx=15, ipady=15)

        self.root.mainloop()

    def switch_ports(self):
        with open('Config.txt', 'w', encoding='utf8') as f:
            config = f'{self.ip.get()}\n{self.port.get()}'
            f.write(config)
            try:
                tn = telnetlib.Telnet(str(self.ip.get()), int(self.port.get()), timeout=5)
                tn.write(f'set{self.inputPort}{self.outputPort}'.encode('ascii') + b"\r\n")
                tn.close()
                self.output.config(text=f'Ports activated', bg='green')
            except Exception as e:
                print(e)
                self.output.config(text=f'No connection with switch', bg='red')

    def check_ports(self):
        with open('Config.txt', 'w', encoding='utf8') as f:
            config = f'{self.ip.get()}\n{self.port.get()}'
            f.write(config)
            try:
                tn = telnetlib.Telnet(str(self.ip.get()), int(self.port.get()), timeout=5)
                tn.write(f'set?'.encode('ascii') + b"\r\n")
                time.sleep(2)
                output = tn.read_some().decode('ascii')
                tn.close()
                output = output.split('\n')
                print(len(output))
                if len(output) == 1:
                    self.output.config(text=f"No switches configured yet", bg='yellow')
                else:
                    final_output = '\t'
                    count = 0
                    while count < len(output) - 1:
                        final_input_port = re.sub('[^0-9]', '', output[count])[0]
                        final_output_port = re.sub('[^0-9]', '', output[count])[1:3]
                        final_output += f'Input {final_input_port} Output: {final_output_port}' 
                        final_output += '\t' if len(final_output_port) > 1 else '\t\t'
                        count += 1

                    self.output.config(text=final_output, bg='green')
            except Exception as e:
                self.output.config(text=f'No connection with switch', bg='red')

    def chooseInput(self, button):
        self.inputPort = button
        self.output.config(text=f'Input Port {self.inputPort}\t\tOutput Port {self.outputPort}', bg='gray', fg='white')

    def chooseOutput(self, button):
        self.outputPort = button
        self.output.config(text=f'Input Port {self.inputPort}\t\tOutput Port {self.outputPort}', bg='gray', fg='white')


if __name__ == '__main__':
    OpticalSwitch()
