import numpy as np
import population


def extract_pop(combinepop, options):
    # prefon = options["pre_fon"]  # idk what it is
    popsize = len(combinepop) // 2
    # rank = np.concatenate([ind["rank"] for ind in combinepop])
    rank = np.vstack([individual["rank"] for individual in combinepop])
    distance = np.vstack([individual["distance"] for individual in combinepop])
    pref = np.vstack([individual["pref"] for individual in combinepop])
    idx = np.arange(1, popsize * 2 + 1)

    # irpPd = np.column_stack((np.arange(len(combinepop)) * 2 + 1, rank, pref, distance))
    # irpPd = irpPd[np.lexsort((irpPd[:, 2], -irpPd[:, 3]))]
    # nextpop = [combinepop[i.astype(int)] for i in irpPd[:len(combinepop) // 2, 0]]

    irpPd = np.column_stack((idx, rank, pref, distance))
    # irpPd = irpPd[np.lexsort([2, -3, -4])]
    irpPd_sorted = irpPd[np.lexsort((irpPd[:, 2], irpPd[:, 1]), axis=0)][::-1]

    indices = irpPd_sorted[:popsize, 0].astype(int)
    nextpop = [combinepop[i - 1] for i in indices]
    nextpop = np.array(nextpop)
    # nextpop = combinepop(irpPd(1:popsize, 1));

    return nextpop


'''
    if prefon == 1:
        irpPd = np.column_stack((idx, rank, pref, distance))
        irpPd = irpPd[np.lexsort((distance, pref, rank,x))]
    else:
        irpPd = np.column_stack((idx, rank, distance))
        irpPd = irpPd[np.lexsort((distance, rank, idx))]


    return nextpop


prefon = opt.prefon;
popsize = length(combinepop) / 2;
rank = vertcat(combinepop.rank);
distance = vertcat(combinepop.distance);                                  % crowding distance is the third sorting criteria 
pref = vertcat(combinepop.pref);                                          % preference is the second sorting criteria
idx=[1:popsize*2]';
if prefon == 1
    % with pref
    irpPd=[idx, rank, pref, distance];
    irpPd=sortrows(irpPd, [2,-3,-4]);
else
    % without pref
    irpPd=[idx, rank, distance];
    irpPd=sortrows(irpPd, [2,-3]);
end
nextpop = combinepop(irpPd(1:popsize,1));
'''
