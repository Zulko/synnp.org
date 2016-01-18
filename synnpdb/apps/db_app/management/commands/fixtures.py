import pandas as pd
import os

from django.core.management.base import BaseCommand
import synnpdb.apps.db_app as db_app
from django.db import transaction


def create_entry(objects_list, model, **kwargs):
    obj = db_app.models.__dict__[model](**kwargs)
    print obj
    obj.save()
    return obj


class Command(BaseCommand):
     


    def _create_entries_from_0_465(self):
        """
        Creates entries from a document listing oligos
        from mlt0001 to mlt00465
        """


    def _create_entries_from_466_610(self):
        """
        Creates entries from a document listing oligos
        from mlt0001 to mlt00465
        """

        data_dir = os.path.join(os.path.dirname(__file__), "data")
        data_file = os.path.join(data_dir, "20151112_genes.xlsx")
        df = pd.read_excel(data_file)
        compounds_names = [
            name
            for name in set(df.ParentCompound)
            if pd.notnull(name)
        ]
        organisms_names = [
            name
            for name in set(df.Spp)
            if pd.notnull(name)
        ]
        with transaction.atomic():

            for name in compounds_names:
                create_entry("Compound", name=name)

            for name in organisms_names:
                create_entry("Organism", name=name)

            for i, row in df.iterrows():
                if pd.isnull(row.ParentCompound):
                    continue

                protein = create_entry(
                    "Protein",
                    name=row.Enzyme,
                    protein_id=row.ProteinID,
                    sequence=row["protein squence"]
                )

                part = create_entry(
                    "DNAPart",
                    name=row["CDS defline"],
                    sequence=row.CDSopt_w_GA[16:-16],
                    type="CDS",
                )

                create_entry(
                    "CDS",
                    codon_optimization_method="???",
                    part=part,
                    protein=protein
                )

                create_entry(
                    "Oligo",
                    name=row._ID_,
                    ordering_batch="2015b",
                    sequence=row.CDSopt_w_GA,
                    target_part=part
                )
        
        def _create_entries_from_20151112(self):
        Annotations_NPgenes_2015

    def handle(self, *args, **options):
        self._create_entries()
