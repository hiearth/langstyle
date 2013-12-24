#!/usr/bin/env python

class MockCharacterImageRepository:

    def __init__(self):
        # {user_id: {character_id: [image_id]}}
        self._character_images = {}

    def get_images(self, user_id, character_id):
        images_link_to_character = self._character_images.get(user_id, {})
        return images_link_to_character.get(character_id, [])

    def get_most_used_images(self, character_id, image_count):
        sorted_most_used_images = []
        image_statistic = self._get_image_statistic(character_id)
        for i in range(0, image_count):
            if not image_statistic:
                break
            image_id = self._get_image_with_max_used_count(image_statistic)
            sorted_most_used_images.append(image_id)
            del image_statistic[image_id]
        return sorted_most_used_images
    
    def _get_image_statistic(self, character_id):
        images_list = [image_ids for char_ids in self._character_images.values()
            for char_id, image_ids in char_ids.items() if char_id == character_id]
        image_statistic = {}
        for images in images_list:
            for image_id in images:
                statistic_count = image_statistic.get(image_id, 0)
                image_statistic[image_id] = statistic_count + 1
        return image_statistic

    def _get_image_with_max_used_count(self, image_statistic):
        max = 0
        image_id_with_max_count = None
        for image_id, statistic_count in image_statistic.items():
            if statistic_count>max:
                image_id_with_max_count = image_id
        return image_id_with_max_count
            

    def link(self, user_id, character_id, image_id):
        if user_id not in self._character_images:
            self._character_images[user_id] = {}
        if character_id not in self._character_images[user_id]:
            self._character_images[user_id][character_id] = []
        if image_id not in self._character_images[user_id][character_id]:
            self._character_images[user_id][character_id].append(image_id)

    def unlink(self, user_id,character_id, image_id):
        if user_id not in self._character_images:
            return
        if character_id not in self._character_images[user_id]:
            return
        if image_id not in self._character_images[user_id][character_id]:
            return
        self._character_images[user_id][character_id].remove(image_id)