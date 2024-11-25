class Television:
    """
    A class representing a Television with basic controls: power, mute, channel, and volume.

    Attributes:
    MIN_VOLUME : int
        Minimum volume level.
    MAX_VOLUME : int
        Maximum volume level.
    MIN_CHANNEL : int
        Minimum channel number.
    MAX_CHANNEL : int
        Maximum channel number.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    
    def __init__(self) -> None:
        """
        Initializes the Television with power off, unmuted, at minimum volume and channel.
        """
        self.__status: bool = False  # Television is initially off
        self.__muted: bool = False   # Television is initially unmuted
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
    
    def power(self) -> None:
        """
        Switches the power status of the television (on or off).
        """
        
        self.__status = not self.__status
    
    def mute(self) -> None:
        """
        Switches the mute status if the TV is on (muted or unmuted).
        """
        if self.__status:
            self.__muted = not self.__muted
            
    def channel_up(self) -> None:
        """
        Increases the channel number by 1.
        If the channel is at the maximum, it wraps around to the minimum channel.
        Only works if the TV is powered on.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
                
    def channel_down(self) -> None:
        """
        Decreases the channel number by 1.
        If the channel is at the minimum, it wraps around to the maximum channel.
        Only works if the TV is powered on.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1 if it is not muted.
        If the volume is at the maximum, it does not increase further.
        Only works if the TV is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1 if it is not muted.
        If the volume is at the minimum, it does not decrease further.
        Only works if the TV is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns the current status of the television including power status, channel, and volume.

        :return: A string representing the current power status, channel, and volume.
        """
        displayed_volume: int = 0 if self.__muted else self.__volume
        return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{displayed_volume}]"
