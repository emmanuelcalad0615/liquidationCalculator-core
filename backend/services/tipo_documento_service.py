from sqlalchemy.orm import Session
from models.tipo_documento import TipoDocumento
from schemas.tipo_documento_schema import TipoDocumentoCreate

def create_tipo_documento(db:Session, tipo_documento: TipoDocumentoCreate):
    db_tipo_documento = TipoDocumento(
        descripcion = tipo_documento.descripcion
    )
    db.add(db_tipo_documento)
    db.commit()
    db.refresh(db_tipo_documento)
    return db_tipo_documento