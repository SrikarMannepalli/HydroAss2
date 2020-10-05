def normalizeQValue(ph=7, temperature=30,turbidity=0, tds=0, nitrates=0, eColi=0):

    normalized_QValue_EColi = 0
    if eColi >= 0 and eColi < 1:
        normalized_QValue_EColi = 98
    elif eColi >= 1 and eColi < 2:
        normalized_QValue_EColi = 89
    elif eColi >= 2 and eColi < 5:
        normalized_QValue_EColi = 80
    elif eColi >= 5 and eColi < 10:
        normalized_QValue_EColi = 71
    elif eColi >= 10 and eColi < 20:
        normalized_QValue_EColi = 63
    elif eColi >= 20 and eColi < 50:
        normalized_QValue_EColi = 53
    elif eColi >= 50 and eColi < 100:
        normalized_QValue_EColi = 45
    elif eColi >= 100 and eColi < 200:
        normalized_QValue_EColi = 37
    elif eColi >= 200 and eColi < 500:
        normalized_QValue_EColi = 27
    elif eColi >= 500 and eColi < 1000:
        normalized_QValue_EColi = 22
    elif eColi >= 1000 and eColi < 2000:
        normalized_QValue_EColi = 18
    elif eColi >= 2000 and eColi < 5000:
        normalized_QValue_EColi = 13
    elif eColi >= 5000 and eColi < 10000:
        normalized_QValue_EColi = 10
    elif eColi >= 10000 and eColi < 20000:
        normalized_QValue_EColi = 8
    elif eColi >= 20000 and eColi < 50000:
        normalized_QValue_EColi = 5
    elif eColi >= 50000 and eColi < 100000:
        normalized_QValue_EColi = 3
    elif eColi >= 100000:
        normalized_QValue_EColi = 2

    normalized_QValue_ph = 0
    if (ph >= 0 and ph < 2) or (ph > 12 and ph <= 14):
        normalized_QValue_ph = 0
    elif (ph >= 2 and ph < 3) or (ph > 11 and ph <= 12):
        normalized_QValue_ph = 2
    elif ph >= 3 and ph < 4:
        normalized_QValue_ph = 4
    elif ph >= 4 and ph < 5:
        normalized_QValue_ph = 8
    elif ph >= 4 and ph < 5:
        normalized_QValue_ph = 24
    elif ph >= 5 and ph < 6:
        normalized_QValue_ph = 55
    elif ph >= 6 and ph < 7:
        normalized_QValue_ph = 90
    elif ph >= 7 and ph < 7.2:
        normalized_QValue_ph = 92
    elif ph >= 7.2 and ph < 7.5:
        normalized_QValue_ph = 93
    elif ph >= 7.5 and ph < 7.7:
        normalized_QValue_ph = 90
    elif ph >= 7.7 and ph < 8:
        normalized_QValue_ph = 82
    elif ph >= 8 and ph < 8.5:
        normalized_QValue_ph = 67
    elif ph >= 8.5 and ph < 9:
        normalized_QValue_ph = 47
    elif ph >= 9 and ph < 10:
        normalized_QValue_ph = 19
    elif ph >= 10 and ph < 11:
        normalized_QValue_ph = 7

    normalized_QValue_temp = 0
    if temperature < -10:
        normalized_QValue_temp = 56
    elif temperature >= -10 and temperature < -7.5:
        normalized_QValue_temp = 63
    elif temperature >= -7.5 and temperature < -5:
        normalized_QValue_temp = 73
    elif temperature >= -5 and temperature < -2.5:
        normalized_QValue_temp = 85
    elif temperature >= -2.5 and temperature < -1:
        normalized_QValue_temp = 90
    elif temperature >= -1 and temperature < 0:
        normalized_QValue_temp = 93
    elif temperature >= 0 and temperature < 1:
        normalized_QValue_temp = 89
    elif temperature >= 1 and temperature < 2.5:
        normalized_QValue_temp = 85
    elif temperature >= 2.5 and temperature < 5:
        normalized_QValue_temp = 72
    elif temperature >= 5 and temperature < 7.5:
        normalized_QValue_temp = 57
    elif temperature >= 7.5 and temperature < 10:
        normalized_QValue_temp = 44
    elif temperature >= 10 and temperature < 12.5:
        normalized_QValue_temp = 36
    elif temperature >= 12.5 and temperature < 15:
        normalized_QValue_temp = 28
    elif temperature >= 15 and temperature < 17.5:
        normalized_QValue_temp = 23
    elif temperature >= 17.5 and temperature < 20:
        normalized_QValue_temp = 21
    elif temperature >= 20 and temperature < 22.5:
        normalized_QValue_temp = 18
    elif temperature >= 22.5 and temperature < 25:
        normalized_QValue_temp = 15
    elif temperature >= 25 and temperature < 27.5:
        normalized_QValue_temp = 12
    elif temperature >= 27.5 and temperature < 30:
        normalized_QValue_temp = 10

    normalized_QValue_tds = 0
    if tds < 0:
        normalized_QValue_tds = 99
    elif tds >= 0 and tds < 50:
        normalized_QValue_tds = 85
    elif tds >= 50 and tds < 100:
        normalized_QValue_tds = 82
    elif tds >= 100 and tds < 150:
        normalized_QValue_tds = 80
    elif tds >= 150 and tds < 450:
        normalized_QValue_tds = 100 - (tds*40)/300
    elif tds >= 450 and tds <= 600:
        normalized_QValue_tds = 130 - (tds*30)/150
    else:
        normalized_QValue_tds = 10
 
    

    normalized_QValue_nitrates = 0
    if nitrates < 0:
        normalized_QValue_nitrates = 98
    elif nitrates >= 0 and nitrates < 0.25:
        normalized_QValue_nitrates = 97
    elif nitrates >= 0.25 and nitrates < 0.5:
        normalized_QValue_nitrates = 96
    elif nitrates >= 0.5 and nitrates < 0.75:
        normalized_QValue_nitrates = 95
    elif nitrates >= 0.75 and nitrates < 1:
        normalized_QValue_nitrates = 94
    elif nitrates >= 1 and nitrates < 1.5:
        normalized_QValue_nitrates = 92
    elif nitrates >= 1.5 and nitrates < 2:
        normalized_QValue_nitrates = 90
    elif nitrates >= 2 and nitrates < 3:
        normalized_QValue_nitrates = 85
    elif nitrates >= 3 and nitrates < 4:
        normalized_QValue_nitrates = 70
    elif nitrates >= 4 and nitrates < 5:
        normalized_QValue_nitrates = 65
    elif nitrates >= 5 and nitrates < 10:
        normalized_QValue_nitrates = 51
    elif nitrates >= 10 and nitrates < 15:
        normalized_QValue_nitrates = 43
    elif nitrates >= 15 and nitrates < 20:
        normalized_QValue_nitrates = 37
    elif nitrates >= 20 and nitrates < 30:
        normalized_QValue_nitrates = 24
    elif nitrates >= 30 and nitrates < 40:
        normalized_QValue_nitrates = 17
    elif nitrates >= 40 and nitrates < 50:
        normalized_QValue_nitrates = 7
    elif nitrates >= 50 and nitrates < 60:
        normalized_QValue_nitrates = 5
    elif nitrates >= 60 and nitrates < 70:
        normalized_QValue_nitrates = 4
    elif nitrates >= 70 and nitrates < 80:
        normalized_QValue_nitrates = 3
    elif nitrates >= 80 and nitrates < 90:
        normalized_QValue_nitrates = 2
    elif nitrates >= 90:
        normalized_QValue_nitrates = 1

    normalized_QValue_turbidity = 0
    if turbidity < 0:
        normalized_QValue_turbidity = 97
    elif turbidity >= 0 and turbidity < 5:
        normalized_QValue_turbidity = 84
    elif turbidity >= 5 and turbidity < 10:
        normalized_QValue_turbidity = 76
    elif turbidity >= 10 and turbidity < 15:
        normalized_QValue_turbidity = 68
    elif turbidity >= 15 and turbidity < 20:
        normalized_QValue_turbidity = 62
    elif turbidity >= 20 and turbidity < 25:
        normalized_QValue_turbidity = 57
    elif turbidity >= 25 and turbidity < 30:
        normalized_QValue_turbidity = 53
    elif turbidity >= 30 and turbidity < 35:
        normalized_QValue_turbidity = 48
    elif turbidity >= 35 and turbidity < 40:
        normalized_QValue_turbidity = 45
    elif turbidity >= 40 and turbidity < 50:
        normalized_QValue_turbidity = 39
    elif turbidity >= 50 and turbidity < 60:
        normalized_QValue_turbidity = 34
    elif turbidity >= 60 and turbidity < 70:
        normalized_QValue_turbidity = 28
    elif turbidity >= 70 and turbidity < 80:
        normalized_QValue_turbidity = 25
    elif turbidity >= 80 and turbidity < 90:
        normalized_QValue_turbidity = 22
    elif turbidity >= 90 and turbidity < 100:
        normalized_QValue_turbidity = 17
    elif turbidity >= 100:
        normalized_QValue_turbidity = 5

    return [
        normalized_QValue_ph,
        normalized_QValue_temp,
        normalized_QValue_turbidity,
        normalized_QValue_tds,
        normalized_QValue_nitrates,
        normalized_QValue_EColi
    ]
