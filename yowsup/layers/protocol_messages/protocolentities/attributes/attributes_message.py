from yowsup.layers.protocol_messages.protocolentities.attributes.attributes_image import ImageAttributes
from yowsup.layers.protocol_messages.protocolentities.attributes.attributes_extendedtext import ExtendedTextAttributes
from yowsup.layers.protocol_messages.protocolentities.attributes.attributes_document import DocumentAttributes
from yowsup.layers.protocol_messages.protocolentities.attributes.attributes_contact import ContactAttributes
from yowsup.layers.protocol_messages.protocolentities.attributes.attributes_location import LocationAttributes


class MessageAttributes(object):
    def __init__(
            self,
            conversation=None,
            image=None,
            contact=None,
            location=None,
            extended_text=None,
            document=None,
            audio=None,
            video=None,
            protocol=None,
            sticker=None
    ):
        self._conversation = conversation  # type: str
        self._image = image  # type: ImageAttributes
        self._contact = contact  # type: ContactAttributes
        self._location = location  # type: LocationAttributes
        self._extended_text = extended_text  # type: ExtendedTextAttributes
        self._document = document  # type: DocumentAttributes

    def __str__(self):
        attrs = []
        if self.conversation is not None:
            attrs.append(("conversation", self.conversation))
        if self.image is not None:
            attrs.append(("image", self.image))
        if self.contact is not None:
            attrs.append(("contact", self.contact))
        if self.location is not None:
            attrs.append(("location", self.location))
        if self.extended_text is not None:
            attrs.append(("extended_text", self.extended_text))

        return "[%s]" % " ".join((map(lambda item: "%s=%s" % item, attrs)))

    @property
    def conversation(self):
        return self._conversation

    @conversation.setter
    def conversation(self, value):
        self._conversation = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def extended_text(self):
        return self._extended_text

    @extended_text.setter
    def extended_text(self, value):
        self._extended_text = value

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        self._document = value