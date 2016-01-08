from django.core.validators import RegexValidator

dna_sequence_validator = RegexValidator("^[CAGTcagt]+$",
    message="Not a valid DNA sequence.")


