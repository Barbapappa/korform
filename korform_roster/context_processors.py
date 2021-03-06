def user_data(request):
    # Logged out users cannot have badge counts
    if not request.user.is_authenticated():
        return {}
    
    members_badge = 0
    members = request.user.profile.members.filter(site=request.site).prefetch_related('site')
    for member in members:
        if member.get_badge_count(request):
            members_badge += 1
    
    contacts_badge = 0
    contacts = request.user.profile.contacts.filter(site=request.site).prefetch_related('site')
    if len(members) != 0 and len(contacts) == 0:
        contacts_badge = u"!"
    
    return {
        'my_members': members,
        'my_contacts': contacts,
        'members_badge': members_badge,
        'contacts_badge': contacts_badge,
    }
