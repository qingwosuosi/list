def merge_range():
    lan_rel={'lan':'python','v':'3.7'}
    rea_al={'why':'hobby','how':'do'}
    d_merage=dict()
    d_merage.update(lan_rel)
    d_merage.update(rea_al)
    desc_list = sorted(dt21s(d_merage),key=lambda x:x[0], reverse=True)
    desc_dict=dict(desc_list)
    asc_list=sorted(dt21s(d_merage),key=lambda x:x[0],reverse=False)
    asc_dict=dict(asc_list)
    print(f'合并后的结果:{d_merage}')
    print(f'按照第0个元素降序排列：{desc_dict}')
    print(f'按照第0个元素升序排列：{asc_dict}')

def dt21s(dic:dict):
    keys=dic.keys()
    values = dic.values()
    lst=[(key,val) for key,val in zip(keys,values)]
    return lst

merge_range()

