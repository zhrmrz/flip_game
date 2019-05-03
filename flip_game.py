class Sol:
    def flip_game(self,str):
        list=[]
        for i in range(len(str)-1):
            if str[i:i+2]=='++':
                list.append(str[:i]+'--'+str[i+2:])
        return list

if __name__ == '__main__':
    p1=Sol()
    print(p1.flip_game('++++'))
