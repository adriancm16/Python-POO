"""
The Budget App has the following features:

-The Class 'Category' instantiate objects based on different budget categories 
 like food, clothing, and entertainment.
 
- 'deposit' method, accepts  amount and description

- 'withdraw' method is similar to the deposit method,
  if there aren't enough founds to withdraw, nothing should be substracted from deposit 

- 'get_balance' method returns the current balance of the budget category 
    based on the deposits and withdrawals that have occurred.

- 'transfer' method that accepts an amount and another budget category as arguments.
  it transfer the amount to other category.
  if there aren't enough founds to transfer, this doesn't execute.

- the function 'create_spend_chart' return a string that is a bar chart,
  This chart shows the percentage spend in each category
  The percentage spent calculate only with withdrawals and not with deposits.


"""




class Category:
  def __init__(self,name):
    self.name=name
    self.total=0.0
    self.ledger=[]

  def __repr__(self):
    output=self.name.center(30,'*')+'\n'

    for i  in self.ledger:
      amount_str=str(i['amount'])
      
      if '.' not in amount_str:
        amount_str+='.00'

      if amount_str[-2]=='.':
        amount_str+='0'
        

      l_amount=30-len(amount_str)
      desc=i['description'][0:l_amount-1]
      output+=desc+amount_str.rjust(30-len(desc))+'\n'

    output+='Total: '+str(self.total)
    return output

  def deposit(self,amount,description=False):
    if not description:
      description=""
    
    self.total+=amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self,amount,description=False):

    do_withdraw=self.check_funds(amount)

    if not description:
      description=""
  
    if do_withdraw:
      self.total-=amount
      self.ledger.append({"amount": -amount, "description": description})
    return do_withdraw

  def get_balance(self):
    return self.total
    
  def transfer(self,amount,instance):

    do_transfer=self.check_funds(amount)

    if do_transfer:
      self.withdraw(amount,"Transfer to "+instance.name)
      instance.deposit(amount,"Transfer from "+self.name)

    return do_transfer

  def check_funds(self,amount):
    if amount>self.total:
      return False

    return True
  
def create_spend_chart(categories):

  total_cat={}
  total=0
  len_cat=0
  cat_name=[]
  axes=""
  for categ in categories:

    if len(categ.name)>len_cat:
      len_cat=len(categ.name)

    total_cat[categ.name]=0
    for i in categ.ledger:

      if i['amount']<0:
        total_cat[categ.name]+=abs(i['amount'])
        total+=abs(i['amount'])

 
  for c in categories:
    total_cat[c.name]=round(total_cat[c.name]*100/total)
    cat_name.append(c.name.ljust(len_cat))

  out='Percentage spent by category\n'
  linea="    -"
  linea+="---"*len(categories)

  for i in range(100,-1,-10):
    out+=(str(i)+'| ').rjust(5)

    for c in categories:
      if total_cat[c.name]>=i:
        out += 'o  '
      else: out +='   '
    out+='\n'
  out+=linea 

  
  for x in range(0,len_cat):
    ax=""
    for c in cat_name:
      ax+=c[x]+"  "
    axes+='\n'+'     '+ax
  out+=axes
  
  return out


#----------TEST----------------------------------------

food = Category("Food") #create a category for food
food.deposit(1000, "initial deposit")# deposit 1000 to food
food.withdraw(10.15, "groceries")# withdraw 10.15 of groceries from food
food.withdraw(15.89, "restaurant and more food for dessert")# withdraw 15.89 from food
print(food.get_balance())#shows the actual amount from food after to execute the witdraws

clothing = Category("Clothing")#create a category for Clothing
food.transfer(50, clothing)#transfer 50 from food to cloting
clothing.withdraw(25.55)#withdraw 25.55 from cloting
clothing.withdraw(100)#withdraw 100 from cloting

auto = Category("Auto")# creat a category for Auto
auto.deposit(1000, "initial deposit")#deposit 1000 to auto 
auto.withdraw(15)#withdraw 15 from auto


print(food)# shows with details every history executed in food 
print(clothing)# shows with details every history executed in Category
print('check_funds:',clothing.check_funds(25))#check if avalaible funds in cloting exceed 25
print(create_spend_chart([food, clothing, auto]))#create a bar chart to food,clothing and auto categories