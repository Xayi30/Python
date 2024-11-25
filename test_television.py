import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        
        self.tv = Television()

    def teardown_method(self):
        
        del self.tv

    def test_init(self):
        
        assert self.tv._Television__status == False
        assert self.tv._Television__muted == False
        assert self.tv._Television__volume == Television.MIN_VOLUME
        assert self.tv._Television__channel == Television.MIN_CHANNEL

    def test_power(self):
        
        self.tv.power()
        assert self.tv._Television__status == True
        self.tv.power()
        assert self.tv._Television__status == False

    def test_mute(self):
        
        self.tv.power()  
        self.tv.mute()
        assert self.tv._Television__muted == True
        self.tv.mute()
        assert self.tv._Television__muted == False

    def test_channel_up(self):
        
        self.tv.power()  
        self.tv.channel_up()
        assert self.tv._Television__channel == Television.MIN_CHANNEL + 1
        # Test wrap around
        self.tv._Television__channel = Television.MAX_CHANNEL
        self.tv.channel_up()
        assert self.tv._Television__channel == Television.MIN_CHANNEL

    def test_channel_down(self):
        
        self.tv.power()  
        self.tv.channel_down()
        assert self.tv._Television__channel == Television.MAX_CHANNEL
        # Test wrap around
        self.tv._Television__channel = Television.MIN_CHANNEL
        self.tv.channel_down()
        assert self.tv._Television__channel == Television.MAX_CHANNEL

    def test_volume_up(self):
        
        self.tv.power()  
        self.tv.volume_up()
        assert self.tv._Television__volume == Television.MIN_VOLUME + 1
        # Test maximum volume
        self.tv._Television__volume = Television.MAX_VOLUME
        self.tv.volume_up()
        assert self.tv._Television__volume == Television.MAX_VOLUME

    def test_volume_down(self):
        
        self.tv.power()  
        self.tv.volume_down()
        assert self.tv._Television__volume == Television.MIN_VOLUME
        # Test minimum volume
        self.tv._Television__volume = Television.MIN_VOLUME
        self.tv.volume_down()
        assert self.tv._Television__volume == Television.MIN_VOLUME
