import sys

import streamlit as st
import streamlit_antd_components as sac

from chatchat import __version__
from chatchat.server.utils import api_address
from chatchat.webui_pages.dialogue.dialogue import  dialogue_page
from chatchat.webui_pages.feedback.feedback_page import feedback_page
from chatchat.webui_pages.kb_chat import kb_chat
from chatchat.webui_pages.kb_chat_user import kb_chat_user
from chatchat.webui_pages.knowledge_base.knowledge_base import knowledge_base_page
from chatchat.webui_pages.utils import *

api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    is_lite = "lite" in sys.argv  # TODO: remove lite mode

    st.set_page_config(
        # "Langchain-Chatchat WebUI",
        # get_img_base64("chatchat_icon_blue_square_v2.png"),
        "MedSense",
        get_img_base64("doctor.png"),
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://github.com/chatchat-space/Langchain-Chatchat",
            "Report a bug": "https://github.com/chatchat-space/Langchain-Chatchat/issues",
            "About": f"""欢迎使用 Langchain-Chatchat WebUI {__version__}！""",
        },
        layout="centered",
    )

    # use the following code to set the app to wide mode and the html markdown to increase the sidebar width
    st.markdown(
        """
        <style>
        [data-testid="stSidebarUserContent"] {
            padding-top: 20px;
        }
        .block-container {
            padding-top: 25px;
        }
        [data-testid="stBottomBlockContainer"] {
            padding-bottom: 20px;
        }
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.image(
            # get_img_base64("logo-long-chatchat-trans-v2.png"), use_column_width=True
            get_img_base64("MedSense_logo.png"), use_column_width=True
        )
        # st.caption(
        #     f"""<p align="right">当前版本：{__version__}</p>""",
        #     unsafe_allow_html=True,
        # )

        selected_page = sac.menu(
            [
                # sac.MenuItem("多功能对话", icon="chat"),
                sac.MenuItem("RAG Chat", icon="database"),
                sac.MenuItem("Suggestions for improvement", icon="emoji-smile"),
                # sac.MenuItem("知识库管理", icon="hdd-stack"),
            ],
            key="selected_page",
            open_index=0,
        )

        sac.divider()

    if selected_page == "Knowledge Base Management":
        knowledge_base_page(api=api, is_lite=is_lite)
    elif selected_page == "RAG Chat":
        kb_chat_user(api=api)
    elif selected_page == 'Suggestions for improvement':
        feedback_page()
    else:
        dialogue_page(api=api, is_lite=is_lite)
