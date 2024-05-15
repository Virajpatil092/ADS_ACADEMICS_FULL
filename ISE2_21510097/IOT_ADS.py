import pymysql
import schedule
import time

# Define the connection parameters
main_connection_params = {
    "host": "localhost",
    "user": "root",
    "password": "1111",
    "database": "ads_ise",
}


# Execute SQL statement to insert IoT data
def dump_iot_data():
    try:
        # Connect to MySQL database
        with pymysql.connect(**main_connection_params) as connection_main:
            with connection_main.cursor() as cursor_main:
                # Fetch data from lot_data table
                sql_lot_data = "SELECT timestamp, value, location, status FROM lot_data"
                cursor_main.execute(sql_lot_data)
                lot_data = cursor_main.fetchall()

                # Insert data into iot_data_table
                for data in lot_data:
                    timestamp, value, location, status = data
                    sql_insert = "INSERT INTO iot_data_table (timestamp, value, location, status) VALUES (%s, %s, %s, %s)"
                    cursor_main.execute(
                        sql_insert, (timestamp, value, location, status)
                    )

        print("IoT data dumped into the database successfully")

    except Exception as e:
        print(f"Error: {e}")


# Define the scheduler
def schedule_task():
    # Schedule the dump_iot_data function to run every 10 seconds
    schedule.every(10).seconds.do(dump_iot_data)

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)


# Start the scheduler
schedule_task()
