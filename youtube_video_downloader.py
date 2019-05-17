from pytube import YouTube

link = input('enter the link of video you want to be downloaded :  ')
yt = YouTube(link)

videos = yt.streams.all()
# videos = yt.streams.first()

i=1
for stream in videos:
    print(str(i) +" " + ': '+str(stream))
    i+=1

stream_number = int(input('enter the number ,which one you want to download : '))
video = videos[stream_number-1]
video.download()

print('downloaded')