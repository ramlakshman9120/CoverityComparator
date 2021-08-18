import streamlit as st
import numpy as np
import re as re

def read_cids_from_preview_report(preview_report_file):
    cid_list = []
    bytes_data = preview_report_file.readlines()
    substring = "\"cid\" :"
    
    for eachline in bytes_data:
        if substring in (str(eachline)):
            res = re.sub("\D", "", str(eachline))
            cid_list.append(res)

    return cid_list

def display_comparator_reports(cid_list_old,cid_list_new):

    list_of_fixed_cids = np.setdiff1d(cid_list_old, cid_list_new)

    list_of_cids_newly_introduced = np.setdiff1d(cid_list_new,cid_list_old)

    data_load_state.text('CovComparator Reports below!!')

    st.subheader('{0} CIDs fixed due to your changes:'.format(len(list_of_fixed_cids)))
    for eachCID in list_of_fixed_cids:
        st.write(eachCID)

    st.subheader('{0} CIDs newly introduced due to your changes:'.format(len(list_of_cids_newly_introduced)))
    for eachCID in list_of_cids_newly_introduced:
        st.write(eachCID)

    return
    

st.title('COVERITY-COMPARATOR BY SRIRAM')

st.markdown("""
This Application compares two Coverity reports and generates:

1. LISTS ALL THE CIDs FIXED.
2. LISTS ALL CIDs NEWLY INTRODUCED.
""")

st.sidebar.header('Welcome!!!')

old_preview_report_file = st.sidebar.file_uploader('Upload old coverity report')
#st.sidebar.write(old_preview_report_file)
new_preview_report_file = st.sidebar.file_uploader('Upload new coverity report')
#st.sidebar.write(new_preview_report_file)

if st.sidebar.button('Compare Coverity Reports'):
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Comparing the coverity reports...')
    # Read all CIDs from old preview report file.
    list_of_old_cids=read_cids_from_preview_report(old_preview_report_file)
    # Read all CIDs from new preview report file.
    list_of_new_cids=read_cids_from_preview_report(new_preview_report_file)

    display_comparator_reports(list_of_old_cids,list_of_new_cids)
