import os
import sys
from boxsdk import JWTAuth, Client

def main(url):
    auth = JWTAuth.from_settings_file("config.json")
    auth.authenticate_instance()
    client = Client(auth)

    web_link_url = url

    user = client.user().get()
    print(f"User: {user.id}:{user.name}")

    shared_folder = client.get_shared_item(web_link_url, "")
    print(f"Shared Folder: {shared_folder.id}:{shared_folder.name}")
    print("#" * 80)

    print("Type\tID\t\tName")
    if not os.path.isdir("downloads"):
        os.makedirs("downloads")
    os.chdir("downloads")
    items = shared_folder.get_items()
    download_items(items)
    os.chdir("..")

def download_items(items):
    for item in items:
        if item.type == "folder":
            if not os.path.exists(item.name):
                os.mkdir(item.name)
            os.chdir(item.name)

            # print the folder name
            print("-" * 80)
            print(f"\n\n{item.type}\t{item.id}\t{item.name}")
            print("-" * 80)

            download_items(item.get_items())
            os.chdir("..")

        if item.type == "file":
            print(f"{item.type}\t{item.id}\t{item.name}", end="")

            with open(item.name, "wb") as download_file:
                item.download_to(download_file)
            print("\tdone")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <shared_box_url>")
        sys.exit(1)
    main(sys.argv[1])
    print("Done")

