
def data_sample                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ():
  data_sample_success = {
      "name": "Item 1",
      "price": 9.99,
      "description": "This is a description",
      "tax": 0.5
    }
  data_sample_error = {
      "name": "Item 1",
      "price": "fdsfdsf",
      "description": "This is a description",
      "tax": "0.5"
    }

  data_sample_exclude = {
      "name": "Item 1",
      "price": 9.99,
      "description": "This is a description",
      "tax": 0.5
    }

  data_sample_field_validator = {
      "name": "hello",
      "price": 9.99,
      "description": "This is a description",
      "tax": 0.5
    }
  data_sample_field_validator_error = {
      "name": "hello",
      "price": -9.99,
      "description": "This is a description",
      "tax": 0.5
    }
  return data_sample_success, data_sample_error, data_sample_exclude, data_sample_field_validator, data_sample_field_validator_error



