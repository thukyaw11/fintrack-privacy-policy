import streamlit as st

def main():
    st.title("Privacy Policy for Fin Track")

    st.write(
        "At **Fin Track**, we value your privacy and are committed to protecting your personal information. This Privacy Policy explains how we collect, use, and safeguard your data when you use our application."
    )

    st.markdown("---")
    
    st.header("1. Information We Collect")
    st.subheader("1.1. Personal Information")
    st.write("- Name")
    st.write("- Email address")
    st.write("- Login credentials (securely stored)")

    st.subheader("1.2. Usage Information")
    st.write("- Transaction details (e.g., wallet type, amount, categories)")
    st.write("- Interaction with app features (e.g., creating wallets, making transactions)")

    st.subheader("1.3. Device Information")
    st.write("- Unique device identifiers")

    st.markdown("---")
    
    st.header("2. How We Use Your Information")
    st.write(
        "We use your information to:\n"
        "- Facilitate account creation and login.\n"
        "- Enable financial tracking features such as wallet management and transactions.\n"
        "- Provide customer support.\n"
        "- Improve app functionality and user experience.\n"
        "- Comply with legal obligations."
    )

    st.markdown("---")
    
    st.header("3. Sharing of Information")
    st.write(
        "We do not sell or share your personal information with third parties except:\n"
        "- **Service Providers:** To assist in providing the app’s functionality (e.g., cloud storage).\n"
        "- **Legal Obligations:** When required by law or to protect our legal rights."
    )

    st.markdown("---")
    
    st.header("4. Data Security")
    st.write(
        "We implement industry-standard measures to protect your data:\n"
        "- Encryption of sensitive data during storage and transmission.\n"
        "- Restricted access to personal information.\n"
        "- Regular security assessments."
    )
    st.write(
        "However, no method of transmission or storage is 100% secure. While we strive to protect your data, we cannot guarantee absolute security."
    )

    st.markdown("---")

    st.header("5. User Rights")
    st.write(
        "You have the following rights regarding your personal information:\n"
        "- **Access and Update:** View and modify your personal data via your account settings.\n"
        "- **Account Deletion:** Delete your account and associated data through the app.\n"
        "- **Data Portability:** Request a copy of your data in a portable format."
    )
    st.write("To exercise these rights, please contact us at helloeleven968@gmail.com.")

    st.markdown("---")

    st.header("6. Data Retention")
    st.write(
        "We retain your data as long as your account is active or as required for legitimate business purposes. Upon account deletion, your data will be permanently removed from our servers within 30 days, except as required by law."
    )

    st.markdown("---")

    st.header("7. Children’s Privacy")
    st.write(
        "Fin Track is not intended for individuals under the age of 13. We do not knowingly collect data from children. If we learn that a child’s data has been collected, we will delete it promptly."
    )

    st.markdown("---")

    st.header("8. Changes to This Privacy Policy")
    st.write(
        "We may update this Privacy Policy from time to time. Changes will be notified via the app or email. Continued use of the app after updates constitutes acceptance of the revised policy."
    )

    st.markdown("---")

    st.header("9. Contact Us")
    st.write(
        "If you have any questions or concerns about this Privacy Policy, please contact us at:\n"
        "- **Email:** helloeleven968@gmail.com\n"
    )

if __name__ == "__main__":
    main()
