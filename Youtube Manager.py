
import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test= json.load(file)
            #print(test)
            return test
    except FileNotFoundError:
        return[]
    


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):    
        print(f"{index}. {video['name']}, Duration:{video['time']}")
    print("\n")
    print("*" * 70)


def add_video(videos):
      name=input("enter video name:")
      time=input("enter video time:")
      videos.append({'name':name, 'time':time})
      save_data_helper(videos)

def update_video(videos):
      list_all_videos(videos)
      index=int(input("Enter the video number to update"))
      if 1<= index <=len(videos):
          name=input("Enter the New Video Name")
          time=input("Enter the New Video Time")
          videos[index-1]={'name':name, 'time':time}
          save_data_helper(videos)
      else:
          print("Invalid index Selected")



def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the Video Number to be Deleted"))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video selected")


def main():

    videos=load_data()

    while True:
        print("\n Youtube Manager")
        print("1. List all YouTube Video")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete Youtube Video")
        print("5. Exit the App")
        choice=input("Enter Your Choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()

