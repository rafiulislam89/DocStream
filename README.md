# **DocStream**  

## **Overview**  
DocStream is an online platform that enables multiple hospitals to efficiently track, monitor, and share patient health records. Patients can access information about various hospitals and doctors, book appointments online, purchase medicines from an integrated online pharmacy, pay for laboratory tests through a secure payment gateway, and communicate with their appointed doctors via chat.  

## **Project Details**  
- **Project Type:** Software Engineering Project  
- **Degree:** B.Sc. in Computer Science and Engineering (CSE)  
- **Project Duration:** August 2023 - September 2024  

## **Contributors**  
- **[Rafiul Islam](https://www.linkedin.com/in/rafiulislam-cse)**  
- **[Iqbal Ahsan](https://www.linkedin.com/in/iqbal-ahsan)**  

## **Tech Stack**  
### **Programming Languages & Frameworks:**  
- Django (Python Web Framework)  
- Bootstrap  
- JavaScript, Ajax  
- Django REST Framework  

### **Database:**  
- SQLite  

### **APIs & Packages:**  
- MailTrap API (SMTP Fake Testing Server)  
- SSLCommerz Payment Gateway  
- Django PDF Library (for generating reports)  
- Django Channels (for chat functionality)  
- Ngrok (HTTP Tunneling)  
- PyPI Packages  

## **Features**  
### **User Roles:**  
- **Patient**  
- **Doctor**  
- **Hospital Admin**  
- **Lab Worker**  
- **Pharmacist**  

### **Patient Features:**  
✅ Search for hospitals, browse departments, and find doctors.  
✅ View doctor profiles and book appointments.  
✅ Pay for appointments and receive email confirmations.  
✅ Search for doctors across all hospitals.  
✅ Chat with appointed doctors.  
✅ View and download prescriptions (PDF format).  
✅ Select and pay for laboratory tests (Cart system, payment + email confirmation).  
✅ View and download lab reports (PDF format).  
✅ Submit doctor reviews.  
✅ Search for medicines in the online pharmacy.  
✅ Add medicines to the cart, pay online, and receive email confirmation.  

### **Doctor Features:**  
✅ Manage doctor profile.  
✅ Register with multiple hospitals and upload certifications.  
✅ Accept or reject patient appointments (email notifications sent to patients).  
✅ View patient profiles, create and manage prescriptions, and access reports.  
✅ Chat with appointed patients.  

### **Hospital Admin Features:**  
✅ Admin Dashboard.  
✅ Approve or reject doctor registrations.  
✅ Manage hospital details (CRUD operations).  
✅ Manage hospital departments.  
✅ Add and manage lab workers.  
✅ Add and manage pharmacists.  

### **Lab Worker Features:**  
✅ Lab Worker Dashboard.  
✅ Create patient lab reports.  
✅ Create and manage hospital tests.  

### **Pharmacist Features:**  
✅ Pharmacist Dashboard.  
✅ Add and manage medicines.  
✅ Search for medicines in the system.  

## **Installation & Setup**  
### **Clone the Repository**  
```sh  
git clone https://github.com/rafiulislam89/DocStream.git  
cd DocStream  
```

### **Set Up Virtual Environment**  
```sh  
python -m venv venv  
```

### **Activate the Virtual Environment**  
- **Windows:**  
  ```sh  
  venv\Scripts\activate  
  ```
- **Mac/Linux:**  
  ```sh  
  source venv/bin/activate  
  ```

### **Install Dependencies**  
```sh  
pip install -r requirements.txt  
```

### **Set Up Environment Variables**  
```sh  
cp .env.example .env  
```
- Update the `.env` file with required credentials for MailTrap and SSLCommerz.  

### **Upgrade Django REST Framework (if needed)**  
```sh  
pip install --upgrade djangorestframework-simplejwt  
```

### **Run Migrations**  
```sh  
python manage.py migrate  
```

### **Start the Application**  
```sh  
python manage.py runserver  
```

## **API & Dependencies**  
- **Django REST Framework** - Toolkit for building web APIs.  
- **Django Widget Tweaks** - Tweaks form field rendering in templates.  
- **Pillow** - Python imaging library.  
- **Mailtrap API** - SMTP fake testing server for email functionalities.  
- **Django Environ** - Secure credentials management using `.env` files.  
- **SSLCommerz API** - Secure payment gateway for transactions in Bangladesh.  
- **Django Debug Toolbar** - Displays debugging information for developers.  
- **xhtml2pdf** - Generates and downloads PDF documents (prescriptions, reports).  

## **Documentation & Presentation**  
- **[MKDocs Documentation](#)** (Detailed project guide with screenshots)  

# Visitor Count  
<p align="center">
  <img src="https://visitor-count-b8lb.vercel.app/api/Github_Username?hexColor=00ff00" />
</p>


---  
🚀 Developed by **[Rafiul Islam](https://www.linkedin.com/in/rafiulislam-cse)** & **[Iqbal Ahsan](https://www.linkedin.com/in/iqbal-ahsan)**  

