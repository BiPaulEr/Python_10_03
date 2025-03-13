def fonction(r, *args, a = 2, **kwargs):
    print(kwargs)
    print(args)
    print("ok")

dictionnaire = {"ok": "ok", "ok1": "ok2", "r1":6, "t":90}

fonction(3, 4, 5, **dictionnaire) #(4, 5, {'ok': 'ok', 'ok1': 'ok2', 'r': 6, 't': 90})

fonction(3, 4, 5, ok="ok", ok1 = "ok2", r1=6, t = 90)
tu = (1, 2,3,4,5,6,7,8,9,10)
fonction(*tu) #(2, 3, 4, 5, 6, 7, 8, 9, 10)