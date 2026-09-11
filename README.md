# Path Guard

Tower defense — pick a path, place towers, hold the line for 40 waves.

**Color = threat:** green Grunts → yellow Scouts → Skitters (splash resist) → orange Brutes → dark red Raiders. Steel **Shells** shrug damage. Wave 20 mid **Titan** · Wave 40 finale **Titans**.

**Towers (build 64 roster):** Archer · Barrier · Crossbow · Frost · Bank · Fire · Cannon · Lightning · Sniper (cost order). Build bar is **category-first**: Marksman · Elemental · Gunnery · Support (tap category → towers + ← Back; Support last). In-category icons are larger (~48px sprites); drill-down buttons expand to fill the row. Counters matter — Marksman weak/Immune vs Shell/Titan; Frost/Lightning Scout Immune; Gunnery/Lightning answer armor. **Beacon removed.**

**Maps:** Spiral (Easy) → Serpentine (Medium) → Crosscut (Medium-Hard) → **Ridge** (Medium-Hard) → Winding (Hard) → Gauntlet (Brutal) → **Crucible** (Nightmare). Hard Mode optional. Per-map wins & best times in localStorage. Win overlay uses plain Perfect/Good/Close labels (no star ratings).

Gold from kills + **Bank** income only (no interest, early-call, perfect-clear, or challenge bonuses). Waves around 5 / 10 / 15 / 20 / 25 / 30 / 35 / 40 stay denser/tougher as normal hard waves. **Double-tap** a tower to upgrade. Sell confirms. Mute FX anytime. Speed cycles 1x → 2x → 3x → 5x. Start with **10 lives**.

**UX (build 64):** Inline tower-menu info (Back + selected; other slots → name/role/cost/?/×). No floating tip; no `#tower-stats` while picking from the bar. **Per-tower Aim** on Upgrade/Sell row (First/Strong/Close). **FX** on util row (Speed · Pause · Maps · FAQ · FX) — More submenu removed. Fire = constant flame. Sprite `?v=64`.

**Achievements:** first clear each map, Hard Mode win, Titan kill — checklist always on win/lose overlays. Titan death gets a fanfare float.
