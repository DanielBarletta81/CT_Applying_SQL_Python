import mysql.connector

from mysql.connector import Error


#Task 1: Add a Member

#Write a Python function to add a new member to the 'Members' table in the gym's database.
    # Example code structure
 #   def add_member(id, name, age):
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints
#Expected Outcome: A Python function that successfully adds a new member to the 'Members' table
#  in the gym's database. The function should handle errors gracefully,
#  such as duplicate member IDs or violations of other constraints.

db_name = "fitness_center_db"
user = "root"
password = "Babinz2023!"
host = "localhost"

def add_member(cursor, id, name, age):
    try:
       new_member = (id, name, age)
       query = "INSERT INTO Members(id, name, age) VALUES (%s, %s, %s)"
       
       cursor.execute(query, new_member)
       
       
    except Error as e:
         print(f"An exception occurred: {e}")


def add_workout_session(cursor, member_id, date, duration_minutes, calories_burned):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints
    try:
        new_session = (member_id, date, duration_minutes, calories_burned)
        query = "INSERT INTO WorkoutSessions(member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
       
        cursor.execute(query, new_session)

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred: {e}")



def update_member_age(cursor, member_id, new_age):
        # SQL query to update age
        # Check if member exists
        # Error handling
        try:
            update_member = (member_id, new_age)
            query = "INSERT INTO Members(member_id, age) VALUES (%s, %s)"
       
            cursor.execute(query, update_member)
        
        except mysql.connector.Error as db_err:
            print(f' Database Error: \n {db_err}')
       
        except Exception as e:
            print(f"An exception occurred: {e}")




def delete_workout_session(cursor, session_id):
        # SQL query to delete a session
        # Error handling for non-existent session ID
    try:
        delete_session = (session_id)
        query = "DELETE FROM WorkoutSessions(session_id) VALUES (%s)"
       
        cursor.execute(query, delete_session)
    
    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred: {e}")



def main():
    # establish connection
    conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
            )
    if conn is not None:
        print("*** Welcome to CT Fitness Center Database ***")
        print("Menu: ")
        print("1. Add a Member. ")
        print("2. Add a Workout Session. ")
        print("3. Update Member Age. ")
        print("4. Delete a Workout Session. ")
    
        choice = input("Select an Option (1-4)")

        

        try:
            cursor = conn.cursor()

            if choice == "1":

                id = input("Enter new member id #. ")
                name = input("Enter member name: ")
                age = input("Enter member age: ")

                add_member(cursor, id, name, age)
            
                conn.commit()
            elif choice == "2":

                member_id = input("Enter Member Id: ")
                date = input("Enter a date for Workout: ")
                duration_minutes = input("How long (minutes) is this Session? ")
                calories_burned = input("How many calories will be burned? ")
                

                add_workout_session(member_id, date, duration_minutes, calories_burned)
            
                conn.commit()

            elif choice == "3":

                member_id = input("Enter Member Id: ")
                age = input(f"Enter update age for Member Id: {member_id} ")
               
                update_member_age(member_id, age)
            
                conn.commit()

            elif choice == "4":

                session_id = input("Enter Session Id for Workout to delete: ")
                
               
                delete_workout_session(session_id)
            
                conn.commit()

        except mysql.connector.Error as db_err:
            print(f' Database Error: \n {db_err}')
         
     
        except Exception as e:
            print(f'An exception occurred {e}')

        finally:
            if conn and conn.is_connected():
                conn.close()
                print("MySQL connection closed.")

    

           

if __name__ == "__main__":
     main()