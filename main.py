import requests

endpoint = "https://tiktok.com/@{username}?is_copy_url=1&is_from_webapp=v1"

username = input("Enter a TikTok username: ")

response = requests.get(endpoint.format(username=username))

def fix_url(url):
    url = url.replace("\\", "/")  # Replace backward slashes with forward slashes
    url = bytes(url, 'utf-8').decode('unicode_escape')  # Decode the characters
    return url

html = response.content.decode("utf-8")
avatarLarger = fix_url(html.split('"avatarLarger":"')[1].split('"')[0])
avatarMedium = fix_url(html.split('"avatarMedium":"')[1].split('"')[0])
avatarThumb = fix_url(html.split('"avatarThumb":"')[1].split('"')[0])
commentSetting = html.split('"commentSetting":')[1].split(",")[0]
downloadSetting = html.split('"downloadSetting":')[1].split(",")[0]
duetSetting = html.split('"duetSetting":')[1].split(",")[0]
ftc = html.split('"ftc":')[1].split(",")[0]
id = html.split('"id":"')[1].split('"')[0]
isADVirtual = html.split('"isADVirtual":')[1].split(",")[0]
isEmbedBanned = html.split('"isEmbedBanned":')[1].split(",")[0]
nickname = html.split('"nickname":"')[1].split('"')[0]
openFavorite = html.split('"openFavorite":')[1].split(",")[0]
privateAccount = html.split('"privateAccount":')[1].split(",")[0]
relation = html.split('"relation":')[1].split(",")[0]
secUid = html.split('"secUid":"')[1].split('"')[0]
secret = html.split('"secret":')[1].split(",")[0]
signature = html.split('"signature":"')[1].split('"')[0]
stitchSetting = html.split('"stitchSetting":')[1].split(",")[0]
ttSeller = html.split('"ttSeller":')[1].split(",")[0]
uniqueId = html.split('"uniqueId":"')[1].split('"')[0]
verified = html.split('"verified":')[1].split(",")[0]
diggCount = html.split('"diggCount":')[1].split(",")[0]
followerCount = html.split('"followerCount":')[1].split(",")[0]
followingCount = html.split('"followingCount":')[1].split(",")[0]
heart = html.split('"heart":')[1].split(",")[0]
heartCount = html.split('"heartCount":')[1].split(",")[0]


json = {
    "avatarLarger": avatarLarger,
    "avatarMedium": avatarMedium,
    "avatarThumb": avatarThumb,
    "commentSetting": commentSetting,
    "downloadSetting": downloadSetting,
    "duetSetting": duetSetting,
    "ftc": ftc,
    "id": id,
    "isADVirtual": isADVirtual,
    "isEmbedBanned": isEmbedBanned,
    "nickname": nickname,
    "openFavorite": openFavorite,
    "privateAccount": privateAccount,
    "relation": relation,
    "secUid": secUid,
    "secret": secret,
    "signature": signature,
    "stitchSetting": stitchSetting,
    "ttSeller": ttSeller,
    "uniqueId": uniqueId,
    "verified": verified,
    "diggCount": diggCount,
    "followerCount": followerCount,
    "followingCount": followingCount,
    "heart": heart,
    "heartCount": heartCount
}

# Print the user's stats
print(json["nickname"])
print(json["uniqueId"])
print(json["followerCount"])
print(json["followingCount"])
print(json["heartCount"])
print(json["avatarThumb"])
