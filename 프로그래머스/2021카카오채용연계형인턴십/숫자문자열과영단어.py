def solution(s):
    answer = s
    alpha = {'0':'zero', '1':'one', '2':'two', '3':'three',
            '4':'four', '5':'five', '6':'six', '7':'seven',
            '8':'eight', '9':'nine'}
    for k, v in alpha.items():
        answer = answer.replace(v, k)
    return int(answer)
