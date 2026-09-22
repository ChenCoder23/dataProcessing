/**
 * 前端脚本：演示浏览器如何调用后端 API。
 *
 * fetch() 是浏览器提供的 HTTP 客户端。
 * 每个函数都对应一个用户动作，并把结果重新渲染到页面。
 */

const taskList = document.querySelector("#task-list");
const taskForm = document.querySelector("#task-form");
const message = document.querySelector("#message");

function showMessage(text, isError = false) {
  message.textContent = text;
  message.style.color = isError ? "#dc2626" : "#2563eb";
}

async function loadTasks() {
  try {
    const response = await fetch("/api/tasks");
    if (!response.ok) throw new Error("读取任务失败");
    const tasks = await response.json();
    renderTasks(tasks);
  } catch (error) {
    showMessage(error.message, true);
  }
}

function renderTasks(tasks) {
  if (tasks.length === 0) {
    taskList.innerHTML = '<div class="empty">还没有任务，先添加一条吧！</div>';
    return;
  }

  taskList.innerHTML = tasks.map((task) => `
    <article class="task ${task.completed ? "done" : ""}">
      <div>
        <h3>${escapeHtml(task.title)}</h3>
        <p>${escapeHtml(task.description || "暂无说明")}</p>
      </div>
      <div class="task-actions">
        <button type="button" onclick="toggleTask(${task.id}, ${!task.completed})">
          ${task.completed ? "标记未完成" : "完成"}
        </button>
        <button type="button" class="danger" onclick="deleteTask(${task.id})">删除</button>
      </div>
    </article>
  `).join("");
}

async function createTask(event) {
  event.preventDefault();
  const formData = new FormData(taskForm);
  const payload = {
    title: formData.get("title"),
    description: formData.get("description") || null,
  };

  const response = await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!response.ok) {
    showMessage("添加失败，请检查输入内容。", true);
    return;
  }
  taskForm.reset();
  showMessage("任务添加成功！");
  await loadTasks();
}

async function toggleTask(id, completed) {
  // 为了简单起见，更新时先读取当前任务，再提交完整的 PUT 数据。
  const current = await (await fetch(`/api/tasks/${id}`)).json();
  await fetch(`/api/tasks/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: current.title, description: current.description, completed }),
  });
  await loadTasks();
}

async function deleteTask(id) {
  if (!confirm("确定要删除这条任务吗？")) return;
  const response = await fetch(`/api/tasks/${id}`, { method: "DELETE" });
  if (response.ok) {
    showMessage("任务已删除。");
    await loadTasks();
  }
}

// 用户输入可能包含 HTML 字符，渲染前转义可以避免 XSS。
function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, (character) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;",
  }[character]));
}

taskForm.addEventListener("submit", (event) => createTask(event).catch((error) => showMessage(error.message, true)));
document.querySelector("#refresh-button").addEventListener("click", loadTasks);
loadTasks();

