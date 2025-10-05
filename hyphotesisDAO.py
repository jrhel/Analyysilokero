import db_connection_handler

def create_hypothesis(claim: str, analysis_id: int):
    params = [claim, analysis_id]
    row_id = db_connection_handler.execute("INSERT INTO Hypothesis (claim, analysis_id) VALUES (?, ?)", params)
    print("row_id for", claim, "is", row_id, type(row_id))
    if claim in get_hypotheses(analysis_id):
        return True
    else:
        return False

def get_hypotheses(analysis_id: int):
    params = [analysis_id]
    result = db_connection_handler.query("SELECT * FROM Hypothesis WHERE analysis_id = ?", params)[0]
    print("Found H:", result)
    return result