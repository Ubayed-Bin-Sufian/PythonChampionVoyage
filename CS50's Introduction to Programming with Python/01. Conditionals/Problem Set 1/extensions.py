def main():

#prompts the user for the name of a file, insensitive
    file_name = input("File name: ").strip().lower()
    extension(file_name)


def extension(file_name):

#outputs image/gif for .gif
    if file_name.endswith(".gif"):
        print("image/gif")

#outputs image/jpeg for .jpg & .jpeg
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print("image/jpeg")

#outputs image/png for .png
    elif file_name.endswith(".png"):
        print("image/png")

#outputs application/pdf for .pdf and application/zip for .zip
    elif file_name.endswith(".pdf"):
        print("application/pdf")

#outputs text/plain for .txt
    elif file_name.endswith(".txt"):
        print("text/plain")

#outputs application/zip for .zip
    elif file_name.endswith(".zip"):
        print("application/zip")

    else:
        print("application/octet-stream")

main()
