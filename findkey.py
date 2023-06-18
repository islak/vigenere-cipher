
ascii_freq = {32: 0.167564443682168,
              101: 0.08610229517681191,
              116: 0.0632964962389326,
              97: 0.0612553996079051,
              110: 0.05503703643138501,
              105: 0.05480626188138746,
              111: 0.0541904405334676,
              115: 0.0518864979648296,
              114: 0.051525029341199825,
              108: 0.03218192615049607,
              100: 0.03188948073064199,
              104: 0.02619237267611581,
              99: 0.02500268898936656,
              10: 0.019578060965172565,
              117: 0.019247776378510318,
              109: 0.018140172626462205,
              112: 0.017362092874808832,
              102: 0.015750347191785568,
              103: 0.012804659959943725,
              46: 0.011055184780313847,
              121: 0.010893686962847832,
              98: 0.01034644514338097,
              119: 0.009565830104169261,
              44: 0.008634492219614468,
              118: 0.007819143740853554,
              48: 0.005918945715880591,
              107: 0.004945712204424292,
              49: 0.004937789430804492,
              83: 0.0030896915651553373,
              84: 0.0030701064687671904,
              67: 0.002987392712176473,
              50: 0.002756237869045172,
              56: 0.002552781042488694,
              53: 0.0025269211093936652,
              65: 0.0024774830020061096,
              57: 0.002442242504945237,
              120: 0.0023064144740073764,
              51: 0.0021865587546870337,
              73: 0.0020910417959267183,
              45: 0.002076717421222119,
              54: 0.0019199098857390264,
              52: 0.0018385271551164353,
              55: 0.0018243295447897528,
              77: 0.0018134911904778657,
              66: 0.0017387002075069484,
              34: 0.0015754276887500987,
              39: 0.0015078622753204398,
              80: 0.00138908405321239,
              69: 0.0012938206232079082,
              78: 0.0012758834637326799,
              70: 0.001220297284016159,
              82: 0.0011037374385216535,
              68: 0,
              85: 0.0010426370083657518,
              113: 0.00100853739070613,
              76: 0.0010044809306127922,
              71: 0.0009310209736100016,
              74: 0.0008814561018445294,
              72: 0.0008752446473266058,
              79: 0.0008210528757671701,
              87: 0.0008048270353938186,
              106: 0.000617596049210692,
              122: 0.0005762708620098124,
              47: 0.000519607185080999,
              60: 0.00044107665296153596,
              62: 0.0004404428310719519,
              75: 0.0003808001912620934,
              41: 0.0003314254660634964,
              40: 0.0003307916441739124,
              86: 0.0002556203680692448,
              89: 0.00025194420110965734,
              58: 0.00012036277683200988,
              81: 0.00010001709417636208,
              90: 8.619977698342993e-05,
              88: 6.572732994986532e-05,
              59: 7.41571610813331e-06,
              63: 4.626899793963519e-06,
              127: 3.1057272589618137e-06,
              94: 2.2183766135441526e-06,
              38: 2.0282300466689395e-06,
              43: 1.5211725350017046e-06,
              91: 6.97204078542448e-07,
              93: 6.338218895840436e-07,
              36: 5.070575116672349e-07,
              33: 5.070575116672349e-07,
              42: 4.436753227088305e-07,
              61: 2.5352875583361743e-07,
              126: 1.9014656687521307e-07,
              95: 1.2676437791680872e-07,
              9: 1.2676437791680872e-07,
              123: 6.338218895840436e-08,
              64: 6.338218895840436e-08,
              5: 6.338218895840436e-08,
              27: 6.338218895840436e-08,
              30: 6.338218895840436e-08}

def findKeyLength(ciphertext):
    copiedString = ciphertext[:]
    myDict={}
    for j in range(2,30):
        everyjth = [ciphertext[i] for i in range(j, len(ciphertext), j+1)]
        ciphertext= ''.join(everyjth); 
        hasNumber = False
        for char in ciphertext:
            if char.isdigit():
                hasNumber = True
                break
        if hasNumber:
            textLen = len(ciphertext)
            numLetters = [0] * 256  # Initialize a list of 256 elements for all ASCII characters
            for char in ciphertext:
                numLetters[ord(char)] += 1
            ic = sum([entry * (entry - 1) for entry in numLetters])
            ic /= textLen * (textLen - 1)
            ic_abs = abs(0.0667-ic)
            myDict[j+1] = ic_abs
            KeyLength = min(myDict, key=lambda k: myDict[k])
            ciphertext = copiedString[:]
        else:
            print("no")
    return KeyLength

def findKey(ciphertext, key_length):
    # Divide the ciphertext into blocks based on the maximum key length
    blocks = []
    byte_list=[]

    for i in range(0,len(ciphertext),2):
        byte_list.append(ciphertext[i:i+2])

    for i in range(key_length):
        block = ''
        for j in range(i, len(byte_list), key_length):
            block += byte_list[j]
        blocks.append(block)

   # Find the most likely letter for each position in the key
    key = ''
    block_dict={}
    for block in blocks:
        freqs = [0]*256
        for i in range(0, len(block)-1, 2):
            hex = block[i:i+2]
            #create a dictionary mapping each character to the number of occurances 
            c = chr(int(hex, 16))  # Convert hex to int and then to Unicode character
            freqs[ord(c)] += 1
            if ord(c) in block_dict.keys():
                block_dict[ord(c)] += 1 
            else: 
                block_dict[ord(c)] = 1          
            
        total = sum(block_dict.values())   
        for key in block_dict: 
            block_dict[key] = block_dict[key]/total

        #find the sum of all the freqencies
        sum_of_values = 0
        for value in block_dict.values():
            sum_of_values += value

        shift_decrypt(block)

finalKey=[]
def shift_decrypt(ciphertext):
    
    correlation ={} 
    for shift in range(256):
        plaintext = []
        char_freq = {}
        my_ascii_freq = {}
        isValid = True
        # for hex in ciphertext:
        for i in range(0, len(ciphertext)-1, 2):
            hex = ciphertext[i:i+2]
            decimal = (int(hex, 16))
            new_decimal = (decimal^shift) % 256
            plaintext.append(new_decimal)

        if max(plaintext)>126 or min(plaintext)<32:
            continue 

        for i in plaintext:
            if i not in char_freq:
                char_freq[i] = 1
            else:
                char_freq[i] += 1

        total = sum(char_freq.values())
        for key in char_freq:
            char_freq[key] = char_freq[key]/total
        sum_of_values = 0
        for value in char_freq.values():
            sum_of_values += value

        result = 0
        for key in char_freq:
            if key in ascii_freq:
                result = result + char_freq[key] * ascii_freq[key]
      
        correlation.update({shift: result})

    if len(correlation)!= 0 : 
        key_for_largest_value = max(correlation, key=correlation.get)
        key_for_largest_value= str(key_for_largest_value)
        finalKey.append(key_for_largest_value) 
    else:
        finalKey.append('0') 

    if (len(finalKey) == 10):
        print("SECRET KEY: ")
        print(finalKey)
    

ciphertext = "F94720DC5BD9F775FD74C14661D60FD7F731A968CB0262DD46D6F231B2668E4320DD4ACEF67DA874C74D6E8F46D6B972AF79DE566FC85DD9E979A42E8E7668CA0FDCFC67B86CC1526DCA41CCB97EBB20CD4A65CE5F98FD78BA69DA436C8F47D9EB75AA61DC4720C74ECBB977AF65CB4620C65B98FF63B26D8E5668CA0FDCFC62B467C0026CC642D1ED70A969C14C738F40DEB97CB863C6436EC64CD9F531BE6FC35275DB46D6FE31BC6ECA0262DD40CDFE79A920DA4A658F4CD7EA65FD6FC80268C648D0B976AF61CA4720CC5DC1E965B267DC4370C746DBB975B876C74165DC0FDCF666B320DA4D20D847DDEB74FD74C647798F4CD9F731BF658E5773CA4B98F07FFD73DB41688F4CD7F47CB872CD4B61C30FD9E961B169CD4374C640D6EA31BC738E5065C240CCFC31BE61DD4A20CB46CBE974B373CB50738F4ED6FD31BE6FC35275DB4ACAB965B872C34B6ECE43CBB731946E8E5675DD4194B962A863C60261DF5FD4F072BC74C74D6EDC0FDBEB74BC74CB02618F41DDFC75FD66C15020C14ACFB965A470CB5120C04998FA63A470DA4D67DD4EC8F178BE20DD5B73DB4AD5EA31AA68C741688F42D1F778B069D44720DB47DDB97FB863CB5173C65BC1B97EBB20DD4763DA5DDDB97AB8798E4669DC5BCAF073A874C74D6E8F4CD0F87FB365C25120CE41DCB962A870DE4E798F5BD0FC31B871DB4B76CE43DDF765FD6FC802618F58CAF065A965C00273C648D6F865A872CB0C20EE5B98ED79B820DD436DCA0FCCF07CB82C8E5668CA40CAFC65B463CF4E20CB4ACEFC7DB270C3476EDB5C98F07FFD69C0446FDD42D9ED78B26E8E5668CA40CAE031BC6ECA0263C042C8EC65B8728E5163C64AD6FA74FD73C64D778F5FCAF67CB473CB026FC90FC8EB7EAB69CA4B6EC80FC8EB7EAB61CC4E798F5CDDFA64AF658E4172D65FCCF662A473DA476DDC0398FA79BC6EC94B6EC80FCCF178AE20CF4C63C64AD6ED31BC72DA0269C15BD7B970FD73CD4B65C14CDDB71B8968CB0264CA59DDF57EAD6DCB4C748F40DEB972B26DDE5774CA5D98FA7EB374DC4D6CC34ADCB972B26DC3576EC64CD9ED78B26E8E4C65DB58D7EB7AAE20DE506FC246CBFC62FD65C8446FDD5BD4FC62AE20CF4C648F46D6FC69AD65C05169D94A98FA7EB374CF41748F4DDDED66B865C00270CA40C8F574FD6FDC0263C042C8EC65B872DD026FC10FD7E961B273C756658F5CD1FD74AE20C14420DB47DDB966B272C2462C8F5DDDE97DBC63C74C678F42D7EA65FD6DCF4B6C8F4ED6FD31B061C05B20CA57DBEC63AE69C14C738F58D1ED79FD74CB4E65CC40D5F464B369CD4374C640D6EA3FFD46C15020C24ED6E031BC70DE4E69CC4ECCF07EB3738E5668CA5CDDB972B26EDA4363DB5C98F464AE748E40658F42D9FD74FD73CB4175DD4A98F876BC69C051748F4DD7ED79FD65CF5465DC4BCAF661AD69C04520CE41DCB965B5658E4B6EC54ADBED78B26E8E4D668F46D4F574BA69DA4B6DCE5BDDB97CB873DD4367CA5C96B950A920DE5065DC4AD6ED3DFD68C15565D94ACAB531A968CB0273C043CDED78B26E8E4D668F5CDDFA64AF69DA5B20DF5DD7FB7DB86DDD026CCE48CBB966B86CC20262CA47D1F775FD6FDA4A65DD0FD9EB74BC738E4D668F4CD7F47CA86EC74161DB46D7F762FD74CB4168C140D4F676A42E8E616FC15BDDF461B272CF50798F4CCAE061A96FC95061DF47C1B978AE20DB4C61CD43DDB965B220C34765DB0FCCF174FD72CB5375C65DDDF474B374DD0E20C64198ED79BC748E4B74DC0FCDEA74FD77C1576CCB0FD1F461B273CB0273DA4CD0B962B876CB50658F46D6FA7EB376CB4C69CA41DBFC62FD6FC00274C74A98EA68AE74CB4F20DA5CDDEB62F120CF5120DB4098FC7DB46DC74C61DB4A98F470B3798E4D668F5BD0FC31BF65C04766C65BCBB97EBB20DA476CCA5FCAF672B873DD4B6EC801B2"
keylen = findKeyLength(ciphertext)

findKey(ciphertext, keylen)
