from django import test

from courier_income import factories
from courier_income import models


class CreateAndUpdateDailyIncomeRecordsTests(test.TestCase):

    def setUp(self):
        self.courier = self.create_courier()
    
    def test_create_one_daily_income_after_creating_a_trip_income(self):
        self.create_trip_income(courier=self.courier)
        self.assertEqual(self.courier.daily_incomes.count(), 1)

    def test_create_daily_income_with_correct_date_after_creating_a_trip_income(self):
        trip_income = self.create_trip_income(courier=self.courier)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.date, trip_income.date)

    def test_create_daily_income_with_correct_amount_after_creating_a_trip_income(self):
        trip_income = self.create_trip_income(courier=self.courier)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.amount, trip_income.amount)

    def test_create_one_daily_income_after_creating_a_reward(self):
        self.create_reward(courier=self.courier)
        self.assertEqual(self.courier.daily_incomes.count(), 1)

    def test_create_daily_income_with_correct_date_after_creating_a_reward(self):
        reward = self.create_reward(courier=self.courier)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.date, reward.date)

    def test_create_daily_income_with_correct_amount_after_creating_a_reward(self):
        reward = self.create_reward(courier=self.courier)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.amount, reward.amount)

    def test_create_one_daily_income_after_creating_a_forfeit(self):
        self.create_forfeit(courier=self.courier)
        self.assertEqual(self.courier.daily_incomes.count(), 1)

    def test_create_daily_income_with_correct_date_after_creating_a_forfeit(self):
        forfeit = self.create_forfeit(courier=self.courier)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.date, forfeit.date)

    def test_create_daily_income_with_correct_amount_after_creating_a_forfeit(self):
        forfeit = self.create_forfeit(courier=self.courier)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.amount, -forfeit.amount)

    def test_update_existing_daily_income_after_creating_a_trip_income(self):
        daily_income = self.create_daily_income(courier=self.courier)
        self.assertEqual(self.courier.daily_incomes.count(), 1)
        self.create_trip_income(courier=self.courier, date=daily_income.date)
        self.assertEqual(self.courier.daily_incomes.count(), 1)

    def test_correct_updated_daily_income_amount_after_creating_a_trip_income(self):
        daily_income = self.create_daily_income(courier=self.courier)
        last_amount = daily_income.amount
        trip_income = self.create_trip_income(courier=self.courier, date=daily_income.date)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.amount, last_amount + trip_income.amount)

    def test_update_existing_daily_income_after_creating_a_reward(self):
        daily_income = self.create_daily_income(courier=self.courier)
        self.assertEqual(self.courier.daily_incomes.count(), 1)
        self.create_reward(courier=self.courier, date=daily_income.date)
        self.assertEqual(self.courier.daily_incomes.count(), 1)

    def test_correct_updated_daily_income_amount_after_creating_a_reward(self):
        daily_income = self.create_daily_income(courier=self.courier)
        last_amount = daily_income.amount
        reward = self.create_reward(courier=self.courier, date=daily_income.date)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.amount, last_amount + reward.amount)

    def test_update_existing_daily_income_after_creating_a_forfeit(self):
        daily_income = self.create_daily_income(courier=self.courier)
        self.assertEqual(self.courier.daily_incomes.count(), 1)
        self.create_forfeit(courier=self.courier, date=daily_income.date)
        self.assertEqual(self.courier.daily_incomes.count(), 1)

    def test_correct_updated_daily_income_amount_after_creating_a_forfeit(self):
        daily_income = self.create_daily_income(courier=self.courier)
        last_amount = daily_income.amount
        forfeit = self.create_forfeit(courier=self.courier, date=daily_income.date)
        daily_income = self.courier.daily_incomes.last()
        self.assertEqual(daily_income.amount, last_amount - forfeit.amount)

    # region functions
    def create_courier(self) -> models.Courier:
        return factories.CourierFactory()

    def create_trip_income(self, **kwargs) -> models.TripIncome:
        return factories.TripIncomeFactory(**kwargs)

    def create_reward(self, **kwargs) -> models.Reward:
        return factories.RewardFactory(**kwargs)

    def create_forfeit(self, **kwargs) -> models.Forfeit:
        return factories.ForfeitFactory(**kwargs)

    def create_daily_income(self, **kwargs) -> models.DailyIncome:
        return factories.DailyIncomeFactory(**kwargs)

    # endregion functions