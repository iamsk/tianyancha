from tianyancha import Tianyancha

if __name__ == '__main__':
    t = Tianyancha('')
    for k, v in t.api_mappings.items():
        print('#### {}'.format(v['name']))
        print('\n')
        print('*', 'method: ', k)
        for kk, vv in v.items():
            print('*', kk, vv)
        print('\n')
