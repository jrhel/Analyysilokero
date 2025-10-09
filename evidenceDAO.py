import db_connection_handler

def create_evidence(observation: str, source: str, analysis_id: int):
    params = [observation, source, analysis_id]
    row_id = db_connection_handler.execute("INSERT INTO Evidence (observation, source, analysis_id) VALUES (?, ?, ?)", params)    
    print("New Evidence: row_id for", observation, "is", row_id, type(row_id))
    if observation in get_evidence(analysis_id):
        print("PRAAAAAAAISE")
        return True
    else:
        return False

def get_evidence(analysis_id: int):
    info = get_evidence_info(analysis_id)
    evidence = []
    for row in info:
        evidence.append(row[1])
    print("EVES: ", evidence)
    return evidence

def get_source(analysis_id: int, evidence: str):
    params = [analysis_id, evidence]
    source = db_connection_handler.query("SELECT source FROM Evidence WHERE analysis_id = ? AND observation = ?", params)[0][0]
    return source


def get_evidence_info(analysis_id: int):
    params = [analysis_id]
    result = db_connection_handler.query("SELECT * FROM Evidence WHERE analysis_id = ?", params)
    print("Found H:", result)
    return result

def update_evidence(new_observation: str, source: str, old_observation: str, analysis_id: int):
    params = [new_observation, source, old_observation, analysis_id]
    db_connection_handler.execute("UPDATE Evidence SET observation = ?, source = ? WHERE observation = ? AND analysis_id = ?", params)