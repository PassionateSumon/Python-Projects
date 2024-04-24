
import json

def load_data():
    try:
        with open('YTmanagerProject.txt', 'r') as file:
            return json.load(file)
    except:
        return []
        
def dataSaveHelper(videos):
    with open('YTmanagerProject.txt', 'w') as file:
        json.dump(videos, file)

       
def listAllVideos(videos):
    print('\n')
    print('-' * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('\n')
    print('-' * 50)

def addNewVideo(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    dataSaveHelper(videos)

def updateVideoDetails(videos):
    listAllVideos(videos)
    ind = int(input("Enter the index to update: "))
    if 1 <= ind < len(videos):
       prevTime = videos[ind-1]['time']
       name = input("Enter video name: ")
       time = input("Enter video time: ")
       if time == '': 
           videos[ind-1] = {'name': name, 'time': prevTime}
       else:
           videos[ind-1] = {'name': name, 'time': time}
       dataSaveHelper(videos)
    else:
        print("Invalid index!!")

    
def deleteVideo(videos):
    listAllVideos(videos)
    ind = int(input("Enter the index to delete: "))
    if 1 <= ind < len(videos):
       del videos[ind-1] 
       print("Successfully deleted..")
       dataSaveHelper(videos)
    else:
        print("Invalid index for deleting!!")


def main():
    videos = load_data()
    while True: 
        print("\n YouTube Manager || Choose an option")
        print("1. List all YouTube videos: ")
        print("2. Add a YouTube video: ")
        print("3. Update a YouTube video details: ")
        print("4. Delete a YouTube video: ")
        print("5. Exit: ")
        choice = input("choose an option: ")
        # print(videos)
        
        match choice:
            case '1':
                listAllVideos(videos) 
            case '2':
                addNewVideo(videos)
            case '3':
                updateVideoDetails(videos)
            case '4':
                deleteVideo(videos) 
            case '5':
                break 
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()