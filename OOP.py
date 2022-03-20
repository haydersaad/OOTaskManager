#importing the libraries we need
import datetime
import argparse
import pickle
import uuid

# import os
# """Finding file path for use later on"""
# cwd = os.path.dirname(os.path.abspath(__file__))
# #print(cwd)
# filepath = os.path.join(cwd, '.todo.pickle')

class Task:
# Representation of a task
  
#   Attributes:
#               - created - date
#               - completed - date
#               - name - string
#               - unique id - number
#               - priority - int value of 1, 2, or 3; 1 is default
#               - due date - date, this is optional
 
    def __init__(self,name,priority,due_date): #initializing a new task
        self.unique_id=str(uuid.uuid1()) #creating unique id using uuid
        self.name=name #settting name as the name we entered
        self.priority=priority #setting priority as priority we entered. If we didn't enter anything it will default to 1
        self.due_date=due_date #setting due date as due date we entered. If we didnt enter anythinng it will default to None
        self.completed=None #initialise the object with state of Completion as None
        self.created_time=datetime.date.today() #storing the time the task was created

class Tasks:
  # """A list of `Task` objects."""

    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        # your code here
        import webbrowser #this is revenge. 
        webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        try: #we use try because the file may or may not exist yet.
            #reading my pickle file
            with open('.todo.pickle','rb') as f:
                self.tasks=pickle.load(f)
            #print(self.tasks)
        except:
            pass

    def pickle_tasks(self):
        """Pickle your task list to a file"""
        # your code here
        with open('.todo.pickle','wb') as f:
            pickle.dump(self.tasks,f) 

    # Complete the rest of the methods, change the method definitions as needed
    def list(self): #creating the list function to display a list of the not completed tasks sorted by the priority.
        print('ID','|','Age','|','Due Date','|','Priority','|','Task')
        print()
        self.tasks.sort(key=lambda row: (row[2]), reverse=False)# I have sorted only using priority. It doesn't seem to be possible to sort by due date as due date can be anything like tomorrow or 31/12/2021.
        for i in self.tasks: #for every task in entire list of tasks
            age=str((i[5]-(datetime.date.today())).days) #we can calculate age in days using following formula. We subtract creation_date stored as an object attribute by the current date.
            if i[4]==None: #if completion is None(i.e. not completed) then only we print. Otherwise, we don't show the completed tasks.
                print(i[0],'|',age+'d','|',i[3],'|',i[2],'|',i[1])

    def report(self): #creating the report function to display a list of items whether they are completed or not, sorted by priority.
        print('ID','|','Age','|','Due Date','|','Priority','|','Task','|','Created','|','Completed')
        print()
        self.tasks.sort(key=lambda row: (row[2]), reverse=False)
        for i in self.tasks: #for every task in entire list of tasks
            age=str((i[5]-(datetime.date.today())).days) #we can calculate age in days using following formula. We subtract creation_date stored as an object attribute by the current date.
            if i[4]==None: #if completion is None(i.e. not completed) then we print in this format(only difference between the two formats is that if completed we print the date of completion, if not completed, we print No)
                print(i[0],'|',age+'d','|',i[3],'|',i[2],'|',i[1],'|',i[5].strftime("%m/%d/%Y"),'| No',)
            else:
                print(i[0],'|',age+'d','|',i[3],'|',i[2],'|',i[1],'|',i[5].strftime("%m/%d/%Y"),'|',i[4].strftime("%m/%d/%Y"))

    def delete(self,id): #to delete the task assosciated with a specific id
        for i in self.tasks: #for every task in entire list of tasks
            if str(i[0])==str(id): #if id of any of the tasks matches the id we entered
                del self.tasks[self.tasks.index(i)] #then delete the task associated with the id

    def done(self,id): #to mark a task assosciated with a specific id as complete
        for i in self.tasks: #for every task in entire list of tasks
            if str(i[0])==str(id): #if id of any of the tasks matches the id we entered
                i[4]=datetime.date.today() #set completion date to current date
        
    def query(self,search_term):
        print('ID','|','Age','|','Due Date','|','Priority','|','Task','|','Created','|','Completed')
        print()
        self.tasks.sort(key=lambda row: (row[2]), reverse=False) # I have sorted only using priority. It doesn't seem to be possible to sort by due date as due date can be anything like tomorrow or 31/12/2021.
        for i in self.tasks: #for every task in entire list of tasks
            if search_term in i[1]: #if any of the search terms appear anywhere in the name of any task
                age=str((i[5]-(datetime.date.today())).days) #we can calculate age in days using following formula. We subtract creation_date stored as an object attribute by the current date.
                if i[4]==None: #if completion is None(i.e. not completed) then we print in this format(only difference between the two formats is that if completed we print the date of completion, if not completed, we print No)
                    print(i[0],'|',age+'d','|',i[3],'|',i[2],i[1],'|',i[5].strftime("%m/%d/%Y"),'| No')
                else:
                    print(i[0],'|',age+'d','|',i[3],'|',i[2],i[1],'|',i[5].strftime("%m/%d/%Y"),'|',i[4].strftime("%m/%d/%Y"))

    def add(self,name,priority,due_date): #the function for adding a task to the task list 
        task=Task(name,priority,due_date) #initialising a new task object
        task_list_form=[task.unique_id,task.name,task.priority,task.due_date,task.completed,task.created_time] #creating a list: i[0]=id, i[1]=task name, i[2]=priority, i[3]=due date, i[4]=completed(or not; initially not), i[5]=date and time of creation
        self.tasks.append(task_list_form) #appending the list to our tasks file.
        print('Created task',task.unique_id) #confirmation of new task


def main():
    
    #the entire main was made off the template in the final project instruction video
    parser=argparse.ArgumentParser(description='Update your ToDo list')
    parser.add_argument('--add',type=str,required=False,help='a task string to add to your list')
    parser.add_argument('--priority',type=int,required=False,default=1,help='priority of task; default value is 1')
    parser.add_argument('--due',type=str,required=False,default=None,help='due date')
    parser.add_argument('--delete',type=str,required=False,help='Delete a task')
    parser.add_argument('--list',action='store_true',required=False,help='list all tasks that have not been completed')
    parser.add_argument('--report',action='store_true',required=False,help='List all tasks, including both completed and incomplete tasks')
    parser.add_argument('--query', type=str, required=False, nargs="+",help='Search for tasks that match a search term')
    parser.add_argument('--done',type=str,required=False,help='Complete a task by passing the done argument and the unique identifier')

    #Parse the argument
    args=parser.parse_args()

    tasks=Tasks()
    
    if args.add: #if add functionality is called
        tasks.add(args.add,args.priority,args.due) #forward values of name(from --add), priority(from --priority), and due date(from --due)
        #print(task_list.tasks)

    elif args.list: #if list functionality called
        tasks.list()

    elif args.query: #if query functionality called
        for i in args.query: #for every search term
            tasks.query(i) #forwarding search term we wish to find in task names

    elif args.done: #if done functionality called
        tasks.done(args.done) #forward value of the id number of task we wish to complete

    elif args.delete: #if delete functionality called
        tasks.delete(args.delete) #forward value of the id number of task we wish to delete
    
    elif args.report: #if report functionality called
        tasks.report()
        
    #writing a pickle file
    tasks.pickle_tasks()
    exit()
        
        
if __name__=='__main__':
    main()