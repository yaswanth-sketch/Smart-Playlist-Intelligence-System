playlist = []
n = int(input("Enter number of songs: "))

for i in range(n):
    value = int(input("Enter duration in seconds: "))
    playlist.append(value)
invalid = False
for d in playlist:
    if d <= 0:
        invalid = True
        break
if invalid:
    print("Invalid playlist: Contains invalid duration")
else:
    total_duration = 0
    for d in playlist:
        total_duration = total_duration + d
    num_songs = len(playlist)
    category = ""
    recommendation = ""
    if total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Add more songs"
    elif total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Reduce playlist length"
    else:
        repetitive = False
        for i in range(len(playlist)):
            count = 0
            for j in range(len(playlist)):
                if playlist[i] == playlist[j]:
                    count = count + 1
            if count > 1:
                repetitive = True
                break
        if repetitive:
            category = "Repetitive Playlist"
            recommendation = "Add variety"
        else:
            min_val = playlist[0]
            max_val = playlist[0]
            for d in playlist:
                if d < min_val:
                    min_val = d
                if d > max_val:
                    max_val = d
            if (max_val - min_val) <= 300:
                category = "Balanced Playlist"
                recommendation = "Good listening session"
            else:
                category = "Irregular Playlist"
                recommendation = "Adjust songs"
    print("Total Duration:", total_duration, "seconds")
    print("Songs:", num_songs)
    print("Category:", category)
    print("Recommendation:", recommendation)