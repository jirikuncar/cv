"""Generate the JK flow SVGs embedded in docs/index.html."""

import math

COLORS = ["pydantic", "veeva", "datadog", "stubhub", "sdsc", "cern", "oss", "pydantic", "orcid", "mdh", "cuni"]


def normal(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy) or 1
    return -dy / n, dx / n


def offset(pts, d):
    out = []
    for j, (x, y, r) in enumerate(pts):
        prev = normal(pts[j - 1], pts[j]) if j else None
        nxt = normal(pts[j], pts[j + 1]) if j < len(pts) - 1 else None
        n1, n2 = prev or nxt, nxt or prev
        mx, my = n1[0] + n2[0], n1[1] + n2[1]
        m = math.hypot(mx, my) or 1
        s = d / max(0.35, (mx * n1[0] + my * n1[1]) / m)
        out.append((x + mx / m * s, y + my / m * s, r, d))
    return out


def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy) or 1
    return dx / n, dy / n, n


def rounded(pts):
    f = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")
    d, length, cur = f"M{f(pts[0][0])} {f(pts[0][1])}", 0.0, pts[0][:2]
    for j in range(1, len(pts) - 1):
        a, p, b = pts[j - 1], pts[j], pts[j + 1]
        u, v = unit(a, p), unit(p, b)
        cross = u[0] * v[1] - u[1] * v[0]
        turn = math.acos(max(-1, min(1, u[0] * v[0] + u[1] * v[1])))
        if abs(cross) < 1e-3 or not p[2]:
            length += math.dist(cur, p[:2])
            cur = p[:2]
            d += f"L{f(p[0])} {f(p[1])}"
            continue
        dd = p[3] if len(p) > 3 else 0
        r = max(2, p[2] - math.copysign(1, cross) * dd)
        t = r * math.tan(turn / 2)
        room = min(u[2], v[2]) / 2
        if t > room:
            t, r = room, room / math.tan(turn / 2)
        s = (p[0] - u[0] * t, p[1] - u[1] * t)
        e = (p[0] + v[0] * t, p[1] + v[1] * t)
        length += math.dist(cur, s) + r * turn
        cur = e
        d += f"L{f(s[0])} {f(s[1])}A{f(r)} {f(r)} 0 0 {1 if cross > 0 else 0} {f(e[0])} {f(e[1])}"
    z = pts[-1]
    length += math.dist(cur, z[:2])
    return d + f"L{f(z[0])} {f(z[1])}", length


def svg(name, ux, uy, gl, g, x0, F, monogram="jk"):
    """Origin is the timeline rail at the bottom edge of the header."""
    yb, top = -F, -F - 10 * uy
    u = min(ux, uy)
    P = lambda x, y, r=0: (x0 + x * ux, top + y * uy, r * u)
    fork, join = yb + F * 0.2, -F * 0.3
    hook = [P(0, 7), P(0, 10, 1.6), P(3.2, 10, 1.6), P(3.2, 0, 0.6)]
    if monogram == "jk":
        xs, xl = x0 + 5.6 * ux, x0 + 9.2 * ux
        mid = (xs + len(COLORS) * gl, top + 5 * uy, 0.4 * u)
        shapes = [(hook + [P(5.6, 0, 0.6), P(5.6, 10)], xs), ([P(9.2, 0), mid, P(9.2, 10, 1)], xl)]
    else:
        xl = x0 + 9.2 * ux
        shapes = [(hook + [P(9.2, 0, 0.2), P(5, 5, 0.4), P(9.2, 10, 1)], xl)]
    out = [f'<svg class="jk jk-{name}" aria-hidden="true">']
    for i, color in enumerate(COLORS):
        lane = (i - (len(COLORS) - 1) / 2) * gl
        tail = [(-(i + 1) * g, join, 30), (-(i + 1) * g, 0, 0)]
        paths = []
        for shape, exit_x in shapes:
            letters = offset(shape, lane)
            full = offset(shape + [(exit_x, fork, 30)], lane) + tail
            _, a = rounded(letters)
            d, total = rounded(full)
            paths.append(f'<path pathLength="1000" style="--a:{a / total * 1000:.0f}" d="{d}"/>')
        out.append(f'<g style="--i:{i};stroke:var(--{color})">{"".join(paths)}</g>')
    out.append("</svg>")
    return "".join(out)


if __name__ == "__main__":
    import sys

    monogram = sys.argv[1] if len(sys.argv) > 1 else "jk"
    half = (len(COLORS) - 1) / 2
    print(svg("wide", 23, 42, 5, 10, -(half + 1) * 10 - 9.2 * 23, 120, monogram))
    print(svg("narrow", 27, 24, 4.5, 4, 12 + half * 4.5, 80, monogram))
