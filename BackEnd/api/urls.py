from django.urls import path
from . import views


urlpatterns = [
    path('api_tourism_comapny', views.all_companies, name='all_tourism_companies'),
    path('api_tourism_comapny/<int:id>', views.oneTourismCompany, name='one_tourism_company'),
    path('api_tourism_places', views.all_places, name='all_tourism_places'),
    path('api_tourism_places/<int:id>', views.oneTourismPlace, name='one_tourism_places'),
    path('', views.tourismApi,name='tourism'),
    path('doctors', views.all_doctor,name='all_doctor'),
    path('doctor/<int:id>', views.one_doctor,name='one_doctor'),
    path('treatments', views.all_TretmentCenter,name='all_treatment'),
    path('treatment/<int:id>', views.one_TretmentCenter,name='one_treatment'),
    path('treatment/<str:email>', views.one_TretmentCenter_emaill,name='one_treatment_email'),
    path('users_api',views.all_users,name='users_api'),
    ########## changes 
    path('activate/<uuid:token>/', views.activate, name='activate'),
    path('filterdoctors',views.filter_doctors,name='filterdoctor'),
    ########### end of changes
    path('one_user_api/<int:id>',views.one_user,name='one_user_api'),
    path('login_api',views.loGin,name='login'),
    path('tourism_reservations',views.all_tourism_reservations,name='Tourism_Reservations'),
    path('all_tourism_reservations_book',views.all_tourism_reservations_book,name='all_tourism_reservations_book'),
    path('one_tourism_reservation/<int:id>',views.one_tourism_reservation,name='One_Tourism_Reservation'),
    path('all_medical_reservations',views.all_medical_reservations,name='All_Medical_Reservations'),
    path('all_medical_reservations_book',views.all_medical_reservations_book,name='all_medical_reservations_book'),
    path('one_medical_reservation/<int:id>',views.one_medical_reservation,name='One_Medical_Reservation'),
    path('medical_reservation_data',views.medical_reservation_data,name='medicalreservationdata'),
    path('tourism_reservation_data',views.tourism_reservation_data,name='tourismreservationdata'),
    path('treatment_doctors',views.Get_Treatment_Center_Doctors,name='treatmentDoctors'),
    path('treatment_reservations',views.Get_Treatment_Center_Reservations,name='treatmentReservations'),
    path('tourism/<str:email>',views.one_TourismCompany_emaill,name='one_company_email'),
    path('tourism_company_places',views.Get_Tourism_Company_Places,name='tourismcompanyplaces'),
    path('tourism_company_reservations',views.Get_Tourism_Company_Reservations,name='tourismcompanyreservations'),
    path('doctors_search',views.Search_Doctors,name='Doctors_Search'),
    path('delete_doctor/<int:doctor_id>',views.delete_doctor,name='delete_doctor'),
    path('delete_place/<int:place_id>',views.delete_tourism,name='delete_place'),
    path('searchtreatments',views.Search_Treatments,name='searchhairtreatments'),
    path('searchPlaces',views.Search_Places,name='searchplace'),
    path('searchCompanies',views.Search_Tourism_Companies,name='searchCompany'),
    path('rating_treatment',views.treatment_center_Rate,name="rateTreatment"),
    path('checking_treatment_rating',views.CEHCKING_Rating,name='checkingfortreatment'),
    path('rating_tourism',views.tourism_company_Rate,name="rateTourism"),
    path('checking_tourism_rating',views.CEHCKING_Rating_Tourism,name="ratingTourismcheck"),
    path('checking_book_medical_',views.checking_book_medical,name="checkingBookMedical"),
    path('checking_book_tourism_',views.checking_book_tourism,name="checkingBookTourism"),
    path('accept_email',views.sending_email_accept , name="acceptEmail"),
    path('reject_email',views.sending_email_reject,name="emailReject"),
    path('feedback_treatment',views.treatment_center_feedback,name="feedbackTreatment"),
    path('checking_treatment_feedback',views.checking_feedback,name='feedbackcheckingfortreatment'),
    path('treatment_center_feedbacks',views.all_feedback,name="treatmentCenterFeedbacks"),
    path('feedback_tourism',views.tourism_company_feedback,name="feedbackTourism"),
    path('checking_tourism_feedback',views.checking_feedback_tourism_company,name='feedbackcheckingfortourism'),
    path('tourism_company_feedbacks',views.all_feedback_tourism_company,name="tourismcompanyFeedbacks"),
    path('activate/<uuid:token>/', views.activate, name='activate'),
    path('filterdoctors',views.filter_doctors,name='filterdoctor'),
    path('tourism_payment_list',views.tourism_payment_list,name="tourism_payment_list"),
    path('tourism_get_payment',views.get_payment_tourism,name="get_payment_tourism"),
    path('get_payment',views.get_payment,name="get_payment"),
    path('payment_done',views.payment_list,name="payment_done_medical"),
    path('reply_treatment_feedback',views.reply_feedback_treatment,name="replytreatmentfeedback"),
    path('one_treatment_feedback',views.get_one_treatment_feedback,name="onetreatmentfeedback"),
    path('reply_tourism_feedback',views.reply_feedback_tourism,name="replytourismfeedback"),
    path('one_tourism_feedback',views.get_one_tourism_feedback,name='onetourismfeedback')
]
