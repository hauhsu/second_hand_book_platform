import os

def populate():
    add_book('Clean Code', 500, 'Hau Hsu')
    add_book('Memoy System', 500, 'Hau Hsu')
    add_book('Data Structure in C++', 500, 'Hau Hsu')
    

def add_book(name, price, owner):
    b = Book.objects.get_or_create(name=name, price=price, owner=owner)
    return b

if __name__ == '__main__':
    print 'Starting population script...'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
            'second_hand_book_platform.settings')
    from basic.models import Book
    populate()
