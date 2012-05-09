connotation
===========

Probability that the a message is a particular connotation:

                      p1 * ... * pn
    p = -----------------------------------------
        p1 * ... * pn + (1 - p1) * ... * (1 - pn)

where `px` is the probability that word `x` has the given connotation.

Or, if you prefer Haskell,

```haskell
probability ps = product ps / (product ps + product [1 - px | px <- ps])
```
