"""
This is a script that defines the main classes for managing the DokuWiki content in connection
with Airtable, i.e. creating new pages or updating the existing ones.
"""

import os
import dokuwiki as dw
import wikicontents
import json


# in addition to tables that are associated with wiki pages,
# there can be tables not associated with pages and pages not associated with tables
# i.e. update_table has to check this but both update_table and update_pages should be callable separately
class WikiManager:

    def __init__(self, version):
        with open('config.json', 'r') as f:
            config = json.load(f)
        if version not in ["official", "test"]:
            print('Unknown version specified, choose from: "official" or "test".')
            return
        else:
            self.wiki = dw.DokuWiki(config[version]["wiki_url"],
                                    config[version]["username"],
                                    os.environ[config[version]["password_key"]])
            self.user_key = os.environ['AIRTABLE_API_KEY']
            self.table = None
            self.used_table_name = None
            self.defined_tables = ['tools_public_sample', 'ftse100+givingpolicies',
                                   'Charity experiments', 'Third sector', 'papers_mass']

    def setup_table(self, table_name):
        if table_name == 'tools_public_sample':
            table_base = 'appBzOSifwBqSuVfH'
            self.table = wikicontents.ToolTable(self.wiki, table_base, table_name, self.user_key)
            self.used_table_name = table_name

        elif table_name == 'ftse100+givingpolicies':
            table_base = 'apprleNrkR7dTtW60'
            self.table = wikicontents.FtseTable(self.wiki, table_base, table_name, self.user_key)
            self.used_table_name = table_name

        elif table_name == 'Charity experiments':
            table_base = 'appBzOSifwBqSuVfH'
            self.table = wikicontents.ExperimentTable(self.wiki, table_base, table_name, self.user_key)
            self.used_table_name = table_name

        elif table_name == 'Third sector':
            table_base = 'appBzOSifwBqSuVfH'
            self.table = wikicontents.ThirdSectorTable(self.wiki, table_base, table_name, self.user_key)
            self.used_table_name = table_name

        elif table_name == 'papers_mass':
            table_base = 'appBzOSifwBqSuVfH'
            self.table = wikicontents.PapersTable(self.wiki, table_base, table_name, self.user_key)
            self.used_table_name = table_name

        else:
            table_base = 'appBzOSifwBqSuVfH'
            self.table = wikicontents.Table(self.wiki, table_base, table_name, self.user_key)
            self.used_table_name = table_name

    def create_table(self):
        self.table.set_table_page()
        if self.used_table_name not in self.defined_tables:
            print("Go to '{}' in your DokuWiki to see the table. To change its formatting, "
                  "please implement an appropriate class.".format(self.table.dw_table_page))

    def create_pages(self):
        self.table.set_pages()
        if self.used_table_name not in self.defined_tables:
            print("Go to 'test:test_page' in your DokuWiki to see the possible page content. "
                  "To change its formatting, please implement an appropriate class.")

    def update_table(self):
        """Re-generate the full table on DW if any record has been modified.
        When done, reset the 'Modified' fields in the Airtable."""
        modified_records = 0
        for record in self.table.records:
            if 'Modified' in record['fields']:
                modified_records += 1
                self.table.airtable.update(record['id'], {'Modified': False})
        if modified_records > 0:
            self.table.set_table_page()
            if self.table.linked_pages:
                print("The table has linked DW pages. Remember to call manager.update_pages() to update them.")

    def update_pages(self):
        """Re-generate the pages on DW associated with any records that have been modified.
        When done, reset the 'Modified' fields in the Airtable."""
        modified_records = []
        for record in self.table.records:
            if 'Modified' in record['fields']:
                modified_records.append(record)
                self.table.airtable.update(record['id'], {'Modified': False})
        if len(modified_records) > 0:
            self.table.records = modified_records
            self.table.set_pages()
