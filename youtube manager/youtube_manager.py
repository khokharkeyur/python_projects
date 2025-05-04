import json

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)


def list_all_videos(video):
    for index, video in enumerate(video, start=1):
        print(f"{index}. {video['title']} - {video['time']}")


def add_video(video):
    title = input("Enter the video title: ")
    time = input("Enter the video time: ")
    new_video = {
        "title": title,
        "time": time
    }
    video.append(new_video)
    save_data(video)
    print(f"Video '{title}' added successfully!")

def update_video(video):
    list_all_videos(video)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(video):
        title = input("Enter the new video title: ")
        time = input("Enter the new video time: ")
        video[index]['title'] = title if title else video[index]['title']
        video[index]['time'] = time if time else video[index]['time']
        save_data(video)
        print(f"Video '{title}' updated successfully!")
    else:
        print("Invalid index. Please try again.")

def delete_video(video):
    list_all_videos(video)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 0 <= index < len(video):
        deleted_video = video.pop(index)
        save_data(video)
        print(f"Video '{deleted_video['title']}' deleted successfully!")
    else:
        print("Invalid index. Please try again.")

def main():
    videos = load_data()
    while True:
            print("\n Youtube Manager | choose an option ")
            print("1. List all youtube videos ")
            print("2. Add a youtube video ")    
            print("3. Update a youtube video details ")
            print("4. Delete a youtube video ")
            print("5. Exit the app ")
            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    list_all_videos(videos)
                    # print("Listing all youtube videos...")
                case "2":
                    add_video(videos)
                case '3':
                    update_video(videos)
                case '4':
                    delete_video(videos)
                case '5':
                    break
                case _:
                    print("Invalid Choice")


if __name__ ==  "__main__":
    main() 