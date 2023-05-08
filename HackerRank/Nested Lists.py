if __name__ == '__main__':
    records=[]
    scores=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)

    scores=sorted(list(set(scores)))
    filtered=[]
    for name,score in records:
        if score==scores[1]:
            filtered.append(name)

    filtered=sorted(filtered)
    for name in filtered:
        print(name)