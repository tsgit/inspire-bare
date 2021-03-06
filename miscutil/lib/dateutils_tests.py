# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Unit tests for dateutils library."""

__revision__ = "$Id$"

import unittest
import dateutils

class ConvertFromDateCVSTest(unittest.TestCase):
    """
    Testing conversion of CVS dates.
    """

    def test_convert_good_cvsdate(self):
        """dateutils - conversion of good CVS dates"""
        # here we have to use '$' + 'Date...' here, otherwise the CVS
        # commit would erase this time format to put commit date:
        datecvs = "$" + "Date: 2006/09/21 10:07:22 $"
        datestruct_beginning_expected = (2006, 9, 21, 10, 7, 22)
        self.assertEqual(dateutils.convert_datecvs_to_datestruct(datecvs)[:6],
                         datestruct_beginning_expected)

        # here we have to use '$' + 'Date...' here, otherwise the CVS
        # commit would erase this time format to put commit date:
        datecvs = "$" + "Id: dateutils_tests.py,v 1.6 2007/02/14 18:33:02 tibor Exp $"
        datestruct_beginning_expected = (2007, 2, 14, 18, 33, 02)
        self.assertEqual(dateutils.convert_datecvs_to_datestruct(datecvs)[:6],
                         datestruct_beginning_expected)

    def test_convert_bad_cvsdate(self):
        """dateutils - conversion of bad CVS dates"""
        # here we have to use '$' + 'Date...' here, otherwise the CVS
        # commit would erase this time format to put commit date:
        datecvs = "$" + "Date: 2006/AA/21 10:07:22 $"
        datestruct_beginning_expected = (0, 0, 0, 0, 0, 0)
        self.assertEqual(dateutils.convert_datecvs_to_datestruct(datecvs)[:6],
                         datestruct_beginning_expected)

class ConvertIntoDateGUITest(unittest.TestCase):
    """
    Testing conversion into dategui with various languages.
    """

    def test_convert_good_to_dategui_en(self):
        """dateutils - conversion of good text date into English GUI date"""
        datetext = "2006-07-16 18:36:01"
        dategui_en_expected = "16 Jul 2006, 18:36"
        dategui_en = dateutils.convert_datetext_to_dategui(datetext,
                                                           ln='en')
        self.assertEqual(dategui_en, dategui_en_expected)


    def test_convert_good_to_dategui_sk(self):
        """dateutils - conversion of good text date into Slovak GUI date"""
        datetext = "2006-07-16 18:36:01"
        dategui_sk_expected = "16 júl 2006, 18:36"
        dategui_sk = dateutils.convert_datetext_to_dategui(datetext,
                                                           ln='sk')
        self.assertEqual(dategui_sk, dategui_sk_expected)


    def test_convert_no_month_to_dategui_en(self):
        """dateutils - conversion of no month text date into English GUI date"""
        datetext = "2006-00-00 00:00:00"
        dategui_en_expected = "2006"
        dategui_en = dateutils.convert_datetext_to_dategui(datetext,
                                                           ln='en')
        self.assertEqual(dategui_en, dategui_en_expected)

    def test_convert_no_day_to_dategui_en(self):
        """dateutils - conversion of no day text date into English GUI date"""
        datetext = "2006-12-00 00:00:00"
        dategui_en_expected = "Dec 2006"
        dategui_en = dateutils.convert_datetext_to_dategui(datetext,
                                                           ln='en')
        self.assertEqual(dategui_en, dategui_en_expected)

    def test_convert_bad_to_dategui_en(self):
        """dateutils - conversion of bad text date into English GUI date"""
        datetext = "2006-02-AA 18:36:01"
        dategui_sk_expected = "N/A"
        dategui_sk = dateutils.convert_datetext_to_dategui(datetext,
                                                           ln='en')
        self.assertEqual(dategui_sk, dategui_sk_expected)

    def test_convert_bad_to_dategui_sk(self):
        """dateutils - conversion of bad text date into Slovak GUI date"""
        datetext = "2006-02-AA 18:36:01"
        dategui_sk_expected = "nepríst."
        dategui_sk = dateutils.convert_datetext_to_dategui(datetext,
                                                           ln='sk')
        self.assertEqual(dategui_sk, dategui_sk_expected)

def create_test_suite():
    """
    Return test suite for the dateutils.
    """
    return unittest.TestSuite((unittest.makeSuite(ConvertFromDateCVSTest,
                                                  'test'),
                               unittest.makeSuite(ConvertIntoDateGUITest,
                                                 'test')))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(create_test_suite())
