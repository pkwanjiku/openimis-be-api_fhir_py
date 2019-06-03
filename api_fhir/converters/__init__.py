from api_fhir.exceptions import FhirRequestProcessException
from api_fhir.models import CodeableConcept, ContactPoint, Address, Coding, Identifier, IdentifierUse


class BaseFHIRConverter(object):
    @classmethod
    def to_fhir_obj(cls, obj):
        raise NotImplementedError('`toFhirObj()` must be implemented.')

    @classmethod
    def to_imis_obj(cls, data, audit_user_id):
        raise NotImplementedError('`toImisObj()` must be implemented.')

    @classmethod
    def valid_condition(cls, condition, error_message, errors=None):
        if errors is None:
            errors = []
        if condition:
            errors.append(error_message)
        return condition

    @classmethod
    def check_errors(cls, errors=None):
        if errors is None:
            errors = []
        if len(errors) > 0:
            base_massage = "The request cannot be processed due to the following issues:\n"
            message = base_massage + ",\n".join(errors)
            raise FhirRequestProcessException(message)

    @classmethod
    def build_codeable_concept(cls, code, system):
        codeable_concept = CodeableConcept()
        coding = Coding()
        coding.system = system
        coding.code = code
        codeable_concept.coding = [coding.__dict__]
        return codeable_concept

    @classmethod
    def build_fhir_identifier(cls, value, type_system, type_code):
        identifier = Identifier()
        identifier.use = IdentifierUse.USUAL.value
        type = cls.build_codeable_concept(type_code, type_system)
        identifier.type = type.__dict__
        identifier.value = value
        return identifier

    @classmethod
    def build_fhir_contact_point(cls, value, contact_point_system, contact_point_use):
        contact_point = ContactPoint()
        contact_point.system = contact_point_system
        contact_point.use = contact_point_use
        contact_point.value = value
        return contact_point

    @classmethod
    def build_fhir_address(cls, value, use, type):
        current_address = Address()
        current_address.text = value
        current_address.use = use
        current_address.type = type
        return current_address


from api_fhir.converters.patientConverter import PatientConverter
