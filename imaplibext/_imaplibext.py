import imaplib
import socket
from typing import Union, Tuple, AnyStr, List, Any
import sys


class IMAP4(imaplib.IMAP4):
    def __init__(self, host='', port=imaplib.IMAP4_PORT, timeout=None, maxbytes=None):
        # type: (AnyStr, int) -> None
        # Override standard __init__ - we need to add a timeout option and a maxbytes option.

        # This timeout option is used below in the 'open' function override.
        if timeout:
            socket.setdefaulttimeout(timeout)

        # This maxbytes option is used below to override the max bytes allowed to be returned from UID commands and
        # others if defined.  Otherwise it leaves it at the 10000 default.
        if maxbytes:
            imaplib._MAXLINE = maxbytes

        imaplib.IMAP4.__init__(self, host, port)
        return  # PEP compliance

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
        # type: (Union[AnyStr, None], Union[AnyStr, tuple]) -> Tuple[AnyStr, list]
        """Search mailbox for matching messages.

        (typ, [data]) = <instance>.search(charset, criterion, ...)

        'data' is space separated list of matching message UID numbers.
        If UTF8 is enabled, charset MUST be None.
        """

        # conn.uid('SEARCH', charset, criteria)
        return self.uid('SEARCH', charset, " ".join(criteria))

    def sort(self, sort_criteria, charset, *search_criteria):
        # type: (AnyStr, Union[AnyStr, None], Union[AnyStr,tuple]) -> Tuple[AnyStr, list]
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

        # Charset is a required argument, so if we give a charset of "None", we can assume UTF-8 here.
        if not charset:
            charset = 'UTF-8'

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
    def __init__(self, host='', port=imaplib.IMAP4_PORT, timeout=None, maxbytes=None,
                 keyfile=None, certfile=None, ssl_context=None):
        # type: (AnyStr, int, int, any, any, any) -> None
        # Override standard __init__ - we need to add a timeout option.
        # This timeout option is used below in the 'open' function override.
        self.timeout = timeout
        if timeout:
            socket.setdefaulttimeout(timeout)

        # This maxbytes option is used below to override the max bytes allowed to be returned from UID commands and
        # others if defined.  Otherwise it leaves it at the 10000 default.
        if maxbytes:
            imaplib._MAXLINE = maxbytes

        if sys.version_info.major < 3:
            if ssl_context:
                print("Warning: Defining `ssl_context` is not supported in "
                      "Python 2's IMAP_SSL implementation.")
            imaplib.IMAP4_SSL.__init__(self, host, port, keyfile, certfile)
        else:
            imaplib.IMAP4_SSL.__init__(self, host, port, keyfile, certfile, ssl_context)

        return  # PEP compliance

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
        # type: (Union[AnyStr, None], Union[AnyStr, tuple]) -> Tuple[AnyStr, list]
        """Search mailbox for matching messages.

        (typ, [data]) = <instance>.search(charset, criterion, ...)

        'data' is space separated list of matching message UID numbers.
        If UTF8 is enabled, charset MUST be None.
        """

        # conn.uid('SEARCH', charset, criteria)
        return self.uid('SEARCH', charset, " ".join(criteria))

    def sort(self, sort_criteria, charset, *search_criteria):
        # type: (AnyStr, Union[AnyStr, None], Union[AnyStr,tuple]) -> Tuple[AnyStr, list]
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

        # Charset is a required argument, so if we give a charset of "None", we can assume UTF-8 here.
        if not charset:
            charset = 'UTF-8'

        return self.uid('SORT', sort_criteria, charset, ' '.join(search_criteria))

    def store(self, message_set, command, flags):
        # type: (AnyStr, AnyStr, AnyStr) -> Tuple[AnyStr, list]
        """Alters flag dispositions for messages in mailbox, using UID values.

        (typ, [data]) = <instance>.store(message_set, command, flags)
        """

        # conn.uid('STORE', msg_uid, '-FLAGS', '(\Seen)')
        return self.uid('STORE', message_set, command, flags)
