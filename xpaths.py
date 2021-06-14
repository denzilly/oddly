


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
    "cookies" : '//*[id="onetrust-accept-btn-handler"]'
    }

    return xpaths


    

def b_xpaths(div,row):
    xpaths = {
        "email" : '//*[@id="email"]',
        "password" : '//*[@id="password"]',
        "login" : "/html/body/div/div[3]/table/tbody/tr[4]/td[2]/button",
        "market" : f"/html/body/div[3]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div/div[{div}]/div[2]/div[{row}]/table/tbody/tr/td[1]/div",
        "bid" : f"/html/body/div[3]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div/div[{div}]/div[2]/div[{row}]/table/tbody/tr/td[4]/div/span",
        "offer":f"/html/body/div[3]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div/div[{div}]/div[2]/div[{row}]/table/tbody/tr/td[5]/div/span"
    }

    return xpaths



def m_insert_q(nr,new_id,now):

    query = f"""
    
INSERT INTO MARKET_DATA(
id,
time,
ASIAN_STRIKE_CALL_OPTION_TOTAL_GOALS_BID,
ASIAN_STRIKE_CALL_OPTION_TOTAL_GOALS_OFFER,
AUSTRIA_BID,
AUSTRIA_OFFER,
BELGIUM_BID,
BELGIUM_OFFER,
CALL_OPTION_100_ON_TOTAL_GOALS_BID,
CALL_OPTION_100_ON_TOTAL_GOALS_OFFER,
CALL_OPTION_110_ON_TOTAL_GOALS_BID,
CALL_OPTION_110_ON_TOTAL_GOALS_OFFER,
CALL_OPTION_120_ON_TOTAL_GOALS_BID,
CALL_OPTION_120_ON_TOTAL_GOALS_OFFER,
CALL_OPTION_130_ON_TOTAL_GOALS_BID,
CALL_OPTION_130_ON_TOTAL_GOALS_OFFER,
CALL_OPTION_140_ON_TOTAL_GOALS_BID,
CALL_OPTION_140_ON_TOTAL_GOALS_OFFER,
CALL_OPTION_150_ON_TOTAL_GOALS_BID,
CALL_OPTION_150_ON_TOTAL_GOALS_OFFER,
CROATIA_BID,
CROATIA_OFFER,
CZECH_REPUBLIC_BID,
CZECH_REPUBLIC_OFFER,
DENMARK_BID,
DENMARK_OFFER,
ENGLAND_BID,
ENGLAND_OFFER,
FINLAND_BID,
FINLAND_OFFER,
FRANCE_BID,
FRANCE_OFFER,
GERMANY_BID,
GERMANY_OFFER,
GROUP_A_BID,
GROUP_A_OFFER,
GROUP_B_BID,
GROUP_B_OFFER,
GROUP_C_BID,
GROUP_C_OFFER,
GROUP_D_BID,
GROUP_D_OFFER,
GROUP_E_BID,
GROUP_E_OFFER,
GROUP_F_BID,
GROUP_F_OFFER,
HUNGARY_BID,
HUNGARY_OFFER,
ITALY_BID,
ITALY_OFFER,
NETHERLANDS_BID,
NETHERLANDS_OFFER,
NORTH_MACEDONIA_BID,
NORTH_MACEDONIA_OFFER,
POLAND_BID,
POLAND_OFFER,
PORTUGAL_BID,
PORTUGAL_OFFER,
RED_CARDS_BID,
RED_CARDS_OFFER,
RUSSIA_BID,
RUSSIA_OFFER,
SCOTLAND_BID,
SCOTLAND_OFFER,
SLOVAKIA_BID,
SLOVAKIA_OFFER,
SPAIN_BID,
SPAIN_OFFER,
SWEDEN_BID,
SWEDEN_OFFER,
SWITZERLAND_BID,
SWITZERLAND_OFFER,
TOTAL_GOALS_ALL_GAMES_EC2021_BID,
TOTAL_GOALS_ALL_GAMES_EC2021_OFFER,
TURKEY_BID,
TURKEY_OFFER,
UKRAINE_BID,
UKRAINE_OFFER,
WALES_BID,
WALES_OFFER,
YELLOW_CARDS_BID,
YELLOW_CARDS_OFFER)

VALUES (
{new_id},
'{now}',
'{nr["ASIAN_STRIKE_CALL_OPTION_TOTAL_GOALS_BID"]}',
'{nr["ASIAN_STRIKE_CALL_OPTION_TOTAL_GOALS_OFFER"]}',
'{nr["AUSTRIA_BID"]}',
'{nr["AUSTRIA_OFFER"]}',
'{nr["BELGIUM_BID"]}',
'{nr["BELGIUM_OFFER"]}',
'{nr["CALL_OPTION_100_ON_TOTAL_GOALS_BID"]}',
'{nr["CALL_OPTION_100_ON_TOTAL_GOALS_OFFER"]}',
'{nr["CALL_OPTION_110_ON_TOTAL_GOALS_BID"]}',
'{nr["CALL_OPTION_110_ON_TOTAL_GOALS_OFFER"]}',
'{nr["CALL_OPTION_120_ON_TOTAL_GOALS_BID"]}',
'{nr["CALL_OPTION_120_ON_TOTAL_GOALS_OFFER"]}',
'{nr["CALL_OPTION_130_ON_TOTAL_GOALS_BID"]}',
'{nr["CALL_OPTION_130_ON_TOTAL_GOALS_OFFER"]}',
'{nr["CALL_OPTION_140_ON_TOTAL_GOALS_BID"]}',
'{nr["CALL_OPTION_140_ON_TOTAL_GOALS_OFFER"]}',
'{nr["CALL_OPTION_150_ON_TOTAL_GOALS_BID"]}',
'{nr["CALL_OPTION_150_ON_TOTAL_GOALS_OFFER"]}',
'{nr["CROATIA_BID"]}',
'{nr["CROATIA_OFFER"]}',
'{nr["CZECH_REPUBLIC_BID"]}',
'{nr["CZECH_REPUBLIC_OFFER"]}',
'{nr["DENMARK_BID"]}',
'{nr["DENMARK_OFFER"]}',
'{nr["ENGLAND_BID"]}',
'{nr["ENGLAND_OFFER"]}',
'{nr["FINLAND_BID"]}',
'{nr["FINLAND_OFFER"]}',
'{nr["FRANCE_BID"]}',
'{nr["FRANCE_OFFER"]}',
'{nr["GERMANY_BID"]}',
'{nr["GERMANY_OFFER"]}',
'{nr["GROUP_A_BID"]}',
'{nr["GROUP_A_OFFER"]}',
'{nr["GROUP_B_BID"]}',
'{nr["GROUP_B_OFFER"]}',
'{nr["GROUP_C_BID"]}',
'{nr["GROUP_C_OFFER"]}',
'{nr["GROUP_D_BID"]}',
'{nr["GROUP_D_OFFER"]}',
'{nr["GROUP_E_BID"]}',
'{nr["GROUP_E_OFFER"]}',
'{nr["GROUP_F_BID"]}',
'{nr["GROUP_F_OFFER"]}',
'{nr["HUNGARY_BID"]}',
'{nr["HUNGARY_OFFER"]}',
'{nr["ITALY_BID"]}',
'{nr["ITALY_OFFER"]}',
'{nr["NETHERLANDS_BID"]}',
'{nr["NETHERLANDS_OFFER"]}',
'{nr["NORTH_MACEDONIA_BID"]}',
'{nr["NORTH_MACEDONIA_OFFER"]}',
'{nr["POLAND_BID"]}',
'{nr["POLAND_OFFER"]}',
'{nr["PORTUGAL_BID"]}',
'{nr["PORTUGAL_OFFER"]}',
'{nr["RED_CARDS_BID"]}',
'{nr["RED_CARDS_OFFER"]}',
'{nr["RUSSIA_BID"]}',
'{nr["RUSSIA_OFFER"]}',
'{nr["SCOTLAND_BID"]}',
'{nr["SCOTLAND_OFFER"]}',
'{nr["SLOVAKIA_BID"]}',
'{nr["SLOVAKIA_OFFER"]}',
'{nr["SPAIN_BID"]}',
'{nr["SPAIN_OFFER"]}',
'{nr["SWEDEN_BID"]}',
'{nr["SWEDEN_OFFER"]}',
'{nr["SWITZERLAND_BID"]}',
'{nr["SWITZERLAND_OFFER"]}',
'{nr["TOTAL_GOALS_ALL_GAMES_EC2021_BID"]}',
'{nr["TOTAL_GOALS_ALL_GAMES_EC2021_OFFER"]}',
'{nr["TURKEY_BID"]}',
'{nr["TURKEY_OFFER"]}',
'{nr["UKRAINE_BID"]}',
'{nr["UKRAINE_OFFER"]}',
'{nr["WALES_BID"]}',
'{nr["WALES_OFFER"]}',
'{nr["YELLOW_CARDS_BID"]}',
'{nr["YELLOW_CARDS_OFFER"]}'

)

    """

    return query