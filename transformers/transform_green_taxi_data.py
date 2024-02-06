if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # filter data
    data = data[
        (data["passenger_count"] > 0) &
        (data["trip_distance"] > 0)
    ]

    # add new date column
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # remove space from columns 
    data.columns = (data.columns
        .str.replace(' ', '_')
        .str.lower()
    )

    # print(len(data['lpep_pickup_date'].unique().tolist()))
    # print(data.shape)
    print(data['vendorid'].unique().tolist())

    return data


# vendor_id is one of the existing values in the column (currently)
@test
def test_vendor_id(output, *args) -> None:
    # can roughly understand this but i'll try
    UNIQUE_VENDORID_VALUES = output['vendorid'].unique().tolist()

    assert output['vendorid'].isin(UNIQUE_VENDORID_VALUES).all(), 'VendorID has values outside existing values in column'


@test
def test_passenger_count(output, *args) -> None:
    # passenger_count is greater than 0
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

@test
def test_trip_distance(output, *args) -> None:
    # trip_distance is greater than 0
    
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero passengers'

