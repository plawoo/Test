with open('message.txt', 'r', encoding='utf-8') as mf, open('message_tr.txt', 'w', encoding='utf-8') as mf_new:
    for line in mf.readlines():
        data = line.strip()
        if len(data) != 0:
            mf_new.write(data)
            mf_new.write('\n')