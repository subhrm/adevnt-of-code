from collections import defaultdict


def make_graph(edges):
    g = defaultdict(set)
    for a, b in edges:
        g[a].add(b)
    return g


def solve_part_a(g, sequences) -> int:
    res = 0
    bad_seqs = []
    for seq in sequences:
        good_seq = True
        prev = set()
        for a in seq:
            succesors = g[a]
            if len(prev & succesors) > 0:
                good_seq = False
                break
            prev.add(a)

        if good_seq:
            res += seq[len(seq) // 2]
        else:
            bad_seqs.append(seq)

    print(f"{len(bad_seqs)=}")
    return res, bad_seqs


def solve_part_b(g, bad_seqs):
    res = 0

    for seq in bad_seqs:
        n = len(seq)
        prev = set()
        for i in range(n):
            a = seq[i]
            succesors = g[a]
            conflicts = prev & succesors
            if conflicts:
                idx = min([seq.index(c) for c in conflicts])
                seq.pop(i)
                seq.insert(idx, a)

            prev.add(a)

        res += seq[n // 2]

    return res


def process_file(file_path: str) -> int:
    print(f"Processing {file_path=}")
    edges = []
    sequences = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                a, b = map(int, line.split("|"))
                edges.append((a, b))
            elif len(line) > 0:
                seq = list(map(int, line.split(",")))
                sequences.append(seq)

    print(f"{len(edges)=} {len(sequences)=}")
    g = make_graph(edges)
    res_part_a, bad_seqs = solve_part_a(g, sequences)
    res_part_b = solve_part_b(g, bad_seqs)
    return res_part_a, res_part_b


if __name__ == "__main__":
    print(process_file("example_05.txt"))
    print(process_file("input_05.txt"))
