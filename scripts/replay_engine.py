def replay(log_frames, derive_function):
    """
    Replay log events through a derivation function.
    """
    results = []
    for frame in log_frames:
        result = derive_function(frame)
        results.append(result)
    return results
