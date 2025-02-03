import streamlit as st
import time
import graphviz

# Set the app title
st.title("Standalone Segmentation Tool")

# Create a form for the drop down menus
with st.form("selection_form"):
    st.header("Select Segmentation Filters")
    engine_names = st.multiselect("Engine Name Desc", ["X1", "B6.7", "L9"])
    build_year = st.multiselect("Build Year", ["2021", "2022", "2023", "2024"])
    applications = st.multiselect("Application", ["AUTO", "RV", "SCHOOL BUS", "FIRE TRUCK"])
    fail_codes = st.multiselect("Fail Code", ["AA", "BB", "CC", "DD"])
    segmentation_level = st.selectbox("Number of Segmentation Level", list(range(1, 11)))
    
    # Use a submit button to save selections
    submit_form = st.form_submit_button("Save Selections")

# Store the selections in session_state (if submitted)
if submit_form:
    st.success("Selections saved!")
    st.session_state.selections = {
         "engine_names": engine_names,
         "build_year": build_year,
         "applications": applications,
         "fail_codes": fail_codes,
         "segmentation_level": segmentation_level,
    }
    st.write("Your selections:")
    st.write(st.session_state.selections)

# Button to simulate data collection
if st.button("Collect Segmentation Data"):
    # Use the selections from session_state or defaults if not saved
    selections = st.session_state.get("selections", {
         "engine_names": [],
         "build_year": [],
         "applications": [],
         "fail_codes": [],
         "segmentation_level": 1
    })
    st.write("Collecting data with the following selections:")
    st.write(selections)
    st.info("Collecting data...")
    time.sleep(3)
    # After waiting, display a dummy hyperlink
    st.markdown("[Dummy Data Link](http://example.com/dummy-data)")

# Button to simulate segmentation analysis
if st.button("Perform Segmentation Analysis"):
    # Retrieve the segmentation level from saved selections (default is 1)
    seg_level = st.session_state.get("selections", {}).get("segmentation_level", 1)
    st.write(f"Performing segmentation analysis for tree depth: {seg_level}")
    st.info("Performing analysis...")
    time.sleep(3)
    
    # Build a dummy hierarchical (binary) tree chart using Graphviz.
    # Each node will have two splits until the requested level is reached.
    graph = graphviz.Digraph()
    graph.node("0", "Root")
    
    def build_tree(parent, current_level, max_level, counter):
        # Stop adding children if we've reached the maximum level.
        if current_level == max_level:
            return
        # Create left child
        counter[0] += 1
        left = str(counter[0])
        graph.node(left, f"Level {current_level + 1} L")
        graph.edge(parent, left)
        build_tree(left, current_level + 1, max_level, counter)
        
        # Create right child
        counter[0] += 1
        right = str(counter[0])
        graph.node(right, f"Level {current_level + 1} R")
        graph.edge(parent, right)
        build_tree(right, current_level + 1, max_level, counter)
    
    counter = [0]  # Using a list to act as a mutable counter.
    build_tree("0", 1, seg_level, counter)
    
    st.graphviz_chart(graph)
