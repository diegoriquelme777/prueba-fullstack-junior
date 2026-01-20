import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filtro, setFiltro] = useState(""); // filtro por estado

  useEffect(() => {
    fetch("http://localhost:8000/api/pedidos")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Error al obtener los pedidos");
        }
        return res.json();
      })
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Cargando pedidos...</p>;
  if (error) return <p style={{ color: "red" }}>Error: {error}</p>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Pedidos</h1>

      {/* Tarjetas de resumen */}
      <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
        <div style={{ padding: "10px", border: "1px solid #ccc", borderRadius: "5px" }}>
          <strong>Total Pedidos:</strong> {data.resumen.total_pedidos}
        </div>
        <div style={{ padding: "10px", border: "1px solid #ccc", borderRadius: "5px" }}>
          <strong>Total Items:</strong> {data.resumen.total_items}
        </div>
        <div style={{ padding: "10px", border: "1px solid #ccc", borderRadius: "5px" }}>
          <strong>Monto Neto:</strong> ${data.resumen.monto_total_neto.toLocaleString("es-CL")}
        </div>
      </div>

      {/* Filtro por estado */}
      <div style={{ marginBottom: "10px" }}>
        <label htmlFor="estadoFiltro">Filtrar por estado: </label>
        <select
          id="estadoFiltro"
          value={filtro}
          onChange={(e) => setFiltro(e.target.value)}
        >
          <option value="">Todos</option>
          <option value="Pendiente">Pendiente</option>
          <option value="Enviado">Enviado</option>
          <option value="Entregado">Entregado</option>
        </select>
      </div>

      {/* Tabla de pedidos */}
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Fecha</th>
            <th>Cliente</th>
            <th>Ciudad</th>
            <th>Estado</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          {data.pedidos_formateados
            .filter((p) => filtro === "" || p.estado === filtro)
            .map((pedido) => (
              <tr key={pedido.id}>
                <td>{pedido.id}</td>
                <td>{pedido.fecha}</td>
                <td>{pedido.cliente_nombre}</td>
                <td>{pedido.ciudad}</td>
                <td>
                  <span
                    style={{
                      padding: "5px 10px",
                      borderRadius: "5px",
                      color: "white",
                      backgroundColor:
                        pedido.estado_badge === "warning"
                          ? "orange"
                          : pedido.estado_badge === "info"
                          ? "blue"
                          : "green",
                    }}
                  >
                    {pedido.estado}
                  </span>
                </td>
                <td>${pedido.total.toLocaleString("es-CL")}</td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

