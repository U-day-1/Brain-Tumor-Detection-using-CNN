from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Brain Tumor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_disease = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_gkgqj2yq.json")

img_glioma = Image.open("./images/Glioma.jpg")
img_meningioma = Image.open("./images/menin.jpg")
img_pitutary = Image.open("./images/Te-pi_0091.jpg")


# st.title("Main Page")
st.title("Learn More")
st_lottie(lottie_disease, height=300, key="disease")
st.subheader("Read articles about some Types of Brain Tumor.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Glioma ")
        st.write("##")
        st.write(
            """
            A glioma is a tumor that forms in the brain or spinal cord. 
            There are several types, including astrocytomas, ependymomas and oligodendrogliomas. 
            Gliomas can affect children or adults. Some grow very quickly. Most people with gliomas 
            need a combination of treatments such as surgery, radiation therapy and chemotherapy.
            - Types: Gliomas categorized by glial cell type: Astrocytomas (from astrocytes), oligodendrogliomas (from oligodendrocytes), and ependymomas (from ependymal cells).
            - Grades: Graded I-IV based on aggressiveness. I-II are low-grade, III-IV are high-grade—latter more aggressive and faster-growing.

            - Symptoms: Vary with location and size—headaches, nausea, vomiting, seizures, cognitive changes, and neurological deficits.

            - Diagnosis:  Involves imaging (MRI/CT) and biopsy for type and grade determination.

            - Treatment: Options include surgery, radiation, and chemotherapy based on type, grade, and location.

            - Prognosis: Varies based on type, grade, and surgical removal. High-grade gliomas often have a poorer prognosis. removed. High-grade gliomas, in particular, tend to have a poorer prognosis.
            """
        )
       # st.write("[Learn More](https://www.nhs.uk/conditions/actinic-keratoses)")
    with right_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.image(img_glioma)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.image(img_meningioma)

    with right_column:
        st.header("Meningioma")
        st.write("##")
        st.write(
            """
            Meningiomas are tumors that arise from the meninges, which are the layers of tissue covering the brain and spinal cord. These tumors are typically slow-growing and often benign, meaning they are not cancerous. Here are some key points about meningiomas:
            - Location: Meningiomas can appear anywhere on the meninges, commonly near the brain's surface or along the spinal cord.

            - Incidence: More common in women, often diagnosed in adults over 40.

            - Symptoms: Vary based on size and location, including headaches, seizures, vision/hearing changes, limb weakness, and personality changes. Some are asymptomatic and found incidentally during imaging.

            - Types: Classified by WHO into grades I-III; Grade I is benign, Grade II is atypical, and Grade III is malignant.

            - Diagnosis: Involves MRI or CT scans, with biopsy if needed for type and grade determination.

            - Treatment: Options include observation, surgery, radiation, and medication based on size, location, and grade. Benign meningiomas often treated effectively with surgery.

            - Prognosis: Generally favorable, especially for benign tumors. Outcome varies with factors such as location and grade. Regular monitoring may be advised.
            
           """
        )
   

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Pitutary")
        st.write("##")
        st.write(
            """
            Pituitary Tumor is an abnormal growth that is seen within the pituitary gland. In majority of the cases these tumors are benign. There are some pituitary tumors which make the pituitary gland secrete abnormally high levels of hormones, which may result in hormonal imbalance while there are some tumors, which cause the gland to secrete lower levels of hormones.
            - Type: Pituitary tumors originate in the pituitary gland, a small gland at the base of the brain.

            - Location: Found in the pituitary gland, these tumors can be functional (secreting hormones) or non-functional (not secreting hormones).

            - Incidence: Common, often benign. More frequent in adults but can occur at any age.

            - Symptoms: Vary based on hormone secretion and tumor size. May include hormonal imbalances, headaches, vision changes, and fatigue.

            - Types: Classified as functional (secreting hormones, e.g., prolactinomas, growth hormone-secreting tumors) or non-functional. Some are microadenomas (small) or macroadenomas (large).

            - Diagnosis: Involves hormone level tests, imaging (MRI/CT), and sometimes a biopsy to determine hormone secretion.

            - Treatment: Options include medication, surgery, or radiation. Treatment depends on hormone secretion, tumor size, and symptoms.

            - Prognosis: Generally favorable, especially for benign tumors. Hormonal management and regular monitoring may be needed. Surgery or other interventions may be necessary in certain cases.
            """
        )
       
    with right_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.image(img_pitutary)
