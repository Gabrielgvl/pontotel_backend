from models import Company, db, Quotation


def seed():
    companies = [{"ABEV3.SAO": "AMBEV S/A"}, {"AZUL4.SAO": "AZUL"}, {"BTOW3.SAO": "B2W DIGITAL"}, {"B3SA3.SAO": "B3"},
                 {"BBSE3.SAO": "BB SEGURIDADE"}, {"VRML3.SAO": "BR MALLS PAR"}, {"BBDC4.SAO": "BRADESCO"},
                 {"BRKM5.SAO": "BRASKEM"},
                 {"BRAP4.SAO": "BRADESPAR"}, {"BBAS3.SAO": "BANCO DO BRASIL"}]

    db.session.query(Quotation).delete()
    db.session.query(Company).delete()
    db.session.commit()

    for company in companies:
        symbol, name = list(company.items())[0]
        Company(symbol=symbol, name=name).save()
