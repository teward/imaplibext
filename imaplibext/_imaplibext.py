import imaplib
from typing import Union, Tuple, AnyStr, List, Any

__title__ = 'imaplibext._imaplibext'
__author__ = 'Thomas Ward'
__copyright__ = '2017 Thomas Ward'
__license__ = 'GPL 3.0/LGPL 3.1'
__all__ = (
    'IMAP4',
    'IMAP4_SSL'
)


class IMAP4(imaplib.IMAP4):
    def search(self, charset, *criteria):
        # type: (AnyStr, Union[AnyStr, tuple]) -> Tuple[AnyStr, list]
        """Search mailbox for matching messages.

        (typ, [data]) = <instance>.search(charset, criterion, ...)

        'data' is space separated list of matching message UID numbers.
        If UTF8 is enabled, charset MUST be None.
        """

        # conn.uid('SEARCH', charset, criteria)
        return self.uid('SEARCH', charset, " ".join(criteria))

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

    def store(self, message_set, command, flags):
        # type: (AnyStr, AnyStr, AnyStr) -> Tuple[AnyStr, list]
        """Alters flag dispositions for messages in mailbox, using UID values.

        (typ, [data]) = <instance>.store(message_set, command, flags)
        """

        # conn.uid('STORE', msg_uid, '-FLAGS', '(\Seen)')
        return self.uid('STORE', message_set, command, flags)


# noinspection PyPep8Naming
class IMAP4_SSL(imaplib.IMAP4_SSL):
    def search(self, charset, *criteria):
        # type: (AnyStr, Union[AnyStr, tuple]) -> Tuple[AnyStr, list]
        """Search mailbox for matching messages.

        (typ, [data]) = <instance>.search(charset, criterion, ...)

        'data' is space separated list of matching message UID numbers.
        If UTF8 is enabled, charset MUST be None.
        """

        # conn.uid('SEARCH', charset, criteria)
        return self.uid('SEARCH', charset, " ".join(criteria))

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

    def store(self, message_set, command, flags):
        # type: (AnyStr, AnyStr, AnyStr) -> Tuple[AnyStr, list]
        """Alters flag dispositions for messages in mailbox, using UID values.

        (typ, [data]) = <instance>.store(message_set, command, flags)
        """

        # conn.uid('STORE', msg_uid, '-FLAGS', '(\Seen)')
        return self.uid('STORE', message_set, command, flags)
