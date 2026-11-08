import numpy as np
from scipy import stats

def users_needed_per_arm(baseline, lift, alpha, power):
    """Users needed in EACH group to detect an absolute change of `lift`
    with a two-sided two-proportion z-test."""
    p1, p2 = baseline, baseline + lift
    p_bar = (p1 + p2) / 2
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_power = stats.norm.ppf(power)
    top = (z_alpha * np.sqrt(2 * p_bar * (1 - p_bar)) + z_power * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return top / (p2 - p1) ** 2

def two_proportion_test(x_a, n_a, x_b, n_b, alpha=0.05):
    p_a, p_b = x_a / n_a, x_b / n_b
    p_pool = (x_a + x_b) / (n_a + n_b)
    se_pool = np.sqrt(p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b))
    z = (p_a - p_b) / se_pool
    p_value = 2 * stats.norm.sf(abs(z))
    se_diff = np.sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
    margin = stats.norm.ppf(1 - alpha / 2) * se_diff
    return {
        "rate_A": p_a, "rate_B": p_b, "difference (A - B)": p_a - p_b,
        "z": z, "p_value": p_value,
        "CI low": p_a - p_b - margin, "CI high": p_a - p_b + margin,
    }

def welch_test(a, b, alpha=0.05):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    n_a, n_b = len(a), len(b)
    m_a, m_b = a.mean(), b.mean()
    v_a, v_b = a.var(ddof=1), b.var(ddof=1)
    se_diff = np.sqrt(v_a / n_a + v_b / n_b)
    t = (m_a - m_b) / se_diff
    df = se_diff**4 / ((v_a / n_a) ** 2 / (n_a - 1) + (v_b / n_b) ** 2 / (n_b - 1))
    p_value = 2 * stats.t.sf(abs(t), df)
    margin = stats.t.ppf(1 - alpha / 2, df) * se_diff
    return {
        "mean_A": m_a, "mean_B": m_b, "difference (A - B)": m_a - m_b,
        "t": t, "df": df, "p_value": p_value,
        "CI low": m_a - m_b - margin, "CI high": m_a - m_b + margin,
    }


def students_t_test(a, b, alpha=0.05):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    n_a, n_b = len(a), len(b)
    m_a, m_b = a.mean(), b.mean()
    df = n_a + n_b - 2
    var_pool = ((n_a - 1) * a.var(ddof=1) + (n_b - 1) * b.var(ddof=1)) / df
    se_diff = np.sqrt(var_pool * (1 / n_a + 1 / n_b))
    t = (m_a - m_b) / se_diff
    p_value = 2 * stats.t.sf(abs(t), df)
    margin = stats.t.ppf(1 - alpha / 2, df) * se_diff
    return {
        "mean_A": m_a, "mean_B": m_b, "difference (A - B)": m_a - m_b,
        "t": t, "df": df, "p_value": p_value,
        "CI low": m_a - m_b - margin, "CI high": m_a - m_b + margin,
    }


def mann_whitney_test(a, b, alpha=0.05):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    n_a, n_b = len(a), len(b)
    u, p_value = stats.mannwhitneyu(a, b, alternative="two-sided")
    diffs = np.sort(np.subtract.outer(a, b).ravel())
    k = int(np.floor(n_a * n_b / 2 - stats.norm.ppf(1 - alpha / 2) * np.sqrt(n_a * n_b * (n_a + n_b + 1) / 12)))
    k = max(k, 0)
    return {
        "median_A": np.median(a), "median_B": np.median(b), "difference (A - B)": np.median(diffs),
        "U": u, "p_value": p_value,
        "CI low": diffs[k], "CI high": diffs[len(diffs) - 1 - k],
    }