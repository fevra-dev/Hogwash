# Motion — Animation That Communicates vs. Animation That Performs

Part of domains/design/. Load alongside patterns.md whenever the design moves. New in August 2026; motion had no coverage in this skill before.

**The question this file asks:** does the movement tell the user something about a state change, or is it there because interfaces are supposed to move now? Everything below follows from that one distinction.

## Motion Theater

The kinetic version of every static pattern in patterns.md. Decorative animation with no state to communicate: elements that fade up on scroll because scroll-reveal is a thing, cards that lift on hover without any affordance behind the lift, hero elements drifting continuously, counters that tick up to a number nobody asked to watch arrive.

The test is the same removal test the rest of this skill runs. **Take the animation out. If nothing about the interface became harder to understand, it was theater.** Motion that communicates fails this test loudly: remove the transition showing a panel sliding in from the left and the panel now appears from nowhere, and the user has lost the information about where it came from and where it will go back to.

The AI-specific version: generated frontends apply the same entrance animation uniformly to every section, which is Paragraph Symmetry from core/structural-patterns.md expressed in time rather than space. Uniform motion carries no information precisely because it is uniform.

## Easing Carries Meaning

The most common failure is not too much motion but the wrong curve, and the wrong curve reads as cheapness without the viewer knowing why.

- **Ease-out** — starts at full speed, decelerates to rest. The correct default for anything entering, and for anything responding to a user action. It reads as responsive because the motion begins immediately.
- **Ease-in** — accelerates as it leaves. For exits only. On an entrance it feels sluggish, because the user waits through the slow start before anything registers.
- **Standard / asymmetric ease-in-out** — quick acceleration, slower deceleration, for elements moving from one on-screen position to another. Asymmetric matters: if acceleration and deceleration are symmetric the motion reads as mechanical.
- **Linear** — only for motion with no felt beginning or end: marquees, indeterminate spinners, determinate progress. Linear easing anywhere else is the single clearest sign that nobody chose the curve.

## Duration Bands

Treat these as a well-supported range rather than exact figures.

| Band | Use |
|---|---|
| ~100ms | The perceptual threshold for "instant." Hard floor for direct-manipulation feedback. |
| 150–300ms | Micro-interactions: hover, press, small toggles. |
| 200–500ms | Standard transitions and most view changes. |
| 300–500ms | Heavier components (drawers, large panels) at the top of the range; small modals at the bottom. |
| 800–1200ms | Bounce and elastic effects only, and only when that register is wanted. Never a default. |

A generated interface that uses one duration for everything has the same problem as one that uses one easing curve. Weight should track what is actually moving.

## Reduced Motion Is Not a Kill Switch

The failure here runs in both directions, and the second one is less obvious.

**Ignoring the preference.** `prefers-reduced-motion` is a mature CSS media query, baseline since January 2020, reflecting a real OS-level setting. Parallax, scrolljacking, large panning movement, autoplay video, and continuous loops can trigger vestibular symptoms; migraine and photosensitive conditions overlap the same trigger list. The affected population is large and well documented, though published prevalence figures vary enough that they are better treated as "a large population" than as one precise number.

**Implementing it as `animation: none`.** The subtler mistake. Some motion is load-bearing for orientation: a transitional animation showing exactly how a state changed is *more* accessible with the motion than without it. Stripping everything removes that help along with the harm.

The correct pattern is substitution, not deletion: swap the triggering animation for a calmer equivalent. A scale-and-pulse becomes an opacity dissolve. The state change still reads; the vestibular trigger is gone. Two WCAG success criteria sit behind this directly, 2.3.3 Animation from Interactions and 1.3.4 Orientation.

## Sources

Curve selection, duration bands, and the reduced-motion material come from the operator's own design corpus (`accessibility-motion-qa-reference.md`, Cluster E, last checked July 27 2026), which synthesizes Material Design's official motion guidelines, Nielsen Norman Group, web.dev, and MDN for `prefers-reduced-motion` baseline status. The Eric Bailey position that "animation isn't unnecessary" and the substitution-over-deletion pattern follow MDN's own reference implementation, via that file. Duration figures carry that file's confidence flag: the general pattern is Verified and extremely consistent across independent sources; specific millisecond values are a well-supported range rather than single correct numbers. Motion theater and the uniform-entrance observation are this skill's own extension of its existing removal test and symmetry rules into the time dimension.
