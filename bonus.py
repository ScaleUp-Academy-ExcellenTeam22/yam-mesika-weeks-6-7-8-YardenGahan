from datetime import datetime


def read_line(file_path, line_num)-> str:
    """
    this functions pens input file and returns the wanted line.
    @param: file_path: a path to a file
    @param line_num: number of a wanted line from the file
    @return: line from the file
    try:
        with open(file_path, 'r') as input_file:
            content = input_file.readlines()
            return content[line_num - 1]
    except FileNotFoundError:
        write_error_to_file(f"Couldn't open the file: {file_path}.")
    except OSError:
        write_error_to_file(f"The path '{file_path}' is invalid.")
    except EOFError:
        write_error_to_file(f"End of file! Nothing left to read")
        input_file.close()
    except IndexError:
        write_error_to_file(f"The file only has {len(content)} rows!")
        input_file.close()
    except Exception as unknown:
        write_error_to_file(unknown.__str__())
        input_file.close()
    finally:
        input_file.close()


def write_error_to_file(error_message):
    # Prints the exception to the files including the message and time stamp
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open('log.txt', 'a') as errors:
        errors.write(f'{error_message} {dt_string} \n')
        
