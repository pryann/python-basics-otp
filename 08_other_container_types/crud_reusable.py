def generate_id(items: list[dict]) -> int:
    return max(item["id"] for item in items) + 1


def get_all(items: list[dict]) -> list[dict]:
    return items


def find_by_id(items: list[dict], id: int) -> dict | None:
    for item in items:
        if item["id"] == id:
            return item


def update_by_id(items: list[dict], id: int, update_item: dict) -> dict | None:
    item = find_by_id(items, id)
    if item is not None:
        index = items.index(item)
        items[index].update(update_item)
        return items[index]


def create(items: list[dict], item: dict) -> dict:
    new_item = {"id": generate_id(items)}
    new_item.update(item)
    items.append(new_item)
    return items[-1]


def delete_by_id(items: list[dict], id: int) -> dict | None:
    item = find_by_id(items, id)
    if item is not None:
        items.remove(item)
        return item
