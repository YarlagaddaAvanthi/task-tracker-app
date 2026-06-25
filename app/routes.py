from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Task

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("base.html", title="Task Tracker Home")


@main_bp.route("/tasks")
@login_required
def tasks():
    all_tasks = (
        Task.query.filter_by(user_id=current_user.id)
        .order_by(Task.created_at.desc())
        .all()
    )

    total = len(all_tasks)
    pending = sum(1 for t in all_tasks if t.status == "Pending")
    in_progress = sum(1 for t in all_tasks if t.status == "In Progress")
    completed = sum(1 for t in all_tasks if t.status == "Completed")

    summary = {
        "total": total,
        "pending": pending,
        "in_progress": in_progress,
        "completed": completed,
    }

    return render_template(
        "tasks.html",
        title="Tasks",
        tasks=all_tasks,
        summary=summary,
    )


@main_bp.route("/tasks/add", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        priority = request.form.get("priority")

        if not title:
            flash("Title is required.", "error")
            return redirect(url_for("main.add_task"))

        new_task = Task(
            title=title,
            description=description,
            priority=priority or "Medium",
            status="Pending",
            user_id=current_user.id,
        )
        db.session.add(new_task)
        db.session.commit()

        flash("Task added successfully!", "success")
        return redirect(url_for("main.tasks"))

    return render_template("add_task.html", title="Add Task")


@main_bp.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        flash("You are not allowed to edit this task.", "error")
        return redirect(url_for("main.tasks"))

    if request.method == "POST":
        task.title = request.form.get("title")
        task.description = request.form.get("description")
        task.priority = request.form.get("priority")
        task.status = request.form.get("status")

        if not task.title:
            flash("Title is required.", "error")
            return redirect(url_for("main.edit_task", task_id=task.id))

        db.session.commit()
        flash("Task updated successfully!", "success")
        return redirect(url_for("main.tasks"))

    return render_template("edit_task.html", title="Edit Task", task=task)


@main_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        flash("You are not allowed to delete this task.", "error")
        return redirect(url_for("main.tasks"))

    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "success")
    return redirect(url_for("main.tasks"))