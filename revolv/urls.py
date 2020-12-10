from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from revolv.base import views as base_views
from revolv.project import views as project_views
from revolv.base.views import solarathome, bring_solar_tou_your_community, select_chapter, intake_form, intake_form_submit, account_settings, editprofile, donation_update

from revolv.project.views import ProjectView
from revolv.solar_ed_week.views import (solar_education, host_event, become_partner, become_sponsor)

from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    (r'^ckeditor/', include('ckeditor.urls')),  # for assets for the ckedit widget, etc
    url(r'^sitemap\.xml/$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', base_views.HomePageView.as_view(), name='home'),
    url(r'^project/', include('revolv.project.urls', namespace='project')),
    url(r'^my-portfolio/$', base_views.DashboardRedirect.as_view(), name='dashboard'),
    url(r'^my-portfolio/categories/$', base_views.CategoryPreferenceSetterView.as_view(), name='dashboard_category_setter'),
    url(r'^my-portfolio/admin/', include('revolv.administrator.urls', namespace='administrator')),
    url(r'^my-portfolio/ambassador/', include('revolv.ambassador.urls', namespace='ambassador')),
    url(r'^my-portfolio/donor/', include('revolv.donor.urls', namespace='donor')),
    url(r'^payment_ajax_url/$', 'revolv.base.views.payment_data_table', name='payment_ajax_url'),
    url(r'^repayment_table/$', 'revolv.base.views.repayment_table',name='repayment_table'),
    url(r'^ambassador_data_table/$', 'revolv.base.views.ambassador_data_table', name='ambassador_data_table'),
    url(r'^ambassador_data_table_auto_reinvestors/$', 'revolv.base.views.ambassador_data_table_auto_reinvestors',
        name='ambassador_data_table_auto_reinvestors'),
    url(r'^my-portfolio/donationreport/', base_views.DonationReportView.as_view(), name='donationreport'),
    url(r'^my-portfolio/financialreport/', base_views.DonationReportForProject.as_view(), name='financialreport'),
    url(r'^my-portfolio/repaymentreport/', base_views.RepaymentReport.as_view(), name='repaymentreport'),
    url(r'^my-portfolio/matchingdonors/', base_views.MatchingDonorsView.as_view(), name='matchingdonors'),
    url(r'^my-portfolio/donationsourcetracking/', base_views.DonationSourceTrackingView.as_view(), name='donationsourcetracking'),
    url(r'^my-portfolio/reinvest_list/', base_views.ReinvestmentRedirect.as_view(), name='reinvest_list'),
    url(r'^my-portfolio/donationhistory/', base_views.DonationHistory.as_view(), name='donation_history'),
    url(r'^my-portfolio/sendmail/', 'revolv.base.views.sendmail', name='sendmail'),
    url(r'^my-portfolio/senddonoremail/', 'revolv.base.views.send_donor_email', name='senddonoremail'),
    url(r'^account_settings/', 'revolv.base.views.account_settings', name='account_settings'),
    url(r'^user_update/', base_views.editprofile.as_view(), name='user_update'),
    url(r'^donation_update/', 'revolv.base.views.donation_update', name='donation_update'),
    url(r'^get-involved/leonardo-dicaprio-foundation-partners-re-volv/', 'revolv.base.views.leo_page', name='leo_page'),
    url(r'^get-involved/faq', 'revolv.base.views.faq', name='faq'),


    url(r'^about-us/re-volv', 'revolv.base.views.aboutus', name='aboutus'),
    url(r'^about-us/team/', 'revolv.base.views.team', name='team'),
    url(r'^about-us/jobs', 'revolv.base.views.jobs', name='jobs'),
    url(r'^get-involved/solar-ambassador', 'revolv.base.views.solar_ambassador', name='solar_ambassador'),
    url(r'^get-involved/apply', 'revolv.base.views.nonprofit_app', name='nonprofit_app'),
    url(r'^get-involved/solar', 'revolv.base.views.nonprofit_epc', name='nonprofit_epc'),

    url(r'^nonprofit/videos', 'revolv.base.views.nonprofit_videos', name='nonprofit_videos'),
    url(r'^webinar/', 'revolv.base.views.webinar_videos', name='webinar_videos'),

    #education center categories
    url(r'^get-involved/education/solarenergyfinancing', 'revolv.base.views.solarenergysection', name='solarenergysection'),
    url(r'^get-involved/education/solarcommunity', 'revolv.base.views.bringsolarsection', name='bringsolarsection'),
    url(r'^get-involved/education/crowdfunding', 'revolv.base.views.solarcrowdfundingsection', name='solarcrowdfundingsection'),
    url(r'^get-involved/education/careers', 'revolv.base.views.solarcareerssection', name='solarcareerssection'),

    #landing page
    url(r'^book/climate-courage', 'revolv.base.views.climate_courage', name='climate_courage'),

    #education center articles
    url(r'^get-involved/education/solarjobs', 'revolv.base.views.solarforall', name='solarforall'),
    url(r'^get-involved/education/reasonforsolar', 'revolv.base.views.reasonforsolar', name='reasonforsolar'),
    url(r'^get-involved/education/bringsolar', 'revolv.base.views.bringsolar', name='bringsolar'),
    url(r'^get-involved/education/waystoget', 'revolv.base.views.waystoget', name='waystoget'),
    url(r'^get-involved/education/launchcrowd', 'revolv.base.views.launchcrowd', name='launchcrowd'),
    url(r'^get-involved/education/impactfilm', 'revolv.base.views.impactfilm', name='impactfilm'),
    url(r'^get-involved/education/meetcrowd', 'revolv.base.views.meetcrowd', name='meetcrowd'),
    url(r'^get-involved/education/lookingsolar', 'revolv.base.views.lookingsolar', name='lookingsolar'),
    url(r'^get-involved/education/solarenergy', 'revolv.base.views.solarenergy', name='solarenergy'),
    url(r'^get-involved/education/solarfinance', 'revolv.base.views.solarfinance', name='solarfinance'),
    url(r'^get-involved/education/solartax', 'revolv.base.views.solartax', name='solartax'),
    url(r'^get-involved/education/solarizenonprofit', 'revolv.base.views.solarizenonprofit', name='solarizenonprofit'),

    url(r'^get-involved/education/solarpolicy', 'revolv.base.views.solarpolicy', name='solarpolicy'),
    url(r'^get-involved/education/historysolar', 'revolv.base.views.historysolar', name='historysolar'),
    url(r'^get-involved/education/leadingcity', 'revolv.base.views.leadingcity', name='leadingcity'),
    url(r'^get-involved/education/beststatesolar', 'revolv.base.views.beststatesolar', name='beststatesolar'),
    url(r'^get-involved/education/solarfacts', 'revolv.base.views.solarfacts', name='solarfacts'),


    url(r'^blog-center/articles/$', 'revolv.base.views.blogcenter', name='blogcenter'),

    url(r'^blog-center/articles/solarinvestment/', 'revolv.base.views.solararticles', name='solararticles'),
    url(r'^blog-center/articles/newyearrevolution/', 'revolv.base.views.newyearrevolution', name='newyearrevolution'),
    url(r'^blog-center/articles/solidarity/', 'revolv.base.views.solidarity', name='solidarity'),
    url(r'^blog-center/articles/electricity-source/', 'revolv.base.views.electricitysource', name='electricitysource'),

    url(r'^monthly_donor', 'revolv.base.views.monthly_donor', name='monthly_donor'),
    url(r'^thanks/postdonation/', 'revolv.base.views.postdonation', name='postdonation'),
    url(r'^thanks/postmonthlydonation/', 'revolv.base.views.postmonthlydonation', name='postmonthlydonation'),
    url(r'^thanks/postnonprofit/', 'revolv.base.views.postnonprofitlead', name='postnonprofitlead'),

    url(r'^thanks/postinstaller/', 'revolv.base.views.postepclead', name='postepclead'),
    url(r'^thanks/postambassador/', 'revolv.base.views.postambassadorlead', name='postambassadorlead'),

    url(r'^re-volv/media', 'revolv.base.views.media_archive', name='media_archive'),
    url(r'^get-involved/education/', 'revolv.base.views.education_center_section', name='education_center_section'),

    url(r'^fundraise_form/', 'revolv.base.views.fundraise_form', name='fundraise_form'),
    url(r'^fundraise/sample', 'revolv.base.views.fundraise_pld', name='fundraise_pld'),
    url(r'^choose/', 'revolv.base.views.fundraise_choose', name='fundraise_choose'),
    url(r'^sampleproject/', 'revolv.base.views.new_campaign', name='new_campaign'),

    url(r'^How_it_works/', 'revolv.base.views.howitworks', name='howitworks'),

    url(r'^newsletter_confirm/', 'revolv.base.views.newsletter_confirm', name='newsletter_confirm'),
    url(r'^donate_confirm/', 'revolv.base.views.donate_confirm', name='donate_confirm'),
    url(r'^email_confirm/', 'revolv.base.views.email_confirm', name='email_confirm'),
#-----
    
    url(r'^terms/privacy_policy', 'revolv.base.views.privacy_policy', name='privacy_policy'),
    url(r'^get-involved/revolv-accelerator/', 'revolv.base.views.revolv_accelerator', name='revolv_accelerator'),
    url(r'^get-involved/leadership-circle/', 'revolv.base.views.leadership_circle', name='leadership_circle'),
    url(r'^solar-education/myths-and-facts/', 'revolv.base.views.myths_and_facts', name='myths_and_facts'),
    url(r'^my-portfolio/monthlyrepaymentreport/', base_views.MonthlyRepaymentReport.as_view(),
        name='monthlyrepaymentreport'),
    url(r'^monthly_repayment_table/$', 'revolv.base.views.monthly_repayment_table', name='monthly_repayment_table'),
    url(r'^repayment_config/$', 'revolv.administrator.views.repayment_config', name='repayment_config'),
    url(r'^my-portfolio/user-details/', base_views.UserListView.as_view(), name='user_details'),

    url(r'^what-we-do/projects/', base_views.ProjectListView.as_view(), name='projects_list'),
    url(r'^what-we-do/fundraise/', base_views.FundraiseListView.as_view(), name='fundraise_list'),
    url(r'^signin/$', base_views.SignInView.as_view(), name='signin'),
    url(r'^login/$', base_views.LoginView.as_view(), name='login'),
    url(r'^projects/completed_projects', 'revolv.base.views.completedproject', name='completed_projects'),
    url(r'^projects/completed_campaigns', 'revolv.base.views.completedcampaigns', name='completed_campaigns'),
    url(r'^signup/$', base_views.SignupView.as_view(), name='signup'),
    url(r'^logout/$', base_views.LogoutView.as_view(), name='logout'),
    url(r'^subscribe/$', 'revolv.base.views.add_email_to_mailing_list', name='subscribe'),
    url(r'^unsubscribe/(?P<action>\w+)/$', 'revolv.base.views.unsubscribe', name='unsubscribe'),
    url(r'^solar_at_home/$',solarathome, name='solar_at_home'),
    url(r'^bring_solar_to_your_community/$',bring_solar_tou_your_community, name='bring_solar_to_your_community'),
    url(r'^bring_solar_to_your_community/chapter/(?P<chapter>\d+)/$',select_chapter, name='chapter'),
    url(r'^bring_solar_to_your_community/intake_form/$',intake_form, name='intake_form'),
    url(r'^bring_solar_to_your_community/intake_form/signup/$','revolv.base.views.intake_form2', name='intake_form2'),
    url(r'^bring_solar_to_your_community/intake_form/nonprofit/$','revolv.base.views.intake_form3', name='intake_form3'),
    url(r'^bring_solar_to_your_community/intake_form/solar/$','revolv.base.views.intake_form4', name='intake_form4'),
    url(r'^bring_solar_to_your_community/intake_form/submit/$',intake_form_submit, name='intake_form_submit'),
    url(r'^my_social_account/$', 'revolv.base.views.social_connection', name='social-connection'),
    url(r'^delete/$', 'revolv.base.views.delete', name='delete'),
    url(r'^edit/$', 'revolv.base.views.edit', name='edit'),
    url(r'^delete_event/$', 'revolv.base.views.delete_event', name='delete_event'),
    url(r'^edit_event/$', 'revolv.base.views.edit_event', name='edit_event'),
    url(r'^add_events_form/$', 'revolv.base.views.add_events_form', name='add_events_form'),
    url(r'^add_matching_donor/$', 'revolv.base.views.add_maching_donors', name='add_matching_donor'),
    url(r'^social_connect_failed/$', 'revolv.base.views.social_exception', name='social-exception'),

    url(r'^password_reset/$', base_views.password_reset_initial, name="password_reset"),
    url(r'^password_reset/done/$', base_views.password_reset_done, name="password_reset_done"),
    url(r'^password_reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$$', base_views.password_reset_confirm, name="password_reset_confirm"),
    url(r'^password_reset/complete/$', base_views.password_reset_complete, name="password_reset_complete"),
    url(r'^password_change/$', base_views.password_change, name="password_change"),
    url(r'^export_csv/$', 'revolv.base.views.export_csv', name='export_csv'),
    url(r'^export_excel/$', 'revolv.base.views.export_xlsx', name='export_excel'),
    url(r'^export_repayment_csv/$', 'revolv.base.views.export_repayment_csv', name='export_repayment_csv'),
    url(r'^export_repayment_xlsx/$', 'revolv.base.views.export_repayment_xlsx', name='export_repayment_xlsx'),
    url(r'^my-portfolio/solar-event-report/', base_views.SolarWeekEventReportView.as_view(),
        name='solarweekeventreportview'),
    url(r'^event_data_table/$', 'revolv.base.views.solar_ed_event_data_table',
        name='solar_ed_event_data_table'),
    url(r'^my-portfolio/solar-partners-report/', base_views.SolarWeekPartnerReportView.as_view(),
        name='solarweekpartnersreportview'),
    url(r'^partner_data_table/$', 'revolv.base.views.solar_ed_partner_data_table',
        name='solar_ed_partners_data_table'),

    # wagtail urls, see http://wagtail.readthedocs.org/en/v1.0b2/howto/settings.html
    # note: we're not including the search module for public users, so we don't define it here
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'social/', include('social.apps.django_app.urls', namespace='social')),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'^harborhouse/$','revolv.base.views.harborhouse', name="harborhouse"),
    url(r'^riverrevitalizationfoundation/$','revolv.base.views.riverrevitalizationfoundation', name="riverrevitalizationfoundation"),
    url(r'^campketcha/$','revolv.base.views.campketcha', name="campketcha"),
    url(r'^project/faithbaptistchurch/$','revolv.base.views.faithbaptistchurch', name="faithbaptistchurch"),

    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry')),
    # url(r'^solar-education/solar-education-week/', include('revolv.solar_ed_week.urls')),
    url(r'^solar-education/solar-education-week/host-event/$', host_event, name='host_event'),
    url(r'^solar-education/solar-education-week/become-partner/$', become_partner, name='become_partner'),
    url(r'^solar-education/solar-education-week/become-sponsor/$', become_sponsor, name='become_sponsor'),
    url(r'^solar-education/solar-education-week/$', solar_education, name='solar_education'),

    url(r'', include(wagtail_urls)),



) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
