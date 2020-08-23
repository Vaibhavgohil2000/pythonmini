import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.conn = sqlite3.connect("emp.db")
            #5      
            try:
                  self.conn.execute('''create table if not exists emp1(name text, salary integer , emp_type char)''')
                  print('table is created')
            except:
                  pass
      

      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            self.conn.execute("insert into emp1 values (?,?,?)",(ename,esalary,etype))
            self.conn.commit()
            print("record added")

      def display(self):
            #7
            name = input("enter the emp name: ")
            with self.conn:
                  dataEmp = self.conn.execute(
                        'select name,emp_type,salary from emp1 where name=:name',
                        {'name': name})
                  for i in dataEmp:
                        print("name :" , i[0])
                        print("Employee Type :", i[1])
                        print("Salary : ", i[2])
                  
      

      
