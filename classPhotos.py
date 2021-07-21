def classPhotos(redShirtHeights, blueShirtHeights):
    iterator = 0
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[iterator] == blueShirtHeights[iterator]:
        return False
    elif redShirtHeights[iterator] > blueShirtHeights[iterator]:
        for x in redShirtHeights:
            if x <= blueShirtHeights[iterator]:
                return False
            else:
                iterator += 1
    else:
        if redShirtHeights[iterator] < blueShirtHeights[iterator]:
            for x in redShirtHeights:
                if x >= blueShirtHeights[iterator]:
                    return False
                else:
                    iterator += 1

    return True
