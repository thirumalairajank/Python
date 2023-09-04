#Using dictionary to store the complaints
complaints_db={}

#Main function to get data from user about complaints
def main():
       complaint_id = 0
       status = "pending"
       while True:

          print("\nComplaint Management System")

          print("1. Register Complaint")

          print("2. View Complaints")

          print("3. Update Complaint Status")

          print("4. Exit")
          
          choice = input("Enter your choice: ")

          if choice == "1":
                complaint_id +=1
                if complaint_id <=1:
                    employee_id=input("Enter employee_id: ")
                    title=input("Enter complaint title: ")
                    description=input("Enter complaint description: ")
                    complaints_db.update({employee_id: {complaint_id :{"status":status, "complaint_data": {"title":title,"description":description}}}})
                    print(complaints_db)
                    print("Complaint Registered Successfully")
                else:
                    employee_id=input("Enter employee_id: ")
                    if employee_id in complaints_db:
                        title=input("Enter complaint title: ")
                        description=input("Enter complaint description: ")
                        if complaint_id not in complaints_db[employee_id].keys():
                           complaints_db[employee_id][complaint_id]={"status":status, "complaint_data": {"title":title,"description":description}}
                           print(complaints_db)
                           print("Complaint Registered Successfully")
                    else:   
                        title=input("Enter complaint title: ")
                        description=input("Enter complaint description: ")
                        complaints_db[employee_id]={complaint_id: {"status":status, "complaint_data": {"title":title,"description":description}}}
                        print(complaints_db)
                        print("Complaint Registered Successfully")
                
          if choice == "2":
                employee_id=input("Enter employee_id: ")
                if employee_id in complaints_db:
                  print(complaints_db.get(employee_id))
                else:
                  print("Enter correct employee_id")
                  
                """
                #if they know both employee_id and complaint_id
                
                employee_id=input("Enter employee_id: ")
                complaint_id=input("Enter complaint_id: ")
                if employee_id in complaints_db and complaint_id in complaints_db:
                  print(complaints_db.get(employee_id,complaint_id))
                else:
                  print("Enter correct employee_id, complaint_id")
                """
                  
          if choice == "3":
                  employee_id=input("Enter employee_id: ")
                  complaint_id=input("Enter complaint_id: ")
                  if (status=="pending") in complaints_db.get(employee_id,complaint_id):
                    status = "opened"
                    complaints_db[employee_id][int(complaint_id)].update({"status":status})
                    print("Status updated Successfully")
                    print(complaints_db.get(employee_id))
                  else:
                    print("Status already updated")
                    print(complaints_db.get(employee_id))
                  
          if choice == "4":
                break
                        
                
main()