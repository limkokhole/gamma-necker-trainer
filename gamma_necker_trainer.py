import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation

# ── NEW: import and prepare your beep ─────────────────────────────────────
import simpleaudio as sa

# ---------- build a 0.5-s 40 Hz click-train ----------
fs, burst_dur = 44_100, 0.5           # Hz, seconds
click_train = np.zeros(int(fs*burst_dur))
click_train[::int(fs/40)] = 1.0        # impulse every 25 ms (40 Hz)
audio = (click_train * 32767).astype(np.int16)
beep  = sa.WaveObject(audio, num_channels=1, bytes_per_sample=2, sample_rate=fs)

# ── Helper to generate cube vertices ─────────────────────────────────────
def get_vertices(center, size):
    x, y, z = center
    d = size / 2
    return np.array([
        [x-d, y-d, z-d], [x+d, y-d, z-d],
        [x+d, y+d, z-d], [x-d, y+d, z-d],
        [x-d, y-d, z+d], [x+d, y-d, z+d],
        [x+d, y+d, z+d], [x-d, y+d, z+d],
    ])

# ── Common setup ────────────────────────────────────────────────────────
AX_LIM = (-12, 12)
INNER_CENTER = (8, -15, 0)
INNER_SIZE   = 4
OFFSET = 30
x0, x1 = AX_LIM; y0, y1 = AX_LIM; z0, z1 = AX_LIM
cube_size = min(x1-x0, y1-y0, z1-z0)
cube_center = ((x0+x1)/2, (y0+y1)/2, (z0+z1)/2)
ALL_EDGES = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

# ── Figure 1: Animated Necker‐Cube ───────────────────────────────────────
fig1 = plt.figure(figsize=(12,12))
ax1  = fig1.add_subplot(111, projection='3d', proj_type='ortho')
ax1.set_box_aspect((1,1,1))
ax1.set_xlim(*AX_LIM); ax1.set_ylim(*AX_LIM); ax1.set_zlim(*AX_LIM)

ruler_verts = get_vertices(cube_center, cube_size)
inner_verts = get_vertices(INNER_CENTER, INNER_SIZE)

# thin skeleton
for verts in (ruler_verts, inner_verts):
    ax1.add_collection3d(Line3DCollection(
        [(verts[i], verts[j]) for i,j in ALL_EDGES],
        colors='black', linewidths=1, zorder=1))

# bold‐edge sets
BOLD_SETS = [
    [(0,1),(0,3),(0,4),(1,2),(2,3),(2,6),(3,7),(4,7),(6,7)],
    [(0,1),(0,4),(1,2),(1,5),(2,6),(4,5),(4,7),(5,6),(6,7)]
]
ruler_bold = []
inner_bold = []
for edges in BOLD_SETS:
    sr = [(ruler_verts[i], ruler_verts[j]) for i,j in edges]
    si = [(inner_verts[i], inner_verts[j]) for i,j in edges]
    cr = Line3DCollection(sr, colors='black', linewidths=10, zorder=2)
    ci = Line3DCollection(si, colors='black', linewidths=10, zorder=2)
    ax1.add_collection3d(cr); ruler_bold.append(cr)
    ax1.add_collection3d(ci); inner_bold.append(ci)

# start with the first pattern
for grp in (ruler_bold, inner_bold):
    for idx, col in enumerate(grp):
        col.set_visible(idx==0)

def update(frame):
    idx = frame % 2
    # toggle visibility
    for grp in (ruler_bold, inner_bold):
        for j, col in enumerate(grp):
            col.set_visible(j==idx)

    # ── play the beep (non‐blocking) ───────────────
    beep.play()

    return ruler_bold + inner_bold

ani = FuncAnimation(fig1, update, frames=[0,1], interval=3000, blit=False)

# ── Figure 2 (static) ───────────────────────────────────────────────────
fig2 = plt.figure(figsize=(12,12))
ax2  = fig2.add_subplot(111, projection='3d', proj_type='ortho')
ax2.set_box_aspect((1,1,1))
ax2.set_xlim(*AX_LIM); ax2.set_ylim(*AX_LIM); ax2.set_zlim(*AX_LIM)
for verts in (ruler_verts, inner_verts):
    ax2.add_collection3d(Line3DCollection(
        [(verts[i], verts[j]) for i,j in ALL_EDGES],
        colors='black', linewidths=1, zorder=1))

# 1) grab the FigureManager
mgr1 = fig1.canvas.manager # Get Fig 1’s manager, not the “current” one

def minimize_fig1():
    try:
        mgr1.window.showMinimized()  # QtAgg: minimize window
    except AttributeError:
        mgr1.window.iconify()         # TkAgg: iconify window

timer = fig1.canvas.new_timer(interval=30_000)  # 30 000 ms = 30 s
timer.single_shot = True
timer.add_callback(minimize_fig1)
timer.start()

plt.show()
