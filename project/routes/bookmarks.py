from flask import Blueprint, request, jsonify, current_app
import validators
from flasgger import swag_from

from project.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED,HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST
from project.models.bookmark import BookmarkModel
from project.routes import API_PREFIX

BOOKMARKS_PREFIX: str = "/bookmarks"
bookmarks = Blueprint("Bookmarks", __name__, url_prefix=API_PREFIX + BOOKMARKS_PREFIX)


@bookmarks.post("")
@swag_from('../docs/bookmarks/create.yaml')
def create_bookmark():

    body = request.get_json().get('body', '')
    url = request.get_json().get('url', '')
    if not validators.url(url):
        return jsonify({
            'error': 'Enter a valid url'
        }), HTTP_400_BAD_REQUEST

    bookmark = BookmarkModel(body=body, url=url, visits=1)
    bookmark.save_to_db()

    current_app.logger.info('Bookmark created', extra={
        'result': 'Bookmark Created',
    })
    
    return jsonify({
        'message': 'Bookmark Created',
    }), HTTP_201_CREATED


@bookmarks.get("")
@swag_from('../docs/bookmarks/list.yaml')
def get_bookmarks():
    page = request.args.get('page', 1, type=int)
    per_page= request.args.get('count', 10, type=int)

    current_app.logger.info('Bookmarks received', extra={
        'page': page,
        'per_page': per_page,
    })

    bookmarks = BookmarkModel.find_all_paginate(page=page, per_page=per_page)


    data: list[BookmarkModel] = []
    for item in bookmarks.items:
        data.append({
            'id': item.id,
            'body': item.body,
            'url': item.url,
            'short_url': item.short_url
        })
    return jsonify({
         'results': data,
         'meta': {
             'page': bookmarks.page,
             'pages': bookmarks.page,
             'total_count': bookmarks.total,
             'prev_page': bookmarks.prev_num,
             'next_page': bookmarks.next_num,
             'has_next': bookmarks.has_next,
             'has_prev': bookmarks.has_prev
         }
    }), HTTP_200_OK

@bookmarks.put("/<id>")
@swag_from('../docs/bookmarks/put.yaml')
def update_bookmark(id):
    current_app.logger.info('Bookmarks id', extra={
        'id': id
    })
    bookdata = BookmarkModel.find_by_id(id)
    data = request.get_json()
    if data.get('body'):
        bookdata.body = data['body']
    if data.get('url'):
        bookdata.url = data['url']
    bookdata.save_to_db()

    return jsonify({
         'results':  {
             'body': bookdata.body,
             'url': bookdata.url
         }
    }), HTTP_200_OK
@bookmarks.delete("/<id>")
@swag_from('../docs/bookmarks/delete.yaml')
def delete_bookmark(id):
    current_app.logger.info('Bookmarks id', extra={
        'id': id
    })
    book_del_data = BookmarkModel.find_by_id(id)
    if book_del_data==None:
        print(())
        return jsonify({
            'message': 'No Content',
        }), HTTP_204_NO_CONTENT
    else:
        book_del_data.delete_from_db()

        return jsonify({
            'message': 'Bookmark deleted',
        }),HTTP_200_OK