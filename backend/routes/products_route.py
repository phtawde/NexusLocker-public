# API routes for Product related routes

from flask import Blueprint, jsonify, request
from backend.services.product_service import searchProducts, getLatestProducts, getAllProducts

products_bp = Blueprint("products", __name__, url_prefix="/api/products")

@products_bp.get("/featured")
def home():

    # Return 4 most recently added products
    # Route: GET /api/products/featured
    # Response: 200: JSON array

    product_list = getLatestProducts(4)
    products = [item.getDict() for item in product_list]

    return jsonify(products)


@products_bp.get("/search")
def search():

    # Search products for specific query
    # Route: GET /api/products/search?q=<query>
    # Response: 200: JSON array; Empty array when no match found

    query = request.args.get("q", "").strip()

    if not query:
        return jsonify([])

    ref_products = searchProducts("description", query)
    products = [item.getDict() for item in ref_products]

    return jsonify(products)



@products_bp.get("/<int:product_id>")
def product(product_id):

    # Get a product's details by its ID
    # Route: GET /api/products/<int:product_id>
    # Args: product_id
    # Response: 200: JSON object of product details
    #           404: JSON error object if non-existent

    ref_product = searchProducts("id", product_id)

    if ref_product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(ref_product.getDict())


@products_bp.get("")
def products():

    # Get all products
    # Route: GET /api/products
    # Response: 200: JSON array; Empty array when no products found

    ref_products = getAllProducts()
    product_info = [item.getDict() for item in ref_products]

    return jsonify(product_info)
