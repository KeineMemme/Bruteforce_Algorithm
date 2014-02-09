class D_Bruteforcer:
    __digits = []
    __length = 0

    def __init__(self,length,boolDigits,boolUpCharacters,boolLowCharacters,boolExtraCharacters):
        self.__length = int(length)+1
        #Normal Digits
        if boolDigits is True:
            i = 48
            while i <= 57:
                self.__digits.append(chr(i))
                i+=1
        #Up-Characters
        if boolUpCharacters is True:
            i = 65
            while i <= 90:
                self.__digits.append(chr(i))
                i+=1
        #Low-Characters
        if boolLowCharacters is True:
            i = 97
            while i <= 122:
                self.__digits.append(chr(i))
                i+=1
        #Extra-Characters
        if boolExtraCharacters is True:
            #Add here more Characters
            self.__digits.append("$")
            self.__digits.append("!")
            self.__digits.append("?")
            self.__digits.append("ß")
            self.__digits.append("_")
            self.__digits.append("-")
            self.__digits.append("Ä")
            self.__digits.append("ä")
            self.__digits.append("Ö")
            self.__digits.append("ö")
            self.__digits.append("Ü")
            self.__digits.append("ü")
            self.__digits.append("*")
            #Add more Extra-Characters here..

    def decimal_to_bruteFormat(self, number):
        r = []
        go_on = number
        while go_on > 0:
            r.append(go_on%self.__digits.__len__())
            go_on = int(go_on/self.__digits.__len__())
        return r

    def bruteFormat_to_str(self, bruteFormat):
        raw = []
        str = ""
        for d in bruteFormat:
            str += self.__digits[d]
        return str

    def attack(self):
        counter = 1
        str = ""
        n = 1
        nllstr = ""
        while n < self.__length:
            nllstr+="0"
            print(nllstr)   # For all 0, 00, 000, 0000.. Use also this string for any attack..
            n+=1
        while str.__len__() < self.__length:
            bruteFormat = self.decimal_to_bruteFormat(counter)
            str = self.bruteFormat_to_str(bruteFormat)
            print(str) # You can do what you want with str :)
            counter+=1






