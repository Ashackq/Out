def is_variable(term):
    return isinstance(term, str) and term.islower()


def unify(x, y, subst):
    if subst is None:
        return None
    elif x == y:
        return subst
    elif is_variable(x):
        return unify_var(x, y, subst)
    elif is_variable(y):
        return unify_var(y, x, subst)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], subst))
    else:
        return None


def unify_var(var, term, subst):
    if var in subst:
        return unify(subst[var], term, subst)
    elif term in subst:
        return unify(var, subst[term], subst)
    else:
        subst[var] = term
        return subst


def apply_substitution(subst, term):
    if is_variable(term):
        return subst.get(term, term)
    elif isinstance(term, list):
        return [apply_substitution(subst, t) for t in term]
    else:
        return term


term1 = ["ancestor", "X", ["parent", "X", "Y"]]
term2 = ["ancestor", ["grandparent", "Z"], ["parent", "Z", ["child", "W"]]]

subst = unify(term1, term2, {})

print("Substitution:", subst)
