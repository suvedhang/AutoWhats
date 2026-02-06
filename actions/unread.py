def get_unread_breakdown(page):
    chat_rows = page.query_selector_all('div[role="row"]')

    result = []
    total_unread = 0

    for row in chat_rows:
        # Chat name
        name_el = row.query_selector('span[dir="auto"]')
        if not name_el:
            continue

        chat_name = name_el.inner_text().strip()

        # Unread badge (if any)
        badge = row.query_selector('span[aria-label*="unread"]')
        if badge:
            text = badge.inner_text().strip()
            unread = int(text) if text.isdigit() else 1

            result.append({
                "name": chat_name,
                "unread": unread
            })
            total_unread += unread

    return {
        "total": total_unread,
        "chats": result
    }
