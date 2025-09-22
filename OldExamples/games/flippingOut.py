import random  #gives access to random

HoT = ['heads', 'tails'] # list of options

def flippingOut(n):
    for i in range(0,n):
        result = random.choice(HoT)
        if(result == 'heads'):
            print(
                '''
                                                            
                            ████████████                                                                                          
                         ████           ████                                            
                      ██     ██     ██    ████                                          
                    ████     ██     ██    ████                                          
                    ██       ██     ██      ████                                        
                    ██       ██     ██      ████                                        
                    ██       █████████      ████                                        
                    ██       ██     ██      ████                                        
                    ██       ██     ██      ████                                        
                    ██       ██     ██      ████                                        
                    ████     ██     ██    ████                                          
                      ██                 ████                                                                                   
                        ██████      ████████                                            
                            ████████████                                                                                                                 
                '''
            )
        else:
            print(
               '''
                                                            
                            ████████████                                                
                        ██████      ████████                                            
                      ████              ████                                            
                      ██     █████████    ████                                          
                    ████        ██        ████                                          
                    ██          ██         ████ 
                    ██          ██         ████ 
                    ██          ██         ████ 
                    ██          ██         ████ 
                    ██          ██         ████ 
                    ██          ██         ████                                                                                                                                                                                                        
                      ████              ████                                            
                        ██████      ██████                                            
                            ████████████                                                                                                                 
                
                '''
            )
    #print(i+1,result)
n = int(input("How many coin flips?"))
flippingOut(n)