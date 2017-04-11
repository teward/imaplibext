import imaplib
from typing import Union, Tuple, AnyStr, List, Any

__title__ = 'imaplibext._imaplibext'
__author__ = 'Thomas Ward'
__version__ = '0.3.1'
__copyright__ = '2017 Thomas Ward'
__license__ = 'AGPLv3+'
__all__ = (
    'IMAP4',
    'IMAP4_SSL'
)


class IMAP4(imaplib.IMAP4):
    def copy(self, message_set, new_mailbox):
        # type: (AnyStr, AnyStr) -> Tuple[AnyStr, list]
        """Copy 'message_set' messages onto end of 'new_mailbox'.

        (typ, [data]) = <instance>.copy(message_set, new_mailbox)
        """

        # conn.uid('COPY', message_set, new_mailbox)
        return self.uid('COPY', message_set, new_mailbox)

    def fetch(self, message_set, message_parts):
        # type: (AnyStr, AnyStr) -> Tuple[AnyStr, List[Tuple[Any]]]
        """Fetch (parts of) messages, using UID values.

        (typ, [data, ...]) = <instance>.fetch(message_set, message_parts)

        'message_parts' should be a string of selected parts
        enclosed in parentheses, eg: "(UID BODY[TEXT])".

        'data' are tuples of message part envelope and data.
        """

        # conn.uid('FETCH', msgset, parts)
        return self.uid('FETCH', message_set, message_parts)

    def search(self, charset, *criteria):
        # type: (AnyStr, Union[AnyStr, tuple]) -> Tuple[AnyStr, list]
        """Search mailbox for matching messages.

        (typ, [data]) = <instance>.search(charset, criterion, ...)

        'data' is space separated list of matching message UID numbers.
        If UTF8 is enabled, charset MUST be None.
        """

        # conn.uid('SEARCH', charset, criteria)
        return self.uid('SEARCH', charset, " ".join(criteria))

    def sort(self, sort_criteria, charset, *search_criteria):
        # type: (AnyStr, AnyStr, Union[AnyStr,tuple]) -> Tuple[AnyStr, list]
        """IMAP4rev1 extension SORT command.

        (typ, [data]) = <instance>.sort(sort_criteria, charset, search_criteria, ...)
        """

        # conn.uid('SORT', '(SORT CRITERION)', 'CHARSET', 'SEARCH_CRITERIA')

        # Preprocess the search_criterion tuple - make sure all string data is split up in order
        # to make each component of the argument as its own tuple item, instead of strings with
        # spaces.
        _search_criterion = []
        for criterion in search_criteria:
            criterion = str(criterion)
            if ' ' in criterion:
                for subcriterion in criterion.split():
                    _search_criterion.append(subcriterion)
            else:
                _search_criterion.append(criterion)

        search_criteria = tuple(list(_search_criterion))

        # Preprocess the 'sort criteria' provided - make sure it's all in parentheses.
        while True:
            if sort_criteria[0] != '(':
                sort_criteria = '(' + sort_criteria
                continue

            if sort_criteria[len(sort_criteria) - 1] != ')':
                sort_criteria += ')'
                continue

            break

        return self.uid('SORT', sort_criteria, charset, ' '.join(search_criteria))

    def store(self, message_set, command, flags):
        # type: (AnyStr, AnyStr, AnyStr) -> Tuple[AnyStr, list]
        """Alters flag dispositions for messages in mailbox, using UID values.

        (typ, [data]) = <instance>.store(message_set, command, flags)
        """

        # conn.uid('STORE', msg_uid, '-FLAGS', '(\Seen)')
        return self.uid('STORE', message_set, command, flags)


# noinspection PyPep8Naming
class IMAP4_SSL(imaplib.IMAP4_SSL):
    def copy(self, message_set, new_mailbox):
        # type: (AnyStr, AnyStr) -> Tuple[AnyStr, list]
        """Copy 'message_set' messages onto end of 'new_mailbox'.

        (typ, [data]) = <instance>.copy(message_set, new_mailbox)
        """

        # conn.uid('COPY', message_set, new_mailbox)
        return self.uid('COPY', message_set, new_mailbox)

    def fetch(self, message_set, message_parts):
        # type: (AnyStr, AnyStr) -> Tuple[AnyStr, List[Tuple[Any]]]
        """Fetch (parts of) messages, using UID values.

        (typ, [data, ...]) = <instance>.fetch(message_set, message_parts)

        'message_parts' should be a string of selected parts
        enclosed in parentheses, eg: "(UID BODY[TEXT])".

        'data' are tuples of message part envelope and data.
        """

        # conn.uid('FETCH', msgset, parts)
        return self.uid('FETCH', message_set, message_parts)

    def search(self, charset, *criteria):
        # type: (AnyStr, Union[AnyStr, tuple]) -> Tuple[AnyStr, list]
        """Search mailbox for matching messages.

        (typ, [data]) = <instance>.search(charset, criterion, ...)

        'data' is space separated list of matching message UID numbers.
        If UTF8 is enabled, charset MUST be None.
        """

        # conn.uid('SEARCH', charset, criteria)
        return self.uid('SEARCH', charset, " ".join(criteria))

    def sort(self, sort_criteria, charset, *search_criteria):
        # type: (AnyStr, AnyStr, Union[AnyStr,tuple]) -> Tuple[AnyStr, list]
        """IMAP4rev1 extension SORT command.

        (typ, [data]) = <instance>.sort(sort_criteria, charset, search_criteria, ...)
        """

        # conn.uid('SORT', '(SORT CRITERION)', 'CHARSET', 'SEARCH_CRITERIA')

        # Preprocess the search_criterion tuple - make sure all string data is split up in order
        # to make each component of the argument as its own tuple item, instead of strings with
        # spaces.
        _search_criterion = []
        for criterion in search_criteria:
            criterion = str(criterion)
            if ' ' in criterion:
                for subcriterion in criterion.split():
                    _search_criterion.append(subcriterion)
            else:
                _search_criterion.append(criterion)

        search_criteria = tuple(list(_search_criterion))

        # Preprocess the 'sort criteria' provided - make sure it's all in parentheses.
        while True:
            if sort_criteria[0] != '(':
                sort_criteria = '(' + sort_criteria
                continue

            if sort_criteria[len(sort_criteria) - 1] != ')':
                sort_criteria += ')'
                continue

            break

        return self.uid('SORT', sort_criteria, charset, ' '.join(search_criteria))

    def store(self, message_set, command, flags):
        # type: (AnyStr, AnyStr, AnyStr) -> Tuple[AnyStr, list]
        """Alters flag dispositions for messages in mailbox, using UID values.

        (typ, [data]) = <instance>.store(message_set, command, flags)
        """

        # conn.uid('STORE', msg_uid, '-FLAGS', '(\Seen)')
        return self.uid('STORE', message_set, command, flags)
