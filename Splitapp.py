import threading
lock = threading.Lock()
class Splitapp:

    #To create Group and add members to the group 
    def create_group(self):
        try:
            groupname =  input('Enter name of the group\n')
            number_people = int(input('Enter number of people in group\n')) 
            member = []
            print('Add names: - \n')
            for i in range(0,number_people):
                val = input()
                member.append(val)
    
            self.dict  = {}
            self.dict['GroupName'] = groupname
            self.dict['Members'] = member 
            print(self.dict)  
        except Exception as e:
            print('Not able to create group') 


    #To add expense 
    def add_expense(self):
        try:
            Description = input('Enter the description of expense\n')
            itemlist = int(input('How much items are there?\n'))
            self.MainDict = {}
            self.MainDict['Name'] = Description
            listf = []
 #------------------------------------------------------------------------------------------       
            for i in range(0,itemlist):
                Dictitems = {}
                name = input('Enter name of item number {0}\n'.format(i+1))
                val = int(input('Enter Value of item number {0}\n'.format(i+1)))
                Dictitems['name'] = name
                Dictitems['Value'] = val
                paid_by = int(input('Enter number of people who Paid\n'))
                ls = []
                dict2 = {}
#-------------------------------------------------------------------------------------------- 
                limit1 = 0           
                for j in range(0,paid_by):
                    person = input('Enter name of person {0}\n'.format(j+1))
                    if person not in self.dict['Members']:
                        self.dict['Members'].append(person)
                    addval = int(input('Enter Amount?\n'))
                    limit1 = limit1 + addval
                    dict2[person] = addval
                if limit1>val:
                    return 'paid value should not be greater than original value'    
                ls.append(dict2)
                Dictitems['paid by'] = ls 
#---------------------------------------------------------------------------------------------------------------------------------
                ls1 = []
                dict3 = {}
                limit2 = 0
                owed_by = int(input('Enter number of people who Owed\n'))
                for k in range(0,owed_by):
                    person_owed = input('Enter name of person {0}\n'.format(k+1))
                    if person_owed not in self.dict['Members']:
                        self.dict['Members'].append(person_owed)
                    addval_owed = int(input('Enter Amount?\n'))
                    limit2 = limit2 + addval_owed
                    dict3[person_owed] = addval_owed
                if limit2>val:
                    return 'owed value should not be greater than original value'     
                ls1.append(dict3)
                Dictitems['owed by'] = ls1 
                listf.append(Dictitems)
            self.MainDict['items'] = listf 
            print("Expense : - \n{0}".format(self.MainDict)) 
            print("Group Members : - \n{0}".format(self.dict))    
        except Exception as e:
            print('Not able to add expense')     
     
            
    #Extended method of update_expense method        
    def options(self):
        update_value = input("what do you want to update?\n 1.Expense name \n 2.items_name \
        \n 3.items value \n 4.Update the amount person who paid \n 5.Update the amount of person who owed\n 6. To quit\n")
        return update_value


    #Extended method of update_expense method
    def check_values(self,person,value,type):
        count = 0
        k = 0
        for key in self.MainDict['items'][0][type][0].keys():
            count = count + self.MainDict['items'][0][type][0][key]
            k += 1
        count = count -  self.MainDict['items'][0][type][0][person]
        count = count + value
        return count

    #To Update expense and its details
    def update_expense(self):
        try:
            lock.acquire()
            input1 = self.options()
            if input1 == '1':
                name = input('Enter new expense name\n')  
                self.MainDict['Name'] = name
            elif input1 == '2':
                item_name =input('Enter new item name\n')  
                self.MainDict['items'][0]['name'] = item_name
            elif input1 == '3':
                item_val =int(input('Enter new item value\n'))  
                self.MainDict['items'][0]['Value'] = item_val
            elif input1 == '4':
                person = input('Enter name of person\n')
                value = int(input('Enter amount'))
                count = self.check_values(person,value,'paid by')
                if count > self.MainDict['items'][0]['Value']:
                    return 'value cannot be update its more than original value'   
                else:
                    self.MainDict['items'][0]['paid by'][0][person] = value   
            elif input1 == '5':
                person = input('Enter name of person\n')
                value = int(input('Enter amount\n'))
                count = self.check_values(person,value,'owed by')
                if count > self.MainDict['items'][0]['Value']:
                    return 'value cannot be update its more than original value'   
                else:
                    self.MainDict['items'][0]['owed by'][0][person] = value
            else:
                pass  
            lock.release() 
        except Exception as e:
            print('Not able to update expense')         




    #To Delete expense if they want
    def delete_expense(self):
        try:
            a = input('want to delete? y or n\n')
            if a == 'y':
                input1 = input('Enter name of expense you want to delete')
                for i in self.MainDict[input1]['items']['paid by']:
                    if i in self.dict['Members']:
                        self.dict['Members'].remove(i)
                del self.MainDict[input1]
                print('expense deleted')
            else:
                pass  
        except Exception as e:
            print('Not able to Delete expense')      


    #To give the details of balance 
    def get_balance(self):
        try:
            balance = {}
            balance['name'] = self.dict['GroupName']
            new_dict = {}
            for i in self.dict['Members']:
                if i in self.MainDict['items'][0]['paid by'][0].keys():
                    if i in self.MainDict['items'][0]['owed by'][0].keys():
                        ans = self.MainDict['items'][0]['paid by'][0][i] - self.MainDict['items'][0]['owed by'][0][i]
                        new_dict[i] = {'balances':ans}
                elif i in self.MainDict['items'][0]['owed by'][0].keys():
                    ans = 0 - self.MainDict['items'][0]['owed by'][0][i]  
                    new_dict[i] = {'balances':ans}    
                new_dict[i]['owes by'] = []
                new_dict[i]['owes to'] = []
            balance['Balances'] = new_dict 
            print(balance) 
        except Exception as e:
            print('Not able to get Balance')


        



def main():
    Kanchan = Splitapp()
    print("------------------------------------------------------------------\nTo create Group")
    Kanchan.create_group()
    print('------------------------------------------------------------------\nTo Add expense')
    print(Kanchan.add_expense())
    print('------------------------------------------------------------------\nTo Update expense')
    print(Kanchan.update_expense())
    print('-------------------------------------------------------------------\nTo delete expense')
    Kanchan.delete_expense()
    print('------------------------------------------------------------------\n Get Balance status')
    Kanchan.get_balance()
    



if __name__ == "__main__":
    main()
