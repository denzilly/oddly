


def get_xpaths(row):
    xpaths = []
    #xpath for country name, since order changes
    xpaths.append(f"/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/section/div/div/div[2]/table/tbody/tr[{row}]/td[1]/span[2]/span/div/a[1]")

    #xpaths for the odds of first 10 bookies
    for x in range(2,12):
        xpaths.append(f"/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/section/div/div/div[2]/table/tbody/tr[{row}]/td[{x}]/p")


    return xpaths
