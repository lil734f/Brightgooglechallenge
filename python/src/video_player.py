"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        ordered_videos = []
        for video in all_videos:
            video_format = f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]"
            ordered_videos.append(video_format)
        
        ordered_videos.sort()
        print("Here's a list of all available videos:")
        for video in ordered_videos:
            print(f"  {video}")

    def playing(self):
        "Return video object currently playing"
        all_videos = self._video_library.get_all_videos()
        for v in all_videos:
            if v._status == 1:
                return(v)
        return(None)

    def paused(self):
        "Return video object currently playing"
        all_videos = self._video_library.get_all_videos()
        for v in all_videos:
            if v._status == 2:
                return(v)
        return(None)
    """Had discussions with others (worked in conjunction with others) about these 2 functions (about how to store the status of video),
    the code below was quite simple from then and was completed in a similar fashion to many other
    this is seen below"""

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
        else:
            if self.playing() is not None:
                print("Stopping video: {}".format(self.playing()._title))
                self.playing()._status = 0
            elif self.paused() is not None:
                    print("Stopping video: {}".format(self.paused()._title))
                    self.paused()._status = 0
            print("Playing video: {}".format(video._title))
            video._status = 1

    def stop_video(self):
        """Stops the current video."""
        if self.playing() is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: {}".format(self.playing()._title))
            self.playing()._status = 0

    def play_random_video(self):
        """Plays a random video from the video library."""
        video = random.choice(self._video_library.get_all_videos())
        self.play_video(video._video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self.paused() is not None:
            print("Video already paused: {}".format(self.paused()._title))
        elif self.playing() is not None:
            print("Pausing video: {}".format(self.playing()._title))
            self.playing()._status = 2
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.playing() is not None:
            print("Cannot continue video: Video is not paused")
        elif self.paused() is not None:
            print("Continuing video: {}".format(self.paused()._title))
            self.paused()._status = 1
        else:
            print("Cannot continue video: No video is currently playing")
        
    def show_playing(self):
        """Displays video currently playing."""
        if self.playing() is not None:
            tup = self.playing()._tags
            print("Currently playing: {} ({}) [{}]".format(self.playing()._title, self.playing()._video_id, " ".join(tup)))
        elif self.paused() is not None:
            tup = self.paused()._tags
            print("Currently playing: {} ({}) [{}] - PAUSED".format(self.paused()._title, self.paused()._video_id, " ".join(tup)))
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
