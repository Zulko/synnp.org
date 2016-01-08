""" Basic models, such as user profile """

from django.db import models
from django.contrib.auth.models import User
from validators import dna_sequence_validator

# PEOPLE


class Laboratory(models.Model):
    """A laboratory is both a group of users and a location for
    samples.

    For this project it will be one of

    - Cai Lab
    - Tyers Lab
    - Wright Lab
    """
    is_active = models.BooleanField()
    name = models.CharField(
        u'Name', max_length=255,
        help_text='Name of the laboratory (e.g. Cai Lab)'
    )


class LabMember(models.Model):
    """A lab member is simply a user of the website, attached to a
    laboratory.
    """
    user = models.OneToOneField(User)
    laboratory = models.ForeignKey(
        Laboratory,
        help_text="Name of the user's laboratory."
    )


###


class Organism(models.Model):

    """ The biological description of an organism

    """
    name = models.CharField(u'Name', max_length=255)
    taxid = models.CharField(
        u'TaxID', max_length=255,
        help_text="Taxonomic ID of the organism"
    )
    infos = models.CharField(
        u'infos', max_length=255,
        help_text="Any useful infos on the organism."
    )


class Protein(models.Model):
    name = models.CharField(u'Name', max_length=255)
    protein_id = models.CharField(
        u'ProteinID', max_length=255,
        help_text="ID of the protein e.g. B0B503",
    )
    sequence = models.CharField(
        u'Sequence', max_length=255,
        help_text="Amino-acid sequence of the protein e.g. MSSEDKLR...")


class DNAPart(models.Model):

    """Any DNA part (promoter, terminator, CDS).

    Note that DNAParts are "theoretical" parts (i.e. simply sequences),
    unlike "constructs" which are actual DNA molecules stored somewhere.
    """
    name = models.CharField(
        u'Name', max_length=255
    )
    type = models.CharField(
        u'Type', max_length=255,
        help_text="One of 'promoter', 'terminator', 'CDS'"
    )
    sequence = models.CharField(
        u'Type', max_length=50000,
        validators=[dna_sequence_validator],
        help_text='A valid ATGC sequence'
    )
    from_organism = models.CharField(
        u'Organism', max_length=255,
        help_text="Original organism for the sequence (if applicable)"
    )


class Backbone(models.Model):
    """ The backbone can be assembled """
    name = models.CharField(
        u'Name', max_length=255
    )
    description = models.CharField(
        u"description", max_length=255,
        help_text="Description of the backbone (resistance, rep. origin)."
                  " May be extended in the future."
    )


class CDS(models.Model):
    """A CDS is a type of DNAPart. A CDS encodes a protein.

    In the SynNP project we'll have natural CDS (original version) and CDS
    optimized from natural CDS with some optimization algorithm.
    """
    part = models.OneToOneField(DNAPart, primary_key=True)
    protein = models.ForeignKey(Protein)
    codon_optimization_method = models.CharField(
        u'Optimization', max_length=255,
        help_text="Name or reference of the optimization method used (the "
                  "details and steps of the method can be kept outside the DB)"
    )
    optimized_for = models.ForeignKey(
        Organism,
        help_text="Indicates the organism that the CDS was optimized for")
    derived_from = models.ForeignKey('self')

class Oligo(models.Model):
    """An Oligo is a sequence that has been ordered to create a part
    """
    name = models.CharField(
        u'Name', max_length=255
    )
    target_part = models.ForeignKey(
        DNAPart,
        help_text="The Part that will be obtained with this oligo"
    )
    ordering_batch = models.CharField(
        u'Name', max_length=255
    )


class Compound(models.Model):
    """ A compound is a molecule produced by a gene pathway. For instance an
    antibiotic. The finality of the SynNP project is to produce efficient
    compounds with high purity
    """

    name = models.CharField(
        u'Name', max_length=255,
        help_text="Common name of the compound."
    )
    derived_from = models.ForeignKey('self')


class Pathway(models.Model):
    """ A pathway is a set of enzymes which together produce a specific
    compound
    """
    name = models.CharField(
        u'Name', max_length=255,
        help_text="Common name of the pathway")
    compound = models.ForeignKey(
        Compound,
        help_text="Compound produced by the pathway"
    )
    enzymes = models.ManyToManyField(
        Protein,
        help_text="All enzymes in the pathway"
    )
    is_core_pathway = models.BooleanField(
        u'Is core Pathway',
        help_text='True or False whether other pathways are built around '
                  'this pathway'
    )


class StorageLocation(models.Model):
    """All informations that enable to find a sample.

    """
    laboratory = models.ForeignKey(Laboratory)
    location = models.CharField(
        u'Location', max_length=255,
        help_text="Description to locate the sample (may be lab-specific)"
    )


class Assembly(models.Model):
    """Any physical (=existing) DNA sequence made of DNApart(s) on a backbone.

    For instance:
    - a part (e.g. a promoter) on a backbone
    - a YAC (=a series of parts on a backbone)
    """
    name = models.CharField(u'Name', max_length=255)
    location = models.ForeignKey(StorageLocation)
    sequence = models.CharField(
        "Sequence", max_length=50000,
        help_text="The sequence of the construct stored in genbank format "
                  "with annotations, so that it can be nicely displayed"
    )
    parts = models.ManyToManyField(
        DNAPart,
        help_text=" All DNAParts featured the construct."
                  " Note that this field does not give the order in which the"
                  " parts are assembled. This order is given in the sequence."
    )
    backbone = models.ForeignKey(Backbone)


class Strain(models.Model):
    """ A strain means here a physical sample from an organism, possibly
    carrying a construct (plasmid or YAC)
    """
    name = models.CharField(u'Name', max_length=255)
    organism = models.ForeignKey(
        Organism,
        help_text="Original organism of the strain"
    )
    assembly = models.ForeignKey(
        Assembly,
        help_text="Construct contained by the strain (void if none)"
    )


class Assay(models.Model):
    """An assay is a test made on a strain carrying a YAC to test the pathway
    encoded by the YAC.
    """
    strain = models.ForeignKey(
        Strain,
        help_text="Strain on which the assay was made."
    )
    results_summary = models.CharField(
        u'Results summary', max_length=1000,
        help_text="Quick summary of what was found in the assay."
    )


class YACassembly(models.Model):
    """A special class of assembly """
    assembly = models.ForeignKey(Assembly)