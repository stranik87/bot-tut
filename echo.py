import time
from handlers import (
    get_last_udpate,
    send_text,
    send_photo,
    send_sticker,
    send_video,
    send_audio,
    send_document,
    send_voice,
    send_location,
    send_contact,
)


def main():
    last_update = get_last_udpate()
    
    last_update_id = last_update['update_id']

    while True:
        current_update = get_last_udpate()
        current_update_id = current_update['update_id']

        if last_update_id != current_update_id:
            chat_id = current_update['message']['chat']['id']

            if 'text' in current_update['message']:
                text    = current_update['message']['text']
                if text == '/start':
                    send_text(chat_id=chat_id)
                else:
                    send_text(chat_id=chat_id, text=text)

            elif 'photo' in current_update['message']:
                print('photo')
                photo_id = current_update['message']['photo'][0]['file_id']
                send_photo(chat_id=chat_id, photo_id=photo_id)

            elif 'sticker' in current_update['message']:
                sticker_id = current_update['message']['sticker']['file_id']
                send_sticker(chat_id=chat_id, sticker=sticker_id)
                
            elif 'video' in current_update['message']:
                video_id = current_update['message']['video']['file_id']
                send_video(chat_id=chat_id,video=video_id)
                
            elif 'audio' in current_update['message']:
                audio_id = current_update['message']['audio']['file_id']
                send_audio(chat_id=chat_id,audio=audio_id)
                
            elif 'document' in current_update['message']:
                document_id = current_update['message']['document']['file_id']
                send_document(chat_id=chat_id,document=document_id)
                
            elif 'voice' in current_update['message']:
                voice_id = current_update['message']['voice']['file_id']
                send_voice(chat_id=chat_id,voice=voice_id)
                
            elif 'location' in current_update['message']:
                latitude_id = current_update['message']['location']['latitude']
                longitude_id = current_update['message']['location']['longitude']
                send_location(chat_id=chat_id,latitude=latitude_id,longitude=longitude_id)
                
            elif 'contact' in current_update['message']:
                
                phone_number = current_update['message']['contact']['phone_number']
                first_name = current_update['message']['contact']['first_name']
                send_contact(chat_id=chat_id,phone_number=phone_number,first_name=first_name)
                

            last_update_id = current_update_id

        time.sleep(1)

main()