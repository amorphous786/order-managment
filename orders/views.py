from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
import json
from .models import Order
from .forms import OrderForm

class OrderListView(ListView):
    """Main order list view with pagination"""
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10  # Show 10 orders per page
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add pagination info for JavaScript
        paginator = context['paginator']
        page_obj = context['page_obj']
        
        context['pagination_info'] = {
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'total_orders': paginator.count,
            'orders_per_page': self.paginate_by,
        }
        return context

@method_decorator(csrf_exempt, name='dispatch')
class CreateOrderView(View):
    """Create a new order via AJAX"""
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            form = OrderForm(data)
            if form.is_valid():
                order = form.save()
                return JsonResponse({
                    'success': True,
                    'order': {
                        'order_id': order.order_id,
                        'customer_name': order.customer_name,
                        'freight': str(order.freight),
                        'ship_name': order.ship_name,
                        'ship_country': order.ship_country,
                    }
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

@method_decorator(csrf_exempt, name='dispatch')
class UpdateOrderView(View):
    """Update an existing order via AJAX"""
    
    def post(self, request, order_id):
        try:
            order = get_object_or_404(Order, order_id=order_id)
            data = json.loads(request.body)
            form = OrderForm(data, instance=order)
            if form.is_valid():
                order = form.save()
                return JsonResponse({
                    'success': True,
                    'order': {
                        'order_id': order.order_id,
                        'customer_name': order.customer_name,
                        'freight': str(order.freight),
                        'ship_name': order.ship_name,
                        'ship_country': order.ship_country,
                    }
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

@method_decorator(csrf_exempt, name='dispatch')
class DeleteOrderView(View):
    """Delete an order via AJAX"""
    
    def delete(self, request, order_id):
        try:
            order = get_object_or_404(Order, order_id=order_id)
            order.delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

class GetOrderView(View):
    """Get order details for editing"""
    
    def get(self, request, order_id):
        try:
            order = get_object_or_404(Order, order_id=order_id)
            return JsonResponse({
                'success': True,
                'order': {
                    'order_id': order.order_id,
                    'customer_name': order.customer_name,
                    'freight': str(order.freight),
                    'ship_name': order.ship_name,
                    'ship_country': order.ship_country,
                }
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

# API view for paginated orders (for AJAX pagination)
class OrdersAPIView(View):
    """API view to get paginated orders for AJAX pagination"""
    
    def get(self, request):
        try:
            page = request.GET.get('page', 1)
            orders = Order.objects.all()
            paginator = Paginator(orders, 10)  # 10 orders per page
            
            try:
                page_obj = paginator.page(page)
            except:
                page_obj = paginator.page(1)
            
            orders_data = []
            for order in page_obj:
                orders_data.append({
                    'order_id': order.order_id,
                    'customer_name': order.customer_name,
                    'freight': str(order.freight),
                    'ship_name': order.ship_name,
                    'ship_country': order.ship_country,
                })
            
            return JsonResponse({
                'success': True,
                'orders': orders_data,
                'pagination': {
                    'current_page': page_obj.number,
                    'total_pages': paginator.num_pages,
                    'has_previous': page_obj.has_previous(),
                    'has_next': page_obj.has_next(),
                    'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
                    'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
                    'total_orders': paginator.count,
                }
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
