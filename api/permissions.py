from rest_framework import permissions

class IsStaffOrSafeMethod(permissions.BasePermission):
	def has_permission(self, request, view):
		# Read-only permissions are allowed for any request
		if request.method in permissions.SAFE_METHODS:
			return True
		# Write permissions are only allowed to the staff users
		return request.user.is_staff

	def has_object_permission(self, request, view, obj):
		# Read-only permissions are allowed for any request
		if request.method in permissions.SAFE_METHODS:
			return True
		# Write permissions are only allowed to the staff users
		return request.user.is_staff


class IsStaff(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user.is_staff

	def has_object_permission(self, request, view, obj):
		return request.user.is_staff