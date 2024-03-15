import streamlit as st
import example_utils
from vapor import session, renderer, dataset, camera

print("Supported dataset types:", dataset.Dataset.GetDatasetTypes())

ses = session.Session()
data = example_utils.OpenExampleDataset(ses)

print("Time Coordinate Variable Name:", data.GetTimeCoordVarName())
print("Coordinate Variable Names:", data.GetCoordVarNames())

print("Dimensions:")
for dim in data.GetDimensionNames():
    print(f"  {dim}:", data.GetDimensionLength(dim, 0))

print("Data Variables:")
for var in data.GetDataVarNames():
    print(f"  {var}")
    print(f"    Time Varying:", bool(data.IsTimeVarying(var)))
    print(f"    Dimensionality:", data.GetVarGeometryDim(var))
    print(f"    Coordinates:", data.GetVarCoordVars(var, True))
    print("     Data Range:", data.GetDataRange(var))
with st.sidebar:
    slider1= st.slider("Vapor parameter 1",0,100)
    print(ses.GetRenderers())
    radio1 = st.radio("which Renderer do you want?","""ContourRenderer
FlowRenderer
ImageRenderer
ModelRenderer
Renderer
SliceRenderer
TwoDDataRenderer
VolumeIsoRenderer
VolumeRenderer
WireFrameRenderer""".split("\n"))
ren = data.NewRenderer(renderer.WireFrameRenderer)
ren.SetVariableName(data.GetDataVarNames(2)[0]) # Set to first 2D data variable

ses.GetCamera().ViewAll()
im = ses.RenderToImage()
print(im)
# for some reason thsi only works on the first time we start streamlit
st.title("Vapor in Streamlit")
st.markdown("""## Description
This App is meant to attempt to demonstrate how all the powers of Vapor+Python are now expanded by leveraging streamlit existing UI elements, and the option to further extend with custom components (Anything HTML+JS).
""")
st.image(im)
