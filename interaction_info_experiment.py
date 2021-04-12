# -*- coding: utf-8 -*-

"""
@author: zyw
@file: interaction_info_experiment.py
@time: 2021/3/6
"""

"""
Extract the 'href' and 'img-src' of the interaction tags from each sample.
Note that, considering the tags in sub-frames if there are nested frames in the sample.
Two parts:
    (1). href attribute of the tags;
    (2). src attribute of the img tags if there are.
In addition to <img> tags, there are some other view-tags inside the interaction tags, such as <video>.
Manually inspect such unusual tags, and consider their src-attributes. 
"""

import os
import sys

from publicsuffixlist import PublicSuffixList
from lxml import etree
from frame_tree import *
from urllib import parse
from pprint import pprint


def build_frame_tree(sample_end_url: str, sample_dir: str):
    """
    Given the end_url and the directory of the one sample, build its frame tree.
    Layer traverse the directory to get the frame node.
    :param sample_end_url:
    :param sample_dir:
    :return:
    """
    file_list = os.listdir(sample_dir)
    root_rect = {'x': 0, 'y': 0, 'width': 1664, 'height': 919}
    frame_root_node = FrameNode('root', sample_end_url, root_rect, sample_dir, 'root')
    frame_tree = FrameTree(frame_root_node)

    queue = []      # Queue records the directory of the sub-frames.
    redirection_file = os.path.join(sample_dir, 'redirection_tags.txt')
    sub_frame_tag_list = [frame_tag for frame_tag in file_list if frame_tag[:7] == 'iframe_']
    with open(redirection_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            line = line.strip('\n').split('\t')
            if line[0] in sub_frame_tag_list:
                frame_rect = extract_rect(line[3])[0]
                temp_item = analyze_iframe_html_src(line[4])
                # No src field in the iframe, use sample_end_url instead.
                if not temp_item:
                    frame_src = sample_end_url
                else:
                    frame_src = analyze_iframe_html_src(line[4])[0][1]
                sub_frame_dir = os.path.join(sample_dir, line[0])
                frame_level = frame_root_node.frame_level + '/' + line[0]
                sub_frame_node = FrameNode(line[0], frame_src, frame_rect, sub_frame_dir, frame_level, frame_root_node)
                queue += [sub_frame_node]

    # The remaining frame directories contain no performance log and screenshot.
    while queue:
        cur_frame_node = queue.pop(0)
        frame_tree.add_node(cur_frame_node)
        # Get its sub-frames.
        cur_file_list = os.listdir(cur_frame_node.frame_dir)
        if len(cur_file_list) > 2:
            temp_frame_tag_list = [frame_tag for frame_tag in cur_file_list if frame_tag[:7] == 'iframe_']
            redirection_file = os.path.join(cur_frame_node.frame_dir, 'redirection_tags.txt')
            with open(redirection_file, 'r', encoding='utf-8') as fr:
                for line in fr:
                    line = line.strip('\n').split('\t')
                    if line[0] in temp_frame_tag_list:
                        frame_rect = extract_rect(line[3])[0]
                        temp_item = analyze_iframe_html_src(line[4])
                        # No src field in the iframe, use sample_end_url instead.
                        if not temp_item:
                            frame_src = cur_frame_node.frame_src
                        else:
                            frame_src = analyze_iframe_html_src(line[4])[0][1]
                        sub_frame_dir = os.path.join(cur_frame_node.frame_dir, line[0])
                        frame_level = cur_frame_node.frame_level + '/' + line[0]
                        sub_frame_node = FrameNode(line[0], frame_src, frame_rect, sub_frame_dir, frame_level, cur_frame_node)
                        queue += [sub_frame_node]
    return frame_tree


def get_sample_dir_iie(sample: str, sample_source: str) -> str:
    win_source_dict = {
        'aliyun_1': r'D:\PythonProject\performanceLog_analysis\other_aliyun\tag_info',
        'aliyun_2': r'D:\PythonProject\performanceLog_analysis\other_aliyun\tag_info_2',
        'aliyun_3': r'D:\PythonProject\performanceLog_analysis\other_aliyun\tag_info_3',
        'liang_1': r'D:\PythonProject\performanceLog_analysis\other_liangzhizhou\zyw_task\tag_info',
        'liang_2': r'D:\PythonProject\performanceLog_analysis\other_liangzhizhou\zyw_task\tag_info_2',
        'vmware_1': r'D:\PythonProject\performanceLog_analysis\other_vmware\tag_info',
        'vmware_2': r'D:\PythonProject\performanceLog_analysis\other_vmware\tag_info_2',
        'yan_1': r'D:\PythonProject\performanceLog_analysis\other_yandingkui\zyw_task\tag_info',
        'yan_2': r'D:\PythonProject\performanceLog_analysis\other_yandingkui\zyw_task\tag_info_2',
        'zeng_1': r'D:\PythonProject\performanceLog_analysis\tag_info',
        'zeng_2': r'D:\PythonProject\performanceLog_analysis\tag_info_2',
        'zeng_temp': r'D:\PythonProject\performanceLog_analysis\tag_info_temp'
    }
    mac_source_dict = {
        'aliyun_1': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_aliyun/tag_info',
        'aliyun_2': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_aliyun/tag_info_2',
        'aliyun_3': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_aliyun/tag_info_3',
        'liang_1': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_liangzhizhou/zyw_task/tag_info',
        'liang_2': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_liangzhizhou/zyw_task/tag_info_2',
        'vmware_1': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_vmware/tag_info',
        'vmware_2': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_vmware/tag_info_2',
        'yan_1': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_yandingkui/zyw_task/tag_info',
        'yan_2': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/other_yandingkui/zyw_task/tag_info_2',
        'zeng_1': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/tag_info',
        'zeng_2': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/tag_info_2',
        'zeng_temp': '/Volumes/Seagate Basic/paper_code/performanceLog_analysis/tag_info_temp'
    }

    return os.path.join(win_source_dict[sample_source], sample) if sys.platform[:3] == 'win' else os.path.join(
        mac_source_dict[sample_source], sample)


def get_redirection_tags(sample_dir: str) -> tuple:
    """
    Given the directory of the sample, extract the redirection info from 'redirection_tags.txt'.
    There are no screenshot and performance log in the iframe directory, namely only page source and redirection tags.
    We should also check whether there are inner-frames in the current sample.
    If current sample is not a iframe, it has at least files, namely page_source.html, performance_log.txt, redirection_tags.txt, screenshot.png, and some iframe directories (maybe).
    If current sample is a iframe, it has at least two files, namely page_source.html, redirection_tags.txt, and some iframe directories (maybe).
    :param sample_dir:
    :return: (a, area, onclick, iframe)
    """
    tag_info_file = os.path.join(sample_dir, 'redirection_tags.txt')
    a_list = []
    area_list = []
    onclick_list = []
    iframe_list = []
    with open(tag_info_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            line = line.strip('\n').split('\t')
            tag_label = line[1]
            is_visible = line[2]
            rect = line[3]
            html = line[4] if len(line) == 5 else ''.join(line[4:])
            # Filter the invisible tags.
            if is_visible == '0' or rect == '[]':
                continue
            if tag_label == 'a':
                a_list += [(rect, html)]
            elif tag_label == 'area':
                area_list += [(rect, html)]
            elif tag_label == 'onclick':
                onclick_list += [(rect, html)]
            else:
                iframe_list += [(rect, html)]
    return a_list, area_list, onclick_list, iframe_list


def extract_rect(rect_str: str) -> list:
    """
    :param rect_info: [rect1, rect2, ...]
    :return: [{x1, y1, width1, height1}, {x2, y2, width2, height2}, ...]
    """
    rect_info_list = eval(rect_str)
    return rect_info_list


def check_tag_implicit_href(tag_attrib_dict: dict) -> dict:
    """
    Given an attrib dict of a tag, determine whether there are URLs in the values.
    If yes, return a dict, in which the key is the attrib and the value is the URL.
    :param tag_attrib_dict:
    :return:
    """
    # Filter some useless attrib.
    noise_attrib_set = {'alt', 'class', 'id', 'name', 'onclick', 'rel', 'style', 'target', 'title'}
    attrib_url_dict = {}
    for attrib in tag_attrib_dict:
        if attrib in noise_attrib_set or tag_attrib_dict[attrib] == '':
            continue
        elif '/' in tag_attrib_dict[attrib]:
            attrib_url_dict[attrib] = tag_attrib_dict[attrib]
    return attrib_url_dict


def analyze_a_html_href(html_str: str):
    """
    Extract the attrib and the corresponding URL.
    :param html_str:
    :return:
    """
    tag_html = etree.HTML(html_str)
    a_tag_html = tag_html.xpath('//a')[0]
    a_tag_attrib = a_tag_html.attrib
    attrib_url_list = []
    if len(a_tag_attrib) != 0:
        if 'href' in a_tag_attrib and a_tag_attrib['href'] != '':
            attrib_url_list += [('href', a_tag_attrib['href'])]
        elif 'href' not in a_tag_attrib:
            implicit_dict = check_tag_implicit_href(a_tag_attrib)
            for implicit_key in implicit_dict:
                attrib_url_list += [(implicit_key, implicit_dict[implicit_key])]
    return attrib_url_list


def analyze_area_html_href(html_str: str):
    # Only consider the valid <area> tags. Namely the <area> tags with 'href' field.
    tag_html = etree.HTML(html_str)
    area_tag_html = tag_html.xpath('//area')[0]
    area_tag_attrib = area_tag_html.attrib
    attrib_url_list = []
    if len(area_tag_attrib) != 0 and 'href' in area_tag_attrib and area_tag_attrib['href'] != '':
        attrib_url_list += [('href', area_tag_attrib['href'])]
    return attrib_url_list


def analyze_onclick_html_js(html_str: str):
    # The content of the 'onclick' field is JS code.
    tag_html = etree.HTML(html_str)
    onclick_tag_html = tag_html.xpath('//*[@onclick]')[0]
    onclick_tag_attrib = onclick_tag_html.attrib
    attrib_js_list = []
    if onclick_tag_attrib['onclick'] != '':
        attrib_js_list += [('js', onclick_tag_attrib['onclick'])]
    return attrib_js_list


def analyze_iframe_html_src(html_str: str):
    """
    In our experiments, we consider <frame>, <iframe>, and <object> as the frame tags.
    Here, we only consider the 'src' of <frame> and <iframe> tags, and the 'data' of <object> tags.
    :param html_str:
    :return:
    """
    tag_html = etree.HTML(html_str)
    iframe_tag_html_list = tag_html.xpath('//iframe[@src]')
    frame_tag_html_list = tag_html.xpath('//frame[@src]')
    object_tag_html_list = tag_html.xpath('//object[@data]')
    iframe_src_list = []
    if iframe_tag_html_list and 'src' in iframe_tag_html_list[0].attrib and iframe_tag_html_list[0].attrib['src'] != '':
        iframe_src_list += [('src', iframe_tag_html_list[0].attrib['src'])]
    elif frame_tag_html_list and 'src' in frame_tag_html_list[0].attrib and frame_tag_html_list[0].attrib['src'] != '':
        iframe_src_list += [('src', frame_tag_html_list[0].attrib['src'])]
    elif object_tag_html_list and 'data' in object_tag_html_list[0].attrib and object_tag_html_list[0].attrib['data'] != '':
        iframe_src_list += [('src', object_tag_html_list[0].attrib['data'])]
    return iframe_src_list


def analyze_a_tag_info(a_info_list: list):
    """
    Analyze both the rect and the HTML code.
    Only consider the <a> tag and its rect in this func, namely rect[0].
    :param a_info_list: [(rect, html), (rect, html), ...]
    :return:
    """
    a_href_info_list = []       # [(rect, href_info), (rect, href_info), ...]
    for i, item in enumerate(a_info_list):
        tag_rect = extract_rect(item[0])[0]
        attrib_url_list = analyze_a_html_href(item[1])
        for attrib_url_item in attrib_url_list:
            attrib, href = attrib_url_item[0], attrib_url_item[1]
            a_href_info_list += [(tag_rect, attrib, href)]
    return a_href_info_list


def analyze_area_tag_info(area_info_list: list):
    area_href_info_list = []        # [(rect, href_info), ...]
    for i, item in enumerate(area_info_list):
        tag_rect = extract_rect(item[0])[0]
        attrib_url_list = analyze_area_html_href(item[1])
        for attrib_url_item in attrib_url_list:
            attrib, href = attrib_url_item[0], attrib_url_item[1]
            area_href_info_list += [(tag_rect, attrib, href)]
    return area_href_info_list


def analyze_onclick_tag_info(onclick_info_list: list):
    onclick_js_info_list = []     # [(rect, js_info), ...]
    for i, item in enumerate(onclick_info_list):
        tag_rect = extract_rect(item[0])[0]
        attrib_js_list = analyze_onclick_html_js(item[1])
        for attrib_js_item in attrib_js_list:
            attrib, js_code = attrib_js_item[0], attrib_js_item[1]
            onclick_js_info_list += [(tag_rect, attrib, js_code)]
    return onclick_js_info_list


def analyze_iframe_tag_info(sample: str, source: str, iframe_info_list: list):
    iframe_src_info_list = []
    for i, item in enumerate(iframe_info_list):
        tag_rect = extract_rect(item[0])[0]
        attrib_src_list = analyze_iframe_html_src(item[1])
        if not attrib_src_list:
            print(sample, source, item[1], '\n')
        for attrib_src_item in attrib_src_list:
            attrib, src = attrib_src_item[0], attrib_src_item[1]
            iframe_src_info_list += [(tag_rect, attrib, src)]
    return iframe_src_info_list


def extract_interaction_tags_per_frame(sample: str, source: str, end_url: str):
    sample_dir = get_sample_dir_iie(sample, source)
    frame_tree = build_frame_tree(end_url, sample_dir)
    frame_node_list = frame_tree.parse_frame_tree()
    agg_info_list = []
    # Only consider the <a>, <area>, and <onclick> tags.
    for frame_node in frame_node_list:
        a_list, area_list, onclick_list, _ = get_redirection_tags(frame_node.frame_dir)
        a_href_info_list = analyze_a_tag_info(a_list)
        area_href_info_list = analyze_area_tag_info(area_list)
        onclick_js_info_list = analyze_onclick_tag_info(onclick_list)
        # Arrange the extracted info.
        for a_info in a_href_info_list:
            temp_item = ['a', source, frame_node.frame_level, frame_node.frame_src, str(a_info[0]), a_info[2]]
            temp_item_str = '\t'.join(temp_item) + '\n'
            agg_info_list += [temp_item_str]
        for area_info in area_href_info_list:
            temp_item = ['area', source, frame_node.frame_level, frame_node.frame_src, str(area_info[0]), area_info[2]]
            temp_item_str = '\t'.join(temp_item) + '\n'
            agg_info_list += [temp_item_str]
        for onclick_info in onclick_js_info_list:
            temp_item = ['onclick', source, frame_node.frame_level, frame_node.frame_src, str(onclick_info[0]), onclick_info[2]]
            temp_item_str = '\t'.join(temp_item) + '\n'
            agg_info_list += [temp_item_str]
    return agg_info_list


def save_agg_tag_info(save_root_dir: str, sample: str, source: str, tag_info_list: list):
    # The save directory of the the sample tags.
    sample_source_dir = os.path.join(save_root_dir, source)
    if not os.path.exists(sample_source_dir):
        os.mkdir(sample_source_dir)
    sample_file = sample + '.txt'
    sample_file = os.path.join(sample_source_dir, sample_file)
    with open(sample_file, 'w', encoding='utf-8') as fw:
        tag_info_str = ''.join(tag_info_list)
        fw.write(tag_info_str)
        print("%s - %s has %d tags. Done." % (source, sample, len(tag_info_list)))


def analyze_a_inner_visual_tags(html_str: str, path):
    """
    Given the HTML code of <a>, analyze its inner visual tags, such as <img>.
    Involving the following tasks:
        1. Any other visual tags except to <img>?
        2. Any other attribute indicating the URL of the visual element except to 'src'?
    -------------------------------------------------
    // target tags
    <button>: data-clipboard-text, href, onclick
    <div>: data-androidlink, data-ioslink, data-lazy-background, data-original, data-src, href, onclick, src, style
    <f>: href
    <img>: data-original, data-src, data-url, lay-src, lazy-src, original, originalsrc, _src, src, srcset, style
    <input>: data-clipboard-text, onclick, style, value
    <link>: href
    <mip-img>: src
    <ms-img>: src
    <object>: codebase, data
    <source>: data-lazy-srcset, src, srcset
    <video>: poster, src
    :param html_str:
    :return:
    """
    # Useless tags. We focus on the media-related tags.
    noise_tag_set = {'a', 'abbr', 'acronym', 'address', 'apan', 'aside',
                     'b', 'base', 'bdo', 'big', 'blink', 'blockquote', 'br', 'btn',
                     'canvas', 'center', 'circle', 'cite', 'code', 'cufon',
                     'dd', 'del', 'delect', 'desc', 'dfn', 'dl', 'dt', 'duv',
                     'e', 'em', 'embed', 'figure', 'font', 'fontcolor', 'footer', 'form', 'g', 'gm',
                     'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr',
                     'i', 'icon', 'image', 'ins', 'kbd', 'label', 'legend', 'li', 'line', 'lineargradient', 'listing', 'lor',
                     'mark', 'marquee', 'mask', 'menu', 'menuitem', 'meta', 'meter', 'mip-i-space',
                     'nav', 'nobr', 'noframes', 'noscript', 'ol', 'optgroup', 'option', 'output',
                     'p', 'pan', 'param', 'path', 'picture', 'polygon', 'polyline', 'pre', 'progress', 'q', 'rect', 'rp', 'rt', 'ruby',
                     's', 'samp', 'script', 'section', 'select', 'small', 'span', 'spanv',
                     'stop', 'strike', 'strong', 'style', 'sub', 'sup', 'svg',
                     'table', 'td', 'text', 'td', 'th', 'time', 'title', 'tr', 'track', 'tspan', 'tt',
                     'u', 'use', 'ul', 'var', 'wbr', 'xmp'}

    temp_tag_set = {'map', 'area', 'iframe', 'object'}

    useful_tag_set = {'button', 'div', 'f', 'img', 'input', 'link', 'mip-img', 'ms-img', 'object', 'source', 'video'}

    tag_html = etree.HTML(html_str)
    a_tag_html = tag_html.xpath('//a')[0]
    for sub_tag in a_tag_html.iter():
        # # Filter the comments.
        # if not isinstance(sub_tag.tag, str):
        #     continue
        # # Filter the empty tags.
        # if not sub_tag.attrib:
        #     continue
        # if sub_tag.tag in noise_tag_set or sub_tag.tag in useful_tag_set:
        #     continue
        # if sub_tag.tag in temp_tag_set:
        #     continue
        if sub_tag.tag != 'object':
            continue
        has_path = False
        for key in sub_tag.attrib:
            if '/' in sub_tag.attrib[key]:
                has_path = True
                break
        if has_path:
            print(sub_tag.tag, sub_tag.attrib, '\t', path)


def agg_area_visual_info():
    area_visual_info_list = []
    with open('./data/total_malicious.txt', 'r') as fr:
        for i, line in enumerate(fr):
            line = line.rstrip('\n').split('\t')
            sample, source, end_url = line[0], line[2], line[3]
            sample_dir = get_sample_dir_iie(sample, source)
            frame_tree = build_frame_tree(end_url, sample_dir)
            for frame_node in frame_tree.parse_frame_tree():
                area_list = get_redirection_tags(frame_node.frame_dir)[1]
                if len(area_list) == 0:
                    continue
                for area_item in area_list:
                    area_rect = extract_rect(area_item[0])[0]
                    print(frame_node.frame_dir, sample, source, frame_node.frame_src, frame_node.frame_level, str(area_rect))
                    item_info = [sample, source, frame_node.frame_src, frame_node.frame_level, str(area_rect)]
                    item_info = '\t'.join(item_info)
                    area_visual_info_list += [item_info]
    save_file_path = './data/sample_visual_info/area_visual_info.txt'
    with open(save_file_path, 'w', encoding='utf-8') as fw:
        cache_str = '\n'.join(area_visual_info_list) + '\n'
        fw.write(cache_str)


def parse_style_attribute(style_str: str) -> str:
    """
    Given the value of style attribute, parse the string and return the target info.
    :param style_str:
    :return:
    """
    def get_url(base_str: str, start: int):
        # Match the '(' and ')'.
        stack = []
        # Find the '('.
        left_index = start
        while left_index < len(base_str):
            if base_str[left_index] == '(':
                stack += ['(']
                left_index += 1
                break
            left_index += 1
        # Find the ')'.
        right_index = left_index + 1
        for i in range(left_index, len(base_str)):
            if base_str[i] == '(':
                stack += ['(']
            if base_str[i] == ')' and stack[-1] == '(':
                stack.pop()
            if not stack:
                right_index = i
                break
        # Ignore both the '(' and ')'.
        sub_str = style_str[left_index: right_index]
        # Ignore the redundant symbols.
        sub_str = sub_str.strip('"')
        sub_str = sub_str.strip("'")
        sub_str = sub_str.strip(' ')
        return sub_str

    url_str = ''
    start_index = style_str.find('background-image')
    if start_index != -1:
        start_index += len('background-image')
        url_str = get_url(style_str, start_index)
    else:
        start_index = style_str.find('background')
        if start_index != -1:
            start_index += len('background')
            url_str = get_url(style_str, start_index)
    return url_str


def agg_a_visual_info():
    """
    Two purposes:
        1. The source of the visual elements;
        2. The implicit destination of the <a>.
    The implicit destination means that the actual destination after clicking is different with the 'href' attribute of <a>.
    This phenomenon is usually conducted through adding some 'href'-related attributes into the inner sub-tags of <a>.
    For example, assigning the 'onclick', 'href', or 'data-ioslink' of the inner <div> of <a>.
    After our measurements, we found that the following visual-related tags may introduce the 'src' or 'href' attributes.
    ------------------------------------------------------------------------------
    <button>: data-clipboard-text, href, onclick
    <div>: data-androidlink, data-ioslink, data-lazy-background, data-original, data-src, href, onclick, src, style
    <f>: href
    <img>: data-original, data-src, data-url, lay-src, lazy-src, original, originalsrc, _src, src, srcset, style
    <input>: data-clipboard-text, onclick, style, value
    <link>: href
    <mip-img>: src
    <ms-img>: src
    <object>: codebase, data
    <source>: data-lazy-srcset, src, srcset
    <video>: poster, src
    ------------------------------------------------------------------------------
    :return:
    """
    useful_tags = {'button', 'div', 'f', 'img', 'input', 'link', 'mip-img', 'ms-img', 'object', 'source', 'video'}
    a_visual_src_info_list = []
    a_visual_dst_info_list = []
    with open('./data/total_malicious.txt', 'r') as fr:
        for i, line in enumerate(fr):
            if (i+1) % 1000 == 0:
                print("%d samples have been processed." % (i+1))
            line = line.rstrip('\n').split('\t')
            sample, source, end_url = line[0], line[2], line[3]
            sample_dir = get_sample_dir_iie(sample, source)
            frame_tree = build_frame_tree(end_url, sample_dir)
            for frame_node in frame_tree.parse_frame_tree():
                a_list = get_redirection_tags(frame_node.frame_dir)[0]
                for a_item in a_list:
                    a_rect = extract_rect(a_item[0])[0]
                    tag_html = etree.HTML(a_item[1])
                    a_tag_html = tag_html.xpath('//a')[0]
                    for sub_tag in a_tag_html.iter():
                        src_related_list = []
                        dst_related_list = []
                        # Filter the noise tags.
                        if not sub_tag.attrib or sub_tag.tag not in useful_tags:
                            continue
                        # Extract the 'src'-related attribute of the inner visual tags.
                        if sub_tag.tag == 'button':
                            if 'data-clipboard-text' in sub_tag.attrib and ('/' in sub_tag.attrib['data-clipboard-text'] or '%2f' in sub_tag.attrib['data-clipboard-text'] or '%2F' in sub_tag.attrib['data-clipboard-text']):
                                dst_related_list += [(sub_tag.tag, 'data-clipboard-text', sub_tag.attrib['data-clipboard-text'])]
                            if 'href' in sub_tag.attrib and ('/' in sub_tag.attrib['href'] or '%2f' in sub_tag.attrib['href'] or '%2F' in sub_tag.attrib['href']):
                                dst_related_list += [(sub_tag.tag, 'href', sub_tag.attrib['href'])]
                            if 'onclick' in sub_tag.attrib and ('/' in sub_tag.attrib['onclick'] or '%2f' in sub_tag.attrib['onclick'] or '%2F' in sub_tag.attrib['onclick']):
                                dst_related_list += [(sub_tag.tag, 'onclick', sub_tag.attrib['onclick'])]
                        elif sub_tag.tag == 'div':
                            if 'data-androidlink' in sub_tag.attrib and ('/' in sub_tag.attrib['data-androidlink'] or '%2f' in sub_tag.attrib['data-androidlink'] or '%2F' in sub_tag.attrib['data-androidlink']):
                                dst_related_list += [(sub_tag.tag, 'data-androidlink', sub_tag.attrib['data-androidlink'])]
                            if 'data-ioslink' in sub_tag.attrib and ('/' in sub_tag.attrib['data-ioslink'] or '%2f' in sub_tag.attrib['data-ioslink'] or '%2F' in sub_tag.attrib['data-ioslink']):
                                dst_related_list += [(sub_tag.tag, 'data-ioslink', sub_tag.attrib['data-ioslink'])]
                            if 'href' in sub_tag.attrib and ('/' in sub_tag.attrib['href'] or '%2f' in sub_tag.attrib['href'] or '%2F' in sub_tag.attrib['href']):
                                dst_related_list += [(sub_tag.tag, 'href', sub_tag.attrib['href'])]
                            if 'onclick' in sub_tag.attrib and ('/' in sub_tag.attrib['onclick'] or '%2f' in sub_tag.attrib['onclick'] or '%2F' in sub_tag.attrib['onclick']):
                                dst_related_list += [(sub_tag.tag, 'onclick', sub_tag.attrib['onclick'])]
                            if 'data-lazy-background' in sub_tag.attrib and ('/' in sub_tag.attrib['data-lazy-background'] or '%2f' in sub_tag.attrib['data-lazy-background'] or '%2F' in sub_tag.attrib['data-lazy-background']):
                                src_related_list += [(sub_tag.tag, 'data-lazy-background', sub_tag.attrib['data-lazy-background'])]
                            if 'data-original' in sub_tag.attrib and ('/' in sub_tag.attrib['data-original'] or '%2f' in sub_tag.attrib['data-original'] or '%2F' in sub_tag.attrib['data-original']):
                                src_related_list += [(sub_tag.tag, 'data-original', sub_tag.attrib['data-original'])]
                            if 'style' in sub_tag.attrib and ('/' in sub_tag.attrib['style'] or '%2f' in sub_tag.attrib['style'] or '%2F' in sub_tag.attrib['style']):
                                # Extract the URL in 'style' attribute.
                                style_url = parse_style_attribute(sub_tag.attrib['style'])
                                if len(style_url) > 0:
                                    src_related_list += [(sub_tag.tag, 'style', style_url)]
                        elif sub_tag.tag == 'f':
                            if 'href' in sub_tag.attrib and ('/' in sub_tag.attrib['href'] or '%2f' in sub_tag.attrib['href'] or '%2F' in sub_tag.attrib['href']):
                                dst_related_list += [(sub_tag.tag, 'href', sub_tag.attrib['href'])]
                        elif sub_tag.tag == 'img':
                            if 'data-original' in sub_tag.attrib and ('/' in sub_tag.attrib['data-original'] or '%2f' in sub_tag.attrib['data-original'] or '%2F' in sub_tag.attrib['data-original']):
                                src_related_list += [(sub_tag.tag, 'data-original', sub_tag.attrib['data-original'])]
                            if 'data-src' in sub_tag.attrib and ('/' in sub_tag.attrib['data-src'] or '%2f' in sub_tag.attrib['data-src'] or '%2F' in sub_tag.attrib['data-src']):
                                src_related_list += [(sub_tag.tag, 'data-src', sub_tag.attrib['data-src'])]
                            if 'data-url' in sub_tag.attrib and ('/' in sub_tag.attrib['data-url'] or '%2f' in sub_tag.attrib['data-url'] or '%2F' in sub_tag.attrib['data-url']):
                                src_related_list += [(sub_tag.tag, 'data-url', sub_tag.attrib['data-url'])]
                            if 'lay-src' in sub_tag.attrib and ('/' in sub_tag.attrib['lay-src'] or '%2f' in sub_tag.attrib['lay-src'] or '%2F' in sub_tag.attrib['lay-src']):
                                src_related_list += [(sub_tag.tag, 'lay-src', sub_tag.attrib['lay-src'])]
                            if 'lazy-sr' in sub_tag.attrib and ('/' in sub_tag.attrib['lazy-sr'] or '%2f' in sub_tag.attrib['lazy-sr'] or '%2F' in sub_tag.attrib['lazy-sr']):
                                src_related_list += [(sub_tag.tag, 'lazy-sr', sub_tag.attrib['lazy-sr'])]
                            if 'original' in sub_tag.attrib and ('/' in sub_tag.attrib['original'] or '%2f' in sub_tag.attrib['original'] or '%2F' in sub_tag.attrib['original']):
                                src_related_list += [(sub_tag.tag, 'original', sub_tag.attrib['original'])]
                            if 'originalsrc' in sub_tag.attrib and ('/' in sub_tag.attrib['originalsrc'] or '%2f' in sub_tag.attrib['originalsrc'] or '%2F' in sub_tag.attrib['originalsrc']):
                                src_related_list += [(sub_tag.tag, 'originalsrc', sub_tag.attrib['originalsrc'])]
                            if '_src' in sub_tag.attrib and ('/' in sub_tag.attrib['_src'] or '%2f' in sub_tag.attrib['_src'] or '%2F' in sub_tag.attrib['_src']):
                                src_related_list += [(sub_tag.tag, '_src', sub_tag.attrib['_src'])]
                            if 'src' in sub_tag.attrib and ('/' in sub_tag.attrib['src'] or '%2f' in sub_tag.attrib['src'] or '%2F' in sub_tag.attrib['src']):
                                src_related_list += [(sub_tag.tag, 'src', sub_tag.attrib['src'])]
                            if 'srcset' in sub_tag.attrib and ('/' in sub_tag.attrib['srcset'] or '%2f' in sub_tag.attrib['srcset'] or '%2F' in sub_tag.attrib['srcset']):
                                src_related_list += [(sub_tag.tag, 'srcset', sub_tag.attrib['srcset'])]
                            if 'style' in sub_tag.attrib and ('/' in sub_tag.attrib['style'] or '%2f' in sub_tag.attrib['style'] or '%2F' in sub_tag.attrib['style']):
                                # Extract the URL in 'style' attribute.
                                style_url = parse_style_attribute(sub_tag.attrib['style'])
                                if len(style_url) > 0:
                                    src_related_list += [(sub_tag.tag, 'style', style_url)]
                        elif sub_tag.tag == 'input':
                            if 'data-clipboard-text' in sub_tag.attrib and ('/' in sub_tag.attrib['data-clipboard-text'] or '%2f' in sub_tag.attrib['data-clipboard-text'] or '%2F' in sub_tag.attrib['data-clipboard-text']):
                                dst_related_list += [(sub_tag.tag, 'data-clipboard-text', sub_tag.attrib['data-clipboard-text'])]
                            if 'onclick' in sub_tag.attrib and ('/' in sub_tag.attrib['onclick'] or '%2f' in sub_tag.attrib['onclick'] or '%2F' in sub_tag.attrib['onclick']):
                                dst_related_list += [(sub_tag.tag, 'onclick', sub_tag.attrib['onclick'])]
                            if 'value' in sub_tag.attrib and ('/' in sub_tag.attrib['value'] or '%2f' in sub_tag.attrib['value'] or '%2F' in sub_tag.attrib['value']):
                                dst_related_list += [(sub_tag.tag, 'value', sub_tag.attrib['value'])]
                            if 'style' in sub_tag.attrib and ('/' in sub_tag.attrib['style'] or '%2f' in sub_tag.attrib['style'] or '%2F' in sub_tag.attrib['style']):
                                # Extract the URL in 'style' attribute.
                                style_url = parse_style_attribute(sub_tag.attrib['style'])
                                if len(style_url) > 0:
                                    src_related_list += [(sub_tag.tag, 'style', style_url)]
                        elif sub_tag.tag == 'link':
                            if 'href' in sub_tag.attrib and ('/' in sub_tag.attrib['href'] or '%2f' in sub_tag.attrib['href'] or '%2F' in sub_tag.attrib['href']):
                                dst_related_list += [(sub_tag.tag, 'href', sub_tag.attrib['href'])]
                        elif sub_tag.tag == 'mip-img':
                            if 'src' in sub_tag.attrib and ('/' in sub_tag.attrib['src'] or '%2f' in sub_tag.attrib['src'] or '%2F' in sub_tag.attrib['src']):
                                src_related_list += [(sub_tag.tag, 'src', sub_tag.attrib['src'])]
                        elif sub_tag.tag == 'ms-img':
                            if 'src' in sub_tag.attrib and ('/' in sub_tag.attrib['src'] or '%2f' in sub_tag.attrib['src'] or '%2F' in sub_tag.attrib['src']):
                                src_related_list += [(sub_tag.tag, 'src', sub_tag.attrib['src'])]
                        elif sub_tag.tag == 'object':
                            if 'codebase' in sub_tag.attrib and ('/' in sub_tag.attrib['codebase'] or '%2f' in sub_tag.attrib['codebase'] or '%2F' in sub_tag.attrib['codebase']):
                                src_related_list += [(sub_tag.tag, 'codebase', sub_tag.attrib['codebase'])]
                            if 'data' in sub_tag.attrib and ('/' in sub_tag.attrib['data'] or '%2f' in sub_tag.attrib['data'] or '%2F' in sub_tag.attrib['data']):
                                dst_related_list += [(sub_tag.tag, 'data', sub_tag.attrib['data'])]
                        elif sub_tag.tag == 'source':
                            if 'data-lazy-srcset' in sub_tag.attrib and ('/' in sub_tag.attrib['data-lazy-srcset'] or '%2f' in sub_tag.attrib['data-lazy-srcset'] or '%2F' in sub_tag.attrib['data-lazy-srcset']):
                                src_related_list += [(sub_tag.tag, 'data-lazy-srcset', sub_tag.attrib['data-lazy-srcset'])]
                            if 'src' in sub_tag.attrib and ('/' in sub_tag.attrib['src'] or '%2f' in sub_tag.attrib['src'] or '%2F' in sub_tag.attrib['src']):
                                src_related_list += [(sub_tag.tag, 'src', sub_tag.attrib['src'])]
                            if 'srcset' in sub_tag.attrib and ('/' in sub_tag.attrib['srcset'] or '%2f' in sub_tag.attrib['srcset'] or '%2F' in sub_tag.attrib['srcset']):
                                src_related_list += [(sub_tag.tag, 'srcset', sub_tag.attrib['srcset'])]
                        elif sub_tag.tag == 'video':
                            if 'poster' in sub_tag.attrib and ('/' in sub_tag.attrib['poster'] or '%2f' in sub_tag.attrib['poster'] or '%2F' in sub_tag.attrib['poster']):
                                src_related_list += [(sub_tag.tag, 'poster', sub_tag.attrib['poster'])]
                            if 'src' in sub_tag.attrib and ('/' in sub_tag.attrib['src'] or '%2f' in sub_tag.attrib['src'] or '%2F' in sub_tag.attrib['src']):
                                src_related_list += [(sub_tag.tag, 'src', sub_tag.attrib['src'])]

                        # Record the visual info.
                        for src_item in src_related_list:
                            src_temp_item = [sample, source, frame_node.frame_src, frame_node.frame_level, str(a_rect), src_item[0], src_item[1], src_item[2]]
                            src_temp_item = '\t'.join(src_temp_item)
                            a_visual_src_info_list += [src_temp_item]
                        for dst_item in dst_related_list:
                            dst_temp_item = [sample, source, frame_node.frame_src, frame_node.frame_level, str(a_rect), dst_item[0], dst_item[1], dst_item[2]]
                            dst_temp_item = '\t'.join(dst_temp_item)
                            a_visual_dst_info_list += [dst_temp_item]
    # Save the collected info.
    src_info_file = './data/sample_visual_info/a_visual_src_info.txt'
    with open(src_info_file, 'w', encoding='utf-8') as fw:
        src_info_str = '\n'.join(a_visual_src_info_list) + '\n'
        fw.write(src_info_str)
    dst_info_file = './data/sample_visual_info/a_visual_dst_info.txt'
    with open(dst_info_file, 'w', encoding='utf-8') as fw:
        dst_info_str = '\n'.join(a_visual_dst_info_list) + '\n'
        fw.write(dst_info_str)


def analyze_onclick_visual_tags():
    """
    If the 'onclick' corresponds to something visual tags (like <img>), what is the 'src'-related attribute of such visual tags?
    Traverse all the the 'onclick' tags and get the visual element it depends on.
    --------------------------------------------------------------------------------
    button: style
    div: data-clipboard-text, data-echo, data-original, data-url, style
    img: data-default-img, data-img-url, data-src, data-original, data-orig, data-webp-img, original, originalsrc, ng-src, src, style, tppabs
    input: data-url, src, style
    ms-img: ms-attr
    object: data
    source: srcset
    --------------------------------------------------------------------------------
    :return:
    """
    onclick_visual_src_info_list = []
    useful_tag_list = ['button', 'div', 'img', 'input', 'ms-img', 'object', 'source']
    with open('./data/total_malicious.txt', 'r') as fr:
        for i, line in enumerate(fr):
            if i % 1000 == 0:
                print('%d has been processed.' % i)
            line = line.rstrip('\n').split('\t')
            sample, source, end_url = line[0], line[2], line[3]
            sample_dir = get_sample_dir_iie(sample, source)
            frame_tree = build_frame_tree(end_url, sample_dir)
            for frame_node in frame_tree.parse_frame_tree():
                onclick_list = get_redirection_tags(frame_node.frame_dir)[2]
                if len(onclick_list) == 0:
                    continue
                for onclick_item in onclick_list:
                    onclick_rect = extract_rect(onclick_item[0])[0]
                    tag_html = etree.HTML(onclick_item[1])
                    onclick_tag_html = tag_html.xpath('//*[@onclick]')[0]
                    for sub_tag in onclick_tag_html.iter():
                        src_related_list = []
                        if not isinstance(sub_tag.tag, str) or sub_tag.tag not in useful_tag_list or not sub_tag.attrib:
                            continue

                        if sub_tag.tag == 'button':
                            if 'style' in sub_tag.attrib and ('/' in sub_tag.attrib['style'] or '%2f' in sub_tag.attrib['style'] or '%2F' in sub_tag.attrib['style']):
                                style_url = parse_style_attribute(sub_tag.attrib['style'])
                                if len(style_url) > 0:
                                    src_related_list += [(sub_tag.tag, 'style', style_url)]
                        elif sub_tag.tag == 'div':
                            if 'data-clipboard-text' in sub_tag.attrib and ('/' in sub_tag.attrib['data-clipboard-text'] or '%2f' in sub_tag.attrib['data-clipboard-text'] or '%2F' in sub_tag.attrib['data-clipboard-text']):
                                src_related_list += [(sub_tag.tag, 'data-clipboard-text', sub_tag.attrib['data-clipboard-text'])]
                            if 'data-echo' in sub_tag.attrib and ('/' in sub_tag.attrib['data-echo'] or '%2f' in sub_tag.attrib['data-echo'] or '%2F' in sub_tag.attrib['data-echo']):
                                src_related_list += [(sub_tag.tag, 'data-echo', sub_tag.attrib['data-echo'])]
                            if 'data-original' in sub_tag.attrib and ('/' in sub_tag.attrib['data-original'] or '%2f' in sub_tag.attrib['data-original'] or '%2F' in sub_tag.attrib['data-original']):
                                src_related_list += [(sub_tag.tag, 'data-original', sub_tag.attrib['data-original'])]
                            if 'data-url' in sub_tag.attrib and ('/' in sub_tag.attrib['data-url'] or '%2f' in sub_tag.attrib['data-url'] or '%2F' in sub_tag.attrib['data-url']):
                                src_related_list += [(sub_tag.tag, 'data-url', sub_tag.attrib['data-url'])]
                            if 'style' in sub_tag.attrib and ('/' in sub_tag.attrib['style'] or '%2f' in sub_tag.attrib['style'] or '%2F' in sub_tag.attrib['style']):
                                style_url = parse_style_attribute(sub_tag.attrib['style'])
                                if len(style_url) > 0:
                                    src_related_list += [(sub_tag.tag, 'style', style_url)]
                        elif sub_tag.tag == 'img':
                            if 'data-default-img' in sub_tag.attrib and ('/' in sub_tag.attrib['data-default-img'] or '%2f' in sub_tag.attrib['data-default-img'] or '%2F' in sub_tag.attrib['data-default-img']):
                                src_related_list += [(sub_tag.tag, 'data-default-img', sub_tag.attrib['data-default-img'])]
                            if 'data-img-url' in sub_tag.attrib and ('/' in sub_tag.attrib['data-img-url'] or '%2f' in sub_tag.attrib['data-img-url'] or '%2F' in sub_tag.attrib['data-img-url']):
                                src_related_list += [(sub_tag.tag, 'data-img-url', sub_tag.attrib['data-img-url'])]
                            if 'data-src' in sub_tag.attrib and ('/' in sub_tag.attrib['data-src'] or '%2f' in sub_tag.attrib['data-src'] or '%2F' in sub_tag.attrib['data-src']):
                                src_related_list += [(sub_tag.tag, 'data-src', sub_tag.attrib['data-src'])]
                            if 'data-original' in sub_tag.attrib and ('/' in sub_tag.attrib['data-original'] or '%2f' in sub_tag.attrib['data-original'] or '%2F' in sub_tag.attrib['data-original']):
                                src_related_list += [(sub_tag.tag, 'data-original', sub_tag.attrib['data-original'])]
                            if 'data-orig' in sub_tag.attrib and ('/' in sub_tag.attrib['data-orig'] or '%2f' in sub_tag.attrib['data-orig'] or '%2F' in sub_tag.attrib['data-orig']):
                                src_related_list += [(sub_tag.tag, 'data-orig', sub_tag.attrib['data-orig'])]
                            if 'data-webp-img' in sub_tag.attrib and ('/' in sub_tag.attrib['data-webp-img'] or '%2f' in sub_tag.attrib['data-webp-img'] or '%2F' in sub_tag.attrib['data-webp-img']):
                                src_related_list += [(sub_tag.tag, 'data-webp-img', sub_tag.attrib['data-webp-img'])]
                            if 'original' in sub_tag.attrib and ('/' in sub_tag.attrib['original'] or '%2f' in sub_tag.attrib['original'] or '%2F' in sub_tag.attrib['original']):
                                src_related_list += [(sub_tag.tag, 'original', sub_tag.attrib['original'])]
                            if 'originalsrc' in sub_tag.attrib and ('/' in sub_tag.attrib['originalsrc'] or '%2f' in sub_tag.attrib['originalsrc'] or '%2F' in sub_tag.attrib['originalsrc']):
                                src_related_list += [(sub_tag.tag, 'originalsrc', sub_tag.attrib['originalsrc'])]
                            if 'ng-src' in sub_tag.attrib and ('/' in sub_tag.attrib['ng-src'] or '%2f' in sub_tag.attrib['ng-src'] or '%2F' in sub_tag.attrib['ng-src']):
                                src_related_list += [(sub_tag.tag, 'ng-src', sub_tag.attrib['ng-src'])]
                            if 'src' in sub_tag.attrib and ('/' in sub_tag.attrib['src'] or '%2f' in sub_tag.attrib['src'] or '%2F' in sub_tag.attrib['src']):
                                src_related_list += [(sub_tag.tag, 'src', sub_tag.attrib['src'])]
                            if 'tppabs' in sub_tag.attrib and ('/' in sub_tag.attrib['tppabs'] or '%2f' in sub_tag.attrib['tppabs'] or '%2F' in sub_tag.attrib['tppabs']):
                                src_related_list += [(sub_tag.tag, 'tppabs', sub_tag.attrib['tppabs'])]
                            if 'style' in sub_tag.attrib and ('/' in sub_tag.attrib['style'] or '%2f' in sub_tag.attrib['style'] or '%2F' in sub_tag.attrib['style']):
                                style_url = parse_style_attribute(sub_tag.attrib['style'])
                                if len(style_url) > 0:
                                    src_related_list += [(sub_tag.tag, 'style', style_url)]
                        elif sub_tag.tag == 'input':
                            if 'data-url' in sub_tag.attrib and ('/' in sub_tag.attrib['data-url'] or '%2f' in sub_tag.attrib['data-url'] or '%2F' in sub_tag.attrib['data-url']):
                                src_related_list += [(sub_tag.tag, 'data-url', sub_tag.attrib['data-url'])]
                            if 'src' in sub_tag.attrib and ('/' in sub_tag.attrib['src'] or '%2f' in sub_tag.attrib['src'] or '%2F' in sub_tag.attrib['src']):
                                src_related_list += [(sub_tag.tag, 'src', sub_tag.attrib['src'])]
                            if 'style' in sub_tag.attrib and ('/' in sub_tag.attrib['style'] or '%2f' in sub_tag.attrib['style'] or '%2F' in sub_tag.attrib['style']):
                                style_url = parse_style_attribute(sub_tag.attrib['style'])
                                if len(style_url) > 0:
                                    src_related_list += [(sub_tag.tag, 'style', style_url)]
                        elif sub_tag.tag == 'ms-img':
                            if 'ms-attr' in sub_tag.attrib and ('/' in sub_tag.attrib['ms-attr'] or '%2f' in sub_tag.attrib['ms-attr'] or '%2F' in sub_tag.attrib['ms-attr']):
                                src_related_list += [(sub_tag.tag, 'ms-attr', sub_tag.attrib['ms-attr'])]
                        elif sub_tag.tag == 'object':
                            if 'data' in sub_tag.attrib and ('/' in sub_tag.attrib['data'] or '%2f' in sub_tag.attrib['data'] or '%2F' in sub_tag.attrib['data']):
                                src_related_list += [(sub_tag.tag, 'data', sub_tag.attrib['data'])]
                        elif sub_tag.tag == 'source':
                            if 'srcset' in sub_tag.attrib and ('/' in sub_tag.attrib['srcset'] or '%2f' in sub_tag.attrib['srcset'] or '%2F' in sub_tag.attrib['srcset']):
                                src_related_list += [(sub_tag.tag, 'srcset', sub_tag.attrib['srcset'])]
                        # Record the visual info.
                        for src_item in src_related_list:
                            src_temp_item = [sample, source, frame_node.frame_src, frame_node.frame_level, str(onclick_rect), src_item[0], src_item[1], src_item[2]]
                            src_temp_item = '\t'.join(src_temp_item)
                            onclick_visual_src_info_list += [src_temp_item]
    # Save the extracted info.
    onclick_src_info_file = './data/sample_visual_info/onclick_visual_src_info.txt'
    with open(onclick_src_info_file, 'w', encoding='utf-8') as fw:
        onclick_src_info_str = '\n'.join(onclick_visual_src_info_list)
        fw.write(onclick_src_info_str)


def agg_onclick_owner_tags():
    """
    Two main goals:
        1. Which kind of tags usually employ such 'onclick' attribute?
            - Done.
        3. What is the destination of the 'onclick'?
    :return:
    """
    onclick_owner_tag_info_list = []        # Record the tag that employ 'onclick'.
    with open('./data/total_malicious.txt', 'r') as fr:
        for i, line in enumerate(fr):
            line = line.rstrip('\n').split('\t')
            sample, source, end_url = line[0], line[2], line[3]
            sample_dir = get_sample_dir_iie(sample, source)
            frame_tree = build_frame_tree(end_url, sample_dir)
            for frame_node in frame_tree.parse_frame_tree():
                onclick_list = get_redirection_tags(frame_node.frame_dir)[2]
                if len(onclick_list) == 0:
                    continue
                for onclick_item in onclick_list:
                    onclick_rect = extract_rect(onclick_item[0])[0]
                    tag_html = etree.HTML(onclick_item[1])
                    onclick_tag_html = tag_html.xpath('//*[@onclick]')[0]
                    # The first tag is the tag that employ 'onclick' attribute, while other tags are its inner sub tags.
                    owner_tag = list(onclick_tag_html.iter())[0]
                    temp_item = [sample, source, frame_node.frame_src, frame_node.frame_level, str(onclick_rect), owner_tag.tag, owner_tag.attrib['onclick']]
                    temp_item = '\t'.join(temp_item)
                    onclick_owner_tag_info_list += [temp_item]
    onclick_owner_info_file = './data/sample_visual_info/onclick_owner_tag_info.txt'
    with open(onclick_owner_info_file, 'w', encoding='utf-8') as fw:
        owner_info_str = '\n'.join(onclick_owner_tag_info_list) + '\n'
        fw.write(owner_info_str)


def extract_onclick_urls(onclick_html) -> list:
    """
    If there are plain URLs in the 'onclick' JS code, we extract them.
    Otherwise, we deem them all as function call.
    :param onclick_html: HTMl code of the 'onclick' attribute.
    :return: URL list
    """
    if len(onclick_html) == 0:
        return []
    # Extract the plain URl in the 'onclick' attribute. The JS code may contain more than one quotation-pair.
    url_list = []
    left = 0
    while left < len(onclick_html):
        while left < len(onclick_html) and onclick_html[left] not in ('"', "'"):
            left += 1
        if left >= len(onclick_html):
            break
        quotation = onclick_html[left]
        right = left + 1
        while right < len(onclick_html) and onclick_html[right] != quotation:
            right += 1
        temp_url = onclick_html[left+1: right]
        if '/' in temp_url or '%2f' in temp_url or '%2F' in temp_url:
            url_list += [temp_url]
        left = right + 1
    return url_list

if __name__ == '__main__':
    extract_onclick_url()
