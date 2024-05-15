import subprocess


def backup_mysql_database(
    mysql_dump_path, hostname, username, password, database, output_file_path
):
    # Construct the command
    command = [
        mysql_dump_path,
        f"--host={hostname}",
        f"--user={username}",
        f"--password={password}",
        database,
    ]

    # Redirect output to file
    with open(output_file_path, "w") as output_file:
        # Start the process
        process = subprocess.Popen(command, stdout=output_file, stderr=subprocess.PIPE)

        # Wait for process to complete
        _, error_output = process.communicate()
        exit_code = process.wait()

        if exit_code != 0:
            raise RuntimeError(
                f"Failed to execute mysqldump command. Exit code: {exit_code}, Error: {error_output.decode('utf-8')}"
            )


if __name__ == "__main__":
    mysql_dump_path = "C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysqldump"
    hostname = "localhost"
    username = "root"
    password = "1111"
    database = "my_database"
    output_file_path = "ADS_ISE2.sql"

    try:
        backup_mysql_database(
            mysql_dump_path, hostname, username, password, database, output_file_path
        )
        print("Backup completed successfully.")
    except Exception as e:
        print("Error:", e)
