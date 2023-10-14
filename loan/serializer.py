from rest_framework import serializers

from loan.models import loan



class loanSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = loan
        fields = (
            "id",
            'borrower_id',
            "loan_id",
            "loan_product_id",
            "loan_application_id",
            "loan_disbursed_by_id",
            "loan_principal_amount",
            "loan_released_date",
            "loan_interest_method",
            "loan_interest_type",
            "loan_interest_period",
            "loan_interest",
            "loan_duration_type",
            "loan_duration",
            "loan_duration_period",
            "loan_payment_scheme_id",
            "loan_num_of_repayments",
            "loan_decimal_places",
            "loan_interest_start_date",
            "loan_fees_pro_rata",
            "loan_do_not_adjust_remaining_pro_rata",
            "loan_first_repayment_pro_rata",
            "loan_first_repayment_date",
            "first_repayment_amount",
            "last_repayment_amount",
            "loan_override_maturity_date",
            "override_each_repayment_amount",
            "loan_interest_each_repayment_pro_rata",
            "loan_interest_schedule",
            "loan_principal_schedule",
            "loan_balloon_repayment_amount",
            "automatic_payments",
            "payment_posting_period",
            "total_amount_due",
            "balance_amount",
            "due_date",
            "total_paid",
            "child_status_id",
            "loan_fee_schedule_3951",
            "loan_fee_id_3951",
            "created_by",
            "created",
            "modified",
            "updated_by",
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

