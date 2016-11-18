from django.test import TestCase
from lists.models import List, Item
from lists.forms import ItemForm, EMPTY_ITEM_ERROR, DUPLICATE_ITEM_ERROR, \
    ExistingListItemForm


class ItemFormTest(TestCase):

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()

        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        items_list = List.objects.create()
        form = ExistingListItemForm(for_list=items_list, data={'text': ''})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'do me'})
        new_item = form.save(for_list=list_)

        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)

    def test_form_renders_item_text_input(self):
        items_list = List.objects.create()
        form = ExistingListItemForm(for_list=items_list)

        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_duplicate_items(self):
        items_list = List.objects.create()
        Item.objects.create(list=items_list, text='no twins!')
        form = ExistingListItemForm(
            for_list=items_list,
            data={'text': 'no twins!'})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])
