class Guest(object):
    def __init__(self, guest_name, inviter, brought, consumed):
        self.guest_name = guest_name
        self.inviter = inviter
        self.brought = brought
        self.consumed = consumed
        self.left_over = brought - consumed
        self.invitee = []


def invite_him(guest, result):
    total_left_over = guest.left_over
    for invitee in guest.invitee:
        total_left_over += invitee.left_over
    if total_left_over >= 0:
        result[guest.guest_name] = 'Welcome'
    else:
        if guest.left_over >= 0:
            result[guest.guest_name] = 'Welcome'
        else:
            result[guest.guest_name] = 'Not Welcome'


def party_invite(guest_list):
    adam = Guest('Adam', None, 0, 0)
    persons = {'Adam': adam}
    for guest_name, inviter_name, brought, consumed in guest_list:
        # key error will throw if the inviter is not present yet
        guest = Guest(guest_name, persons[inviter_name], brought, consumed)
        persons[inviter_name].invitee.append(guest)
        persons[guest_name] = guest

    result = {}
    for person_name, person in persons.iteritems():
        if person_name != 'Adam':
            invite_him(person, result)
    print result


if __name__ == '__main__':
    invites = [
        ("Beth", "Adam", 4, 2),
        ("Cass", "Adam", 3, 4),
        ("Dole", "Adam", 2, 3),
        ("Evan", "Beth", 3, 1),
        ("Fury", "Evan", 2, 2),
        ("Greg", "Dole", 6, 2),
        ("Hugh", "Cass", 4, 4),
        ("Ivan", "Cass", 6, 4),
        ("Juan", "Cass", 3, 1),
        ("Kale", "Ivan", 1, 6),
        ("Leon", "Ivan", 2, 5),
        ("Mark", "Ivan", 1, 6)]

    party_invite(invites)
