import pystac
from pystac import ProviderRole
from pystac.link import Link
from pystac.extensions.eo import Band

INSPIRE_METADATA_ASSET_KEY = "inspire-metadata"
SAFE_MANIFEST_ASSET_KEY = "safe-manifest"
PRODUCT_METADATA_ASSET_KEY = "product-metadata"

SENTINEL_LICENSE = Link(
    rel="license",
    target="https://sentinel.esa.int/documents/" +
    "247904/690755/Sentinel_Data_Legal_Notice",
)

ACQUISITION_MODES = [
    "Stripmap (SM)",
    "Interferometric Wide Swath (IW)",
    "Extra Wide Swath (EW)",
    "Wave (WV)",
]
SENTINEL_CONSTELLATION = "Sentinel 1"

SENTINEL_PROVIDER = pystac.Provider(
    name="ESA",
    roles=[
        ProviderRole.PRODUCER,
        ProviderRole.PROCESSOR,
        ProviderRole.LICENSOR,
    ],
    url="https://earth.esa.int/web/guest/home",
)

SAFE_MANIFEST_ASSET_KEY = "safe-manifest"

SENTINEL_SLSTR_BANDS = {
    'B01':
    Band.create(name='B01',
                common_name='coastal',
                description='Band 1 - Coastal aerosol',
                center_wavelength=0.443,
                full_width_half_max=0.027),
    'B02':
    Band.create(name='B02',
                common_name='blue',
                description='Band 2 - Blue',
                center_wavelength=0.490,
                full_width_half_max=0.098),
    'B03':
    Band.create(name='B03',
                common_name='green',
                description='Band 3 - Green',
                center_wavelength=0.560,
                full_width_half_max=0.045),
}

SENTINEL_OLCI_BANDS = {
    'Oa01':
    Band.create(name='Oa01',
                description='Band 1 - Aerosol correction, improved water constituent retrieval',
                center_wavelength=400,
                bandwidth=15),
    'Oa02':
    Band.create(name='Oa02',
                description='Band 2 - Yellow substance and detrital pigments (turbidity)',
                center_wavelength=412.5,
                bandwidth=10),
    'Oa03':
    Band.create(name='Oa03',
                description='Band 3 - Chlorophyll absorption maximum, biogeochemistry, vegetation',
                center_wavelength=442.5,
                bandwidth=10),
    'Oa04':
    Band.create(name='Oa04',
                description='Band 4 - Chlorophyll',
                center_wavelength=490,
                bandwidth=10),
    'Oa05':
    Band.create(name='Oa05',
                description='Band 5 - Chlorophyll, sediment, turbidity, red tide',
                center_wavelength=510,
                bandwidth=10),
    'Oa06':
    Band.create(name='Oa06',
                description='Band 6 - Chlorophyll reference (minimum)',
                center_wavelength=560,
                bandwidth=10),    
    'Oa07':
    Band.create(name='Oa07',
                description='Band 7 - Sediment loading',
                center_wavelength=620,
                bandwidth=10),
    'Oa08':
    Band.create(name='Oa08',
                description='Band 8 - 2nd Chlorophyll absorption maximum, sediment, yellow substance / vegetation',
                center_wavelength=665,
                bandwidth=10),
    'Oa09':
    Band.create(name='Oa09',
                description='Band 9 - Improved fluorescence retrieval',
                center_wavelength=673.75,
                bandwidth=7.5),
    'Oa10':
    Band.create(name='Oa10',
                description='Band 10 - Chlorophyll fluorescence peak, red edge',
                center_wavelength=681.25,
                bandwidth=7.5),
    'Oa11':
    Band.create(name='Oa11',
                description='Band 11 - Chlorophyll fluorescence baseline, red edge transition',
                center_wavelength=708.75,
                bandwidth=10),    
    'Oa12':
    Band.create(name='Oa12',
                description='Band 12 - O2 absorption / clouds, vegetation',
                center_wavelength=753.75,
                bandwidth=7.5),
    'Oa13':
    Band.create(name='Oa13',
                description='Band 13 - O2 absorption / aerosol correction',
                center_wavelength=761.25,
                bandwidth=2.5),
    'Oa14':
    Band.create(name='Oa14',
                description='Band 14 - Atmospheric correction',
                center_wavelength=764.375,
                bandwidth=3.75),
    'Oa15':
    Band.create(name='Oa15',
                description='Band 15 - O2 absorption used for cloud top pressure, fluorescence over land',
                center_wavelength=767.5,
                bandwidth=2.5),
    'Oa16':
    Band.create(name='Oa16',
                description='Band 16 - Atmospheric / aerosol correction',
                center_wavelength=778.75,
                full_width_half_max=15),
    'Oa17':
    Band.create(name='Oa17',
                description='Band 17 - Atmospheric / aerosol correction, clouds, pixel co-registration',
                center_wavelength=865,
                bandwidth=20),
    'Oa18':
    Band.create(name='Oa18',
                description='Band 18 - Water vapour absorption reference. Common reference band with SLSTR. Vegetation monitoring',
                center_wavelength=885,
                full_width_half_max=10),
    'Oa19':
    Band.create(name='Oa19',
                description='Band 19 - Water vapour absorption, vegetation monitoring (maximum REFLECTANCE)',
                center_wavelength=900,
                bandwidth=10),
    'Oa20':
    Band.create(name='Oa20',
                description='Band 20 - Water vapour absorption, atmospheric / aerosol correction',
                center_wavelength=940,
                bandwidth=20),
    'Oa21':
    Band.create(name='Oa21',
                description='Band 21 - Water vapour absorption, atmospheric / aerosol correction',
                center_wavelength=1020,
                bandwidth=40),
}

SENTINEL_LICENSE = Link(
    rel="license",
    target="https://sentinel.esa.int/documents/" +
    "247904/690755/Sentinel_Data_Legal_Notice",
)
