#!/usr/bin/env python3
from __future__ import annotations

import os
import struct
import zlib


FONT_5X7: dict[str, list[int]] = {
    " ": [0, 0, 0, 0, 0, 0, 0],
    ".": [0, 0, 0, 0, 0, 0b01100, 0b01100],
    ":": [0, 0b01100, 0b01100, 0, 0b01100, 0b01100, 0],
    "+": [0, 0b00100, 0b00100, 0b11111, 0b00100, 0b00100, 0],
    "-": [0, 0, 0, 0b11111, 0, 0, 0],
    ">": [0b10000, 0b01000, 0b00100, 0b00010, 0b00100, 0b01000, 0b10000],
    "/": [0b10000, 0b01000, 0b00100, 0b00010, 0b00001, 0, 0],
    "0": [0b01110, 0b10001, 0b10011, 0b10101, 0b11001, 0b10001, 0b01110],
    "1": [0b00100, 0b01100, 0b00100, 0b00100, 0b00100, 0b00100, 0b01110],
    "2": [0b01110, 0b10001, 0b00001, 0b00010, 0b00100, 0b01000, 0b11111],
    "3": [0b11110, 0b00001, 0b00001, 0b01110, 0b00001, 0b00001, 0b11110],
    "4": [0b00010, 0b00110, 0b01010, 0b10010, 0b11111, 0b00010, 0b00010],
    "5": [0b11111, 0b10000, 0b10000, 0b11110, 0b00001, 0b00001, 0b11110],
    "6": [0b01110, 0b10000, 0b10000, 0b11110, 0b10001, 0b10001, 0b01110],
    "7": [0b11111, 0b00001, 0b00010, 0b00100, 0b01000, 0b01000, 0b01000],
    "8": [0b01110, 0b10001, 0b10001, 0b01110, 0b10001, 0b10001, 0b01110],
    "9": [0b01110, 0b10001, 0b10001, 0b01111, 0b00001, 0b00001, 0b01110],
    "A": [0b01110, 0b10001, 0b10001, 0b11111, 0b10001, 0b10001, 0b10001],
    "B": [0b11110, 0b10001, 0b10001, 0b11110, 0b10001, 0b10001, 0b11110],
    "C": [0b01110, 0b10001, 0b10000, 0b10000, 0b10000, 0b10001, 0b01110],
    "D": [0b11110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b11110],
    "E": [0b11111, 0b10000, 0b10000, 0b11110, 0b10000, 0b10000, 0b11111],
    "F": [0b11111, 0b10000, 0b10000, 0b11110, 0b10000, 0b10000, 0b10000],
    "G": [0b01110, 0b10001, 0b10000, 0b10111, 0b10001, 0b10001, 0b01110],
    "H": [0b10001, 0b10001, 0b10001, 0b11111, 0b10001, 0b10001, 0b10001],
    "I": [0b01110, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b01110],
    "J": [0b00111, 0b00010, 0b00010, 0b00010, 0b10010, 0b10010, 0b01100],
    "K": [0b10001, 0b10010, 0b10100, 0b11000, 0b10100, 0b10010, 0b10001],
    "L": [0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b11111],
    "M": [0b10001, 0b11011, 0b10101, 0b10101, 0b10001, 0b10001, 0b10001],
    "N": [0b10001, 0b11001, 0b10101, 0b10011, 0b10001, 0b10001, 0b10001],
    "O": [0b01110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110],
    "P": [0b11110, 0b10001, 0b10001, 0b11110, 0b10000, 0b10000, 0b10000],
    "Q": [0b01110, 0b10001, 0b10001, 0b10001, 0b10101, 0b10010, 0b01101],
    "R": [0b11110, 0b10001, 0b10001, 0b11110, 0b10100, 0b10010, 0b10001],
    "S": [0b01111, 0b10000, 0b10000, 0b01110, 0b00001, 0b00001, 0b11110],
    "T": [0b11111, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100],
    "U": [0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110],
    "V": [0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01010, 0b00100],
    "W": [0b10001, 0b10001, 0b10001, 0b10101, 0b10101, 0b10101, 0b01010],
    "X": [0b10001, 0b10001, 0b01010, 0b00100, 0b01010, 0b10001, 0b10001],
    "Y": [0b10001, 0b10001, 0b01010, 0b00100, 0b00100, 0b00100, 0b00100],
    "Z": [0b11111, 0b00001, 0b00010, 0b00100, 0b01000, 0b10000, 0b11111],
}


def clamp(v: int) -> int:
    return 0 if v < 0 else 255 if v > 255 else v


def lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)


def put_px(buf: bytearray, w: int, x: int, y: int, r: int, g: int, b: int, a: int) -> None:
    i = (y * w + x) * 4
    if a == 255:
        buf[i] = r
        buf[i + 1] = g
        buf[i + 2] = b
        buf[i + 3] = 255
        return
    # alpha blend over existing pixel
    dst_r, dst_g, dst_b, dst_a = buf[i], buf[i + 1], buf[i + 2], buf[i + 3]
    src_a = a / 255.0
    dst_af = dst_a / 255.0
    out_a = src_a + dst_af * (1 - src_a)
    if out_a <= 0:
        buf[i] = buf[i + 1] = buf[i + 2] = buf[i + 3] = 0
        return
    out_r = int((r * src_a + dst_r * dst_af * (1 - src_a)) / out_a)
    out_g = int((g * src_a + dst_g * dst_af * (1 - src_a)) / out_a)
    out_b = int((b * src_a + dst_b * dst_af * (1 - src_a)) / out_a)
    buf[i] = clamp(out_r)
    buf[i + 1] = clamp(out_g)
    buf[i + 2] = clamp(out_b)
    buf[i + 3] = clamp(int(out_a * 255))


def fill_rect(buf: bytearray, w: int, h: int, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int, int]) -> None:
    r, g, b, a = color
    x0 = max(0, x0)
    y0 = max(0, y0)
    x1 = min(w, x1)
    y1 = min(h, y1)
    for y in range(y0, y1):
        row_i = (y * w + x0) * 4
        for x in range(x0, x1):
            if a == 255:
                buf[row_i] = r
                buf[row_i + 1] = g
                buf[row_i + 2] = b
                buf[row_i + 3] = 255
            else:
                put_px(buf, w, x, y, r, g, b, a)
            row_i += 4


def fill_round_rect(
    buf: bytearray,
    w: int,
    h: int,
    x: int,
    y: int,
    rw: int,
    rh: int,
    radius: int,
    color: tuple[int, int, int, int],
) -> None:
    r, g, b, a = color
    radius = max(0, min(radius, min(rw, rh) // 2))
    for yy in range(y, y + rh):
        if yy < 0 or yy >= h:
            continue
        for xx in range(x, x + rw):
            if xx < 0 or xx >= w:
                continue
            dx = 0
            dy = 0
            if xx < x + radius:
                dx = x + radius - xx
            elif xx >= x + rw - radius:
                dx = xx - (x + rw - radius - 1)
            if yy < y + radius:
                dy = y + radius - yy
            elif yy >= y + rh - radius:
                dy = yy - (y + rh - radius - 1)
            if dx and dy and (dx * dx + dy * dy > radius * radius):
                continue
            put_px(buf, w, xx, yy, r, g, b, a)


def draw_text(
    buf: bytearray,
    w: int,
    h: int,
    x: int,
    y: int,
    text: str,
    scale: int,
    color: tuple[int, int, int, int],
    letter_spacing: int = 1,
) -> None:
    r, g, b, a = color
    cx = x
    for ch in text:
        glyph = FONT_5X7.get(ch)
        if glyph is None:
            glyph = FONT_5X7.get(" ")
        for row in range(7):
            bits = glyph[row]
            for col in range(5):
                if bits & (1 << (4 - col)):
                    x0 = cx + col * scale
                    y0 = y + row * scale
                    fill_rect(buf, w, h, x0, y0, x0 + scale, y0 + scale, (r, g, b, a))
        cx += 5 * scale + letter_spacing * scale


def measure_text(text: str, scale: int, letter_spacing: int = 1) -> tuple[int, int]:
    if not text:
        return 0, 0
    width = len(text) * (5 * scale + letter_spacing * scale) - letter_spacing * scale
    height = 7 * scale
    return width, height


def downsample_2x(src: bytearray, src_w: int, src_h: int) -> tuple[bytearray, int, int]:
    dst_w = src_w // 2
    dst_h = src_h // 2
    dst = bytearray(dst_w * dst_h * 4)
    for y in range(dst_h):
        for x in range(dst_w):
            acc = [0, 0, 0, 0]
            for oy in (0, 1):
                for ox in (0, 1):
                    sx = x * 2 + ox
                    sy = y * 2 + oy
                    i = (sy * src_w + sx) * 4
                    acc[0] += src[i]
                    acc[1] += src[i + 1]
                    acc[2] += src[i + 2]
                    acc[3] += src[i + 3]
            di = (y * dst_w + x) * 4
            dst[di] = acc[0] // 4
            dst[di + 1] = acc[1] // 4
            dst[di + 2] = acc[2] // 4
            dst[di + 3] = acc[3] // 4
    return dst, dst_w, dst_h


def png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(chunk_type)
    crc = zlib.crc32(data, crc) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + chunk_type + data + struct.pack(">I", crc)


def write_png(path: str, w: int, h: int, rgba: bytes) -> None:
    raw = bytearray()
    stride = w * 4
    for y in range(h):
        raw.append(0)  # filter 0
        start = y * stride
        raw.extend(rgba[start : start + stride])

    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    idat = zlib.compress(bytes(raw), level=9)

    out = bytearray()
    out.extend(b"\x89PNG\r\n\x1a\n")
    out.extend(png_chunk(b"IHDR", ihdr))
    out.extend(png_chunk(b"IDAT", idat))
    out.extend(png_chunk(b"IEND", b""))

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(out)


def main() -> None:
    # Render at 2x then downsample for smoother edges.
    W2, H2 = 2400, 1260
    buf = bytearray(W2 * H2 * 4)

    # Background gradient (very light)
    top = (248, 250, 252)
    mid = (241, 245, 249)
    bot = (226, 232, 240)
    for y in range(H2):
        t = y / max(1, H2 - 1)
        if t < 0.55:
            tt = t / 0.55
            r = lerp(top[0], mid[0], tt)
            g = lerp(top[1], mid[1], tt)
            b = lerp(top[2], mid[2], tt)
        else:
            tt = (t - 0.55) / 0.45
            r = lerp(mid[0], bot[0], tt)
            g = lerp(mid[1], bot[1], tt)
            b = lerp(mid[2], bot[2], tt)
        fill_rect(buf, W2, H2, 0, y, W2, y + 1, (r, g, b, 255))

    # Soft green glows
    def radial_glow(cx: int, cy: int, rx: int, ry: int, color: tuple[int, int, int], alpha: int) -> None:
        for yy in range(max(0, cy - ry), min(H2, cy + ry)):
            dy = (yy - cy) / ry
            for xx in range(max(0, cx - rx), min(W2, cx + rx)):
                dx = (xx - cx) / rx
                d = dx * dx + dy * dy
                if d >= 1:
                    continue
                a = int(alpha * (1 - d) ** 2)
                put_px(buf, W2, xx, yy, color[0], color[1], color[2], a)

    radial_glow(520, 320, 1040, 700, (0, 143, 76), 56)
    radial_glow(2040, 240, 1040, 700, (0, 143, 76), 40)

    # Card + shadow
    shadow = (2, 6, 23, 36)
    fill_round_rect(buf, W2, H2, 140, 180, 2120, 900, 56, shadow)
    fill_round_rect(buf, W2, H2, 120, 160, 2120, 900, 56, (255, 255, 255, 230))
    fill_round_rect(buf, W2, H2, 120, 160, 2120, 900, 56, (226, 232, 240, 120))

    # Abstract shapes (no text): subtle, professional, brand-colored accents.
    def soft_circle(cx: int, cy: int, r: int, color: tuple[int, int, int], alpha: int) -> None:
        for yy in range(max(0, cy - r), min(H2, cy + r)):
            dy = yy - cy
            for xx in range(max(0, cx - r), min(W2, cx + r)):
                dx = xx - cx
                d2 = dx * dx + dy * dy
                if d2 >= r * r:
                    continue
                t = d2 / (r * r)
                a = int(alpha * (1 - t) ** 2)
                put_px(buf, W2, xx, yy, color[0], color[1], color[2], a)

    def ring(cx: int, cy: int, r: int, thickness: int, color: tuple[int, int, int], alpha: int) -> None:
        r2 = r * r
        inner = max(0, r - thickness)
        inner2 = inner * inner
        for yy in range(max(0, cy - r), min(H2, cy + r)):
            dy = yy - cy
            for xx in range(max(0, cx - r), min(W2, cx + r)):
                dx = xx - cx
                d2 = dx * dx + dy * dy
                if d2 >= r2 or d2 <= inner2:
                    continue
                # soften edges
                edge = min(d2 - inner2, r2 - d2) / max(1.0, thickness * thickness)
                a = int(alpha * min(1.0, edge))
                put_px(buf, W2, xx, yy, color[0], color[1], color[2], a)

    # Large soft gradients inside the card
    soft_circle(780, 520, 420, (0, 143, 76), 64)
    soft_circle(1720, 780, 520, (0, 143, 76), 44)
    soft_circle(1820, 420, 360, (15, 23, 42), 22)

    # Thin rings for a "system / loop" vibe
    ring(820, 680, 360, 18, (0, 143, 76), 52)
    ring(820, 680, 250, 14, (0, 143, 76), 38)
    ring(1560, 520, 300, 16, (71, 85, 105), 26)

    # Small accent dots
    fill_round_rect(buf, W2, H2, 420, 420, 22, 22, 11, (0, 143, 76, 255))
    fill_round_rect(buf, W2, H2, 1980, 930, 18, 18, 9, (0, 143, 76, 200))

    # Downsample to 1200x630 and write PNG
    out, W, H = downsample_2x(buf, W2, H2)
    write_png("src/images/blog/weekly-seo-loop-og.png", W, H, bytes(out))


if __name__ == "__main__":
    main()
