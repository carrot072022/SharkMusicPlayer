import cloudinary
import cloudinary.uploader

cloudinary.config( 
    cloud_name = "hoctuvung365", 
    api_key = "749294177453785", 
    api_secret = "WF_2IWs7g3fWq-XdsBSZygJse-Y",
    secure = True
)
# Dashboard: https://cloudinary.com/console/c-d9250c399f733915ed85df04d86bc3

def uploadAndRenderJson(imageFile, audioFile, name, artist):
    url_audio = cloudinary.uploader.upload("audio/" + audioFile, resource_type="video")['secure_url']
    url_image = cloudinary.uploader.upload("images/" + imageFile)['secure_url']
    audio_info = '''{
        name: "'''+ name +'''",
        artist: "'''+ artist.replace("\n", "") +'''",
        cover: "'''+ url_image +'''",
        source: "'''+ url_audio +'''",
        favorited: true
    },
    '''
    open('playlist.txt', 'a').write(audio_info)

with open('listdata.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        imageFile, audioFile, name, artist = line.split('|')
        print(imageFile, audioFile, name, artist)
        uploadAndRenderJson(imageFile, audioFile, name, artist)

# print(cloudinary.uploader.upload("audio/Sao em vô tình - MyShark.mp4", resource_type="video")['secure_url'])