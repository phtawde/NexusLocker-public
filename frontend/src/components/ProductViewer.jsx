import React, { useState, useEffect } from 'react';

// Discover filenames at build time without eagerly importing public assets.
const imageFiles = Object.keys(
    import.meta.glob([
        '/public/assets/product_photos/*/*.jpg',
        '!/public/assets/product_photos/*/thumbnail.jpg',
    ])
);

const ProductViewer = ({ product }) => {
    const [images, setImages] = useState([]);
    const [currentImage, setCurrentImage] = useState(null);

    useEffect(() => {
        const folder = `/public/assets/product_photos/${product.id}/`;

        const imageUrls = imageFiles
            .filter((path) => path.startsWith(folder))
            .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }))
            .map((path) =>
                `${import.meta.env.BASE_URL}${path.slice('/public/'.length)}`
            );

        setImages(imageUrls);
        setCurrentImage(imageUrls[0] ?? null);
    }, [product.id]);

    return (
        <div className='main-content'>
            <div className="product-details-container">
                <div className="product-photos">
                    <div className="preview-window">
                        {currentImage && (
                            <img
                                src={currentImage}
                                alt="Active Product View"
                                style={{
                                    width: '100%',
                                    height: 'auto',
                                    objectFit: 'contain',
                                }}
                            />
                        )}
                    </div>

                    <div className="photo-selector">
                        {images.map((img, index) => (
                            <img
                                key={img}
                                src={img}
                                alt={`Thumbnail ${index + 1}`}
                                onMouseEnter={() => setCurrentImage(img)}
                                style={{
                                    width: '80px',
                                    height: '80px',
                                    cursor: 'pointer',
                                    border: currentImage === img
                                        ? '2px solid #0057e7'
                                        : '1px solid #ccc',
                                    boxSizing: 'border-box',
                                    objectFit: 'cover',
                                }}
                            />
                        ))}
                    </div>
                </div>

                <ul>
                    <h3>e</h3>
                    <p>e</p>
                </ul>
            </div>
        </div>
    );
};

export default ProductViewer;