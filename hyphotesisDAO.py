import db_connection_handler

def create_hypothesis(claim: str, analysis_id: int):
    params = [claim, analysis_id]
    row_id = db_connection_handler.execute("INSERT INTO Hypothesis (claim, analysis_id) VALUES (?, ?)", params)
    print("row_id for", claim, "is", row_id, type(row_id))
    if claim in get_hypotheses(analysis_id):
        print("CLAIM")
        return True
    else:
        return False

def get_hypotheses(analysis_id: int):
    info = get_hypotheses_info(analysis_id)
    hypotheses = []
    for row in info:
        hypotheses.append(row[1])
    print("HYPOS: ", hypotheses)
    return hypotheses

def get_hypotheses_info(analysis_id: int):
    params = [analysis_id]
    result = db_connection_handler.query("SELECT * FROM Hypothesis WHERE analysis_id = ?", params)
    return result