$(function(){
    $('#remove_button').prop('disabled', true);
    $('#remove_button').hide();

    var loadAccountDetails = function(){
        requestAjax(
             {
                url: window.location.origin + "/api/account/details",
                type: "GET",
                data:{}
            },
            function(data){
                var user = JSON.parse(data.user)
                var plan = JSON.parse(data.plan)

                $('.account_email').text(user.email);

                $('.account_password').text(user.password);
                $('.account_status').text(user.status);

                if(plan === null){
                    $('.account_quick_analysis_quota').text('0');
                    $('.account_topic_quota').text('0');
                    $('.account_plan_name').text('-');
                    $('.account_plan_status').text(user.plan_status);
                    $('.account_expiry').text('None');
                }
                else{
                    $('.account_quick_analysis_quota').text(parseInt(plan.quick_analysis_quota) - parseInt(user.quick_analysis_counter));
                    $('.account_topic_quota').text(parseInt(plan.topic_quota) - parseInt(user.topic_quota_counter));
                    $('.account_plan_name').text(plan.plan_name.toLowerCase());
                    $('.account_plan_status').text(user.plan_status);
                    $('.account_expiry').text(getFormattedDatetime(getFutureDate(user.plan_subscribed_at, parseInt(plan.plan_duration))));
                }
            }
        );
    }

    loadAccountDetails();
});