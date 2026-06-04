import random

def generate_captcha():
    d = list(range(10))
    ds = list(map(str, d))

    a = [chr(i) for i in range(65,91)]
    
    li_ds = random.choices(ds, k=2)
    li_a = random.choices(a, k=2)
    
    li_capt = li_a + li_ds
    random.shuffle(li_capt)
    capt = '  '.join(li_capt)
    return capt

def generate_password():
    d = list(range(10))
    ds = list(map(str, d))

    a = [chr(i) for i in range(65,91)]
    
    li_ds = random.choices(ds, k=3)
    li_a = random.choices(a, k=3)
    
    li_pasw = li_a + li_ds
    random.shuffle(li_pasw)
    pasw = ''.join(li_pasw)
    return pasw