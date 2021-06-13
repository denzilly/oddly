


def get_xpaths(row):
    xpaths = []
    #xpath for country name, since order changes
    xpaths.append(f"/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/section/div/div/div[2]/table/tbody/tr[{row}]/td[1]/span[2]/span/div/a[1]")

    #xpaths for the odds of first 10 bookies
    for x in range(2,12):
        xpaths.append(f"/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/section/div/div/div[2]/table/tbody/tr[{row}]/td[{x}]/p")


    return xpaths



def p_xpaths(item):
    xpaths = {
    "country" : f"/html/body/page-container/div/main/div/competition-page/div/div[2]/div/div[1]/div/outright-coupon/div/outright-coupon-card-items/div[1]/abc-card/div/div/abc-card-content/abc-accordion/div/section/outright-item-grid-list/div/outright-item[{item}]/div/div[1]/p",
    "odds" : f"/html/body/page-container/div/main/div/competition-page/div/div[2]/div/div[1]/div/outright-coupon/div/outright-coupon-card-items/div[1]/abc-card/div/div/abc-card-content/abc-accordion/div/section/outright-item-grid-list/div/outright-item[{item}]/div/div[2]/abc-btn-odds/abc-button/div/div[2]/ng-transclude/span",
    "showall" : "/html/body/page-container/div/main/div/competition-page/div/div[2]/div/div[1]/div/outright-coupon/div/outright-coupon-card-items/div[1]/abc-card/div/div/abc-card-content/abc-accordion/div/section/outright-item-grid-list/abc-link/a/span",
    "cookies" : '//*[@id="onetrust-accept-btn-handler"]'
    }

    return xpaths


    