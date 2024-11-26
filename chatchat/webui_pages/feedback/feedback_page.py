"""
题目：
作者：Jack
完成时间：2024/11/20 09:44
解题思路：
心得：
"""

import json
import os
import streamlit as st

# 意见提交页面
def feedback_page():
    st.title("Feedback Submission")

    # 表单输入
    with st.form("feedback_form"):
        user_name = st.text_input("Your Name", "")
        feedback = st.text_area("Your Feedback or Suggestions", "")
        submitted = st.form_submit_button("Submit")

    # 提交后保存意见
    if submitted:
        if feedback.strip():
            # 构建意见数据
            feedback_data = {
                "name": user_name if user_name.strip() else "Anonymous",
                "feedback": feedback.strip(),
            }

            # 保存到文件 (admin 可从此处查看)
            feedback_file = "feedback.json"
            if os.path.exists(feedback_file):
                with open(feedback_file, "r", encoding="utf-8") as f:
                    feedback_list = json.load(f)
            else:
                feedback_list = []

            feedback_list.append(feedback_data)

            with open(feedback_file, "w", encoding="utf-8") as f:
                json.dump(feedback_list, f, ensure_ascii=False, indent=4)

            st.success("Thank you for your feedback! We will review it promptly.")
        else:
            st.error("Feedback content cannot be empty. Please fill it in before submitting.")

# 管理员查看意见页面
def view_feedback_page():
    st.title("View Feedback")

    feedback_file = "feedback.json"
    if os.path.exists(feedback_file):
        with open(feedback_file, "r", encoding="utf-8") as f:
            feedback_list = json.load(f)

        if feedback_list:
            for idx, feedback_item in enumerate(feedback_list, 1):
                st.subheader(f"Feedback {idx}")
                st.text(f"User: {feedback_item['name']}")
                st.write(f"Feedback Content: {feedback_item['feedback']}")
        else:
            st.info("No feedback has been submitted yet.")
    else:
        st.info("Feedback file not found. No feedback has been submitted yet.")

