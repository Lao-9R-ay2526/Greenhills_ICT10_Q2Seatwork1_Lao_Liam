from pyscript import display, document

Nickname = [
    'NickName: Ancient Ruins',
    'NickName: The Land Down Under',
    'NickName: Jellyfish Kingdom',
    'NickName: Land of the Long White Cloud',
    'NickName: The Atoll Nation',
    'NickName: Land of the Eight',
    'NickName: Pleasant Island',
    'NickName: Land of the Thousand Worlds',
    'NickName: Happy Isles',
    'NickName: Friendly Islands',
    'NickName: Polynesian Staple',
    'NickName: Soft Coral Capital',
    'NickName: Land of The Happiest People',
    'NickName: Land of the First Sunrise'
]

def showcase(e):

    checked = [
        document.getElementById('micronesia').checked,
        document.getElementById('australia').checked,
        document.getElementById('palau').checked,
        document.getElementById('zealand').checked,
        document.getElementById('marshall').checked,
        document.getElementById('tuvalu').checked,
        document.getElementById('nauru').checked,
        document.getElementById('papua').checked,
        document.getElementById('solomon').checked,
        document.getElementById('tonga').checked,
        document.getElementById('samoa').checked,
        document.getElementById('fiji').checked,
        document.getElementById('vanuatu').checked,
        document.getElementById('kiribati').checked
    ]


    results = [

        Nickname[0] * checked[0],
        Nickname[1] * checked[1],
        Nickname[2] * checked[2],
        Nickname[3] * checked[3],
        Nickname[4] * checked[4],
        Nickname[5] * checked[5],
        Nickname[6] * checked[6],
        Nickname[7] * checked[7],
        Nickname[8] * checked[8],
        Nickname[9] * checked[9],
        Nickname[10] * checked[10],
        Nickname[11] * checked[11],
        Nickname[12] * checked[12],
        Nickname[13] * checked[13],

    ]

    display(results, target='output')