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

## Approach

### Part I: Count tokens

For each connotation, do the following:

1. Get all the text labelled as a connotation (the corpus).
2. Convert the corpus to lowercase.
3. Break the corpus into tokens. For now `(\w+)` should be a sufficient regex.
4. Count the number of times a token appears in the full corpus.
5. Store total counts for each token to use for future reference.

### Part II: Evaluate a blob

1. Convert the blob to lowercase.
2. Break the blob into tokens the same way the corpus was broken into tokens.
3. Get the, say, 15 most significant tokens from each connotation.
4. Get the probability that the blob has each connotation by using **The Formula**.
5. Ignore any connotations having a probability less than, say, 0.7.
6. If there is only one connotation left, mark the blob as having that connotation. If there is more than one probable connotation, do not mark the blob.

# The Formula

Here is Paul Graham's Common Lisp code for detecting spam[1]:

```lisp
(let ((g (* 2 (or (gethash word good) 0)))
      (b (or (gethash word bad) 0)))
   (unless (< (+ g b) 5)
     (max .01
          (min .99 (float (/ (min 1 (/ b nbad))
                             (+ (min 1 (/ g ngood))
                                (min 1 (/ b nbad)))))))))
```

In our case ,the bias toward `good` does not mean much. So to adjust in pseudo-Haskell, that's

```haskell
probability word = if g + b > 5 then
        max .01 (min .99 (min 1 (b / nbad) / (min 1 (g / ngood) + min 1 (b / nbad))))
    where g = or (gethash word good) 0
          b = or (gethash word bad) 0
```

We also need to be able to rate words in different classes. Graham's spam detection is only using one class, `spam` (and the implicit class `not spam`). We need to extend his system four-fold:

* `positive` (and `not positive`)
* `negative` (and `not negative`)
* `neutral` (and `not neutral`)
* `useless` (and `not useless`)

There's a possibility that we can skip rating for `neutral` and mark a blob as such when it has ~0.5 probabilities for `positive` and `negative`, but the need to generalize the function remains.

```haskell
probability word class = if total > 5 then
        max .01 (min .99 (min 1 (out / nin) / (min 1 (in / nin) + min 1 (out / nout))))
    where total = count word
          nout = count outSet
          nin = count inSet
          out = total - in
          in = or (gethash word class) 0
```


# Database

In the database the following are used as abbreviations for different connotations:

* **+** positive
* **-** negative
* **0** neutral
* **u** useless

# References

[1] Paul Graham's "[A Plan for Spam](http://www.paulgraham.com/spam.html)"