def dedupe_emails_case_preserve_order(emails):
    seen = set()
    result = []
    for e in emails:
        if "@" not in e:   # skip invalid emails
            continue
        lower = e.lower()
        if lower not in seen:
            seen.add(lower)
            result.append(e)
    return result


def first_with_domain(emails, domain):
    domain = domain.lower()
    for i, e in enumerate(emails):
        if "@" not in e:
            continue
        _, d = e.split("@", 1)
        if d.lower() == domain:
            return i
    return None


def domain_counts(emails):
    counts = {}
    for e in emails:
        if "@" not in e:
            continue
        _, d = e.split("@", 1)
        d = d.lower()
        if d in counts:
            counts[d] += 1
        else:
            counts[d] = 1
    return sorted(counts.items())
